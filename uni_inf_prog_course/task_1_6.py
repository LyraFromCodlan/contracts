percentages = [int(percent)+100 for percent in input("Enter increase percentages of 3 consecutive years separated by space: ").split()]
agr = int(
            round((percentages[0]*percentages[1]*percentages[2])**(1/3)-100,0)
        )
print("Average growth in productivity per year for 3 consecutive years is "+str(agr)+"%")