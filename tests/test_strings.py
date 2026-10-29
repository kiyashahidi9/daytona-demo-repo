from calc.strings import reverse, capitalize_words


def test_reverse():
    assert reverse("daytona") == "anotyad"


def test_capitalize_words():
    assert capitalize_words("hello sandbox world") == "Hello Sandbox World"
