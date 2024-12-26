# unit.py
def is_even(number):
    """Bir sayının çift olup olmadığını kontrol eder."""
    return number % 2 == 0

def test_is_even():
    assert is_even(2) is True  # Doğru
    assert is_even(3) is False  # Doğru
    assert is_even(5) is True  # Yanlış
