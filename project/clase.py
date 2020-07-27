from bs4 import BeautifulSoup

if __name__ == '__main__':

    with open('econopy.html', 'r') as file:
        content = file.read()

        #Busqueda por clases CSS
        soup = BeautifulSoup(content, 'html.parser')

        #1
        #for element in soup.find_all(attrs={'class': 'item-price'}):

        #2
        for element in soup.find_all(class_='item-price'):
            if element.name == 'span':
                print(element.text)