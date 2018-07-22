#! python3

import requests
import bs4
import shelve
import os
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logging.disable(logging.CRITICAL)

if not 'scheduledcomics' in os.listdir():
    os.makedirs('scheduledcomics')


def get_comic_src(text):
    soup = bs4.BeautifulSoup(text, 'html.parser')
    comic = soup.select('#comic img')[0]
    return comic['src']


def check_for_updates(shelf, comic_src):
    if not 'comic' in shelf.keys():
        shelf['comic'] = comic_src
        logging.debug(shelf['comic'] + ' ' + src)
        return True
    elif shelf['comic'] == comic_src:
        return False
    else:
        shelf['comic'] = comic_src
        logging.debug('New shelf: ' + shelf['comic'])
        return True


def save_image(src, dest):
    image_res = requests.get(src)
    image = open(dest, 'wb')
    for chunk in image_res.iter_content(10000):
        image.write(chunk)
    image.close()


if __name__ == '__main__':
    r = requests.get('https://xkcd.com/')
    src = get_comic_src(r.text)
    logging.debug(src)
    shelf = shelve.open('comicshelf')
    if check_for_updates(shelf, src):
        print('Updating comic selection...')
        logging.debug(os.path.basename(src))
        save_image('https:' + src, f'scheduledcomics\\{os.path.basename(src)}')
    shelf.close()
