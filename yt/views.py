from django.shortcuts import render, redirect
from pytube import *
# Create your views here.
def youtube(request):
    # Checking if request method is post or not
    if request.method == "POST":
        
        # getting link from the frontend
        link = request.POST['link']
        video = YouTube(link)
        
        # setting resolution for video to be downloaded
        stream = video.streams.get_lowest_resolution()
        
        # downloads video
        stream.download()
        
        # returning back to yt page
        return render(request, 'index.html')
    return render(request, 'index.html')