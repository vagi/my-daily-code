import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.plot([0.001, 1],[0,0])
plt.plot([0, 0],[0.001, 1])
plt.plot([-0.001, -1],[0,0])
plt.plot([0, 0],[-0.001, -1])
plt.xlabel('Axis X')
plt.ylabel('Axis Y')

plt.subplot(1,2,2)
firms = ['first quarter\nX>0 Y>O', 'second quarter\nX<0, Y>O', 'third quarter\nX<0, Y<O',
         'fourth quarter\nX>0, Y<O']
market = [10,10,10,10]
Explode= [0.06,0.06,0.06,0.06]
plt.pie(market,explode=Explode,labels=firms,shadow=True,startangle=0)
plt.axis('equal')
plt.legend(loc='lower center',fontsize=7, title='Field of the Quarters')


plt.show()