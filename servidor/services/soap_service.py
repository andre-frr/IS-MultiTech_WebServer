from spyne import Application, rpc, ServiceBase, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import json

TASKS_FILE = "servidor\tasks.json"


class TaskService(ServiceBase):

    @rpc(String, _returns=String)
    def add_task(ctx, description):
        tasks = load_tasks()
        tasks.append(description)
        save_tasks(tasks)
        return f"Tarefa adicionada: {description}"

    @rpc(_returns=String)
    def list_tasks(ctx):
        tasks = load_tasks()
        return ", ".join(tasks) if tasks else "Nenhuma tarefa."


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)


application = Application([TaskService], 'task.manager.soap',
                          in_protocol=Soap11(), out_protocol=Soap11())

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8001, WsgiApplication(application))
    print("SOAP Server running on port 8001...")
    server.serve_forever()
