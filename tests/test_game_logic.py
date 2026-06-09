from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should tell the player to guess lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "Lower"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should tell the player to guess higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "Higher"

def test_first_attempt_win_scores_100_points():
    result = update_score(0, "Win", 1)
    assert result == 100

def test_later_win_scores_fewer_points():
    result = update_score(0, "Win", 3)
    assert result == 80

def test_wrong_guess_subtracts_points_consistently():
    assert update_score(10, "Too High", 1) == 5
    assert update_score(10, "Too Low", 1) == 5
