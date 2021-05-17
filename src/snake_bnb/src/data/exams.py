import random
from exam import Exam
from datetime import date
import mongoengine

class Exams(mongoengine.DynamicDocument):
    title = mongoengine.StringField(required=True)
    author = mongoengine.StringField()
    exame_code = mongoengine.StringField('{}{}{}'.format(title[0:3], random.randrange(100000, 1000000, 1), author[0:3]))
    creation_date = mongoengine.DateTimeField(date.today())
    exame = mongoengine.EmbeddedDocumentField(Exam)
    meta = {
        'db_alias': 'core',
        'collection': 'exams',
        'indexs': 'exame_code'
    }
