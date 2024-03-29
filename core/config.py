import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# DATABASE # Same URI for production and test
mongo_uri_username : str = os.getenv('MONGO_URI_USERNAME')
mongo_uri_password : str = os.getenv('MONGO_URI_PASSWORD')
mongo_cluster = os.getenv('DB_CLUSTER_NAME')
mongo_uri : str =f'mongodb+srv://{mongo_uri_username}:{mongo_uri_password}@{mongo_cluster}.frz9pqh.mongodb.net/?retryWrites=true&w=majority'
production_database_name : str = os.getenv('PRODUCTION_DATABASE_NAME')
test_database_name : str = os.getenv('TEST_DATABASE_NAME')
db_environment = os.getenv("DB_ENVIRONMENT", "production")

# GOOGLE SPACE
google_space_token : str = os.getenv("GOOGLE_SPACE_TOKEN")
google_space_key : str = os.getenv("GOOGLE_SPACE_KEY")
google_space_webhook_url : str = f'https://chat.googleapis.com/v1/spaces/AAAA1I6l2Ag/messages?key={google_space_key}&token={google_space_token}'
    