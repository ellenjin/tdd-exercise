from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  hand = [3, 4]
  score = blackjack_score(hand)
  assert score == 7

# @pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  hand = [2, 'Queen']
  score = blackjack_score(hand)
  assert score == 12

# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  hand = [8, 'Ace']
  score = blackjack_score(hand)
  assert score == 19


# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  hand = [8, 3, 5, 'Ace']
  score = blackjack_score(hand)
  assert score == 17

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  hand = [8, 3, 0, 'Ace']
  score = blackjack_score(hand)
  assert score == "Invalid"


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  hand = [2, 3, 4, 'Ace', 5, 'Queen']
  score = blackjack_score(hand)
  assert score == "Invalid"

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  hand = [4, 4, 5, 2, 'Queen']
  score = blackjack_score(hand)
  assert score == "Bust"

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
  hand = ['Ace', 'Ace', 'King']
  score = blackjack_score(hand)
  assert score == 12

# @pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
  hand = ['Ace', 'Ace', 'Ace', 'Ace']
  score = blackjack_score(hand)
  assert score == 14