

# pie chart:
import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,        #starting from 90 angle
        shadow= True,
        explode=(0,0,0.3,0),  
        autopct='%1.2f%%'    
        )

plt.title('Interesting Graph\nCheck it out')
plt.show()
