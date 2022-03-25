from flask import abort
from app.leakbuster.model import LeakEmailMD, LeakPasswordMD, PasswordWordlist
import sqlalchemy


class Email:

    def create_mail(self, request):

        try:

            mail_leak = LeakEmailMD(
                email=request.json['email'],
                leak_id=request.json['leak_id']
            )
            password_leak = LeakPasswordMD(
                leak_id=request.json['leak_id'],
                leak_password=request.json['leak_password']
            )

            if request.json['leak_password'] and request.json['leak_password'] != "":
                passWord = PasswordWordlist(leak_password=request.json['leak_password'])
                passWord.commit()

            mail_leak.leak_password.append(password_leak)
            mail_leak.commit()
        except sqlalchemy.exc.IntegrityError as e:
            abort(500, "Integrity Error")
        except KeyError:
            abort(400, "Missing parameters")
        except Exception as e:
            abort(500, f"Error: {e}")
        return {
            "Status": "Success",
            "Message": "Mail registered successfully!",
            "data": mail_leak.serialized
        }

    def get_mails(self, request):
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        data = LeakEmailMD.query.paginate(offset, limit, False)
        return {"Status": "Success", "data": [x.serialized for x in data.items]}

    def get_mail(self, id):
        mail = LeakEmailMD.query.get_or_404(id, description="Mail ID not found")
        return {'Status': 'Success', 'data': mail.serialized}

    def delete_mail(self, id):
        mail = LeakEmailMD.query.get_or_404(id, description="Mail ID not found")
        password = LeakPasswordMD.query.get_or_404(id)
        mail.delete()
        password.delete()
        return {
            "Status": "Success",
            "Message": "Mail Successfully deleted"
        }

    def update_mail(self, request, id):

        mail = LeakEmailMD.query.get_or_404(id, description="Mail ID not found")
        mail.email = request.json['email']
        password = LeakPasswordMD.query.get_or_404(id)
        password.leak_password = request.json['leak_password']
        mail.leak_password.append(password)

        try:
            mail.commit()
        except sqlalchemy.exc.IntegrityError:
            abort(500, "Something went wrong, verify your data and try again")
        return {
            "Status": "Success",
            "Message": "Mail updated successfully",
            "data": mail.serialized
        }
