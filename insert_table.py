import psycopg2
from config import config

def insertcommands(vendor_name):
    sql = """
INSERT INTO info (name, active, amperage, voltage, cost_per_kwh, lastupdated) 
VALUES ('ad', 'Yes', floor(random() * 20 + 1)::int, floor(random() * 20 + 1)::int, floor(random() * 0 + 1)::float, current_timestamp);

          """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql, vendor_name)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
