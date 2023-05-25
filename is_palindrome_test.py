import is_palindrome

solution = is_palindrome.Solution()

# These are the testcases your code will be tested against.
# You can run them as your code will be graded using the command pytest.

def test():
    assert solution.isPalindrome("racecar") is True
    assert solution.isPalindrome("not_a_palindrome") is False
    assert solution.isPalindrome("place ecalp") is True
    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solution.isPalindrome("race a car") is False
    assert solution.isPalindrome(" ") is True
    # TODO: Add more testcases, particulary alphanumeric
