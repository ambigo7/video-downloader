import sys
import os
import re
import requests as r
import wget


filedir = os.path.join('C:/Users/user/Downloads/Video')
ERASE_Line = '\x1b[2K'

def menu():
	print("------------------Facebook Video Downloader--------------------\n")
	print("1. Download Low Resolution Video")
	print("2. Download High Resolution Video")
	print("3. Exit")
	print("\n----------------------© 2020@dendirzkkptr----------------------")


menu()
pilih = input("Masukan Pilihan Anda : ")

if pilih == "1":
	try:
		link = input("Masukan URL  : ")
		html = r.get(link)
		sdvideo.url = re.search('sd_src:"(.?+)"', html.text)[1]
	except r.ConnectionError as e:
		print("OOPS!! Koneksi Bermasalah")
	except r.Timeout as e:
		print("OOPS!! Waktu Permintaan Habis")
	except r.RequestException as e:
		print("OOPS!! URL Bermasalah/URL Tidak ditemukan")
	except (KeyboardInterrupt, SystemExit):
		print("Ok, aku keluar terima kasih")
		sys.exit(1)
	except TypeError:
		print("Mungkin Video di Private atau URL Tidak ditemukan")
	else:
		sd_url = sdvideo_url.replace('sd_src:"', '')
		print("\n")
		print("Normal Quality: "+ sd_url)
		print("\n[+} Lokasi Penyimpanan "+filedir)
		print("[+] Download Video dimulai...")
		print("\n")
		wget.download(sd_url, filedir)
		sys.stdout.write(ERASE_Line)
		print("\n")
		print("Video Selesai di Download")

elif pilih == "2":
	try:
		link = input("Masukan URL : ")
		html = r.get(link)
		hdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]
	except r.ConnectionError as e:
		print("OOPS!! Koneksi Bermasalah")
	except r.Timeout as e:
		print("OOPS!! Waktu Permintaan Habis")
	except r.RequestException as e:
		print("OOPS!! URL Bermasalah/URL Tidak ditemukan")
	except (KeyboardInterrupt, SystemExit):
		print("Ok, aku keluar terima kasih")
		sys.exit(1)
	except TypeError:
		print("Mungkin Video di Private atau URL Tidak ditemukan")
	else:
		hd_url = hdvideo_url.replace('hd_src:"', '')
		print("\n")
		print("High Quality: "+ hd_url)
		print("\n[+}Lokasi Penyimpanan "+filedir)
		print("[+] Download Video dimulai...")
		print("\n")
		wget.download(hd_url, filedir)
		sys.stdout.write(ERASE_Line)
		print("\n")
		print("Video Selesai di Download")

elif pilih == "3":
    print("Keluar")

else:
    print("[-] Masukan Keliru, SIlahkan Coba lagi!")


