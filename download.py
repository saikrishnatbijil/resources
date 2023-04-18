from pytube import YouTube
from pydub import AudioSegment
import ssl
import os
ssl._create_default_https_context = ssl._create_unverified_context

link = str(input('Enter Youtube Video URL :: '))
# resolution = str(input('Resolution ex: 720p, 1080p :: '))
formatOfVid = str(input('Format mp3/mp4 :: ')).lower()
yt = YouTube(link)

stream = yt.streams.get_highest_resolution()
# print(yt.streams)
video_file = stream.download(output_path="/Users/macintoshhd/Downloads",filename=yt.title+".mp4")

if formatOfVid == 'mp3':
    audio = AudioSegment.from_file(video_file, format="mp4")
    audio.export("/Users/macintoshhd/Downloads/"+yt.title+".mp3", format="mp3")
    os.remove(video_file)
else :
    print('Audio export failed')
    