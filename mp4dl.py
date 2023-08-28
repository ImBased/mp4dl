import time
import os
import yt_dlp
from yt_dlp import YoutubeDL
from os import path
#Due to tiktok being kinda of a goober
#User must state if it is a tiktok or youtube(any video tbh)
print (
'''
███╗░░░███╗██████╗░░░██╗██╗██████╗░██╗░░░░░
████╗░████║██╔══██╗░██╔╝██║██╔══██╗██║░░░░░
██╔████╔██║██████╔╝██╔╝░██║██║░░██║██║░░░░░
██║╚██╔╝██║██╔═══╝░███████║██║░░██║██║░░░░░
██║░╚═╝░██║██║░░░░░╚════██║██████╔╝███████╗
╚═╝░░░░░╚═╝╚═╝░░░░░░░░░░╚═╝╚═════╝░╚══════╝
mp4dl.exe (v1.1)

made by https://github.com/imbased
helped by https://github.com/griimnak
^true homie ong


       ''')
def main():
  mode = input('Choose mode: "MP3" or "video" or "tiktok": ')

  videos_path = path.abspath("videos/")
  videos_full_path = videos_path+'/%(title)s.%(ext)s'
  music_path = path.abspath("music/")
  music_full_path = music_path+'/%(title)s.%(ext)s'


  if mode == 'video':
      url = input('Paste YouTube, Twitter, Anime or Bitchute video url: ')
      ydl_opts = {
      "outtmpl" : videos_full_path.format(url),
      'format': 'mp4/bestvideo+bestaudio/best',
      'postprocessor_args' : '-id3v2_version 3',
}

      with YoutubeDL(ydl_opts) as ydl:
       ydl.download(url)
       main()


  if mode == 'tiktok':
      url = input('Paste a TikTok link ')
      ydl_opts = {
      "outtmpl" : videos_full_path.format(url),
      'format': 'best[vcodec=h264][vcodec!=?h265]',
      'postprocessor_args' : '-id3v2_version 3',
   }
#done^?
      with YoutubeDL(ydl_opts) as ydl:
       ydl.download(url)
       main()

  if mode == 'mp3':
      url = input('Paste YouTube, Twitter, Tiktok, Anime or Bitchute video url: ')
      ydl_opts = {
      "outtmpl" : music_full_path.format(url),
      'format': 'bestaudio/best/',
          'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
          }]

   }

      with YoutubeDL(ydl_opts) as ydl:
       ydl.download(url)
       main()
       
main ()


#todo
#bestvideo+bestaudio/
#-o video/%(title)s.%(ext)s'.format(url))✓
#--retries infinite 
# -f (bv*+ba/b)[vcodec!=?h265] "{}" ✓
# --embed-thumbnail ✓?(i mean it already embeds?)
# --postprocessor-args "-id3v2_version 3" ✓
#videos_full_path.format(url),✓
#add mp3(needs ffmpeg.exe rip )
