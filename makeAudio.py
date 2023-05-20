from gtts import gTTS

text = str(input("Paste the script ::: "))
# text = "Today, we have some exciting news from Google's Pixel lineup. Google is entering the world of foldable devices with their highly anticipated Pixel Fold.The Pixel Fold features a stunning flexible display that seamlessly transitions between phone and tablet modes, giving you the best of both worlds. The Pixel Fold has a powerful camera system, capturing stunning photos and videos. Google's Pixel Fold also comes with top-of-the-line processing power, ensuring smooth multitasking and snappy performance.That's all for today's exciting tech update! Stay tuned for more news on the Pixel Fold's official release date and pricing. Don't forget to hit on subscribe, so you don't miss any future updates and I'll catch you in the next video. Stay tech-savvy"
tts = gTTS(text=text, lang='en', tld='co.uk', slow=False)
tts.save('audio.mp3')
