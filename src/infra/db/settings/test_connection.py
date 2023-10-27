from .connection import DbConnectHandler 
from sqlalchemy import text

def test_conncetion():
    first_name = 'Marco'
    last_name = 'Maria'
    age = 40

    
    
    db = DbConnectHandler()
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
    user = result.fetchall()[0]
    print(user)

    assert user.first_name == first_name
    assert user.last_name == last_name
    assert user.age == age

  

        

    