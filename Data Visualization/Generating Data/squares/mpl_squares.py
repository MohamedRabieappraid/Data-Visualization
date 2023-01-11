import matplotlib.pyplot as plt 

input_values =  [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]


plt.style.use('seaborn-v0_8')
# we follow another common Matplotlib convention by calling the subplots() function
# This function can generate one or more plots in the same figure.
# The variable fig represents the entire figure or collection of plots that are generated.
# The variable ax represents a single plot in the figure and is the variable we’ll use most of the time.
fig, ax = plt.subplots()

# We then use the plot() method, which will try to plot the data it’s given in a meaningful way.
# The linewidth parameter at  controls the thickness of the line that plot() generates.
ax.plot(input_values, squares, linewidth = 3)

# Set chart title and label axes.

# The set_title() method at  sets a title for the chart.
ax.set_title("square Numbers", fontsize=24)

#The set_xlabel() and set_ylabel() methods allow you to set a title for each of the axes
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
# the method tick_params() styles the tick marks
ax.tick_params(axis='both', labelsize=14)

# The function plt.show() opens Matplotlib’s viewer and displays the plot
plt.show()
