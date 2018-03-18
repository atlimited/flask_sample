import os.path
from flask import Flask, Response

app = Flask(__name__)
app.config.from_object(__name__)

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_resource(path):  # pragma: no cover
    complete_path = os.path.join(root_dir(), path)
    content = get_file(complete_path)
    return Response(content, mimetype='text/html')

if __name__ == '__main__':  # pragma: no cover
    app.run(host='0.0.0.0', debug=True, port=5000)
