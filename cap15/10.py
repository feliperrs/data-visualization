# ---------------------------------------------------------------------------- #
#!                             USANDO UM COLORMAP                              #
# ---------------------------------------------------------------------------- #

import matplotlib.pyplot as plt

x_values = range(1, 1001)   
y_values = [x**2 for x in x_values] 

plt.style.use('ggplot')

fig, ax = plt.subplots()

# o argumento "c" é semelhante ao "color",  mas é usado para associar uma sequencia de valores a um colormap
# passamos a lista de valores y para c e, em seguida, instruimos o pyplot qual colormap usar com o argumento "cmap"
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)   

ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)


ax.tick_params(labelsize=14)

ax.axis([0,1100, 0, 1_100_000])

ax.ticklabel_format(style='plain') 

plt.show()