## STACK:
PYTHON 3.12.1
PYTHON NATIVE ENVIRONMENT
NoSQL : MONGO DB & MOTOR
ATLAS for hosting DB
FastAPI

## DON'T FORGET TO DO THIS !
Once install Python locally, create a native virtual env
Copy the .env_copy and fill it with your secrets
See the install instructions below

## INSTALL PYTHON 3.12.1
Download there : https://www.python.org/downloads/

## CREATE PYTHON NATIVE VENV
python3 -m venv name_of_venv

## ACTIVATE VENV
source /Users/username/folder/directory_name/venvname/bin/activate

## DEACTIVATE VENV
deactivate

## INSTALL REQUIREMENTS.TXT IN NEW VENV
pip install -r requirements.txt

## TO UPDATE REQUIREMENTS.TXT COMMAND LINE
pip3 freeze > requirements.txt  ====> for mac os
pip freeze  > requirements.txt  ====> for windows os

## UVICORN (server)
 pip install uvicorn
 uvicorn main:app --reload    => run the server
 
## FASTAPI 
 pip install fastapi

## MOTOR (asynchronous driver for MongoDB)
pip install motor

## AOIHTTP (to handle Async for Mailgun instead of Requests) 
pip install aiohttp

## PYTEST / PYTEST ASYNCIO (handles asynchronous functions)
pip install pytest pytest-asyncio

## RUN FILE CODE
python -m folder_name.file_name
OR 
python folder_name.file_name.py


## SCRIPTS 
# Scripts in the scripts folder have to be run as modules => python -m folder.fileName
# Scripts at the project root have to be run like => python fileName.py

   # DON'T FORGET TO EXPORT AS WELL IN THE CONSOLE WHERE YOU RUN UVICORN COMMAND !!!
   # EXPORTING TEST OR PRODUCTION ENV : run consecutive scripts
   set up one environment => export DB_ENVIRONMENT=test
   unset the environment => unset DB_ENVIRONMENT

   # PREPENDING COMMANDS if not exporting the env
   # FOR PRODUCTION DATABASE
   1 - If no existing database => DB_ENVIRONMENT=production python database_initializer.py
   2 - To launch the scrapers => DB_ENVIRONMENT=production python scrapers_launcher.py
   3 - To check the release dates & send notifications => DB_ENVIRONMENT=production python releases_dates_check_launcher.py
   # FOR TEST DATABASE
   1 - Switch to test environment and no existing database => DB_ENVIRONMENT=test python database_initializer.py
   2 - To launch the scrapers => DB_ENVIRONMENT=test python scrapers_launcher.py
   3 - To check the release dates & send notifications => DB_ENVIRONMENT=test python releases_dates_check_launcher.py


## ARCHITECTURE 

BACKEND_PYTHON/
├── core/                                    # 
│   └── config.py                            # Centralizes configuration and manages the access to environment variables
│
├── database/                                # Set up for Atlas
│   └── database_connection.py               # Contains Atlas connection setup and management
│   └── database_operations.py               # CRUD for scraped data
│
├── external_services/                       # Deals with interactions between the application and external systems or services
│   ├── google_webhook_notification.py       # Sends notifications on a dedicated Google Space
│   └── languages_frameworks.py              # Fetches documents from a collection in the db based on provided filters + pagination
│   └── scraping_setup.py                    # Centralizes essential methods for initializing and preprocessing web scraping tasks
│
├── logs/                                    # Cron logs to keep track of failures and successes
│   └── cron_logs.py                         # Database operations for Log_cron collection
│
├── routes/                                  # Routes / API endpoints for services to interact with
│   └── routes_frameworks_languages.py       # Dynamic endpoints with query params for both scraped data collections
│   └── routes_webhook.py                    # Google space
│
├── schemas/                                 # Pydantic schemas for data validation
│   ├── cron_logs.py                         # 
│   └── frameworks_and_languages.py          # 
│   └── pagination.py                        # 
│
├── scraper_libraries/                       # Contains all methods used for the scraper
│   ├── beautifulSoup.py                     # Extracts and manipulates data from HTML content
│   └── markdown.py                          # Converts markdown string to HTML string
│   └── dateutil.py                          # Checks type and converts to ISO 8601 format
│   └── re.py                                # Extracts, manipulates, cleans and normalizes data from HTML tags
│   └── requests.py                          # Sends a request to the url and retrieves a response in HTML
│
├── sources/                                 # Contains scraping sub-sources
│   ├── git_scraper.py                       # Github algorithms
│   └── raw_github_scraper.py                # Github algorithms adjusted to raw format
│   └── wiki_scraper.py                      # Wikipedia algorithms
│
├── tests/                                   # Tests : further coming
│   ├── conftest.py
│
├── .env                                      
├── .gitignore                               # Add 2 venv + Training + collections & Json + files
├── database_initializer.py                  # Script that initializes the cluster & database (with set of documents)
├── main.py                                  # Entrypoint: starts & shuts down the app, includes routes & middleware
├── README.md   
├── releases_dates_check_launcher.py         # Script that compares the release dates to today
├── requirements.txt                         # List project dependencies 
├── scrapers_launcher.py                     # Script that launches the scrapers        


