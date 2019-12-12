import matplotlib.pyplot as plt   

days=[1,2,3,4,5]
sleeping=[5,6,7,5,6]
eating=[2,3,2,2,1]
working=[7,8,9,8,7]
playing=[2,3,2,3,2]


#no labels in stack plots
#work arround to it
plt.plot([],[],color='m',label='sleeping')
plt.plot([],[],color='c',label='eating')
plt.plot([],[],color='r',label='working')
plt.plot([],[],color='b',label='playing')


plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','b'])


plt.xlabel('x')
plt.ylabel('y')
plt.title("Graph")


plt.show()