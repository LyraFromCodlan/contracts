percentages = [float(percent)*0.01+1 for percent in input("Enter increase percantages of 3 consecutive years separated by space: ").split()]



print("Average growth in productivity per year for 3 consecutive years is "+str((percentages[0]*percentages[1]*percentages[2]-1)*100/3) + "%")