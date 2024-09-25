from flask import Flask, request, jsonify 
from models.task import Task

app = Flask(__name__)

# CRUD = creat, read, update, delete
tasks = []
task_id_controle = 1

@app.route('/tasks', methods=['POST'])
def criar_task():
    global task_id_controle
    data = request.get_json()
    nova_task = Task(id=task_id_controle,titulo=data.get("titulo"), descricao=data.get("descrição", ""))
    task_id_controle += 1
    tasks.append(nova_task)
    print(tasks)
    return jsonify({"mensagem": "Nova tarefa criada com sucesso!"})


if  __name__ == "__main__":
    app.run(debug=True)
    