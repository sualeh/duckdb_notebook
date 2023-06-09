# %%
import duckdb

conn = duckdb.connect()
print(f"DuckDB connection {conn}")

# %%

conn.register(
    "people",
    conn.execute(
        """
    SELECT
      *
    FROM
      read_csv_auto('datasets/people.csv', header=True)
"""
    ).df()
)

conn.execute("DESCRIBE people").df()

# %%

conn.register(
    "people_personal",
    conn.execute(
        """
    SELECT
      *
    FROM
      read_csv_auto('datasets/people_personal.csv', header=True)
"""
    ).df()
)

conn.execute("DESCRIBE people_personal").df()

# %%

conn.execute("FROM people LIMIT 5").df()

# %%

conn.execute("FROM people_personal LIMIT 5").df()

# %%

conn.execute(
    """
  SELECT
    people.Id,
    people.FirstName,
    people.LastName,
    people_personal.FavoriteColor
  FROM
    people
    INNER JOIN people_personal
      ON people.Id = people_personal.Id
"""
).df()

# %%

conn.execute(
    """
  CREATE OR REPLACE TABLE initials
  AS
    SELECT
      substr(FirstName, 1, 1)
        AS Initial,
      COUNT(*)
        AS TotalPeople
    FROM
      people
    GROUP BY
      substr(FirstName, 1, 1)
"""
)

conn.execute("FROM initials ORDER BY Initial").df()

# %%
