import mongoengine

class Teachers(mongoengine.Document):

    teacher_mail = mongoengine.EmailField(required=True)
    teacher_first_name = mongoengine.StringField(required=True)
    teacher_last_name = mongoengine.StringField(required=True)
    password = mongoengine.StringField(required=True)
    phone_number = mongoengine.StringField(required=True)
    profile_picture = mongoengine.ImageField()
    school = mongoengine.StringField(default="Menofia University")
    meta = {
        'db_alias': 'core',
        'collection':'teachers',
        'auto_create_index': False,
        'indexes':[
            'mail'
        ]
    }