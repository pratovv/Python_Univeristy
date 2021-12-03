import psycopg2

con = psycopg2.connect(
  database="Kursovaya", 
  user="postgres", 
  password="1", 
  host="localhost", 
  port="5432"
)

print("Database opened successfully")