import peewee


db = peewee.SqliteDatabase('house_in_toronto.db')

# db = peewee.PostgresqlDatabase(
#     'database_name',  # Required by Peewee.
#     user='postgres',  # Will be passed directly to psycopg2.
#     password='secret',  # Ditto.
#     host='localhost')  # Ditto.


class Advertisement(peewee.Model):
    id = peewee.IntegerField(primary_key=True)
    image = peewee.CharField()
    title = peewee.CharField()
    data = peewee.CharField()
    beds = peewee.CharField()
    descriptions = peewee.CharField()
    prise = peewee.CharField()

    class Meta:
        database = db
        db_table = 'advertisements'


Advertisement.create_table()


def add_data_to_db(
        image: str,
        title: str,
        data: str,
        city: str,
        beds: str,
        descriptions: str,
        prise: str,
):

    new_advertisement = Advertisement.create(
        image=image,
        title=title,
        data=data,
        city=city,
        beds=beds,
        descriptions=descriptions,
        prise=prise,
    )

    new_advertisement.save()
