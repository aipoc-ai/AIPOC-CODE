import os
import vlc 
from time import sleep
import pafy 
from search_youtube.search_youtube import search
#for playing video
with open('AIPOC/AIPOC/features/play_music/audio_query.txt','r') as fb:
        query=fb.readline()
url = search(str(query))
video = pafy.new(url) 
  
 
best = video.getbest() 
  
 
media = vlc.MediaPlayer(best.url) 
  
media.play() 


sleep(5)
while media.is_playing():
     sleep(1)

      