banner ="""
    _       _     _   _____           _         ____  
   / \   __| | __| | |_   _|__   ___ | |___   _|  _ \ 
  / _ \ / _` |/ _` |   | |/ _ \ / _ \| / __| (_) | | |
 / ___ \ (_| | (_| |   | | (_) | (_) | \__ \  _| |_| |
/_/   \_\__,_|\__,_|   |_|\___/ \___/|_|___/ (_)____/                        
\t
\t [ nicedre4m@yahoo.com ]
"""
print (banner)
print ("""
[ 1. Add http:// On Beginning List ]
[ 2. Add https:// On Beginning List ]
[ 3. Add /wp-login.php On End List ]
[ 4. Add / On End List ]
[ 5. Add /xmlrpc.php On End List ]
""")

xploitsec = raw_input("root@youez:~# ")

class youez():

	def httpbeg(self):
		kep = raw_input("Your List : ")
		kep = open(kep, 'r')
		for i in kep:
			i = i.rstrip()
			print("http://"+i)
			with open('http.txt', 'a') as o:
				o.write("http://" + i + '\n')
		print("[ >> ] root@youez:~# successfully !! check http.txt !!")

	def wplogin(self):
		kep = raw_input("Your List : ")
		kep = open(kep, 'r')
		for i in kep:
			i = i.rstrip()
			print(i+"/wp-login.php")
			with open('wplog.txt', 'a') as o:
				o.write(i + "/wp-login.php" + '\n')
		print("[ >> ] root@youez:~# successfully !! check wplog.txt !!")

	def slashend(self):
		kep = raw_input("Your List : ")
		kep = open(kep, 'r')
		for i in kep:
			i = i.rstrip()
			print(i+"/")
			with open('slashend.txt', 'a') as o:
				o.write(i + "/" + '\n')
		print("[ >> ] root@youez:~# successfully !! check slashend.txt !!")

	def httpsbeg(self):
		kep = raw_input("Your List : ")
		kep = open(kep, 'r')
		for i in kep:
			i = i.rstrip()
			print("https://"+i)
			with open('https.txt', 'a') as o:
				o.write("https://" + i + '\n')
		print("[ >> ] root@youez:~# successfully !! check https.txt !!")

	def xmlrpc(self):
		kep = raw_input("Your List : ")
		kep = open(kep, 'r')
		for i in kep:
			i = i.rstrip()
			print(i+"/xmlrpc.php")
			with open('xmlrpc.txt', 'a') as o:
				o.write(i + "/xmlrpc.php" + '\n')
		print("[ >> ] root@youez:~# successfully !! check xmlrpc.txt !!")

dahah = youez()
if xploitsec == '1':
	dahah.httpbeg()
elif xploitsec == '2':
	dahah.httpsbeg()
elif xploitsec == '4':
	dahah.slashend()
elif xploitsec == '5':
	dahah.xmlrpc()
elif xploitsec == '3':
	dahah.wplogin()
else:
	print("?? pilih dulu yg mana goblok")
	