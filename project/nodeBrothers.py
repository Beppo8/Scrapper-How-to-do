from bs4 import BeautifulSoup

if __name__ == '__main__':

    with open('econopy.html', 'r') as file:
        content = file.read()

        #Busqueda por clases CSS
        soup = BeautifulSoup(content, 'html.parser')

        # div = soup.find('div', {'title': 'buyer-name'})
        div = soup.find('div', string='Carson Busses')

        # next_sibling
        # previous_sibling

        print(div.next_sibling.next)

        #next_siblings
        # previous_siblings

        for element in div.next_siblings:
            print(element)

        # parent
        print(span.parent)

        # parents
        for parent in span.parents:
            print(parent.name)