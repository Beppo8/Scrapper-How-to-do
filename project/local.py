import requests
import re

URL = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':

    with open('econopy.html', 'r') as file:
            content = file.read()

            regex = '<div title="buyer-name">(.+?)</div>'

            for title in re.findall(regex, content):
                print(title)