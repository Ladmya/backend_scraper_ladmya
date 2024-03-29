from datetime import datetime
from dateutil import parser
from scraper_libraries.re import sanitize_date_string

def check_date_type_then_convert(release_date):
    sanitized_date = sanitize_date_string(release_date)   
    # Ex: From '1 October 2012 (2012-10-01)' to '2012-10-01'
    try:
    # Checks if the date is already in ISO 8601 format
        datetime.strptime(sanitized_date, '%Y-%m-%dT%H:%M:%SZ')
        return sanitized_date
    except ValueError:
    # If not, parses and converts it to ISO 8601
        try:
            # If the direct ISO 8601 parse fails, use dateutil to parse other formats
            parsed_date = parser.parse(sanitized_date, default=datetime(1900, 1, 1))
            #print('PARSED DATE', parsed_date)
            return parsed_date.isoformat()
            # Ex: From '2012-10-01' to '2012-10-01T00:00:00'
        except ValueError as e:
            print(f"Error parsing date: {e}")
            return None

