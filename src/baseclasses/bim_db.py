import psycopg2
from configuration import *



def delete_bim_from_db(service, pk):

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
                f"""DELETE FROM public.{service} WHERE pk='{pk}'"""
            )
            print("Delete success")
            print(pk)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')





def get_container_from_db():
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
                SELECT pk FROM public.bim_container 
                WHERE data->>'ver' = '0.1' AND  fk_owner = 'ec8e7c12-5475-4b21-930b-c28e1fd64219' 
                ORDER BY date_create DESC
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




def get_from_db(point):

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
                    SELECT pk FROM public.{point}
                    WHERE fk_owner = 'ec8e7c12-5475-4b21-930b-c28e1fd64219'
                    ORDER BY date_create DESC
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

print(get_from_db("bim"))