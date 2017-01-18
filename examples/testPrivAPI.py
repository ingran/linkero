# -*- coding: utf-8 -*-

import core.linkero as linkero

vusers = linkero.config['API']['testPrivAPI']['validUsers']

# TODOS Data
TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        linkero.abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = linkero.reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(linkero.Resource):
    @linkero.auth.login_required
    def get(self, todo_id):
        if linkero.checkUser(vusers) == False:
            linkero.abort(401)  # unauthorized
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    @linkero.auth.login_required
    def delete(self, todo_id):
        if linkero.checkUser(vusers) == False:
            linkero.abort(401)  # unauthorized
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    @linkero.auth.login_required
    def put(self, todo_id):
        if linkero.checkUser(vusers) == False:
            linkero.abort(401)  # unauthorized
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(linkero.Resource):
    @linkero.auth.login_required
    def get(self):
        if linkero.checkUser(vusers) == False:
            linkero.abort(401)  # unauthorized
        return TODOS

    @linkero.auth.login_required
    def post(self):
        if linkero.checkUser(vusers) == False:
            linkero.abort(401)  # unauthorized
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
def loadTestPrivAPI():
    linkero.api.add_resource(TodoList, '/todos')
    linkero.api.add_resource(Todo, '/todos/<todo_id>')