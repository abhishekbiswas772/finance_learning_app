from flask import jsonify
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import request
import os
from sqlalchemy.orm import class_mapper
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models.model import Chapter, SubChapter

blp = Blueprint("Chapters", __name__, "Containing Chapter Details")

@blp.route("/api/v1/finance/get_chapters")
class ChapterService(MethodView):
    def get(self):
        chapter_items = Chapter.query.all()
        if chapter_items:
            data = {"status": True, "data": chapter_items}
            return jsonify(data), 200
        else:
            data = {"status": False, "data": "[]"}
            return jsonify(data), 500
        
    
    def post(self):
        chapter_data = request.json 
        if not chapter_data:
            abort(400, message="No data provided")
        subchapters_data = chapter_data.pop('subchapters', [])
        chapter = Chapter(**chapter_data)
        for subchapter_data in subchapters_data:
            subchapter = SubChapter(**subchapter_data)
            chapter.subchapters.append(subchapter)
        try:
            db.session.add(chapter)
            db.session.commit()
            serialized_chapter = ChapterService.serialize(self, chapter)
            return jsonify({
                "data" : serialized_chapter,
                "status" : True
            }), 201
        except IntegrityError as iErr:
            print(iErr)
            abort(400, message="Chapter or Subchapter already present in database")
        except SQLAlchemyError as sqlError:
            print(sqlError)
            abort(500, message="Error occurred while inserting data into database")

    def serialize(self, instance):
        columns = [column.key for column in class_mapper(instance.__class__).columns]
        return {column: getattr(instance, column) for column in columns}
