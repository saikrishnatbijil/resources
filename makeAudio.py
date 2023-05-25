from gtts import gTTS

# text = str(input("Paste the script ::: "))
text = "Have you ever wondered how much money mrbeast spent to make his studio. When Mrwhoosetheboss interviewed mrbeast, Mrwhoosetheboss counted the total value, and the total is 14 Million Dollars. Sub for more."
# text = "Exciting news just dropped! Google Pixel Fold is here Stay tech-savvy"

tts = gTTS(text=text, lang='en', tld='us', slow=False)
tts.save('audio.mp3')
