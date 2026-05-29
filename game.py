from card import Deck
from player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("プレイヤー", chips=1000)
        self.dealer = Player("ディーラー")

    def ask_bet(self):
        print(f"\n所持チップ: {self.player.chips}")
        while True:
            try:
                amount = int(input("ベット額を入力してください: "))
                self.player.place_bet(amount)
                break
            except ValueError as e:
                print(e)

    def deal_initial(self):
        for _ in range(2):
            self.player.hand.add_card(self.deck.deal())
            self.dealer.hand.add_card(self.deck.deal())

    def show_hands(self, hide_dealer=True):
        print("\n--- 手札 ---")
        print(f"あなた: {self.player.hand}  (合計: {self.player.hand.total()})")
        if hide_dealer:
            print(f"ディーラー: {self.dealer.hand.cards[0]} ??")
        else:
            print(f"ディーラー: {self.dealer.hand}  (合計: {self.dealer.hand.total()})")

    def player_turn(self):
        while True:
            self.show_hands()

            if self.player.hand.is_bust():
                print("バスト！")
                return False

            if self.player.hand.is_blackjack():
                print("ブラックジャック！")
                return True

            action = input("\nヒット(h) / スタンド(s): ").strip().lower()
            if action == 'h':
                self.player.hand.add_card(self.deck.deal())
            elif action == 's':
                break
            else:
                print("h か s を入力してください")

        return True

    def dealer_turn(self):
        # ディーラーは17以上になるまでヒットし続ける
        while self.dealer.hand.total() < 17:
            self.dealer.hand.add_card(self.deck.deal())

    def determine_winner(self):
        player_total = self.player.hand.total()
        dealer_total = self.dealer.hand.total()

        self.show_hands(hide_dealer=False)
        print("\n--- 結果 ---")

        if self.player.hand.is_bust():
            print("あなたの負けです！")
        elif self.player.hand.is_blackjack() and not self.dealer.hand.is_blackjack():
            print("ブラックジャック！1.5倍獲得！")
            self.player.win_blackjack()
        elif self.dealer.hand.is_bust():
            print("ディーラーがバスト！あなたの勝ちです！")
            self.player.win()
        elif player_total > dealer_total:
            print("あなたの勝ちです！")
            self.player.win()
        elif player_total < dealer_total:
            print("ディーラーの勝ちです！")
        else:
            print("引き分けです！")
            self.player.push()

        print(f"所持チップ: {self.player.chips}")

    def reset(self):
        self.player.clear_hand()
        self.dealer.clear_hand()
        if len(self.deck) < 10:
            self.deck = Deck()
            print("デッキをシャッフルしました。")

    def play(self):
        print("=== ブラックジャック ===")

        if self.player.chips <= 0:
            print("チップがなくなりました。ゲームオーバー！")
            return

        self.ask_bet()
        self.deal_initial()
        player_ok = self.player_turn()

        if player_ok and not self.player.hand.is_bust():
            self.dealer_turn()

        self.determine_winner()

        again = input("\nもう一度プレイしますか？(y/n): ").strip().lower()
        if again == 'y':
            self.reset()
            self.play()


if __name__ == "__main__":
    game = Game()
    game.play()
