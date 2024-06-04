#!/usr/bin/python3
"""This function queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords"""
import requests

def fetch_posts(subreddit, hot_list=[], after=None):
    if after == "STOP":
        return hot_list
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {"User-Agent": "Custom"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        if not children:
            return hot_list
        hot_list.extend([post['data']['title'] for post in children])
        after = data['data']['after']
        return fetch_posts(subreddit, hot_list, after)
    else:
        return hot_list

def count_words(subreddit, word_list, count_dict=None):
    if count_dict is None:
        count_dict = {}
    
    hot_posts = fetch_posts(subreddit)
    
    if not hot_posts:
        return

    for post in hot_posts:
        words = post.lower().split()
        for word in words:
            if word in word_list:
                if word in count_dict:
                    count_dict[word] += 1
                else:
                    count_dict[word] = 1

    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_counts:
        print(f"{word}: {count}")

# Example usage
count_words("programming", ["react", "python", "java", "javascript", "scala", "no_results_for_this_one"])

