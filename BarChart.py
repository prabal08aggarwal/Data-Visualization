import matplotlib.pyplot as plt   

x=[2,4,6,8,10]
y=[6,7,8,2,4]
plt.bar(x,y,label='Bar1',color='r')

x2=[1,3,5,7,7]
y2=[6,7,8,2,4]
plt.bar(x2,y2,label='Bar2',color='c')


plt.xlabel('x')
plt.ylabel('y')
plt.title("Graph")
plt.legend()

plt.show()