# ---------------------------------------------------------------------------- #
#!                            15.2 Cubos coloridos                             #
# ---------------------------------------------------------------------------- #

# Use um colormap ao seu grafico de cubos

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, s=10)
ax.ticklabel_format(style='plain') 

plt.show()