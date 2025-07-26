# ---------------------------------------------------------------------------- #
#!              MUDANDO O TIPO DE ROTULO E E A ESPESSURA DA LINHA              #
# ---------------------------------------------------------------------------- #

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Define o titulo do grafico e os eixos do rotulo
ax.set_title("Square Number", fontsize=24) # muda o titulo
ax.set_xlabel("Value", fontsize=14) # muda o nome do eixo x
ax.set_ylabel("Square of Value", fontsize=14) # muda o nome do eixo y

# Define o tamanho dos rotulos de marcacao de escala
ax.tick_params(labelsize=14)

plt.show()