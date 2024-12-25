def hesapla_gecme_notu(vize: float, final: float) -> str:
    """
    Bu fonksiyon, vize ve final notlarına göre öğrencinin geçme notunu hesaplar.

    Args:
    vize (float): Öğrencinin vize sınavı notu.
    final (float): Öğrencinin final sınavı notu.

    Returns:
    str: Öğrencinin geçme durumu ("Geçti" veya "Kaldı").
    """
    gecme_notu = (vize * 0.4) + (final * 0.6)

    if gecme_notu >= 50:
        return "Geçti"
    else:
        return "Kaldı"
