from app.leakbuster import db
from flask import abort
from app.leakbuster.model import LeakSourceMD
import sqlalchemy


class Source:

    def create_leak(self, request):

        try:

            leak_source = LeakSourceMD(
                url=request.json['url'],
                description=request.json['description'],
                date=request.json['date'],
                author=request.json['author']
            )

            db.session.add(leak_source)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            abort(500)
        except KeyError:
            abort(400, "Missing parameter")
        return {
            "Status": "Success",
            "Message": "Leak registered successfully!",
            "data": leak_source.serialized
        }

    def get_leaks(self, request):
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        data = LeakSourceMD.query.paginate(offset, limit, False)
        return {"Status": "Success", "data": [x.serialized for x in data.items]}

    def get_leak(self, id):
        source = LeakSourceMD.query.get_or_404(id, description="Leak Source ID not found")
        return {'Status': 'Success', 'data': source.serialized}

    def delete_leak(self, id):
        source = LeakSourceMD.query.get_or_404(id, description="Leak Source ID not found")
        db.session.delete(source)
        db.session.commit()
        return {
            "Status": "Success",
            "Message": "Leak Successfully deleted"
        }

    def update_leak(self, request, id):

        source = LeakSourceMD.query.get_or_404(id, description="Leak Source ID not found")
        source.url = request.json['url']
        source.date = request.json['date']
        source.description = request.json['description']
        source.author = request.json['author']

        try:
            db.session.add(source)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            abort(500, "Something went wrong, verify user data and try again")
        return {
            "Status": "Success",
            "Message": "Leak Source updated successfully",
            "data": source.serialized
        }
