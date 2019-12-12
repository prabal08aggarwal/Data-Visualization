import matplotlib.pyplot as plt   


#legends are used to distinguish between lines
x= [1,2,3]
y=[5,7,4]

x2=[4,5,6]
y2=[6,8,9]

plt.plot(x,y,label="Line 1")
plt.plot(x2,y2,label='line 2')

plt.xlabel('Plot Number')
plt.ylabel('Var')
plt.title("Graph")

plt.legend()

plt.show()