# backend will send calls to database using shareplum

import os
import requests
import json
import testShare as testShare
from dotenv import load_dotenv
from shareplum import Site
from shareplum import Office365

class _GVI_database:
	
	# initialize databse
	def __init__(self):
		# TODO: any initialization
		load_dotenv()
		user = os.getenv("GVI_USER")
		passwd = os.getenv("GVI_PASSWD")
		url = 'https://cseserviceproj.sharepoint.com'
		self.spSite = testShare.initSite(user, passwd, url)
		self.spList = testShare.getList(self.spSite, "TestList_Collection")
		self.contacts = {}
		self.contacts[0] = {"key": "value"}
	
	# TODO: add any necessary functions for modifying database

	# set a new contact
	def set_contact(self, contact_id, data):
		# TODO: create id system
		testShare.AddItem(self.spList, [data])
		self.contacts[contact_id] = data


	# get a specific contact by id
	def get_contact(self, contact_id):
		# TODO: get by id system
		return self.contacts[contact_id]

	# remove contact id from contacts dict
	def delete_contact(self, contact_id):
		self.contacts.pop(contact_id)

