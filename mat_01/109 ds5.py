
#scatter plots:

import matplotlib.pyplot as plt

month=[1,2,3,4,5,6,7]
sales=[20,15,25,40,30,35,20]

plt.scatter(month,sales, label='mobilesales', color='g', s=25, marker="o")

plt.xlabel('month')
plt.ylabel('sales')
plt.title('mobile sales Analysis')
plt.legend()
plt.show()
