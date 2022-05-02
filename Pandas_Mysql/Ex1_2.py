from sqlalchemy import create_engine
import pandas as pd

# connectie maken met SQLAlchemy
engine = create_engine('mysql://root:@localhost/sakila')

# tabel inlezen
data = pd.read_sql_table("actor", con=engine, index_col='actor_id', parse_dates=['last_update'])

print("All actors:")
print(data)
print("")
print("Actors named 'Mary':")
print(data[data['first_name'] == 'MARY'])
print("")
print("Actors named 'Tim':")
print(data[data['first_name'] == 'TIM'])


