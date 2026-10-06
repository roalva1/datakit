from datakit.stats import mean_numeric


def test_mean_numeric():
    assert mean_numeric([10, 20, 30]) == 20.0


def test_mean_numeric_ignores_none():
    assert mean_numeric([10, None, 30]) == 20.0


def test_mean_numeric_empty_values_returns_none():
    assert mean_numeric([]) is None


def test_mean_numeric_only_missing_values_returns_none():
    assert mean_numeric([None, None]) is None

def test_mean_numeric_with_minimum():
    assert mean_numeric([10, 20, 30], minimum=15) == 25.0

def test_mean_numeric_with_minimum_excludes_all():
    assert mean_numeric([10, 20, 30], minimum=35) is None

def test_mean_numeric_with_minimum_and_none_values():
    assert mean_numeric([10, None, 30], minimum=15) == 30.0


def test_mean_numeric_with_minimum_excludes_all_and_none_values():
    assert mean_numeric([1, 2], minimum=10) is None

def test_mean_numeric_with_minimum_and_none_values_including_lower_bound():
    assert mean_numeric([None, 10, 20], minimum=10) == 15.0
