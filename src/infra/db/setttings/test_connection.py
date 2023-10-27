from .connection import DbConnectHandler 
from sqlalchemy import text

def test_conncetion():
    first_name = 'Marco'
    last_name = 'Maria'
    age = 40

    with DbConnectHandler as DB:
        try:
            db = DB()
            engine = db.engine
            conn = engine.connect()
            query_insert = f'''
                    INSERT INTO users (first_name, last_name, age)
                    VALUES (
                    '{first_name}',
                     '{last_name}', 
                     '{age}'
                    )
                    '''
            conn.execute(text(query_insert))
            conn.commit()
            query_get = f'''
                    SELECT * FROM users
                    '''
            result = conn.execute(text(query_get))
            users = result.fetchall()
            print(users)        
        except Exception as exception:
            conn.rollback()
            raise exception