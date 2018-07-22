#! python3
# I'm Feeling Lucky Google search - opens first several search results in new browser tab

import requests
import sys
import webbrowser
import bs4
import logging
logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

print("Googling...")  # display text while downloading the Google page

# Download Google page by joining command line arguments to the Google URL
res = requests.get("http://google.com/search?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()
logging.debug('Finished downloading Google page: ' + str(res))
# retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')
logging.debug('Soup object created: ' + str(len(soup)))

# open a browser tab for each link
linkElems = soup.select('.r a')
logging.debug(str(len(linkElems)) + ' elements found.')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    logging.debug("Iteration: " + str(i))
    logging.debug("Element: " + str(linkElems[i].get('href')))
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

# after trying the program at first, it didn't work properly. This was caused by a missing %* in the batch file which
# caused the computer to ignore everything after the first command line argument. The program ran but with an empty
# sys.argv, which resulted in an empty res object, and then an empty soup object. Logging helped greatly.
