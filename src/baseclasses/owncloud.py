import requests


def delete_from_cloud(email):

    response = requests.delete(
        f'http://******:****************/ocs/v1.php/cloud/users/{email}')
    return response

#
def delete_file_from_cloud():

    response = requests.delete(
        f'/remote.php/dav/files/***************/PS')
    return response

delete_file_from_cloud()