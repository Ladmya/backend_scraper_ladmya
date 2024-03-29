import requests

# Sends HTTP request to the url & retrieves a response in HTML 
def get_response_in_html(url):
    response = requests.get(url)   # Returns an object
    return response

# Converts HTML response in a string .text
def convert_response_in_string(response):
    response_text = response.text   
    return response_text


