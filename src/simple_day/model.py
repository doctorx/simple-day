from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, NumberAttribute, BooleanAttribute
from .settings import Settings


class SimpleHabit(Model):

    class Meta:
        table_name = 'simple-habit'
        region = 'us-west-1'
        host = Settings().DYNAMODB_URL

    user = UnicodeAttribute(hash_key=True)
    date = UTCDateTimeAttribute(range_key=True)
    action = UnicodeAttribute()
    entity = UnicodeAttribute()
    measurement = UnicodeAttribute()
    measurement_value = NumberAttribute()
    feel = NumberAttribute()
    complete = BooleanAttribute()
