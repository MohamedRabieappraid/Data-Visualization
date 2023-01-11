import json 

# We import the Scattergeo chart type and the Layout class, 
# and then import the offline module to render the map.
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
# Be sure to update the filename so you’re using the 30-day data set.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:

    # We first import the json module to load the data properly from the file,
    # and then store the entire set of data in all_eq_data.
    # The json.load() function converts the data into a format Python can work with: in this case, a giant dictionary.
    all_eq_data = json.load(f)

# We take the data associated with the key 'features' and store it in all_eq_dicts. 
# We know this file contains records about 158 earthquakes,
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# We make an empty list to store the magnitudes, and then loop through the dictionary all_eq_dicts.
# We first make a list called hover_texts to store the label we’ll use for each marker.
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    # Inside this loop, each earthquake is represented by the dictionary eq_dict. 
    # Each earthquake’s magnitude is stored in the 'properties' section of this dictionary under the key 'mag'.
    # We store each magnitude in the variable mag
    mag = eq_dict['properties']['mag']

    # We make empty lists for the longitudes and latitudes. The code eq_dict['geometry'] accesses 
    # the dictionary representing the geometry element of  the earthquake.
    # The second key, 'coordinates', pulls the list of values associated with 'coordinates'.
    # Finally, the 0 index asks for the first value in the list of coordinates, which corresponds to an earthquake’s longitude.
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]

    # At we pull this information and assign it to the variable title, and then append it to the list hover_texts.
    title = eq_dict['properties']['title']

    # and then append it to the list mags.
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
# first 10 magnitude and first 5 latitudes, and longitudes 
# print(mags[:10])
# print(lons[:5])
# print(lats[:5])


# Map the earthquakes.

# bar chart, we define a list called data. We create the Scattergeo object inside this list
# because you can plot more than one data set on any visualization you make.
# A Scattergeo chart type allows you to overlay a scatter plot of geographic data on a map. 
# In the simplest use of this chart type, you only needto provide a list of longitudes and a list of latitudes.

# data = [Scattergeo(lon=lons, lat=lats)]
# Here’s an equivalent way to define the data for the current chart
data = [{
'type': 'scattergeo',
'lon': lons,
'lat': lats,
# When we pass a list that matches the number of markers, Plotly pulls an individual label for each marker it generates.
'text': hover_texts,
# Here we’re using the key 'marker' to specify how big each marker on the map should be.
'marker': { 
    # We use a list comprehension, which generates an appropriate marker size for each value in the mags list.
    'size':[5*mag for mag in mags],
    # The 'color' setting tells Plotly what values it should use to determine where each marker falls on the colorscale.
    'color': mags,
    # We use the mags list to determine the color that’s used. The 'colorscale' setting tells Plotly which 
    # range of colors to use: 'Viridis' is a colorscale 
    # that ranges from dark blue to bright yellow and works well for this data set.
    'colorscale': 'Viridis',
    # We set 'reversescale' to True, because we want to use bright yellow for the lowest values 
    # and dark blue for the most severe earthquakes.
    'reversescale' : True,
    # The 'colorbar' setting allows us to control the appearance of the colorscale shown on the side of the map. 
    # Here we title the colorscale'Magnitude' to make it clear what the colors represent.
    'colorbar': {'title': 'Magnitude'},

},
}]
# We give the chart an appropriate title
my_layout = Layout(title='Global Earthquakes')

# create a dictionary called fig that contains the data and the layout
fig = {'data': data, 'layout': my_layout}

# Finally, we pass fig to the plot() function along with a descriptive filename for the output.
offline.plot(fig, filename='global_earthquakes.html')