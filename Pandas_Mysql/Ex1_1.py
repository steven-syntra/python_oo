import mysql.connector
import pandas as pd

# Voorbeeld met mysql.connector:
# werkt, maar geeft vervelende warning:
# UserWarning: pandas only support SQLAlchemy connectable(engine/connection) or
# database string URI or sqlite3 DBAPI2 connection
# other DBAPI2 objects are not tested, please consider using
# SQLAlchemy

my_conn = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="sakila"
    )

data = pd.read_sql("SELECT * FROM actor", my_conn)

print("All actors:")
print(data)
print("")
print("Actors named 'Mary':")
print(data[data['first_name'] == 'MARY'])
print("")
print("Actors named 'Tim':")
print(data[data['first_name'] == 'TIM'])