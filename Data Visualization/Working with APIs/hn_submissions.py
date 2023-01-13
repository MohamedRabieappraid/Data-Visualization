from operator import itemgetter
import requests

# Make an API call and store the response.

# we make an API call, and then print the status of the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status Code : {r.status_code}")

# Process information about each submission.

# We then convert the response object to a Python list which we store in submission_ids.
submission_ids = r.json()

# We set up an empty list called submission_dicts at to store these dictionaries.
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    # We make a new API call for each submission by generating a URL that includes the current value of submission_id.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    
    # we create a dictionary for the submission currently being processed, 
    # where we store the title of the submission, a link to the discussion
    # page for that item, and the number of comments the article has received sofar.
    submission_dict = {
        'title' : response_dict['title'],
        'hn_link' : f"http://news.ycombinator.com/item?id={submission_id}",
        'comments' : response_dict['descendants'],
    }

    # Then we append each submission_dict to the list submission_dicts.
    submission_dicts.append(submission_dict)

# To do this, we use a function called itemgetter(), which comes from the operator module.
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Once the list is sorted, we loop through the list at and print out three pieces of information about 
# each of the top submissions: the title, a link to the discussion page.
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
