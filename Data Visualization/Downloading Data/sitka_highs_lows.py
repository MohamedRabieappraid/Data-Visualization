import csv 
from datetime import datetime
import matplotlib.pyplot as plt

# After importing the csv module, we assign the name of the file we’re working with to filename.
# filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'

# We then open the file and assign the resulting file  object to f.
with open(filename) as f :

    # we call csv.reader() and pass it the file object as an argument to create a reader object associated with that file.
    # We assign the reader object to reader.
    reader = csv.reader(f)

    # The csv module contains a next() function, which returns the next line in the file when passed the reader object.
    # In the preceding listing, we call next() only once so we get the first line of the file, which contains the file headers.
    # We store the data that’s returned in header_row.
    header_row = next(reader)

    # The enumerate() function returns both the index of each item and the value of each item as you loop through a list.
    #for index, column_header in enumerate(header_row):
       # print(index, column_header)
    
    # Get high temperatures from this file.

    # Get dates, and high and low temperatures from this file.
    # we add the empty list lows to hold low temperatures.
    dates, highs, lows = [], [], []

    # then loop through the remaining rows in the file
    # The reader object continues from where it left off in the CSV file 
    # and automatically returns each line following its current position.
    for row in reader:

        # We then convert the data containing the date information (row[2]) to a datetime object and append it to dates.
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        # Because we’ve already read the header row, the loop will begin at the second line where the actual data begins.
        # On each pass through the loop, we pull the data from index 5, which corresponds to the header TMAX, 
        # and assign it to the variable high.
        # We use the int() function to convert the data, which is stored as a string, to a numerical format so we can use it.
        high = int(row[5])
        # and then extract and store the low temperature for each date from the seventh position in each row (row[6]) v.
        low = int(row[6])

        dates.append(current_date)
        # We then append this value to highs.
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# We pass the list of highs to plot() and pass c='red' to plot the points in red. 
# (We’ll plot the highs in red and the lows in blue).
# We pass the dates and the high temperature values to plot().
# The alpha argument at u controls a color’s transparency. 
# An alpha valueof 0 is completely transparent, and 1 (the default) is completely opaque. 
# By setting alpha to 0.5, we make the red and blue plot lines appear lighter.
ax.plot(dates, highs, c='red', alpha=0.5)

# we add a call to plot() for the low temperatures and color these values blue.
ax.plot(dates, lows, c='blue', alpha=0.5)

# we pass fill_between() the list dates for the x-values and then the two y-value series highs and lows.
# The facecolor argument determines the color of the shaded region; we give it a low alpha value of 0.1 so the filled region connects 
# the two data series without distracting from the information they represent.
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# Format plot.
# We then specify a few other formatting details, such as the title, font size, and labels, 
# which you should recognize from Chapter 15
# we update the title.
plt.title("Daily high and low temperatures - 2018", fontsize=24)

# Because we have yet to add the dates, we won’t label the x-axis, 
# but plt.xlabel() does modify the font size to make the default labels more readable.
plt.xlabel('', fontsize=16)

# The call to fig.autofmt_xdate() draws the date labels diagonally to prevent them from overlapping.
fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()