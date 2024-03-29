from external_services.scraping_setup import scraper_setup
from scraper_libraries.re import get_version_and_date_from_one_tag 
from scraper_libraries.dateutil import check_date_type_then_convert
from scraper_libraries.beautiful_soup import find_git_bodies, find_span_tag
from database.database_operations import insert_indexed_document_in_frameworks_collection


#####  SYMFONY
async def scrape_github_symfony(url):
    soup,name = scraper_setup(url)
    #print('SOUP', str(soup)[:100])
    parent_boxes = soup.find_all('div', class_ = 'd-flex flex-column flex-md-row my-5 flex-justify-center')
    for box in parent_boxes:
    # Stringifies the body where the version name, release date and status are nested.
        bodies = find_git_bodies(box)
        columns = box.find_all('div', 'col-md-2 d-flex flex-md-column flex-row flex-wrap pr-md-6 mb-2 mb-md-0 flex-items-start pt-md-4')
        for body in bodies:
            a_tag = body.find('a', class_='Link')
            span_tag = find_span_tag(body)
            if a_tag:
                version = a_tag.text.strip().lstrip('v') # .lstrip() removes the the leading characters
                status = span_tag.text.strip() if span_tag else "N/A"
            else:
                version = "Version missing"
                status = "N/A"
        for column in columns:
            relative_time_tags = column.find_all('relative-time')
            for relative_time_tag in relative_time_tags:
                release_date = relative_time_tag.get('datetime')
                release_date = check_date_type_then_convert(release_date)
                #Insert into database
                document_insertion = await insert_indexed_document_in_frameworks_collection(name,version,release_date,status)
                print(f'Name: {name}, Version : {version}, Release date : {release_date}, Status: {status}')
    return document_insertion

                ##### ANGULAR
async def scrape_github_angular(url):
    soup,name = scraper_setup(url)
    # Stringifies the body where the version name, release date and status are nested.
    bodies = find_git_bodies(soup)
    for body in bodies:
        h1_tag = body.find('h1')
        span_tag = find_span_tag(body)
        if h1_tag:
            h1_text = h1_tag.text.strip()
            version, release_date = get_version_and_date_from_one_tag(h1_text)
            if version and release_date:
                release_date = check_date_type_then_convert(release_date)
                status = span_tag.text.strip() if span_tag else "N/A"
                # Insert into database
                document_insertion = await insert_indexed_document_in_frameworks_collection(name,version,release_date,status)
                print(f'Name: {name}, Version: {version}, Release date: {release_date}, Status: {status}')
            else:
                print("Version or status missing" )
    return document_insertion

