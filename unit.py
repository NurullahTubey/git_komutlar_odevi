import unittest
from Deneme import hesapla_gecme_notu  # Burada 'Deneme.py' dosyasındaki fonksiyonu import ediyoruz

class TestHesaplaGecmeNotu(unittest.TestCase):

    def test_gecme(self):
        """Geçme durumu testi (50 ve üzeri notlar için)"""
        self.assertEqual(hesapla_gecme_notu(60, 60), "Geçti")
        self.assertEqual(hesapla_gecme_notu(70, 50), "Geçti")
        self.assertEqual(hesapla_gecme_notu(40, 80), "Geçti")
    
    def test_kalma(self):
        """Kalma durumu testi (50 altı notlar için)"""
        self.assertEqual(hesapla_gecme_notu(40, 40), "Kaldı")
        self.assertEqual(hesapla_gecme_notu(20, 40), "Kaldı")
        self.assertEqual(hesapla_gecme_notu(30, 20), "Kaldı")
    
    def test_sinirlarda_gecme(self):
        """Sınırda geçme testi (tam olarak 50 alan öğrenci)"""
        self.assertEqual(hesapla_gecme_notu(50, 50), "Geçti")
        self.assertEqual(hesapla_gecme_notu(45, 55), "Geçti")
    
    def test_sinirlarda_kalma(self):
        """Sınırda kalma testi (tam olarak 49.99 alan öğrenci)"""
        self.assertEqual(hesapla_gecme_notu(40, 50), "Kaldı")
        self.assertEqual(hesapla_gecme_notu(30, 40), "Kaldı")

if __name__ == '__main__':
    unittest.main()
