import mongoengine


class Owner(mongoengine.Document):
    mail = mongoengine.EmailField(required=True)
    first_name = mongoengine.StringField(required=True)
    last_name = mongoengine.StringField(required=True)
    password = mongoengine.StringField(required=True)
    phone_number = mongoengine.StringField(required=True)

    meta = {

    }