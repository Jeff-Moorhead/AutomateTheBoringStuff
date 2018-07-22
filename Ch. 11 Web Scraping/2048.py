#! python3

# 2048.py - Automatically plays 2048 by moving up, right, down, left repeatedly.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

newGame = browser.find_element_by_class_name('restart-button')

newGame.click()

play = browser.find_element_by_class_name('grid-container')
score = browser.find_element_by_class_name('score-container')
print(score.text)
print(play.text)
while score.text != str(2048):
    try:
        play.send_keys(Keys.UP)
        play.send_keys(Keys.RIGHT)
        play.send_keys(Keys.DOWN)
        play.send_keys(Keys.LEFT)
        score = browser.find_element_by_class_name('score-container')
        if score.text == str(2048):
            break
    except:
        print('You lost. Your final score was ' + score.text)
        break
