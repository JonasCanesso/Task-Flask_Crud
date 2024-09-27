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
    return jsonify({"mensagem": "Nova tarefa criada com sucesso!", "id": nova_task.id})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.para_dicionario() for task in tasks]

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for atividade in tasks:
        if atividade.id == id:
            return jsonify(atividade.para_dicionario())

    return jsonify({"mensagem": "Não foi possivel encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):

    task = None
    for atividade in tasks:
        if atividade.id == id:
            task = atividade
            break

    print(task)

    if task == None:
        return jsonify({"mensagem": "Não foi possivel encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['titulo']
    task.descricao = data['descricao']
    task.completa = data['completa']
    print(task)
    return jsonify({"mensagem": "tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for atividade in tasks:
        if atividade.id == id:
            task = atividade
            break

    if task == None:
        return jsonify({"menssagem": "Não foi possivem encontrar a atividar"}), 404
    
    tasks.remove(task)
    return jsonify({"menssagem": "Tarefa deletada com sucesso!"})

if  __name__ == "__main__":
    app.run(debug=True)