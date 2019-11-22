import json
import cherrypy

class notesController:
	def __init__(self, notesdb):
		self.notesdb = notesdb

	# create a new note
	def POST_NOTE(self):
		msg = json.loads(cherrypy.request.body.read())
		self.notesdb.add_note(msg)
		return json.dumps({"result": "success"})

	# get existing notes
	def GET_NOTES(self):
		notes = self.notesdb.get_all_notes()
		return json.dumps({"result": "sucess", "notes": notes})

	# get an existing note
	def GET_NOTE(self, note_id):
		return json.dumps(self.notesdb.get_note(note_id))

	# change an existing note
	def POST_UPDATED_NOTE(self):
		print("here")
		self.notesdb.set_note(json.loads(cherrypy.request.body.read()))
		return json.dumps({"result": "success"})

	# delete an existing note
	def DELETE_NOTE(self, note_id):
		self.notesdb.delete_note(note_id)
		return json.dumps({"result": "success"})
