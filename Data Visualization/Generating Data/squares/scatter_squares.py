import matplotlib.pyplot as plt

x_values=range(1, 1001)

# a list comprehension generates the y-values by looping through the x-values 
# (for x in x_values), squaring each number (x**2) and storing the results in y_values. 
# We then pass the input and output lists to scatter()
y_values=[x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# we call scatter() and use the s argument to set the size of the dots used to draw the graph
# pass color to scatter() with the name of a color to use in quotation
#You can also define custom colors using the RGB color model. To define a color, pass the c argument a tuple with three decimal values
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
# we use the axis() method to specify the range of each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()