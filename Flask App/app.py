from asyncio import tasks
from flask import Flask, render_template,redirect,url_for,request
from models.task import Task



app = Flask(__name__)
tasks = []


@app.route("/")
def index():
    return render_template('index.html',tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    if request.method == 'POST':
        label = request.form['label']
        if not label: return redirect('/')
        new_task = Task(len(tasks)+1, False,label) 
        tasks.append(new_task)
        return redirect('/')

@app.route('/update_task/<string:id>', methods=['POST'])
def update_task(id):
    for task in tasks:
        if(task.id == int(id)):
            task.done = not task.done
    return redirect('/')        

@app.route('/delete_task/<string:id>', methods=['POST'])
def delete_task(id):
    i = 0
    for task in tasks:

        if(task.id == int(id)):
            tasks.pop(i)
            break
        i += 1
    return redirect('/')  

if __name__ == '__main__':
    app.run(debug=True)