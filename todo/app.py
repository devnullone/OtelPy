import requests
from flask import Flask, jsonify
from opentelemetry.trace import (
    format_span_id,
    format_trace_id,
    get_current_span,
    get_tracer_provider
)

# tarcer = get_tracer_provider().get_tracer(__name__)
# with tarcer.start_as_current_span('TODO app.py'):
#     current_span = get_current_span()
#     current_span.add_event('Loading TODO app.py')


app = Flask(__name__)
user_service_host = 'user'

@app.route('/')
def index():
    return 'Hello world'

def get_user():
    r = requests.get(f'http://{user_service_host}:5000/user/profile')
    return r.json()

@app.route('/todo')
def get_todo():
    user = get_user()
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    print("getting todos")
    todos = r.json()
    return jsonify(todos)

@app.route('/todo/<int:id>')
def get_todo_by_id(id):
    user = get_user()
    if id == '5':
        print_trace_data()
        raise Exception('This todo have invalid id: 5')
    r = requests.get(f'https://jsonplaceholder.typicode.com/todos/{id}')
    todo = r.json()
    return jsonify(todo)


def print_trace_data():
    span_context = get_current_span().context
    if span_context:
        trace_id = format_trace_id(span_context.trace_id)
        span_id = format_span_id(span_context.span_id)
        print(f'Trace ID: {trace_id}')
        print(f'Span ID: {span_id}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
