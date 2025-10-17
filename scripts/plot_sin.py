import numpy as np
import matplotlib.pyplot as plt

def sin_plus_un(x):
    return np.sin(x) + 1

x = np.linspace(0, 2 * np.pi, 100)
y = sin_plus_un(x)

plt.plot(x, y)
plt.title("Graph of sin(x) + 1")
plt.xlabel("x (radians)")
plt.ylabel("sin(x) + 1")
plt.grid(True)
plt.show()
# Save the plot as an image file
plt.savefig("sin_plus_un.png")
plt.close()
