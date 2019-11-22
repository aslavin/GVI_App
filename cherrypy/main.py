# main.py
# Andrew Slavin
# 

import cherrypy
import json
from _GVI_database import _GVI_database
from _Notes_database import _Notes_database
from contacts import contactsController
from notes import notesController

# set up cors
class optionsController:
	def OPTIONS(self, *args, **kwargs):
		return "" # return empty string

def CORS():
	cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
	cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
	cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"

cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)

# create new backend
gvidb = _GVI_database() # shared across all controllers
notesdb = _Notes_database()

# load all data
dispatcher = cherrypy.dispatch.RoutesDispatcher()

# create configuration, which is a dict
conf = { 'global': {'server.socket_host': '127.0.0.1',
		     'server.socket_port': 51017},
			 '/': {'request.dispatch':dispatcher,
					'tools.CORS.on': True} # tells it to use the dispatcher on any path
		}

# initialize controllers
contactsController = contactsController(gvidb)
notesController = notesController(notesdb)

# generic notes handlers
dispatcher.connect('postNote', '/notes/', controller=notesController, action='POST_NOTE', conditions=dict(method=['POST']))
dispatcher.connect('getNotes', '/notes/', controller=notesController, action='GET_NOTES', conditions=dict(method=['GET']))
dispatcher.connect('postUpdatedNote', '/update_notes/', controller=notesController, action='POST_UPDATED_NOTE', conditions=dict(method=['POST']))

# generic contact handlers
# dispatcher.connect('getContacts', '/contacts/', controller=contactsController, action='GET_CONTACTS', conditions=dict(method=['GET']))
dispatcher.connect('postContact', '/contacts/', controller=contactsController, action='POST_CONTACT', conditions=dict(method=['POST']))
# dispatcher.connect('deleteContacts', '/contacts/', controller=contactsController, action='DELETE_CONTACTS', conditions=dict(method=['DELETE']))

# specific contact handlers
dispatcher.connect('getContact', '/contacts/:contact_id', controller=contactsController, action='GET_CONTACT', conditions=dict(method=['GET']))
dispatcher.connect('putContact', '/contacts/:contact_id', controller=contactsController, action='PUT_CONTACT', conditions=dict(method=['PUT']))
dispatcher.connect('deleteContact', '/contacts/:contact_id', controller=contactsController, action='DELETE_CONTACT', conditions=dict(method=['DELETE']))

# options handlers - need one for each possible path definied above
dispatcher.connect('contacts_all__op', '/contacts/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
dispatcher.connect('contacts_key_op', '/contacts/:contact_id', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
dispatcher.connect('notes_all_op', '/notes/', controller=notesController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
dispatcher.connect('notes_all_op', '/update_notes/', controller=notesController, action='OPTIONS', conditions=dict(method=['OPTIONS']))


cherrypy.config.update(conf) #tells library what the configuration is

# tell app what the configuration is
app = cherrypy.tree.mount(None, config=conf)
cherrypy.quickstart(app)

