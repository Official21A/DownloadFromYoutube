import pytube
import sys
import os
import datetime

MAIN_DIR = "/TubeDownloads"

if not os.path(MAIN_DIR).exists():
	os.mkdir(MAIN_DIR)

# get user input link
url = input("Enter the link >> ")

start = datetime.datetime.now()

if url == "":
	# in case of not entering 
	url="https://www.youtube.com/watch?v=4SFhwxzfXNc"

# an instance of your YouTube
try:
	youtube = pytube.YouTube(url)
except:	
	print(">: 404 Faild. Check your network or url and try again.")
	sys.exit(-1)

# see all kind of streams we have
for i in video.streams.all():
	print(i)

resolution = input("Enter resolution >> ")	

if not resolution in video.streams.all:
	print(">:> Not valid!")
	sys.exit(-1)

# choose the first one
video = youtube.streams.get_by_resolution(resolution)

print(f">?:Video={video.default_filename}/Size={video.filesize}::started>")
# download it
video.download() # also can input a folder to save into it

finish = datetime.datetime.now()
total = (finish - start).total_seconds()

print(f">: Download complete. \"OK\" Time::{total} seconds")