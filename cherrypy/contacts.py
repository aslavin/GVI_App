# contacts Controller

import json
import cherrypy

class contactsController:

	def __init__(self, gvidb):
		self.gvidb = gvidb
	
	# create a new contact
	def POST_CONTACT(self):
		msg = json.loads(cherrypy.request.body.read())
		self.gvidb.set_contact(0, msg)
		return json.dumps({"result": "success"})
	
	# get an existing contact
	def GET_CONTACT(self, contact_id):
		return json.dumps(self.gvidb.get_contact(int(contact_id)))

	# change an existing contact
	def PUT_CONTACT(self, contact_id):
		self.gvidb.set_contact(int(contact_id), json.loads(cherrpy.request.body.read()))
		return json.dumps({"result": "success"})

	# delete an existing contact
	def DELETE_CONTACT(self, contact_id):
		self.gvidb.delete_contact(int(contact_id))
		return json.dumps({"result": "success"})
