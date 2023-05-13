from sqlalchemy import create_engine


def main():  # pobieranie tabeli

    engine = create_engine(
        "mysql+pymysql://root:root@localhost:3306/company"
    )
    sql = 'SELECT * FROM archived_users;'

    with engine.connect() as conn: # działamy cały czas z tym samym połączeniem
        result = conn.execute(sql)
        for row in result:
            print(row)

    #result = engine.execute(sql) # wszystkie wiersze
    #for row in result: # pobieram wszystkie maile z bd
        #print(row.email)
    #result.fetchone()
    rows = result.fetchall()
        #for row in rows:  #  for row in result:
        #print(row)     # print(row)
    #  print(result)

    #  item = result.fetchone()
    #  print(item.email) # typ RowProxy


if __name__ == '__main__':
    main()

