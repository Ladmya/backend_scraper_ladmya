from external_services.scraping_setup import scraper_setup_raw_github
from scraper_libraries.dateutil import check_date_type_then_convert
from database.database_operations import insert_indexed_document_in_frameworks_collection


####   VUEJS
async def scrape_raw_github_vuejs(url):
    soup,name = scraper_setup_raw_github(url)
    
    h2_elements = soup.find_all('h2')
    for h2_element in h2_elements:
        anchor = h2_element.find('a')
        if anchor:
            release_date_tag = anchor.next_sibling
            if release_date_tag:
                version = anchor.text.strip().lstrip('v')
                release_date = release_date_tag.strip().lstrip('(').rstrip(')')
                release_date = check_date_type_then_convert(release_date)
                # Insert into database
                document_insertion = await insert_indexed_document_in_frameworks_collection(name,version,release_date)
                print(f'Name : {name}, Version : {version}, Release date : {release_date}')
    return document_insertion

