# %%
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

# %%
filename = os.environ["MESSAGES_LIBRARY"]
pythonpath = os.environ["PYTHONPATH"]
conn = sqlite3.connect(f"{pythonpath}/{filename}")
cursor = conn.cursor()

# %%

data_struc = {}


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table in tables:
    table_name = table[0]
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    data_struc[table_name] = columns
conn.close()

print(data_struc)


# %%
