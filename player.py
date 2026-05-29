class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def total(self):
        total = sum(card.value() for card in self.cards)
        # ACEは合計が21を超えた場合に1として再計算
        aces = sum(1 for card in self.cards if card.rank == 'A')
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def is_blackjack(self):
        return len(self.cards) == 2 and self.total() == 21

    def is_bust(self):
        return self.total() > 21

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)


class Player:
    def __init__(self, name, chips=1000):
        self.name = name
        self.hand = Hand()
        self.chips = chips
        self.bet = 0

    def place_bet(self, amount):
        if amount <= 0 or amount > self.chips:
            raise ValueError(f"無効なベット額です（所持チップ: {self.chips}）")
        self.bet = amount
        self.chips -= amount

    def win(self):
        self.chips += self.bet * 2

    def win_blackjack(self):
        # ブラックジャック時は1.5倍（端数は切り捨て）
        self.chips += self.bet + int(self.bet * 1.5)

    def push(self):
        # 引き分けはベット返却
        self.chips += self.bet

    def clear_hand(self):
        self.hand = Hand()
        self.bet = 0
