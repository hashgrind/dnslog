from dnslib.server import *
import sqlite3

db_name = 'dns.db'

class LoggingSilentResolver:
	def handle_request(self, client, query):
		db = sqlite3.connect(db_name)
		cursor = db.cursor()
		cursor.execute('insert into questions values (strftime("%s", "now"), ?, ?)', (client, str(query)))
		db.commit()
		db.close()

	def resolve(self, request, handler):
		self.handle_request(handler.client_address[0], request.q.qname)
		return request.reply()

def main():
	db = sqlite3.connect(db_name)
	db.execute('create table if not exists questions (date datetime, client text, query text)')
	db.close()

	server = DNSServer(LoggingSilentResolver(), port=53, address='0.0.0.0', logger=DNSLogger(), tcp=False)

	server.start_thread()

	while server.isAlive():
		...

if '__main__' == __name__:
	main()

from dnslib.server import *
import sqlite3

db_name = 'dns.db'

class LoggingSilentResolver:
	def handle_request(self, client, query):
		db = sqlite3.connect(db_name)
		cursor = db.cursor()
		cursor.execute('insert into questions values (strftime("%s", "now"), ?, ?)', (client, str(query)))
		db.commit()
		db.close()

	def resolve(self, request, handler):
		self.handle_request(handler.client_address[0], request.q.qname)
		return request.reply()

def main():
	db = sqlite3.connect(db_name)
	db.execute('create table if not exists questions (date datetime, client text, query text)')
	db.close()

	server = DNSServer(LoggingSilentResolver(), port=53, address='0.0.0.0', logger=DNSLogger(), tcp=False)

	server.start_thread()

	while server.isAlive():
		...

if '__main__' == __name__:
	main()

