import psycopg2
import time


conn = psycopg2.connect(
  database="database_name", user='username', password='password', host='ip_address', port='5432'
)
conn.autocommit = True
cursor = conn.cursor()
n = 0


while True:
    n += 1
    try:
        cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
                        INCOME) VALUES ('Alext', 'Fredman', 34, 'M', {})'''.format(n))
        time.sleep(1)
        conn.commit()
    except Exception as e:
        print(e)
        conn.close()
