
from __future__ import unicode_literals
import youtube_dl
import os

filedir = os.path.join('C:/Users/user/Downloads/Video')

def menu():
	print("------------------Youtube Video Downloader--------------------\n")
def copyright():
		print("\n----------------------© 2020@dendirzkkptr----------------------")

menu()


url = input("Masukan URL : ")
ydl_opts = {}
os.chdir(filedir)
print("\n[+} Lokasi Penyimpanan "+filedir)
print("[+] Download Video dimulai...")
print("\n")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

copyright()


