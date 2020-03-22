import pytube										#import pytube
url=input("Enter the youtube URL")					#store user input of youtube url into URL variable
video=pytube.YouTube(url)							#parse the url and store the expression into video variable
youtube=video.streams.first() 						#define youtube variable - call the video variable and have it stream
youtube.download(r"C:\Users\USER\Desktop")		#invoke youtube.download function and specify where you want to store the downloaded video
