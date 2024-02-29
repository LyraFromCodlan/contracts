# Integer22°. С начала суток прошло N секунд (N — целое). Найти количество секунд, прошедших с начала последнего часа. 

seconds = int(input("Enter number of saconds passed: ")) % 3600

print("Number of seconds passed in the last hour: "+str(seconds))