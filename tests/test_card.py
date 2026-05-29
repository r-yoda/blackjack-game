import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from card import Card, Deck


class TestCard:
    def test_number_card_value(self):
        assert Card('♠', '5').value() == 5
        assert Card('♥', '10').value() == 10

    def test_face_card_value(self):
        assert Card('♠', 'J').value() == 10
        assert Card('♥', 'Q').value() == 10
        assert Card('♦', 'K').value() == 10

    def test_ace_value(self):
        # ACEは初期値11
        assert Card('♠', 'A').value() == 11

    def test_card_str(self):
        assert str(Card('♠', 'A')) == '♠A'
        assert str(Card('♥', '10')) == '♥10'


class TestDeck:
    def test_deck_has_52_cards(self):
        deck = Deck()
        assert len(deck) == 52

    def test_deal_reduces_count(self):
        deck = Deck()
        deck.deal()
        assert len(deck) == 51

    def test_deal_returns_card(self):
        deck = Deck()
        card = deck.deal()
        assert isinstance(card, Card)

    def test_deck_is_shuffled(self):
        # 2つのデッキの順序が異なることを確認（稀に同じになる可能性はある）
        deck1 = Deck()
        deck2 = Deck()
        cards1 = [str(deck1.deal()) for _ in range(10)]
        cards2 = [str(deck2.deal()) for _ in range(10)]
        assert cards1 != cards2
