import peewee

db = peewee.SqliteDatabase('house_in_toronto.db')

# db = peewee.PostgresqlDatabase(
#     'postgres',  # Required by Peewee.
#     user='postgres',  # Will be passed directly to psycopg2.
#     password='17122020',  # Ditto.
#     host='localhost')  # Ditto.


class Advertisement(peewee.Model):
    id = peewee.IntegerField(primary_key=True, unique=True)
    image = peewee.CharField(max_length=3000)
    title = peewee.CharField(max_length=3000)
    data = peewee.CharField(max_length=3000)
    beds = peewee.CharField(max_length=3000)
    descriptions = peewee.CharField(max_length=3000)
    prise = peewee.CharField(max_length=3000)

    class Meta:
        database = db
        db_table = 'advertisements'


# db.connect()
# db.create_tables([Advertisement])
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
