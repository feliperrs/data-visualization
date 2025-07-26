# ---------------------------------------------------------------------------- #
#!                     CALCULANDO AUTOMATICAMENTE OS DADOS                     #
# ---------------------------------------------------------------------------- #

import matplotlib.pyplot as plt

x_values = range(1, 1001)   # cria valores de x entre 1 e 1000
y_values = [x**2 for x in x_values] # eleva esses valores ao quadrado

plt.style.use('ggplot')

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=10)   # passa uma lista de valores x, y

ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)


ax.tick_params(labelsize=14)

# Define o intervalo para cada eixo

ax.axis([0,1100, 0, 1_100_000])

plt.show()