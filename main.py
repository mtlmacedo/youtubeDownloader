from pytube import YouTube
import sys

url = sys.argv[1]

video = YouTube(url)
video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

print(video.title)
print(sys.argv[1])
