import pandas as pd
import sqlalchemy as sql

#connect_string = 'mysql://USER:PW@DBHOST/DB'
#query =query = "select * from TABLENAME"
#df = pd.read_sql_query(query, sql_engine)


def insert(data: pd.DataFrame):
    engine = create_engine("sqlite:///{}".format(#"C:\\Users\\Dirk Dirksen\\PycharmProjects\\FoxexBot\\forex.db"))
    with engine.connect() as connection:
        connection.execute("CREATE TABLE IF NOT EXISTS {} "
                           "(pair TEXT NOT NULL, price FLOAT NOT NULL, time INTEGER NOT NULL);".format('my_table'))
        data.to_sql(name='my_table', con=connection, index=False, if_exists='append')

d = pd.DataFrame({
    'pair': ['abc'],
    'price': [1.2],
    'time': [123],
})

insert(d)