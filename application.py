from sqlalchemy import create_engine


def main():
    engine = create_engine(
        "mysql+pymysql://root:root@localhost:3306/company"
    )
    print(engine.table_names())


if __name__ == '__main__':
    main()