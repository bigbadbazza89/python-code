def score_guess(guess, target):
    """This function returns clues for a game of wordle.
    Args:
        guess - some guess
        target - some target

    Example:
    score_guess("hello", "world")
    (0,0,0,2,1)
    """
    return (0,0,1,2,1)

import doctest

doctest.testmod()
# imagine this test automation
assert score_guess("hello", "world") == (0,0,0,2,1)