import os

from dotenv import load_dotenv


# Loading .env file
load_dotenv( os.getenv("ENV_FILE") )

# Your important main infos.
MAIN_USERNAME = os.getenv( "MAIN_USERNAME" )
MAIN_PASSWORD = os.getenv( "MAIN_PASSWORD" )
MAIN_PHONENUMBER = os.getenv( "MAIN_PHONENUMBER" )


EMAIL_GOOGLE_APP = os.getenv( "EMAIL_GOOGLE_APP" )
MAIN_GOOGLE_APP_PASSWORD = os.getenv( "MAIN_GOOGLE_APP_PASSWORD" )