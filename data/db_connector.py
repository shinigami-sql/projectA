import psycopg2 # psycopg2 is the client library, the Python equivalent of psql

# imports load_dotenv function, reads the .env file in the project folder and 
#loads all key-value pairs into the session environment
from dotenv import load_dotenv  

import os # Python library for interacting with the terminal and OS, used here to access environment variables

# loads the .env file into the session environment, 
# adds the key-value pairs to the same pool as system variables like PATH and USER
# override=False prevents load_dotenv from overwriting variables already in the environment,
# allowing GitHub Actions secrets to take priority over .env values`
load_dotenv(override=False)  

# os.environ is the environment variables pool, .get('DATABASE_URL') pulls the db url from it by key name
db_url = os.environ.get('DATABASE_URL')  

# psycopg2.connect() opens the pipeline between Python and the PostgreSQL server
# db_connection is the open pipeline, the active connection to the server
# cursor is the transport inside that pipeline, sends SQL commands and brings results back

# db_connection using DATABASE_URL from .env, contains all connection details in one string
db_connection = psycopg2.connect(db_url)
cursor = db_connection.cursor()




# OLD EXPLICIT CONNECTION KEPT FOR REFERENCE

# sslmode='prefer' uses SSL if available but falls back to non-SSL if the server doesn't support it
# suitable for mixed environments where SSL may or may not be available
# sslmode='require' should always be used for remote/production connections

#db_connection = psycopg2.connect(
	#dbname = 'projectA',
	#user = 'ernestomanuel',
	#host = 'localhost', # localhost points to 127.0.0.1, the loopback address that always refers to this machine
	#port = '5432',
	#sslmode = 'prefer')

#cursor = db_connection.cursor()



