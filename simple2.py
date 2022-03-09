import flask
app = flask.Flask(__name__)

def pipeline(inp):
    output = []
    for i in range(inp):
        output.append(('data1','data2','data3'))
    return output

@app.route('/', methods=['GET'])
def index():
    return str(pipeline(3))
