from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create Two  D6 dice.
# we create an instance of Die with the default six sides.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
# we roll the die 1000 times and store the results of each roll in the list results.
results = []
for roll_num in range(50_000):
    # After creating two instances of Die, we roll the dice and calculate the sum of the two dice for each roll.
    result = die_1.roll()+die_2.roll()
    results.append(result)

# Analyze the results.

# To analyze the rolls, we create the empty list frequencies to store the number of times each value is rolled.
frequencies = []

# We loop through the possible values (1 through 6 in this case)
# The largest possible result (12) is the sum of the largest number on both dice, which we store in max_result.
max_result =die_1.num_sides +die_2.num_sides

# The smallest possible result (2) is the sum of the smallest number on both dice.
#  When we analyze the results, we count the number of results for each value between 2 and max_result.
for value in range(2, max_result+1):

    # count how many times each number appears in results
    frequency = results.count(value)

    # and then append this value to the frequencies list
    frequencies.append(frequency)

# Visualize the results.

# We store these in a list called x_values, which starts at 1 and ends at the number of sides on the die.
x_values = list(range(2, max_result+1))

# Plotly doesn’t accept the results of the range() function directly, so we need to convert the range to a list explicitly using the list() function.
# The Plotly class Bar() represents a data set that will be formatted as a bar chart.
data = [Bar(x=x_values, y=frequencies)]

# Each axis can be configured in a number of ways, and each configuration option is stored as an entry in a dictionary. 
# At this point, we’re just setting the title of each axis.
# When creating the chart, we include the dtick key in the x_axis_config dictionary.
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config ={'title': 'Frequency of Result'}

# The Layout() class returns an object that specifies the layout and configuration of the graph as a whole.
# Here we set the title of the graph and pass the x- and y-axis configuration dictionaries as well.
my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)

# To generate the plot, we call the offline.plot() function.
# This function needs a dictionary containing the data and layout objects, and it also accepts a name for the file where the graph will be saved. We store the output in a file called d6.html.
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
