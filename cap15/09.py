# ---------------------------------------------------------------------------- #
#!                       DEFININDO CORES PERSONALIZADAS                        #
# ---------------------------------------------------------------------------- #

import matplotlib.pyplot as plt

x_values = range(1, 1001)   
y_values = [x**2 for x in x_values] 

plt.style.use('ggplot')

fig, ax = plt.subplots()

# altera a cor do ponto, pode usar tanto nome da cor quanto RGB
ax.scatter(x_values, y_values, color=(0, 0.9, 0), s=10)   

ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)


ax.tick_params(labelsize=14)

ax.axis([0,1100, 0, 1_100_000])

ax.ticklabel_format(style='plain') 

plt.show()