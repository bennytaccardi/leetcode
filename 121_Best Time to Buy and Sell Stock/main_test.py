import pytest
from main import Solution

@pytest.mark.parametrize("test_input,expected", [
    ([7,6,4,3,1], 0),
    ([7,1,5,3,6,4], 5),
    ([7,3,5,3,1,10], 9)])
def test_max_profit(test_input, expected):
    s = Solution()
    res = s.maxProfit(test_input)
    assert res == expected