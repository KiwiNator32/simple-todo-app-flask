from flask import Flask, redirect, render_template, request, url_for
from pathlib import Path
import json
import uuid

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
# setups
def setup(app):
    f = Path('data/data.json')
    if not f.exists():
        f.parent.mkdir(exist_ok=True, parents=True)

        x = {
            "tasks": []
        }

        f.write_text(json.dumps(x, indent=4, sort_keys=True))
setup(app)

# routing

@app.route("/", methods=['GET'])
def main():
    f = open('data/data.json', 'r')
    tasks = json.loads(f.read())

    return render_template('home.html', tasks=tasks, title='Tasks')

@app.route("/tasks", methods=['POST', 'DELETE'])
@app.route("/tasks/<id>", methods=['POST', 'DELETE'])
def tasks(id=None):
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        id = uuid.uuid4()
        task = {
                'id': str(id),
                'title': title,
                'description': description 
            }

        f = Path('data/data.json')
        x = json.loads(f.read_text())
        x["tasks"].append(task)
        f.write_text(json.dumps(x, indent=4, sort_keys=True))

        return redirect(url_for('main'))
    elif request.method == 'DELETE':
        f = Path('data/data.json')
        x = json.loads(f.read_text())

        for task in x["tasks"]:
            if task["id"] == id:
                x["tasks"].remove(task)
                break

        f.write_text(json.dumps(x, indent=4, sort_keys=True))
        return {'id': id}