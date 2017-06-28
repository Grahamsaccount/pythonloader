y = 0
z2 = 3
zold = 0
z = 0
q = 0
filenew = open("input_file.txt","r")
filewr = open
with open() as x:

	if "jpg" in x:

		m = len(x)

		while z < m :
			if x[z:z2] == "src" :
				q = z
				z2 = z2 +1
				z = z +1 

			elif x[z:z2] == "jpg" :
				y = y + 1
				z = z + 1
				print("\n")
				print(y)
				print("\n")
				print(x[q:z2])
				print("\n")
				zold = z2
				z2 = z2 + 1
	
			else:
				z = z + 1
				z2 = z2 + 1
