from flask import abort
from app.leakbuster.model import LeakGeneralMD
import sqlalchemy
from app.leakbuster.utils import get_random_string
import requests
import os


class General:

    def create_general(self, request):

        try:

            url = request.json['url']
            prefix = f"{os.getcwd()}\\leakbuster\\downloads\\"
            path = f"{prefix}leak_{get_random_string(6)}.html"

            resp = requests.get(url).content.decode()

            with open(path, 'wt') as arq:
                arq.write(resp)
            arq.close()

            general = LeakGeneralMD(
                leaks=path,
                leak_id=request.json['leak_id']
            )

            general.commit()
        except sqlalchemy.exc.IntegrityError as e:
            abort(500, "Integrity Error")
        except KeyError:
            abort(400, "Missing parameters")
        except Exception as e:
            abort(500, f"Error: {e}")
        return {
            "Status": "Success",
            "Message": "Leak Content registered successfully!",
            "data": general.serialized
        }

    def get_generals(self, request):
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        data = LeakGeneralMD.query.paginate(offset, limit, False)
        return {"Status": "Success", "data": [x.serialized for x in data.items]}

    def get_general(self, id):
        general = LeakGeneralMD.query.get_or_404(id, description="Leak Content ID not found")
        return {'Status': 'Success', 'data': general.serialized}

    def delete_general(self, id):
        general = LeakGeneralMD.query.get_or_404(id, description="Leak Content ID not found")
        general.delete()
        return {
            "Status": "Success",
            "Message": "Leak Content Successfully deleted"
        }
