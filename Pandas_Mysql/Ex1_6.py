import pandas as pd

my_conn = 'mysql://root:@localhost/sakila'
films = pd.read_sql("SELECT * FROM film WHERE title LIKE '%%ARK%%'", my_conn)

print(films[['title', 'release_year', 'length']])
