import matplotlib.pyplot as plt
import numpy as np
name = ["Yuvi", "Gokul","Sasi"]
age = [19,25,22]
#bar takes color arguments
plt.bar(name, age, color = 'pink')
plt.title("Bar !")
plt.xlabel("name")
plt.ylabel("age")
plt.show()
