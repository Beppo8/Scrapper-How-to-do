from bs4 import BeautifulSoup

if __name__ == '__main__':

    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        a = soup.new_tag('a', href='www.codigofacilito.com',
        target='_blank')

        a.string = 'Link a la plataforma'

        div = soup.new_tag('div', id='item01', title='item-data')

        div.append('\n')
        div.append(a)
        div.append('\n')

        # soup.body.append(div)
        soup.body.insert(1, div) #contets

        print(soup.prettify())