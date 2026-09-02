import random
from itertools import combinations
from collections import Counter

# Texas Hold'em with tokens instead of money
# Simple console game: 1 human + 2 bots

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_VALUES = {r: i + 2 for i, r in enumerate(RANKS)}
CARD_VALUES["A"] = 14

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}{self.suit}"

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, count=1):
        if len(self.cards) < count:
            raise ValueError("Not enough cards in deck.")
        dealt = self.cards[:count]
        self.cards = self.cards[count:]
        return dealt if count > 1 else dealt[0]

def straight_high(values):
    unique = sorted(set(values))
    if 14 in unique:
        unique = [1 if v == 14 else v for v in unique]
        unique = sorted(set(unique))
    for i in range(len(unique) - 4, -1, -1):
        window = unique[i:i + 5]
        if len(window) == 5 and window[0] == window[-1] - 4:
            return window[-1] if 1 not in window else 5
    return None

def score_five(cards):
    values = sorted([CARD_VALUES[c.rank] for c in cards], reverse=True)
    counts = Counter(values)
    sorted_counts = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)

    # Check flush
    suits = {}
    for c in cards:
        suits.setdefault(c.suit, []).append(CARD_VALUES[c.rank])
    flush_cards = [sorted(vals, reverse=True) for vals in suits.values() if len(vals) >= 5]
    if flush_cards:
        flush_values = max(flush_cards)
        flush_high = (
            6, *flush_values[:5]
        )

    # Straight
    straight = straight_high(values)
    flush_flag = False
    for suit, vals in suits.items():
        if len(vals) >= 5:
            flush_flag = True
            flush_values = sorted(vals, reverse=True)
            straight_in_flush = straight_high(flush_values)
            if straight_in_flush is not None:
                return (9, straight_in_flush)  # straight flush
    if straight is not None:
        # regular straight
        if flush_flag:
            # already handled straight flush above
            pass
        else:
            return (5, straight)

    # Four of a kind
    if sorted_counts[0][1] == 4:
        quad_rank = sorted_counts[0][0]
        kicker = max([v for v in values if v != quad_rank])
        return (8, quad_rank, kicker)

    # Full house
    if sorted_counts[0][1] == 3 and len(sorted_counts) > 1 and sorted_counts[1][1] >= 2:
        triple_rank = sorted_counts[0][0]
        pair_rank = sorted_counts[1][0]
        return (7, triple_rank, pair_rank)

    # Flush
    if flush_flag:
        best_flush = sorted([CARD_VALUES[c.rank] for c in cards if c.suit == max(suits, key=lambda s: len(suits[s]))], reverse=True)
        return (6, *best_flush[:5])

    # Three of a kind
    if sorted_counts[0][1] == 3:
        trip_rank = sorted_counts[0][0]
        kickers = sorted([v for v in values if v != trip_rank], reverse=True)
        return (4, trip_rank, *kickers[:2])

    # Two pair
    if sorted_counts[0][1] == 2 and len(sorted_counts) > 1 and sorted_counts[1][1] == 2:
        pair1, pair2 = sorted_counts[0][0], sorted_counts[1][0]
        kicker = max([v for v in values if v not in {pair1, pair2}])
        return (3, max(pair1, pair2), min(pair1, pair2), kicker)

    # One pair
    if sorted_counts[0][1] == 2:
        pair_rank = sorted_counts[0][0]
        kickers = sorted([v for v in values if v != pair_rank], reverse=True)
        return (2, pair_rank, *kickers[:3])

    # High card
    return (1, *values[:5])

def best_hand_for_player(cards):
    best = None
    for combo in combinations(cards, 5):
        score = score_five(list(combo))
        if best is None or score > best:
            best = score
    return best

def compare_hands(h1, h2):
    return h1 > h2

class Player:
    def __init__(self, name, tokens, is_human=False):
        self.name = name
        self.tokens = tokens
        self.is_human = is_human
        self.hole = []
        self.folded = False
        self.all_in = False
        self.round_bet = 0
        self.total_in_hand = 0

    def add_tokens(self, amount):
        self.tokens += amount

    def bet(self, amount):
        if amount <= 0:
            return 0
        amount = min(amount, self.tokens)
        self.tokens -= amount
        self.total_in_hand += amount
        self.round_bet += amount
        if self.tokens == 0:
            self.all_in = True
        return amount

    def reset_for_new_hand(self):
        self.hole = []
        self.folded = False
        self.all_in = False
        self.round_bet = 0
        self.total_in_hand = 0

    def __str__(self):
        return self.name

class TexasHoldem:
    def __init__(self):
        self.players = [
            Player("You", 100, is_human=True),
            Player("Bot 1", 100),
            Player("Bot 2", 100),
        ]
        self.deck = Deck()
        self.community = []
        self.pot = 0
        self.button = 0

    def reset_players(self):
        for p in self.players:
            p.reset_for_new_hand()

    def deal_hole_cards(self):
        for p in self.players:
            p.hole = [self.deck.deal(), self.deck.deal()]

    def show_hole_cards(self):
        for p in self.players:
            if p.is_human:
                print(f"{p.name}: {p.hole[0]} {p.hole[1]} | Tokens: {p.tokens}")
            else:
                print(f"{p.name}: [hidden] [hidden] | Tokens: {p.tokens}")

    def post_blind(self, player, amount):
        actual = player.bet(amount)
        self.pot += actual
        return actual

    def get_action(self, player, to_call, current_bet, stage):
        if player.is_human:
            print(f"\n{player.name} turn.")
            print(f"Community: {self.community if self.community else 'No cards yet'}")
            print(f"Pot: {self.pot} | Current bet to call: {to_call} | Your tokens: {player.tokens}")
            print(f"Your hand: {player.hole[0]} {player.hole[1]}")
            while True:
                print("Actions:")
                print("  1 = Check / Call")
                print("  2 = Bet / Raise")
                print("  3 = Fold")
                print("  4 = All in")
                choice = input("Choose: ").strip()
                if choice == "1":
                    if to_call == 0:
                        return "check"
                    return "call"
                elif choice == "2":
                    if to_call == 0:
                        amount = input("Bet amount (min 10): ").strip()
                    else:
                        amount = input(f"Raise amount (min {max(10, to_call)}): ").strip()
                    try:
                        amount = int(amount)
                    except ValueError:
                        print("Invalid number.")
                        continue
                    if amount < 10:
                        print("Minimum bet/raise is 10 tokens.")
                        continue
                    if amount > player.tokens:
                        print("You don't have enough tokens.")
                        continue
                    return "raise", amount
                elif choice == "3":
                    return "fold"
                elif choice == "4":
                    return "all_in"
                else:
                    print("Invalid choice.")
        else:
            hand_score = best_hand_for_player(player.hole + self.community)
            rank = hand_score[0]
            # Simple bot logic
            if to_call > 0:
                if rank >= 7:
                    return "call"
                if rank >= 4 and random.random() < 0.7:
                    return "call"
                if rank >= 2 and random.random() < 0.3:
                    return "call"
                return "fold"
            else:
                if rank >= 8:
                    return "raise", 25
                if rank >= 5:
                    return "raise", 15
                if rank >= 3:
                    return "raise", 10
                return "check"

    def apply_action(self, player, action, amount, current_bet):
        if action == "fold":
            player.folded = True
            return current_bet

        if action == "check":
            return current_bet

        if action == "call":
            to_add = min(current_bet, player.tokens)
            player.bet(to_add)
            self.pot += to_add
            return current_bet

        if action == "all_in":
            to_add = player.tokens
            player.bet(to_add)
            self.pot += to_add
            player.all_in = True
            return max(current_bet, player.round_bet)

        if action == "raise":
            # amount is the extra amount they want to add
            raise_extra = min(amount, player.tokens)
            player.bet(raise_extra)
            self.pot += raise_extra
            current_bet = max(current_bet, player.round_bet)
            return current_bet

        return current_bet

    def betting_round(self, start_index, stage):
        current_bet = 0
        for p in self.players:
            p.round_bet = 0

        # This is a simplified betting round that allows multiple raises
        # until everyone either checked/called or folded.
        while True:
            raised = False
            for offset in range(len(self.players)):
                idx = (start_index + offset) % len(self.players)
                player = self.players[idx]

                if player.folded or player.all_in or player.tokens <= 0:
                    continue

                # how much the player needs to add to match current bet
                to_call = current_bet - player.round_bet

                action = self.get_action(player, to_call, current_bet, stage)
                if isinstance(action, tuple):
                    action_name, amount = action
                else:
                    action_name = action
                    amount = 0

                if action_name == "fold":
                    player.folded = True
                    continue

                if action_name == "check":
                    continue

                if action_name == "call":
                    call_amount = min(to_call, player.tokens)
                    player.bet(call_amount)
                    self.pot += call_amount
                    player.round_bet += call_amount
                    continue

                if action_name == "raise":
                    # player chooses amount to add
                    # We always require the new total this round to exceed current_bet
                    extra = min(amount, player.tokens)
                    if extra <= 0:
                        print(f"{player.name} tried to raise by 0.")
                        continue
                    player.bet(extra)
                    self.pot += extra
                    player.round_bet += extra
                    current_bet = max(current_bet, player.round_bet)
                    raised = True
                    continue

                if action_name == "all_in":
                    all_in_amount = player.tokens
                    player.bet(all_in_amount)
                    self.pot += all_in_amount
                    player.round_bet += all_in_amount
                    current_bet = max(current_bet, player.round_bet)
                    player.all_in = True
                    continue

            if not raised:
                break

    def deal_community(self, count):
        for _ in range(count):
            self.community.append(self.deck.deal())

    def determine_winner(self):
        active_players = [p for p in self.players if not p.folded]
        if len(active_players) == 1:
            winner = active_players[0]
            winner.add_tokens(self.pot)
            return [winner]

        best_rank = None
        winners = []
        for p in active_players:
            full_cards = p.hole + self.community
            rank = best_hand_for_player(full_cards)
            if best_rank is None or rank > best_rank:
                best_rank = rank
                winners = [p]
            elif rank == best_rank:
                winners.append(p)

        split = self.pot // len(winners)
        extra = self.pot % len(winners)

        for i, p in enumerate(winners):
            pay = split + (1 if i < extra else 0)
            p.add_tokens(pay)

        return winners

    def reset_round(self):
        self.community = []
        self.deck = Deck()
        self.pot = 0
        self.reset_players()
        self.button = (self.button + 1) % len(self.players)

    def play_hand(self):
        self.reset_round()

        # blinds
        dealer = self.button
        small_blind_pos = (dealer + 1) % len(self.players)
        big_blind_pos = (dealer + 2) % len(self.players)

        # big blind = 10, small blind = 5
        small_blind_amt = 5
        big_blind_amt = 10

        self.post_blind(self.players[small_blind_pos], small_blind_amt)
        self.post_blind(self.players[big_blind_pos], big_blind_amt)

        # ensure blinds are reflected in round_bet for calls
        self.players[small_blind_pos].round_bet = small_blind_amt
        self.players[big_blind_pos].round_bet = big_blind_amt

        self.deal_hole_cards()

        print("\n=== New hand ===")
        print(f"Dealer: {self.players[dealer].name}")
        print(f"Small blind: {self.players[small_blind_pos].name} ({small_blind_amt})")
        print(f"Big blind: {self.players[big_blind_pos].name} ({big_blind_amt})")
        self.show_hole_cards()

        start_index = (big_blind_pos + 1) % len(self.players)
        self.betting_round(start_index, "preflop")

        # Flop
        self.deal_community(3)
        print(f"\nFlop: {self.community[:3]}")
        self.betting_round((dealer + 1) % len(self.players), "flop")

        # Turn
        self.deal_community(1)
        print(f"Turn: {self.community[3]}")
        self.betting_round((dealer + 1) % len(self.players), "turn")

        # River
        self.deal_community(1)
        print(f"River: {self.community[4]}")
        self.betting_round((dealer + 1) % len(self.players), "river")

        print(f"\nCommunity cards: {self.community}")
        for p in self.players:
            if not p.folded:
                print(f"{p.name}: {p.hole[0]} {p.hole[1]} -> {best_hand_for_player(p.hole + self.community)}")

        winners = self.determine_winner()
        print("\nWinner(s):")
        for p in winners:
            print(f"  - {p.name} wins {self.pot} tokens" if len(winners) == 1 else f"  - {p.name} splits the pot")

        # Reset pot after winner payout
        self.pot = 0

        for p in self.players:
            print(f"{p.name}: {p.tokens} tokens")

        print("\nPress Enter to continue...")
        input()

def main():
    print("Welcome to Token Texas Hold'em!")
    game = TexasHoldem()

    while True:
        game.play_hand()

        if game.players[0].tokens <= 0:
            print("You are out of tokens. Game over.")
            break

        choice = input("Play another hand? (y/n): ").strip().lower()
        if choice != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()