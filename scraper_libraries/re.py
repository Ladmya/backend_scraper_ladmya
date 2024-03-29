import re  # python built-in

# The regex includes 3 capturing groups, including the non-capturing the middle one to scrap a version suffix
version_date_regex_pattern = r'([\d\.]+(?:-(rc|next|Slam Dunk|alpha|beta)\.\d+)?) \((\d{4}-\d{2}-\d{2})\)'

# Github has 2 types of url, both end up with a "/"
# Wikipedia's url never end up by a "/" 
tech_name_github_regex_patterns = [
    r'raw.githubusercontent\.com/([^/]+)/',
    r'github\.com/([^/]+)/',
    r'en\.wikipedia\.org/wiki/([^/]+)'
] 
# 1- Extracts name from the url
# 2- Extracts and Cleans the data from url to reflect the actual name of the tech
def get_tech_name_from_url(url):
    for pattern in tech_name_github_regex_patterns:
        match_pattern = re.search(pattern, url)
        if match_pattern:
            name = match_pattern.group(1)
            if '_version_history' in name:
                name = name.replace('_version_history', '')
            if 'History_of_' in name:
                name = name.replace('History_of_','')
            if '_(programming_language)' in name:
                name = name.replace('_(programming_language)','')
            return name.capitalize() # .capilize() =>  For data consistency
    else:
        print('Error with pattern tech name')


# More efficient than 2 functions because only 1 search is performed
# Extracts version & date from a tag
def get_version_and_date_from_one_tag(tag):
    match_version_date_pattern = re.search(version_date_regex_pattern,tag)
    if match_version_date_pattern:
        version = match_version_date_pattern.group(1) 
        release_date = match_version_date_pattern.group(3)
        return version, release_date
    else:
        print("Error, can't match the pattern")

# Cleans a date string by removing characteers and normalizing the format
def sanitize_date_string(release_date):
    # Regular expression to extract numeric date part, if present
    # Replaces non-breaking spaces with standard spaces
    sanitized_date = release_date.replace('\xa0', ' ')
    # Removes digits within square brackets to clean up references like [1], [2], etc.
    sanitized_date = re.sub(r'\[\d+\]', '', sanitized_date)
    # See wiki TS date format '1 October 2012 (2012-10-01)'
    match = re.search(r'\d{4}-\d{2}-\d{2}', sanitized_date)
    if match:
        return match.group(0)
    else:
        # Replaces non-breaking spaces and other non-standard characters 
        return sanitized_date.replace('\xa0', ' ')



# def get_version_from_tag(tag):
#     match_version_pattern = re.search(version_date_regex_pattern,tag)
#     if match_version_pattern:
#         # Using .group() from 're' module. 
#         version = match_version_pattern.group(1)
#         return version


# def get_date_from_tag(tag):
#     match_date_pattern = re.search(version_date_regex_pattern,tag)
#     if match_date_pattern:
#         # Using .group() from 're' module. 
#         release_date = match_date_pattern.group(3)
#         return release_date
