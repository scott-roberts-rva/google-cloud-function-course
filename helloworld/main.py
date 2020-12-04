
def hello_world(request):
    request_args = request.args
    request_json = request.get_json(silent=True)
    name = "World"
    if request_args and 'name' in request_args:
        name = request_args['name']
    if request_json and 'name' in request_json:
        name = request_json['name']
    return f"Hello {name}"