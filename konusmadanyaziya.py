import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile('Kayıt.wav') as source:
    audio = recognizer.record(source)  # tüm dosyayı oku

try:
    text = recognizer.recognize_google(audio, language="tr-TR")
    print("Ses metni:")
    print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition sesi anlayamadı.")
except sr.RequestError as e:
    print(f"Google hizmetine erişilemedi; hata: {e}")
