import pytube

url="https://www.youtube.com/watch?v=4SFhwxzfXNc"

youtube = pytube.YouTube(url)

video = youtube.streams.first()

print(video.title, video.video_id, video.age_restricted)

for i in video.streams.all():
	print(i)

video.download()
