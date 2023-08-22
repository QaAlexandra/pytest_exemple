import psycopg2
from configuration import *


def get_file_from_db():
    try:
        connection = psycopg2.connect(
            host=host,
            database=bim_db_name,
            user=bim_db_user,
            password=bim_db_pass,
            port=bim_db_port)
        connection.autocommit = True

        with connection.cursor() as cursor:

            cursor.execute(
                f"""
                   SELECT pk FROM public.file_cloud_user 
                   WHERE   fk_owner = 'ec8e7c12-5475-4b21-930b-c28e1fd64219' 
                   """
            )

            refresh = cursor.fetchone()
            return refresh[0]

    except (Exception, psycopg2.DatabaseError) as error:
        print("Here is an error")
        print(error)
    finally:
        if connection is not None:
            connection.close()
        print('Database connection closed.')


print(get_file_from_db())
