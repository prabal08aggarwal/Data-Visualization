import matplotlib.pyplot as plt   

ages=[22,55,66,76,3,78,12,10,2,45]

bins=[0,10,20,20,30,40,50,60,70,80]

plt.hist(ages,bins,histtype='bar',rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title("Graph")


plt.show()