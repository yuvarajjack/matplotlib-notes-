import matplotlib.pyplot as plt
import numpy as np
#(1,2,1) means left side
plt.subplot(1,2,1)
plt.plot([1,2,3,4],[2,4,6,9], "go")
plt.title("1st Subplot")

#(1,2,2) means 2nd subplot right
plt.subplot(1,2,2)
plt.plot([1,2,3,4],[10,23,22,4], "r^")
plt.title("2 subplot")
plt.show()
