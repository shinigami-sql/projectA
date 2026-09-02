import psycopg2 # psycopg2 is the client library, the Python equivalent of psql

# psycopg2.connect() opens the pipeline between Python and the PostgreSQL server
# db_connection is the open pipeline, the active connection to the server
# cursor is the transport inside that pipeline, sends SQL commands and brings results back

# sslmode='prefer' uses SSL if available but falls back to non-SSL if the server doesn't support it
# suitable for mixed environments where SSL may or may not be available
# sslmode='require' should always be used for remote/production connections

db_connection = psycopg2.connect(
	dbname = 'projectA',
	user = 'ernestomanuel',
	host = 'localhost', # localhost points to 127.0.0.1, the loopback address that always refers to this machine
	port = '5432',
	sslmode = 'prefer')

cursor = db_connection.cursor()

