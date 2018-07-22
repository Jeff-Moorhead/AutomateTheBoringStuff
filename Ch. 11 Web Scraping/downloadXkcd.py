#! python3

# Opens XKCD on a web browser and saves each comic to the hard drive.

import os
import requests
import bs4
import logging

logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
url = "http://xkcd.com"
logging.debug('Current working directory is: ' + os.getcwd())
os.makedirs('xkcdComics', exist_ok=True)
numDownloaded = 0
while not url.endswith('#'):
    # Download the xkcd page
    print('Downloading page %s...' % url)
    res = requests.get(url)  # downloads xkcd page and saves it in variable res
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")  # creates soup object out of res text
    # Find the url of the comic image
    comicElem = soup.select('#comic img')  # finds comic in HTML of xkcd page (saves as a list)
    if len(comicElem) == 0:
        print('No comics could be found.')
        # Get the 'Prev' buttons url
        prevLink = soup.select('a[rel="prev"]')[0]  # finds HTML for Prev button
        url = 'http://xkcd.com' + prevLink.get('href')  # updates URL to go to previous comic
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')  # finds comic source from comicElem html
            # Download the image
            print("Downloading image %s" % comicUrl)
            res = requests.get(comicUrl)  # downloads the comic image
            res.raise_for_status()
            # Save the image to ./xkcdComics
            imageFile = open(os.path.join('xkcdComics', os.path.basename(comicUrl)),
                             'wb')  # opens image in xkcdComics file
            for chunk in res.iter_content(100000):  # writes comic data to imageFile
                imageFile.write(chunk)
            imageFile.close()

            # Get the 'Prev' buttons url
            prevLink = soup.select('a[rel="prev"]')[0]  # finds HTML for Prev button
            url = 'http://xkcd.com' + prevLink.get('href')  # updates URL to go to previous comic
            numDownloaded += 1
        except Exception:
            print('Could not download comic %s' % comicUrl)
            # Get the 'Prev' buttons url
            prevLink = soup.select('a[rel="prev"]')[0]  # finds HTML for Prev button
            url = 'http://xkcd.com' + prevLink.get('href')  # updates URL to go to previous comic

print('%d comics have been downloaded.' % numDownloaded)
