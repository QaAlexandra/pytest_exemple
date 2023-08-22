import psycopg2

from configuration import *


def delete_test_user_from_db(mail):
    global connection
    try:
        connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user_db,
            password=password_db,
            port=port)
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                f"""DELETE FROM public.user WHERE email='{mail}'"""
            )
            print("Delete success")
            print(mail)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')


def change_mail_in_db(from_mail, to_mail):
    global connection
    try:
        connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user_db,
            password=password_db,
            port=port)
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                f"""UPDATE  public.user SET email = '{to_mail}' WHERE email='{from_mail}'"""
            )
            print("Update success")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')


def get_refresh_token(email):
    global connection
    try:
        connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user_db,
            password=password_db,
            port=port)
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT refresh_token FROM public.1111 WHERE email = '{email}' """
            )
            refresh = cursor.fetchone()
            return refresh


    except (Exception, psycopg2.DatabaseError) as error:
        print("Here is an error")
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')


def delete_from_db(point: object, pk: object) -> object:
    try:
        connection = psycopg2.connect(
            host=host,
            database=bim_db_name,
            user=bim_db_user,
            password=bim_db_pass,
            port=bim_db_port
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                f"""DELETE FROM public.{point} WHERE pk= '{fk}'"""
            )
            print("Delete success")
            print(pk)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

