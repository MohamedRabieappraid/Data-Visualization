import requests 

# Make an API call and store the response.

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


# Examine the first repository.

# To look closer at the information returned about each repository, we
# pull out the first item from repo_dicts and store it in repo_dict .
#repo_dict = repo_dicts[0]

# We then print the number of keys in the dictionary to see how much information we have.
#print(f"\nKeys: {len(repo_dict)}")

# we print all the dictionary’s keys to see what kind of information is included.
#for key in sorted(repo_dict.keys()):
#    print(key)

print("\nSelected information about each repository:")

# we loop through all the dictionaries in repo_dicts. 
# Inside the loop, we print the name of each project,
#its owner, how many stars it has, its URL on GitHub, and the project’s description.
for repo_dict in repo_dicts:
    # we print the name of the project.
    print(f"Name: {repo_dict['name']}")

    # we use the key owner to access the dictionary representing the owner, 
    # and then use the key login to get the owner’s login name.
    print(f"Owner: {repo_dict['owner']['login']}")

    # we print how many stars the project has earned.
    print(f"Stars: {repo_dict['stargazers_count']}")

    # print  the URL for the project’s GitHub repository.
    print(f"Repository: {repo_dict['html_url']}")

    # We then show when it was created
    print(f"Created: {repo_dict['created_at']}")

    # when it was last updated
    print(f"Updated: {repo_dict['updated_at']}")

    # we print the repository’s description
    print(f"Description: {repo_dict['description']}")


# Process results.
# we print the keys from response_dict
#print(response_dict.keys())