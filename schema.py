from marshmallow import Schema, fields

class ChapterSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    time_to_complete = fields.Str(required=True)
    subchapters = fields.Nested('SubChapterSchema', many=True)

class SubChapterSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    time_to_complete = fields.Str(required=True)


    
