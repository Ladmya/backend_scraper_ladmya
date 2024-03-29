from external_services.scraping_setup import scraper_setup
from scraper_libraries.dateutil import check_date_type_then_convert
from scraper_libraries.beautiful_soup import find_wiki_table,find_wiki_table_rows, find_wiki_row_cells
from database.database_operations import insert_indexed_document_in_languages_collection


#### PYTHON
async def scrape_wiki_python(url):
    soup,name = scraper_setup(url)
    table = find_wiki_table(soup)
    if table:
        rows = find_wiki_table_rows(table)
        for row in rows:
            cells = find_wiki_row_cells(row)
            if len(cells)>=4:
                if 'data-sort-value' in cells[0].attrs and cells[0]['data-sort-value'].strip():
                    version = cells[0].get('data-sort-value', '').strip() 
                    # Remove all <sup> tags from the second cell ex: 3 january 2019[113]
                    for sup_tag in cells[2].find_all('sup'):
                        sup_tag.decompose()
                    release_date = cells[2].get_text(strip=True) 
                    release_date = check_date_type_then_convert(release_date)
                    # Insert into database
                    document_insertion = await insert_indexed_document_in_languages_collection(name,version,release_date)
                    print(f"Name: {name}, Version: {version}, Release Date: {release_date}")                    
                else:
                    print('Skipping row without Python version data')
        return document_insertion

#### PHP
async def scrape_wiki_php(url):
    soup,name = scraper_setup(url)
    table = find_wiki_table(soup)
    if table:
        rows = find_wiki_table_rows(table)  # Corrected to find rows within the table only
        for row in rows:
            cells = find_wiki_row_cells(row)
            if len(cells) >= 2:  # Ensure there are at least two cells
                # Bs4 ".attrs" method =>  is an attribute of a tag object that gives access to all attributes of that tag in a dictionary format.
                if 'data-sort-value' in cells[0].attrs and cells[0]['data-sort-value'].strip():
                    version = cells[0].get('data-sort-value', '').strip() 
                    # Remove all <sup> tags from the second cell ex: 3 january 2019[113]
                    for sup_tag in cells[1].find_all('sup'):
                        sup_tag.decompose()
                    release_date = cells[1].get_text(strip=True) 
                    release_date = check_date_type_then_convert(release_date)
                    # Insert into database
                    document_insertion = await insert_indexed_document_in_languages_collection(name,version,release_date)
                    print(f"Name: {name}, Version: {version}, Release Date: {release_date}")
                else:
                    print('Skipping row without PHP version data')
        return document_insertion


####  TYPESCRIPT
async def scrape_wiki_typescript(url):
    soup,name = scraper_setup(url)
    table = find_wiki_table(soup)
    if table:
        rows = find_wiki_table_rows(table)  # Corrected to find rows within the table only
        for row in rows:
            cells = find_wiki_row_cells(row)
            if len(cells) >= 2:  # Ensure there are at least two cells
                version = cells[0].text.strip()
                release_date = cells[1].text.strip()
                release_date = check_date_type_then_convert(release_date)
                # Insert into database
                document_insertion = await insert_indexed_document_in_languages_collection(name,version,release_date)
                print(f"Name: {name}, Version: {version}, Release Date: {release_date}")
        return document_insertion


####  JAVA
async def scrape_wiki_java(url):
    soup,name = scraper_setup(url)
    substring = "Java SE" # To select only the SE instead of JDK and J2SE
    table = find_wiki_table(soup)
    rows = find_wiki_table_rows(table)
    for row in rows:
        first_cell = row.find('td')
        if first_cell and 'data-sort-value' in first_cell.attrs:
            if substring in first_cell['data-sort-value']:
                version = first_cell['data-sort-value']
                release_date_cell = find_wiki_row_cells(row)[2]
                release_date = release_date_cell.text.strip() if release_date_cell else 'N/A'
                release_date = check_date_type_then_convert(release_date)
                # Insert into database
                document_insertion = await insert_indexed_document_in_languages_collection(name,version,release_date)
                print(f"Name: {name}, Version: {version}, Release Date : {release_date}")
    return document_insertion


####   JAVASCRIPT
async def scrape_wiki_javascript(url):
    soup,name = scraper_setup(url)
    table = find_wiki_table(soup)
    if table:
        rows = find_wiki_table_rows(table)  # Corrected to find rows within the table only
        for row in rows:
            cells = find_wiki_row_cells(row)
            header_cells = row.find_all('th')
            if len(cells) >= 3:  # Ensure there are at least two cells
                version = 'ES ' + header_cells[0].text.strip()
                release_date = cells[0].text.strip()
                release_date = check_date_type_then_convert(release_date)
                # Insert into database
                document_insertion = await insert_indexed_document_in_languages_collection(name,version,release_date)
                print(f"Name: {name}, Version: {version}, Release Date: {release_date}")
        return document_insertion

####     C sharp
#url = "https://en.wikipedia.org/wiki/C_Sharp_(programming_language)"
