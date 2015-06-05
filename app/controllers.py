from app import app, db, models
from flask.ext.restful import Api, Resource, reqparse, fields, marshal

api = Api(app)

class GlBookAPI(Resource):

	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('id', type=str, location='json')
		self.reqparse.add_argument('name', type=str, location='json')
		self.reqparse.add_argument('note', type=bool, location='json')
		super(GlBookAPI, self).__init__()

	def get(self, id):
		book = models.GlBook.query.get(id)
		return {'GlBook': marshal(book, models.book_fields)}

	# def put(self, id):
	# 	task = [task for task in tasks if task['id'] == id]
	# 	if len(task) == 0:
	# 		abort(404)
	# 	task = task[0]
	# 	args = self.reqparse.parse_args()
	# 	for k, v in args.items():
	# 		if v is not None:
	# 			task[k] = v
	# 	return {'task': marshal(task, task_fields)}

	# def delete(self, id):
	#   task = [task for task in tasks if task['id'] == id]
	#   if len(task) == 0:
	#       abort(404)
	#   tasks.remove(task[0])
	#   return {'result': True}

api.add_resource(GlBookAPI, '/GlBook/<int:id>', endpoint='GlBook')