import re
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
				alt = re.search(r"(alt=\".*\"></a)(.*)",contents[z:]) 
				wmat = re.search(r"(width=\")([0-9]*)",contents[z:]) 
				hmat = re.search(r"(height=\")([0-9]*)",contents[z:])
					

				wid = wmat.group(2) if wmat else None
				hi = hmat.group(2) if hmat else None
				alt = alt.group(1) if alt else None
				
				a = (alt[:-3])
				
				if int(wid) > int(hi):
					f ="\"900\"  "
				else:
					f ="\"500\"  "

			#	print(hi)
			#	print(wid)
				
				y = y + 1	
			#	print("\n",file = filewr)
				print("\n"+'<p>'+str(y)+'. ', file = filewr)
				print('<br>'+contents[q:z2+2]+str(f)+str(a), file = filewr)
			#	print('\n', file = filewr)
				z2 = z2 + 1
				z = z + 1

		#	elif contents[z:z2] == "alt=":

		#		z2 = z2 + 1
		#		z = z + 1

			else:
				z = z + 1
				z2 = z2 + 1
