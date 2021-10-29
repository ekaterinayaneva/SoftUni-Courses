from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        try:
            c = [c for c in self.cards if c.name == card.name][0]
            raise ValueError(f"Card {card.name} already exists!")

            #cards = [c.name for c in self.cards]                                       tova otgore s try i except posle ili tova zakomentiranoto i
            #if card in cards:                                                          produljavame nadolu s logikata bez da pishem excepta (red 18)
             #   raise ValueError(f"Card {card.name} already exists!")

        except IndexError:
            self.cards.append(card)
            self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        card_card = [c for c in self.cards if c.name == card][0]
        self.cards.remove(card_card)
        self.count -= 1

    def find(self, name: str):
        card = [c for c in self.cards if c.name == name][0]
        return card
