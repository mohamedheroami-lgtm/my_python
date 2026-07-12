from gtts import gTTS
import os

# النص الذي سيقرأه البرنامج
text = "Hello! Python is amazing and now it can speak."

# تحويل النص لصوت
tts = gTTS(text=text, lang='en')

# حفظ الملف
tts.save("helo.mp3")

print("تم إنشاء ملف الصوت بنجاح! ابحث عن ملف باسم hello.mp3 في مدير الملفات.")
