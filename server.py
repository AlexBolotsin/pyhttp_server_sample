from aiohttp import web
import db_test

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    print(request.match_info)
    return web.Response(text=text)

async def get_servers(request):
	data = db_test.get_servers()
	text = ', '.join(str(e) for e in data)
	return web.Response(text=text)

async def post_lookup_server(request):
	data = await request.json()
	id = data['id']
	response = db_test.lookup_server(id)
	return web.Response(text=str(response))

async def post_add_server(request):
	data = await request.json()
	name = data['name']
	response = db_test.add_server(name)
	return web.Response(text=str(response))

async def post_delete_server(request):
	data = await request.json()
	id = data['id']
	response = db_test.delete_server(id)
	return web.Response(text=str(response))

async def post_regexp_search(request):
	data = await request.json()
	req = data['request']
	entries = db_test.lookup_by_name(req)
	text = ', '.join(str(e) for e in entries)
	return web.Response(text=text)


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/list', get_servers)
app.router.add_post('/lookup', post_lookup_server)
app.router.add_post('/insert', post_add_server)
app.router.add_post('/delete', post_delete_server)
app.router.add_post('/search', post_regexp_search)

web.run_app(app)