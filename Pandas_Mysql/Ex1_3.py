from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, String, DateTime
import pandas as pd

# connectie maken met SQLAlchemy
engine = create_engine('mysql://root:@localhost/sakila')

# tabel inlezen
data = pd.read_sql_table("actor", con=engine, index_col='actor_id', parse_dates=['last_update'])

# data opslaan in een nieuwe tabel 'actor_backup'
data.to_sql(
    'actor_backup',
    engine,
    if_exists='replace',
    index=True,
    dtype={
        "actor_id": Integer,
        "first_name": String(45),
        "last_name": String(45),
        "last_update": DateTime,
    }
)

print("Backup created")


