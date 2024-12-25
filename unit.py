import unittest
from unittest.mock import patch, mock_open
import json

# Test edilecek fonksiyonlar
from ogrenci_programi import save_to_json, load_from_json  # Programdaki fonksiyonlar import edilmelidir

class TestOgrenciProgrami(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_save_to_json(self, mock_json_dump, mock_open):
        # Test verisi
        data = [
            {"Ad": "Ahmet", "Vize": 60, "Final": 80, "Ortalama": 72.0},
            {"Ad": "Mehmet", "Vize": 75, "Final": 85, "Ortalama": 80.0}
        ]
        
        # Fonksiyonu çağır
        save_to_json(data)
        
        # open fonksiyonunun doğru çağrıldığını kontrol et
        mock_open.assert_called_once_with("ogrenciler.json", "w", encoding="utf-8")
        
        # json.dump fonksiyonunun doğru çağrıldığını kontrol et
        mock_json_dump.assert_called_once_with(data, mock_open(), ensure_ascii=False, indent=4)

    @patch("builtins.open", new_callable=mock_open, read_data='[{"Ad": "Ahmet", "Vize": 60, "Final": 80, "Ortalama": 72.0}]')
    @patch("json.load")
    def test_load_from_json(self, mock_json_load, mock_open):
        # mock_json_load fonksiyonunun dönmesi gereken veriyi belirt
        mock_json_load.return_value = [{"Ad": "Ahmet", "Vize": 60, "Final": 80, "Ortalama": 72.0}]
        
        # Fonksiyonu çağır
        result = load_from_json()
        
        # open fonksiyonunun doğru çağrıldığını kontrol et
        mock_open.assert_called_once_with("ogrenciler.json", "r", encoding="utf-8")
        
        # json.load fonksiyonunun doğru çağrıldığını kontrol et
        mock_json_load.assert_called_once_with(mock_open())
        
        # Sonucun doğru olduğunu kontrol et
        self.assertEqual(result, [{"Ad": "Ahmet", "Vize": 60, "Final": 80, "Ortalama": 72.0}])

    @patch("builtins.open", new_callable=mock_open)
    def test_load_from_json_file_not_found(self, mock_open):
        # FileNotFoundError durumunda boş bir liste döndürmeliyiz
        mock_open.side_effect = FileNotFoundError
        
        result = load_from_json()
        
        # Dosya bulunmadığında boş bir liste dönecek
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
