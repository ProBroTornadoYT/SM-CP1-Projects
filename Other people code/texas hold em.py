#Texas Poker Hold'em Game

import random
from enum import Enum
from itertools import combinations

class Suit(Enum):
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[rank]
    
    def __repr__(self):
        return f"{self.rank}{self.suit.value}"

class Player:
    def __init__(self, name, tokens, is_human=False):
        self.name = name
        self.tokens = tokens
        self.hand = []
        self.current_bet = 0
        self.total_bet = 0
        self.is_human = is_human
        self.is_active = True
        self.is_all_in = False
    
    def add_card(self, card):
        self.hand.append(card)
    
    def bet(self, amount):
        if amount > self.tokens:
            return False
        self.tokens -= amount
        self.current_bet += amount
        self.total_bet += amount
        return True
    
    def reset_hand(self):
        self.hand = []
        self.current_bet = 0
        self.total_bet = 0
        self.is_active = True
        self.is_all_in = False

class TexasHoldem:
    def __init__(self, players):
        self.players = players
        self.deck = []
        self.community_cards = []
        self.pot = 0
        self.side_pots = []
        self.current_bet = 0
        self.button_index = 0
        self.small_blind = 10
        self.big_blind = 20
        self.player_contributions = {}
    
    def create_deck(self):
        """Create and shuffle a standard deck of cards"""
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [Card(rank, suit) for rank in ranks for suit in Suit]
        random.shuffle(self.deck)
    
    def evaluate_hand(self, cards):
        """Evaluate hand strength and return (rank, tie_breaker)"""
        card_values = sorted([c.rank_value for c in cards], reverse=True)
        suits = [c.suit for c in cards]
        
        # Check for flush (all same suit)
        is_flush = len(set(suits)) == 1
        # Check for straight (5 consecutive values)
        is_straight = card_values == list(range(card_values[0], card_values[0]-5, -1))
        
        # Check for Ace-low straight (A-2-3-4-5)
        if not is_straight and card_values == [14, 5, 4, 3, 2]:
            is_straight = True
            card_values = [5, 4, 3, 2, 1]  # Treat Ace as 1
        
        # Count occurrences of each card value
        value_counts = {}
        for val in card_values:
            value_counts[val] = value_counts.get(val, 0) + 1
        
        # Sort by count then value for easier pattern matching
        counts = sorted(value_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
        
        # Return hand rank (8=straight flush, 7=four of a kind, etc.)
        if is_straight and is_flush:
            return (8, card_values)
        elif counts[0][1] == 4:
            return (7, [counts[0][0]] * 4 + [counts[1][0]])
        elif counts[0][1] == 3 and counts[1][1] == 2:
            return (6, [counts[0][0]] * 3 + [counts[1][0]] * 2)
        elif is_flush:
            return (5, card_values)
        elif is_straight:
            return (4, card_values)
        elif counts[0][1] == 3:
            return (3, [counts[0][0]] * 3 + [counts[1][0], counts[2][0]])
        elif counts[0][1] == 2 and counts[1][1] == 2:
            return (2, [counts[0][0]] * 2 + [counts[1][0]] * 2 + [counts[2][0]])
        elif counts[0][1] == 2:
            return (1, [counts[0][0]] * 2 + [counts[1][0], counts[2][0], counts[3][0]])
        else:
            return (0, card_values)
    
    def get_best_hand(self, player):
        """Get best 5-card hand from 7 cards (2 hole + 5 community)"""
        all_cards = player.hand + self.community_cards
        best_hand = None
        best_rank = None
        
        # Try all possible 5-card combinations
        for combo in combinations(all_cards, 5):
            rank = self.evaluate_hand(combo)
            if best_rank is None or rank > best_rank:
                best_rank = rank
                best_hand = combo
        
        return best_hand, best_rank
    
    def deal_cards(self):
        """Deal 2 cards to each player"""
        for _ in range(2):
            for player in self.players:
                if self.deck:
                    player.add_card(self.deck.pop())
    
    def post_blinds(self):
        """Post small and big blinds"""
        sb_index = (self.button_index + 1) % len(self.players)
        bb_index = (self.button_index + 2) % len(self.players)
        
        sb_player = self.players[sb_index]
        bb_player = self.players[bb_index]
        
        # Post small blind
        blind_amount = min(self.small_blind, sb_player.tokens)
        sb_player.bet(blind_amount)
        self.pot += blind_amount
        self.player_contributions[sb_player.name] += blind_amount
        
        # Post big blind
        blind_amount = min(self.big_blind, bb_player.tokens)
        bb_player.bet(blind_amount)
        self.pot += blind_amount
        self.player_contributions[bb_player.name] += blind_amount
        self.current_bet = blind_amount
    
    def flop(self):
        """Reveal first 3 community cards"""
        self.deck.pop()  # Burn card
        for _ in range(3):
            self.community_cards.append(self.deck.pop())
    
    def turn(self):
        """Reveal 4th community card"""
        self.deck.pop()  # Burn card
        self.community_cards.append(self.deck.pop())
    
    def river(self):
        """Reveal 5th community card"""
        self.deck.pop()  # Burn card
        self.community_cards.append(self.deck.pop())
    
    def play_round(self):
        """Execute one complete round of Texas Hold'em"""
        print("\n" + "="*50)
        print("🃏 NEW ROUND 🃏".center(50))
        print("="*50)
        
        # Reset player hands and game state
        for player in self.players:
            player.reset_hand()
        
        self.community_cards = []
        self.pot = 0
        self.side_pots = []
        self.player_contributions = {player.name: 0 for player in self.players}
        self.current_bet = 0
        self.create_deck()
        
        # Post blinds and deal initial cards
        self.post_blinds()
        self.deal_cards()
        
        # Display human player's hand
        for player in self.players:
            if player.is_human:
                print(f"\n👤 {player.name}'s hand: {' '.join(str(c) for c in player.hand)}")
        
        # Betting rounds: Pre-flop, Flop, Turn, River
        self._betting_round("Pre-flop")
        
        if sum(1 for p in self.players if p.is_active) > 1:
            self.flop()
            print(f"\n📋 Flop: {' '.join(str(c) for c in self.community_cards)}")
            self._betting_round("Flop")
        
        if sum(1 for p in self.players if p.is_active) > 1:
            self.turn()
            print(f"\n📋 Turn: {' '.join(str(c) for c in self.community_cards)}")
            self._betting_round("Turn")
        
        if sum(1 for p in self.players if p.is_active) > 1:
            self.river()
            print(f"\n📋 River: {' '.join(str(c) for c in self.community_cards)}")
            self._betting_round("River")
        
        # Determine and award pot to winner(s)
        self._determine_winner()
        self.button_index = (self.button_index + 1) % len(self.players)
    
    def _betting_round(self, stage):
        """Execute a single betting round"""
        print(f"\n💰 {stage} Betting Round:")
        active_players = [p for p in self.players if p.is_active and p.tokens > 0]
        
        # Reset current_bet for new street
        for player in active_players:
            player.current_bet = 0
        
        self.current_bet = 0
        round_complete = False
        
        while not round_complete:
            round_complete = True
            for player in active_players:
                if not player.is_active or player.is_all_in:
                    continue
                
                print(f"\nPot: {self.pot} | Current bet: {self.current_bet}")
                
                if player.is_human:
                    # Human player decision loop
                    while True:
                        print(f"\n👤 {player.name}'s turn (Tokens: {player.tokens}, Current bet: {player.current_bet})")
                        print(f"   1. Fold  2. Check  3. Call  4. Raise  5. All-In")
                        
                        choice = input("Choose action (1-5): ").strip()
                        
                        if choice == '1':
                            player.is_active = False
                            print(f"{player.name} folds")
                            break
                        elif choice == '2':
                            if player.current_bet == self.current_bet:
                                print(f"{player.name} checks")
                                break
                            else:
                                print("Cannot check, must call or raise")
                                continue
                        elif choice == '3':
                            call_amount = min(self.current_bet - player.current_bet, player.tokens)
                            if call_amount > 0:
                                player.bet(call_amount)
                                self.pot += call_amount
                                self.player_contributions[player.name] += call_amount
                                print(f"{player.name} calls {call_amount}")
                            break
                        elif choice == '4':
                            try:
                                raise_to = int(input(f"Raise to (current bet: {self.current_bet}, max: {player.tokens + player.current_bet}): "))
                                if raise_to > self.current_bet and raise_to <= player.tokens + player.current_bet:
                                    raise_amount = raise_to - player.current_bet
                                    player.bet(raise_amount)
                                    self.pot += raise_amount
                                    self.player_contributions[player.name] += raise_amount
                                    self.current_bet = raise_to
                                    print(f"{player.name} raises to {self.current_bet}")
                                    round_complete = False  # Continue betting round
                                    break
                                else:
                                    print(f"Invalid raise. Must be > {self.current_bet} and <= {player.tokens + player.current_bet}")
                                    continue
                            except ValueError:
                                print("Invalid amount")
                                continue
                        elif choice == '5':
                            player.bet(player.tokens)
                            self.pot += player.tokens
                            self.player_contributions[player.name] += player.tokens
                            player.is_all_in = True
                            print(f"{player.name} is all-in with {player.current_bet}!")
                            break
                        else:
                            print("Invalid choice")
                else:
                    # Bot player decision logic
                    call_amount = self.current_bet - player.current_bet
                    
                    if call_amount > player.tokens:
                        # Not enough tokens, go all-in
                        player.bet(player.tokens)
                        self.pot += player.tokens
                        self.player_contributions[player.name] += player.tokens
                        player.is_all_in = True
                        print(f"{player.name} is all-in with {player.current_bet}!")
                    elif random.random() < 0.3 and player.tokens > call_amount:
                        # 30% chance to raise if possible
                        raise_delta = random.randint(10, min(30, player.tokens - call_amount))
                        raise_amount = call_amount + raise_delta
                        player.bet(raise_amount)
                        self.pot += raise_amount
                        self.player_contributions[player.name] += raise_amount
                        self.current_bet = player.current_bet
                        print(f"{player.name} raises to {self.current_bet}")
                        round_complete = False  # Continue betting round
                    elif call_amount > 0:
                        # Call the current bet
                        player.bet(call_amount)
                        self.pot += call_amount
                        self.player_contributions[player.name] += call_amount
                        print(f"{player.name} calls {call_amount}")
                    else:
                        # Check if no bet to call
                        print(f"{player.name} checks")
    
    def _determine_winner(self):
        """Determine winner(s) based on hand evaluation with side pot support"""
        active_players = [p for p in self.players if p.is_active]
        
        # If only one player remains, they win by default
        if len(active_players) == 1:
            winner = active_players[0]
            print(f"\n🏆 {winner.name} wins {self.pot} tokens! (others folded)")
            winner.tokens += self.pot
            return
        
        # Evaluate all active players' hands
        best_hand_rank = None
        hand_rankings = {}
        
        for player in active_players:
            _, hand_rank = self.get_best_hand(player)
            hand_rankings[player.name] = hand_rank
            print(f"{player.name}'s hand: {[str(c) for c in player.hand]} (rank: {hand_rank[0]})")
            
            if best_hand_rank is None or hand_rank > best_hand_rank:
                best_hand_rank = hand_rank
        
        # Calculate main pot and side pots based on all-in amounts
        sorted_contributions = sorted(set(self.player_contributions.values()))
        pots_info = []
        prev_level = 0
        
        for level in sorted_contributions:
            pot_amount = (level - prev_level) * len(active_players)
            eligible_players = [p for p in active_players if self.player_contributions[p.name] >= level]
            pots_info.append((pot_amount, eligible_players))
            prev_level = level
        
        # Award pots to winners, handling ties with pot splits
        winnings = {}
        for pot_amount, eligible in pots_info:
            if eligible:
                # Find best hands among eligible players for this pot
                best_eligible_rank = max(hand_rankings[p.name] for p in eligible)
                best_eligible = [p for p in eligible if hand_rankings[p.name] == best_eligible_rank]
                split_amount = pot_amount // len(best_eligible)
                for winner in best_eligible:
                    winnings[winner.name] = winnings.get(winner.name, 0) + split_amount
        
        # Distribute winnings to all winners
        for player_name, amount in winnings.items():
            winner = next(p for p in self.players if p.name == player_name)
            print(f"\n🏆 {winner.name} wins {amount} tokens!")
            winner.tokens += amount
    
    def display_status(self):
        """Display current tokens for all players"""
        print("\n" + "="*50)
        print("PLAYER STATUS".center(50))
        print("="*50)
        for player in self.players:
            print(f"👤 {player.name}: {player.tokens} tokens")

if __name__ == "__main__":
    # Initialize game with human player and bots
    game = TexasHoldem([
        Player("You", 1000, is_human=True),
        Player("Bot1", 1000),
        Player("Bot2", 1000)
    ])
    
    # Play up to 10 rounds
    round_num = 0
    while all(p.tokens > 0 for p in game.players) and round_num < 10:
        round_num += 1
        print(f"\n{'='*50}")
        print(f"ROUND {round_num}".center(50))
        print(f"{'='*50}")
        game.play_round()
        game.display_status()
    
    # Display final results
    print("\n" + "="*50)
    print("GAME OVER".center(50))
    print("="*50)
    for p in game.players:
        print(f"{p.name}: {p.tokens} tokens")


#the end