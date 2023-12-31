from django.db import models
from mongoengine import Document, FileField, ListField, StringField, connect, DateTimeField, IntField, SequenceField, ReferenceField


class Post_blog(Document):
    id = SequenceField(primary_key=True)
    title = StringField()
    content = StringField()

    created_at  = IntField()
    category = StringField()


class Works_blog(Document):
    id = SequenceField(primary_key=True)
    title = StringField()
    content = StringField()
    images = ListField(StringField())
    created_at  = IntField()
    category = StringField()
# Create your models here.
