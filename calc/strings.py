def reverse(text):
    return text[::-1]


def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())


def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
