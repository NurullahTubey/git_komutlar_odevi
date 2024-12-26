# unit_test_runner.py
import pytest

def run_tests():
    """Pytest testlerini çalıştır ve sonuçları döndür."""
    # Testleri çalıştır
    result = pytest.main(["unit.py", "--tb=no", "--disable-warnings"])

    # Sonuçları yorumla
    if result == 0:
        return "Tüm testler başarılı!"
    else:
        return f"{result} test başarısız oldu!"

# Test çalıştırma
if __name__ == "__main__":
    sonuc = run_tests()
    print(sonuc)

