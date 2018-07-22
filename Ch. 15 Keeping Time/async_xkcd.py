#! python3

import threading
import bs4
import requests
import os


def download_comics(start, end):
    os.makedirs('xkcdcomics', exist_ok=True)

    for url_number in range(start, end + 1):
        try:
            print(f'Downloading comic #{url_number}.')
            r = requests.get(f'http://xkcd.com/{url_number}')
            r.raise_for_status()

            soup = bs4.BeautifulSoup(r.text, 'html.parser')
            comic = soup.select('#comic img')
            assert comic, 'Comic element not found!'

            image_src = comic[0].get('src')
            img = requests.get('http:' + image_src)

            file = open(os.path.join('xkcdcomics', os.path.basename(image_src)), 'wb')
            for chunk in img.iter_content(10000):
                file.write(chunk)
            file.close()
        except AssertionError:
            print(f'Comic #{url_number} not found!')
            

if __name__ == '__main__':
    threads = []
    for i in range(1, 1000, 100):
        thread = threading.Thread(target=download_comics, args=[i, i+100])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    