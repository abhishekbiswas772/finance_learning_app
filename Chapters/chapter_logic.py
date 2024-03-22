from flask import jsonify
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import request
import os
from sqlalchemy.orm import class_mapper
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models.model import Chapter, SubChapter
import json

blp = Blueprint("Chapters", __name__, "Containing Chapter Details")

@blp.route("/api/v1/finance/get_chapters")
class ChapterService(MethodView):
    def get(self):
        chapter_items = Chapter.query.all()
        if chapter_items:
            result = []
            for item in chapter_items:
                data_dict = {
                    'id' : item.id,
                    'title' : item.title,
                    'content' : item.content,
                    'time_to_complete' : item.time_to_complete,
                    'points' : item.points
                }
                data_dict_sub = item.subchapters
                res_sub = []
                for item_sub in data_dict_sub:
                    data_sub_dict = {
                        "id" : item_sub.id,
                        "title" : item_sub.title,
                        "content" : item_sub.content,
                        "chapter_id" : item_sub.chapter_id,
                        'points' : item_sub.points
                    }
                    res_sub.append(data_sub_dict)
                data_dict['sub_chapters'] = res_sub
                result.append(data_dict)
            data = {"status": True, "data": result}
            return jsonify(data), 200
        else:
            data = {"status": False, "data": "[]"}
            return jsonify(data), 500
        
    
    def post(self):
        chapter_data = request.json 
        if not chapter_data:
            abort(400, message="No data provided")
        subchapters_data = chapter_data.pop('subchapters', [])
        chapter = Chapter()
        chapter.title = chapter_data.get("title")
        chapter.content = chapter_data.get("content")
        chapter.time_to_complete = chapter_data.get("time_to_complete")
        chapter.points = chapter_data.get("points")
        for subchapter_data in subchapters_data:
            subchapter = SubChapter(**subchapter_data)
            chapter.subchapters.append(subchapter)
        try:
            db.session.add(chapter)
            db.session.commit()
            return jsonify({
                "status" : True,
                'data' : chapter_data
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

