from bs4 import BeautifulSoup

if __name__ == '__main__':

    with open('econopy.html', 'r') as file:
        content = file.read()

        #Busqueda de un elemento
        soup = BeautifulSoup(content, 'html.parser')

        title = soup.find('title')

        if title:
            print(title)

            print(type(title))
            print(title.name)

            print(title.text)
            print(title.get_text())