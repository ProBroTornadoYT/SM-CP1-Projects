from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Button, Label

menu = {
    "burger": {
        "Vegi Double": 6.67,
        "Fry Potato Patty": 5.23,
        "Chef's Special Vegetarian": 8.99,
        "bread with cheese": 2.00,
    },
    "Drink": {
        "Coke": 1.00,
        "Wine": 10.00,
        "Sprite": 1.00,
        "'I HATE PEP*I!' poster": 5.00,
    },
    "burritoritos": {
        "Veg Burrito": 2.99,
        "Gravy Burrito": 2.99,
        "Saucy Burrito": 2.99,
        "Tortilla with cheese rolled": 1.99,
    },
    "sides": {
        "fries": {
            "Spicy Fries": 1.99,
            "waffle Fries": 2.50,
            "Simple Fries": 1.99,
            "BIG Fries": 2.99,
            "BIG Spicy Fries": 2.99,
            "BIG Waffle Fries": 2.99,
        },
        "Potato Nuggets": 2.99,
        "Apple Slices": 0.50,
        "Ranch": 0.69,
        "Garlic-Butter Ranch": 0.69,
        "Tomato Sauce": 0.69,
    },
}


class OrderApp(App):

  def __init__(self):
    super().__init__()
    self.order = []
    self.view = "menu"

  def compose(self) -> ComposeResult:
    yield VerticalScroll(id="container")

  def on_mount(self):
    self.render_view()

  def render_view(self):
    container = self.query_one("#container")
    container.remove_children()

    if self.view == "menu":
      container.mount(Label("CLICK ITEMS TO ADD:"))
      for category, items in menu.items():
        container.mount(Label(f"\n{category.upper()}"))
        for item, price in items.items():
          if isinstance(price, dict):
            container.mount(Label(f"  {item}:"))
            for sub_item, sub_price in price.items():
              btn = Button(f"{sub_item}: ${sub_price:.2f}")
              btn.item_data = (sub_item, sub_price)
              container.mount(btn)
          else:
            btn = Button(f"{item}: ${price:.2f}")
            btn.item_data = (item, price)
            container.mount(btn)

      container.mount(Label("\n"))
      container.mount(Button("CONTINUE TO ORDER", id="continue"))

    elif self.view == "order":
      container.mount(Label("_-_ORDER:_-_ (Click an item to remove it)"))
      total = 0.0
      for idx, (item, price) in enumerate(self.order):
        total += price
        btn = Button(f"{item}: ${price:.2f}")
        btn.remove_idx = idx
        container.mount(btn)

      container.mount(Label(f"\nTOTAL: ${total:.2f}\n"))
      container.mount(Button("GO BACK", id="back"))

  def on_button_pressed(self, event: Button.Pressed):
    btn = event.button
    if btn.id == "continue":
      self.view = "order"
      self.render_view()
    elif btn.id == "back":
      self.view = "menu"
      self.render_view()
    elif hasattr(btn, "item_data"):
      self.order.append(btn.item_data)
    elif hasattr(btn, "remove_idx"):
      self.order.pop(btn.remove_idx)
      self.render_view()


if __name__ == "__main__":
  OrderApp().run()
