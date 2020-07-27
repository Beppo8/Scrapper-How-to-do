from bs4 import BeautifulSoup

if __name__ == '__main__':

    with open('econopy.html', 'r') as file:
        content = file.read()

        #Busqueda por clases CSS
        soup = BeautifulSoup(content, 'html.parser')

        div = soup.find('div', {'title': 'buyer-info'})

        print(div.contents)

        div_item = div.contents[1]
        span_item = div.contents[3]

        print(div_item.text, span_item.text)

        for child in div.children:
            print(child)

        print(div.contents)
        print(div.children)