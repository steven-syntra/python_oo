from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, String, DateTime
import pandas as pd

# connectie maken met SQLAlchemy
engine = create_engine('mysql://root:@localhost/sakila')

# tabel inlezen
data = pd.read_sql_table("actor", con=engine, index_col='actor_id', parse_dates=['last_update'])

# subset opslaan
subset = data[data['first_name'] == 'JOE']
subset.to_sql('actor_backup', engine, index=True, if_exists='replace') # replace for first records

# nog een subset toevoegen
subset = data[data['first_name'] == 'JULIA']
subset.to_sql('actor_backup', engine, if_exists='append')

# nog een subset toevoegen
subset = data[data['first_name'] == 'TIM']
subset.to_sql('actor_backup', engine, if_exists='append')

print("Selection added")
