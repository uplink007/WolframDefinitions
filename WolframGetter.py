import time
import urllib

import wolframalpha
import json
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin
from urllib.error import HTTPError


def read_json_config(filename="config.json"):
    with open(filename) as fd:
        config: dict = json.load(fd)
    return config


def init_wolfram_client(app_id):
    return wolframalpha.Client(app_id)


def get_word_defenition_from_wolfram(client, word):
    res = client.query(word)
    try:
        if res['@success'] :
            if "Definition" in res.details.keys():
                return res.details["Definition"]
    except AttributeError:
        pass
    return None


def get_math_articles_from_math_world_url(math_world_url ,math_world_postfix, existing_words_list,
                                       element='a', element_class='Hyperlink'):
    temp_word = None
    temp_article = None
    try:
        soup = BeautifulSoup(
            urllib.request.urlopen(urljoin(math_world_url, math_world_postfix)).read(), features="html.parser")
    except HTTPError as e:
        print(e.msg)
        return
    for link in soup.findAll(element, {"class": element_class}):
        if link.text.split('...')[0] in existing_words_list:
            continue
        try:
            soup_inner = BeautifulSoup(
                urllib.request.urlopen(urljoin(math_world_url, link.get('href'))).read(), features="html.parser")
        except HTTPError as e:
            print(e.msg)
            continue
        for link_inner in soup_inner.findAll('div', {"id":"mainContent"}):
            temp_article = link_inner.text
            break
        for link_inner in soup_inner.findAll('h1'):
            temp_word = link_inner.text
            break
        yield {temp_word: temp_article}


if __name__ == '__main__':
    config = read_json_config()
    client = init_wolfram_client(config['app_id'])
    words = set()
    defs_wolfram = None
    articles_math_world = None
    failed_defs = None
    url = config['urls_to_read']['web_url']
    sleep_counter = 0

    try:
        with open('articles.json') as f:
            articles_math_world = json.load(f)
    except IOError:
        articles_math_world = dict()

    for url_postfix in config['urls_to_read']['post_fix_urls']:
        for article in get_math_articles_from_math_world_url(url, url_postfix, articles_math_world.keys()):
            articles_math_world.update(article)

    with open('articles.json', 'w') as j_fd_1:
        json.dump(articles_math_world, j_fd_1)
    try:
        with open('definitions.json') as f:
            defs_wolfram = json.load(f)
    except IOError:
        defs_wolfram = dict()
    try:
        with open('failed_definitions.json') as f:
            failed_defs = json.load(f)
    except IOError:
        failed_defs = list()
    for word in articles_math_world.keys():
        res = None
        if (word in defs_wolfram.keys()) or (word in failed_defs):
            continue
        try:
            res = get_word_defenition_from_wolfram(client, word)
        except HTTPError as e:
            print(e.msg)
            if e.code == 403:
                print("sleep :", (10*sleep_counter))
                time.sleep(10*sleep_counter)
                sleep_counter += 1
                if sleep_counter == 10:
                    break
            continue
        except Exception as e_e:
            print(e_e)
            break
        if res is not None:
            defs_wolfram[word] = res
        else:
            failed_defs.append(word)

    with open('definitions.json', 'w') as j_fd_2:
        json.dump(defs_wolfram, j_fd_2)

    with open('failed_definitions.json', 'w') as j_fd_3:
        json.dump(failed_defs, j_fd_3)

    print('Done')