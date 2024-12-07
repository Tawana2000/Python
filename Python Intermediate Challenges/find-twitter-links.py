# Write a function to find all twitter links in a given text

import re

def find_twitter_links(text):
    """
    Finds all Twitter links in the given text.

    Parameters:
        text (str): The input text to search for Twitter links.

    Returns:
        list: A list of Twitter links found in the text.
    """
    # Regular expression to match Twitter links
    twitter_regex = r'https?://(?:www\.)?twitter\.com/[a-zA-Z0-9_]+(?:/status/\d+)?'
    
    # Use re.findall to find all matches
    twitter_links = re.findall(twitter_regex, text)
    return twitter_links