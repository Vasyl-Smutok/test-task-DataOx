import peewee

db = peewee.SqliteDatabase("house_in_toronto.db")

# db = peewee.PostgresqlDatabase(
#     'postgres',
#     user='postgres',
#     password='17122020',
#     host='localhost')


class Advertisement(peewee.Model):
    id = peewee.IntegerField(primary_key=True, unique=True)
    image = peewee.CharField(max_length=255)
    title = peewee.CharField(max_length=255)
    data = peewee.DateTimeField()
    beds = peewee.CharField(max_length=255)
    descriptions = peewee.CharField(max_length=1000)
    price = peewee.CharField(max_length=63)
    currency = peewee.CharField(max_length=1)

    class Meta:
        database = db
        db_table = "advertisements"


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
    price: str,
    currency: str,
):

    new_advertisement = Advertisement.create(
        image=image,
        title=title,
        data=data,
        city=city,
        beds=beds,
        descriptions=descriptions,
        price=price,
        currency=currency,
    )

    new_advertisement.save()
