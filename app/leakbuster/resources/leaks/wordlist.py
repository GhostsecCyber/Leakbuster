from flask import abort
from app.leakbuster.model import PasswordWordlist
import sqlalchemy


class Wordlist:

    def add_wordlist(self, request):

        wordlist = PasswordWordlist()

        try:
            for passwd in request.json['password']:
                if passwd != "":
                    wordlist = PasswordWordlist(password=passwd)
                    wordlist.commit()

        except sqlalchemy.exc.IntegrityError:
            abort(500, "Integrity Error")
        except KeyError:
            abort(400, "Missing parameters")
        except Exception as e:
            abort(500, f"Error: {e}")
        return {
            "Status": "Success",
            "Message": "Password registered successfully in our wordlist!",
            "data": wordlist.serialized
        }

    def get_wordlists(self, request):
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        data = PasswordWordlist.query.paginate(offset, limit, False)
        return {"Status": "Success", "data": [x.serialized for x in data.items]}
