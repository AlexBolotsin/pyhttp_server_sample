from sqlalchemy import create_engine


def get_servers():
	eng = create_engine('postgresql:///servers')
	con = eng.connect()

	rs = con.execute("SELECT * FROM entries")
	items = rs.fetchall()
	con.close()
	return items

def lookup_server(id):
	eng = create_engine('postgresql:///servers')
	con = eng.connect()

	rs = con.execute("SELECT * FROM entries WHERE id=" + id)
	items = rs.fetchone()
	con.close()
	return items


def delete_server(id):
	eng = create_engine('postgresql:///servers')
	con = eng.connect()

	rs = con.execute("DELETE FROM entries WHERE id=" + id)
	#items = rs.fetchone()
	con.close()
	return "item"

def add_server(name):
	eng = create_engine('postgresql:///servers')
	con = eng.connect()

	rs = con.execute("INSERT INTO entries (server_name) VALUES ('" + name + "')")
	#item = rs.inserted_primary_key
	con.close()
	return "item"

def lookup_by_name(req):
	eng = create_engine('postgresql:///servers')
	con = eng.connect()

	rs = con.execute("SELECT * FROM entries WHERE server_name LIKE '" + req + "'")
	items = rs.fetchall()
	print(items)
	con.close()
	return items