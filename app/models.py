from app import app
from app import db
from flask.ext.restful import fields, marshal

book_fields = {
	'id': fields.String,
	'name': fields.String,
	'note': fields.String
}

class GlBook(db.Model):
	id = db.Column(db.String(32), primary_key = True)
	name = db.Column(db.String(240))
	note = db.Column(db.String(600))

	def __repr__(self):
		return '<GlBook %r>' % (self.name)