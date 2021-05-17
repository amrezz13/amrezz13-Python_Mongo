import json
from answer_student import Answer_student
import mongoengine

class Answers (mongoengine.Document):
    student_name = mongoengine.StringField(required=True)
    student_mail = mongoengine.EmailField(required=True)
    student_id = mongoengine.IntField(required=True)
    exame_code = mongoengine.StringField(required=True)
    student_result = mongoengine.FloatField(default=0)
    student_answers = mongoengine.EmbeddedDocument(Answer_student)
    meta = {
        'db_alias' : 'core',
        'collection' : 'student_answers',
        'indexes' : ['student_id', 'exame_code']
    }