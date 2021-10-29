from poker.validators import ThreeOfAKindValidator,PiarValidator

class FullHouseValidator():
    def __init__(self,cards):
        self.cards = cards
        self.name = "Full House"

    def is_valid(self):
        return ThreeOfAKindValidator(cards=self.cards).is_valid() and PiarValidator(cards=self.cards).is_valid()
        
    def valid_cards(self):
        three_of_a_kind_cards = ThreeOfAKindValidator(cards=self.cards).valid_cards()
        pair_cards = PiarValidator(cards=self.cards).valid_cards()
        all_cards = three_of_a_kind_cards + pair_cards
        return all_cards