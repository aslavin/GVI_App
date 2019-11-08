# Notes DB -- version 1.1
# Matthew J. Malir

import os
import requests
import json
import csv
import pickle
from datetime import datetime


class _Notes_database:
	# initialize database
	def __init__(self):
		try: # try to load existing db
			in_file = open("data/note_db.pickle","rb")
			self.notes = pickle.load(in_file)
		except: # create new db
			self.notes = dict()

	def add_note(self, data):
		now = datetime.now()
		timestamp = now.strftime("%d/%m %H:%M:%S")

		note = data["note"]  # strip leading newline
		self.notes[timestamp] = note

		# update physical db
		self.write_db()

	def set_note(self,timestamp,new_note):
		if timestamp in self.notes.keys():
			self.notes[timestamp] = new_note

		# update physical db
		self.write_db()


	def get_note(self, timestamp):
		if timestamp in self.notes.keys():
			return self.notes[timestamp]
		else:
			return "Not Found."

	def get_all_notes(self):
	 	return json.dumps(self.notes)

	def delete_note(self, timestamp):
		self.notes.pop(timestamp)

		# update physical db
		self.write_db()

	# def delete_all_notes(self):
	# 	self.notes.clear()
	#
	# 	# update physical db
	# 	self.write_db()

	# write changes to physical db
	def write_db(self):
		# write to csv for viewing
		f = open("data/note_db_current.csv","w+")
		w = csv.writer(f)
		for key, val in self.notes.items():
		    w.writerow([key, val])
		    f.write("{}, {}".format(key, val))
		f.close()
		# write to pickle file for restarting db
		out_file = open("data/note_db.pickle","wb")
		pickle.dump(self.notes,out_file)
		out_file.close()


