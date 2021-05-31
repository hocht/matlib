import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth = 3)

#set chart title and label axes.
ax.set_title("Square numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of  value", fontsize = 14)

# Set of tick labels.
ax.tick_params(axis ='both',labelsize = 14)

plt.show()