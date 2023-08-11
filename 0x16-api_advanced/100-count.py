#!/usr/bin/python3
""" Getting count of given keywords """
import requests


def count_words(subreddit, word_list, after='', dictionary={}):
    """ prints a sorted count of given keywords
    (case-insensitive, delimited by spaces """

    word_list = list(dict.fromkeys(word_list))

    url = 'https://www.reddit.com/r/{}/hot/.json?after={}'\
        .format(
            subreddit, after)
    agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0)'
    agent += ' Gecko/20100101 Firefox/102.0'
    headers = {"user-Agent": agent}
    response = requests.get(
        url, headers=headers, allow_redirects=False)
    try:
        results = response.json()
        if response.status_code != 200:
            raise Exception
    except Exception:
        return
    results = results.get('data')
    after = results.get('after')
    children = results.get('children')
    for result in children:
        titleSplited = result['data']['title'].lower().split()
        processWords(titleSplited, word_list, dictionary)

    if after:
        return count_words(subreddit, word_list, after, dictionary)
    if len(dictionary) == 0:
        return
    dictionary = dict(
        sorted(dictionary.items()))
    [print('{}: {}'.format(key, value))
     for key, value in dictionary.items() if value != 0]


def processWords(titleSplited, word_list, dictionary):
    """ Processing words to save the count in the dictionary """
    lowerWordList = list(map(lambda x: x.lower(), word_list[:]))
    lowerTitleSplited = list(map(lambda x: x.lower(), titleSplited[:]))
    for word in lowerWordList:
        numberOfMatches = len(
            list(filter(lambda x: x == word.lower(), lowerTitleSplited)))

        if word not in dictionary.keys():
            dictionary[word] = numberOfMatches
            continue
        dictionary[word] += numberOfMatches
