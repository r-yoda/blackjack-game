import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from card import Card
from player import Hand, Player


class TestHand:
    def test_total_normal(self):
        hand = Hand()
        hand.add_card(Card('♠', '7'))
        hand.add_card(Card('♥', '8'))
        assert hand.total() == 15

    def test_ace_counts_as_11(self):
        hand = Hand()
        hand.add_card(Card('♠', 'A'))
        hand.add_card(Card('♥', '7'))
        assert hand.total() == 18

    def test_ace_counts_as_1_when_bust(self):
        hand = Hand()
        hand.add_card(Card('♠', 'A'))
        hand.add_card(Card('♥', '9'))
        hand.add_card(Card('♦', '5'))
        # A=11だと25でバスト → A=1で計算して15
        assert hand.total() == 15

    def test_double_ace(self):
        hand = Hand()
        hand.add_card(Card('♠', 'A'))
        hand.add_card(Card('♥', 'A'))
        # A=11+1=12（両方11だと22でバスト）
        assert hand.total() == 12

    def test_blackjack(self):
        hand = Hand()
        hand.add_card(Card('♠', 'A'))
        hand.add_card(Card('♥', 'K'))
        assert hand.is_blackjack() is True
        assert hand.total() == 21

    def test_not_blackjack_with_three_cards(self):
        hand = Hand()
        hand.add_card(Card('♠', '7'))
        hand.add_card(Card('♥', '7'))
        hand.add_card(Card('♦', '7'))
        assert hand.is_blackjack() is False

    def test_bust(self):
        hand = Hand()
        hand.add_card(Card('♠', '10'))
        hand.add_card(Card('♥', '8'))
        hand.add_card(Card('♦', '5'))
        assert hand.is_bust() is True

    def test_not_bust(self):
        hand = Hand()
        hand.add_card(Card('♠', '10'))
        hand.add_card(Card('♥', '8'))
        assert hand.is_bust() is False


class TestPlayer:
    def test_player_name(self):
        player = Player("テスト")
        assert player.name == "テスト"

    def test_clear_hand(self):
        player = Player("テスト")
        player.hand.add_card(Card('♠', 'A'))
        player.clear_hand()
        assert len(player.hand.cards) == 0
