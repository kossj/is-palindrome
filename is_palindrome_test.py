import is_palindrome

solution = is_palindrome.Solution()

# These are the testcases your code will be tested against.
# You can run them as your code will be graded using the command pytest.

# To do this, run python -m pip install -r requirements.txt to install the required
# pytest package. Then, simply type pytest into your terminal.

def test():
    assert solution.isPalindrome("racecar") is True
    assert solution.isPalindrome("not_a_palindrome") is False
