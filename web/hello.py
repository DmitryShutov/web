def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    res  = environ['QUERY_STRING'].split("&")
    res = [item+"\r\n" for item in res]
    return res