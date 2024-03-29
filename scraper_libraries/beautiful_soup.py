from bs4 import BeautifulSoup

# Turns the HTTP request response text into a bs4 object
def parse_response(response_text):
    soup = BeautifulSoup(response_text,'lxml')
    return soup

####   WIKIPEDIA FUNCTIONS
# Searches for the first table with the class 'wikitable'
def find_wiki_table(soup):
    table = soup.find('table', class_='wikitable')
    return table

# Searches for all the 'tr' elements in the table
def find_wiki_table_rows(table):
    rows = table.find_all('tr')
    return rows

# Searches for all the 'td' elements in the row
def find_wiki_row_cells(row):
    cells = row.find_all('td')
    return cells

####   GITHUB FUNCTIONS
# Searches for all the containers with a class 'Box-body'
def find_git_bodies(box):
    bodies = box.find_all('div', class_='Box-body')
    return bodies

# Searches for the first 'span' element in a given body
def find_span_tag(body):
    span_tag = body.find('span', class_='Label')
    return span_tag


