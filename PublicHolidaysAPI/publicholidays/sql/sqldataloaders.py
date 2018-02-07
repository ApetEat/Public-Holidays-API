import os.path import dirname, join

from django.db import connection

# Create your models here.


def load_sql_data(filename):
    """
    Load data to newly created database from seed.

    :param filename: sql feed filename
    """
    file_path = join(dirname(__file__), filename)
    sql_statement = open(file_path).read()
    with connection.cursor() as cursor:
        cursor.execute(sql_statement)

# Data to provide to migrations
community_data = lambda: load_sql_data('coummunity.sql')
province_data = lambda: load_sql_data('province.sql')
locality_data = lambda: load_sql_data('locality.sql')
