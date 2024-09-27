import pytest
import requests

#CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    new_task_data = {
        "titulo": "Nova tarefa",
        "descricao": "Descricao da nova tarefa"
    }
    response = requests.post(f'{BASE_URL}/tasks', json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "mensagem" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']

def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completa": True,
            "descricao": "nova descricao",
            "titulo": "New tarefa"
        }
        response = requests.put(f'{BASE_URL}/tasks/{task_id}', json=payload)
        response.status_code == 200
        response_json = response.json()
        assert "mensagem" in response_json

        #  Nova requisicao da tarefa especifica
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["titulo"] == payload["titulo"]
        assert response_json["descricao"] == payload["descricao"]
        assert response_json["completa"] == payload["completa"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 200

        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 404