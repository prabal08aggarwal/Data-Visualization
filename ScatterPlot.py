import matplotlib.pyplot as plt   



x=[1,2,3,4,5,6,7,8]
y=[3,4,5,6,2,6,8,9]
plt.scatter(x,y,label='plot',color='k')
#plt.scatter(x,y,label='plot2',color='r',marker='*')

plt.xlabel('x')
plt.ylabel('y')
plt.title("Graph")
plt.legend()

plt.show()