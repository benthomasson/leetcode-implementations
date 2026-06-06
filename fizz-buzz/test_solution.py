from solution import Solution


def test_example_1():
    assert Solution().fizzBuzz(3) == ["1", "2", "Fizz"]


def test_example_2():
    assert Solution().fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_example_3():
    assert Solution().fizzBuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz",
    ]


def test_n_1():
    assert Solution().fizzBuzz(1) == ["1"]


def test_n_30():
    result = Solution().fizzBuzz(30)
    assert len(result) == 30
    assert result[14] == "FizzBuzz"  # 15
    assert result[29] == "FizzBuzz"  # 30
    assert result[2] == "Fizz"      # 3
    assert result[4] == "Buzz"      # 5
