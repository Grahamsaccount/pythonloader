y = 0
z2 = 4
z = 0
q = 0

rea  = "/home/graham/Internship/Work/python/pythonloader/input_file.txt"
wri = "graham_export_file.txt"
filen = open(rea,"r")
filewr = open(wri,"w")
with open(rea,"r") as x:
	contents = x.read()

	if "jpg" in contents:

		m = len(contents)
	
		while z2 < m :
			if contents[z:z2] == "<img" :
				q = z
				z2 = z2 +1
				z = z +1 

			elif contents[z:z2] == "widt" :
				w = z2 + 4
				w2 = w + 3
				if w2 != 1 or w2 != 2 or w2 != 3 or w2 != 4 or w2 != 5 or w2 != 6 or w2 != 7 or w2 != 8 or w2 != 9 or w2 != 0:
					w2 = w2 - 1

				h = w2 + 11
				h2 = h + 3
				if h2 != 1 or h2 != 2 or h2 != 3 or h2 ! =  4 or h2 != 5 or h2 !=  6 or h2 != 7 or h2 != 8 or h2 != 9 or h2 != 0:
					h2 = h2 - 1
				
				wid = int(contents[w:w2])
				hi = int(contents[h:h2])
				if wid > hi:
					f = "900"
				else:
					f = "500"

				y = y + 1	
				print("\n")
				print('<p>'+str(y)+'.')
				print('<br>'+contents[q:z2+2]+f)
				print('\n')
				z2 = z2 + 1
				z = z + 1

			elif contents[z:z2] == "alt=":
				z2 = z2 + 1
				z = z + 1

			else:
				z = z + 1
				z2 = z2 + 1
