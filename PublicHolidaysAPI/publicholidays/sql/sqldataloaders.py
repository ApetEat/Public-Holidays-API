from os.path import dirname, join

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
country_data = lambda x, y: load_sql_data('country.sql')
community_data = lambda x, y: load_sql_data('community.sql')
province_data = lambda x, y: load_sql_data('province.sql')
locality_data = lambda x, y: load_sql_data('locality.sql')
public_holiday_data = lambda x, y: load_sql_data('publicholidaycalendar.sql')
