#checked iterations 4mil-5mil in <3.36 seconds (minus whatever my reaction time is)
#checked iterations 20mil - 30mil in <29.51 seconds

try:
	f = open('CMax.txt', 'r')
	CMax = int(f.read())
	f.close()
except FileNotFoundError:
	CMax = 0

	
def Check_Number(n):
	#if n < CMax:
	#	print(n, "has been found.")

	steps = 0
	t = True
	save = n
	
	if n==0 or n==1 or n==2:
		return(0)
		
	while n != 4: #if this is infite loop we broke it :D
		print(str(n)[:-2])
		if (n % 2 == 0):			#even
			n = n / 2
			steps += 1
		else:
			n = (n * 3 + 1) / 2		#odd
			steps += 2
	#print(save, "reduces to 4 in", steps, "steps.")	
	return(steps)
	


try:
	n = int(input("Enter the number you want to check: "))
except ValueError:
	print("INCORRECT INPUT: please enter a positive integer.")
	exit()
l = Check_Number(n)
print(n, "reduces to 4 in", l, "steps.")

def Check_Lots_Of_Numbers():
	import csv
	step_dict = {}
	k = int(input("Enter how many additional numbers you want to test (in millions): ")) * 1000000
	
	for j in range(0,k+1):
		n = Check_Number(j)
		if n in step_dict:
			step_dict[n].append(j)
		else:
			step_dict[n] = [j]
	
	#csv reads nested lists not dictionaries so:
	data = []
	for key in step_dict:
		data.append([key, len(step_dict[key])])
	
	with open("data.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(data)
	
#Check_Lots_Of_Numbers()	