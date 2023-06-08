# %%
import duckdb

conn = duckdb.connect()
print(f"DuckDB connection {conn}")

df = conn.execute("""
    SELECT 
      *
    FROM   
      read_csv_auto('datasets/people.csv', header=True)
""").df()
# %%

conn.register("people", df)
conn.execute("DESCRIBE people").df()

# %%
conn.execute("FROM people").df()

# %%
conn.execute("SELECT COUNT(*) AS people_count FROM people").df()

# %%
conn.execute("""
  SELECT 
    substr(FirstName, 1, 1)
      AS initial,
    COUNT(*) 
      AS total_people 
  FROM 
    people 
  GROUP BY
    substr(FirstName, 1, 1)
""").df()
# %%
conn.execute("""
CREATE OR REPLACE TABLE initials 
AS 
  SELECT 
    substr(FirstName, 1, 1)
      AS initial,
    COUNT(*) 
      AS total_people 
  FROM 
    people 
  GROUP BY
    substr(FirstName, 1, 1)
""")
             
conn.execute("FROM initials").df()
# %%
