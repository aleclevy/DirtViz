from . import *


class GetCellDataSchema(ma.SQLAlchemySchema):
    """validates get request for cell data"""

    cellId = ma.Int()
    startTime = ma.DateTime(required=False)
    endTime = ma.DateTime(required=False)

    # @validates('time_created')
    # def is_not_in_future(value):
    #     """'value' is the datetime parsed from time_created by marshmallow"""
    #     now = datetime.now()
    #     if value > now:
    #         raise ValidationError("Can't create notes in the future!")
