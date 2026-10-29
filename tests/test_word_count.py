from calc.strings import word_count


def test_word_count():
    assert word_count("one sandbox per agent") == 4
    assert word_count("") == 0
