import psycopg2
from config import config

def create_tables():
    commands = (
        """
        CREATE TABLE info (
            id SERIAL PRIMARY KEY,
            name VARCHAR(26) NOT NULL,
            active BOOLEAN NOT NULL,
            amperage SMALLINT NOT NULL,
            voltage SMALLINT NOT NULL,
            cost_per_KWH numeric NOT NULL
);
        """
    )
    conn = None
    try:
        params = config()

        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    create_tables()