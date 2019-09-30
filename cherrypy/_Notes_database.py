import os
import requests
import json
from datetime import datetime


class _Notes_database:

	# initialize databse
	def __init__(self):
		self.notes = dict()
		self.outfile = open("note_output.txt","w+")

	def add_note(self, data):
		now = datetime.now()
		timestamp = now.strftime("%d/%m %H:%M:%S")

		note = data["note"]
		self.notes[timestamp] = note
		print(self.notes)

		self.outfile.write("timestamp: {}\n".format(timestamp))
		self.outfile.write("note: \n{}\n\n".format(note))

	def get_note(self, timestamp):
		if timestamp in self.notes.keys():
			return self.notes[timestamp]
		else:
			return "Not Found."

	def get_all_notes(self):
		return json.dumps(self.notes)

	def delete_note(self, timestamp):
		self.notes.pop(timestamp)

	def delete_all_notes(self):
		self.notes.clear()

