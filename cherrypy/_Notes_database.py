import os
import requests
import json


class _Notes_database:

	# initialize databse
	def __init__(self):
		self.notes = dict()

	def add_note(self, timestamp, data):
		self.notes[timestamp] = data

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

