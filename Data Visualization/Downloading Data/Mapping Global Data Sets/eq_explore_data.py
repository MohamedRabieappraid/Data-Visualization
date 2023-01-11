import json

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
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
mags, lons, lats = [], [], []
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

    # and then append it to the list mags.
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# first 10 magnitude and first 5 latitudes, and longitudes 
print(mags[:10])
print(lons[:5])
print(lats[:5])

# we create a file to write this same data into a more readable format.
#readable_file = 'data/readable_eq_data.json'
#with open(readable_file,'w') as f :

    # The json.dump() function takes a JSON data object and a file object, and writes the data to that file.
    # The indent=4 argument tells dump() to format the data using indentation that matches the data’s structure.
#    json.dump(all_eq_data, f, indent=4)
