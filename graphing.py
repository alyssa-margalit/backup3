import matplotlib.pyplot as plt
#matplotlib inline
plt.style.use('ggplot')

x = ['Wizard', 'Hero', 'Villain', 'Peasant']
energy = [5, 6, 15, 22]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, energy, color='green')
plt.xlabel("people")
plt.ylabel("numbers")
plt.title("people trying to get treasure")

plt.xticks(x_pos, x)

plt.show()