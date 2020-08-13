from flask_restplus import Api, Resource, fields, reqparse
from flask import Blueprint, request
from .models import Data
from source.main import db



api_bp = Blueprint('api', __name__)
api = Api(app=api_bp, version="1.0", title="title",
          description="description")
ns = api.namespace('api', description='description')

# add model description like serializer
# model = api.model('Log', {
#     'string': fields.String,
#     'date': fields.DateTime,
#     etc...
# })

# or in argument style
parser = reqparse.RequestParser()
parser.add_argument('argument')


@ns.route('/')
class APIList(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(parser)
    def get(self):
        try:
            args = parser.parse_args()
            # work with argument
            return {}
        except KeyError as e:
            ns.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            ns.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.expect(parser)
    def post(self):
        try:
            log = request.get_json()
            # work with argument
            return {
                'data': {},
            }
        except KeyError as e:
            ns.abort(500, e.__doc__, status="Could not save information", statusCode="500")
        except Exception as e:
            ns.abort(400, e.__doc__, status="Could not save information", statusCode="400")
