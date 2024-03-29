from scraper_libraries.re import get_tech_name_from_url
from scraper_libraries.requests import get_response_in_html, convert_response_in_string
from scraper_libraries.beautiful_soup import parse_response
from scraper_libraries.markdown import convert_markdown_string_to_html_string


# Centralizes the setup process of the scraper in the core 
def scraper_setup(url):

    response = get_response_in_html(url)
    response_text = convert_response_in_string(response)
    soup = parse_response(response_text)
    name = get_tech_name_from_url(url)

    return soup,name

# Centralizes the setup process of the scraper in the core for raw github pages
def scraper_setup_raw_github(url):

    response = get_response_in_html(url)
    response_text = convert_response_in_string(response)
    response_text = convert_markdown_string_to_html_string(response_text)
    soup = parse_response(response_text)
    name = get_tech_name_from_url(url)

    return soup,name