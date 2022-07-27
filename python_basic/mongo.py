import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()




def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://{}:{}@{}".format('root','example','mongo')
    print(CONNECTION_STRING)

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['db_edu']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    tabla1 = dbname['fields']
    persona1 = {
            '_id': '62e1bf676b9ab88e3eaa6316',
            'nombre':'Eduardo',
            'apellido':'Gonik',
            'edad':28
            }
    persona2 = {
            'nombre':'Julia',
            'apellido':'Gonik',
            'edad':22,
            'profesion':'coder'
            }


    x = tabla1.insert_many([persona1, persona2])
    tabla_toda = pd.DataFrame(
                        tabla1.find()
                        )
    print(tabla_toda)
    print(os.environ.get("PRUEBAZA", "no lei la variable de entorno"))



    print(x)
