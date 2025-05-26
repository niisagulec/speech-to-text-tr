# Ses Dosyasından Metin Çevirme (Speech-to-Text)

Bu proje, bir `.wav` uzantılı ses dosyasındaki konuşmayı metne dönüştürmek için Python'daki `speech_recognition` kütüphanesini kullanır. Özellikle Türkçe dilindeki konuşmaları tanımak için `Google Speech Recognition API` kullanılmıştır.

## Özellikler

- `.wav` dosyasındaki sesi okuyup yazıya döker.
- Google’ın konuşma tanıma servisini kullanır.
- Türkçe dil desteği ile çalışır (`language="tr-TR"`).

## Gereksinimler

- Python 3.x
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- `Kayıt.wav` isimli bir ses dosyası (proje dizininde yer almalı)

## Kurulum

Aşağıdaki komutu çalıştırarak gerekli kütüphaneyi yükleyebilirsiniz:

```bash
pip install SpeechRecognition
