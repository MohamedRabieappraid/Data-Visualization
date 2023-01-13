import requests 

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
# We continue to print the status of the API call response so we’ll know if there is a problem.
# we store the URL of the API call in the url variable.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# we define headers for the API call that ask explicitly to use this version of the API.
headers = {'Accept':'application/vnd.github.v3+json'}

# Then we use requests to make the call to the API.
# We call get() and pass it the URL and the header that we defined, 
# and we assign the response object to the variable r.
r= requests.get(url, headers=headers)

# The response object has an attribute called status_code, which tells us whether the request was successful.
# (A status code of 200 indicates a successful response.)
# we print the value of status_code so we can make sure the call went through successfully.
print(f"Status code: {r.status_code}")

# Process results.
# Store API response in a variable.
# The API returns the information in JSON format, so we use the json() method to convert the information to a Python dictionary.
# We store the resulting dictionary in response_dict.
response_dict = r.json()

# we print the value associated with 'total_count', which represents the total number of Python repositories on GitHub.
# The value associated with 'items' is a list containing a number of dictionaries,each of which contains data about an individual Python repository.
print(f"Total repositories: {response_dict['total_count']}")


# Explore information about the repositories.

# we store this list of dictionaries in repo_dicts. We then print the
# length of repo_dicts to see how many repositories we have information for.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# We then create two empty lists to store the data we’ll include in the initial chart.
# We first define a new empty list, labels, to hold the text we want to display for each project.
# We update the name of the list we’re creating from repo_names to repo_links to more accurately 
# communicate the kind of information we’re putting together for the chart.
repo_links, stars, labels = [], [], []

# we loop through all the dictionaries in repo_dicts. 
# Inside the loop, we print the name of each project,
#its owner, how many stars it has, its URL on GitHub, and the project’s description.
for repo_dict in repo_dicts:
    repo_name=repo_dict['name']

    # We then pull the URL for the project from repo_dict and assign it to the temporary variable repo_url.
    repo_url = repo_dict['html_url']
    # we generate a link to the project.
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    # In the loop where we process the data, we pull the owner and the description for each project.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']

    # Plotly allows you to use HTML code within text elements,so we generate a string for the label with
    # a line break (<br />) between the project owner’s username and the description.
    label = f"{owner}<br />{description}"
    # We then store this label in the list labels.
    labels.append(label)

# Make visualization.

# we define the data list.
data =[{
    'type': 'bar',

    # we use this list for the x-values in the chart. The result looks the same as before,
    #  but now the viewer can click any of the project names at the bottom of the chart to visit that project’s home page on GitHub.
    'x': repo_links,
    'y':stars,

    # In the data dictionary, we add an entry with the key 'hovertext' and assign it the list we just created.
    'hovertext':labels,
    # The marker settings shown here affect the design of the bars. 
    # We set a custom blue color for the bars and specify that they’ll be outlined with a dark gray line that’s 1.5 pixels wide.
    'marker': {
        'color': 'rgb(60,100,150)',
        'line' : {'width' : 1.5, 'color' : 'rgb(25,25,25)'},
    },
    # We also set the opacity of the bars to 0.6 to soften the appearance of the chart a little.
    'opacity' : 0.6,
}] 


# we define the layout for this chart using the dictionary approach.
# Instead of making an instance of the Layout class, we build a dictionary with the layout specifications we want to use.
my_layout ={
    'title':'Most-Starred Python Projects on GitHub',

    # We use the 'titlefont' key to define the font size of the overall chart title.
    'titlefont': {'size':28},

    # Within the 'xaxis' dictionary, we add settings to control the font size of the x-axis title ('titlefont') 
    # and also of the tick labels ('tickfont').
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont':  {'size': 14},
        },

    #  we define similar settings for the y-axis.
    'yaxis': {
        'title':'Stars',
        'titlefont': {'size' : 24},
        'tickfont' : {'size': 14 },
        },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')