import peewee

db = peewee.PostgresqlDatabase(
    "postgres", user="postgres", password="17122020", host="localhost"
)


class Advertisement(peewee.Model):
    image = peewee.CharField()
    title = peewee.CharField()
    data = peewee.CharField()
    beds = peewee.CharField()
    descriptions = peewee.TextField()
    price = peewee.CharField(max_length=63)
    currency = peewee.CharField(max_length=1)

    class Meta:
        database = db
        db_table = "advertisements"


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
