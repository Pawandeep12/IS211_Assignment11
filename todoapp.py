from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


todo_items = []

@app.route('/')
def index():
    
    return render_template('index.html', items=todo_items)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form.get('task')
    email = request.form.get('email')
    priority = request.form.get('priority')
    
    
    if not task or not email or priority not in ['Low', 'Medium', 'High']:
        return redirect(url_for('index'))
    
    
    todo_items.append({'task': task, 'email': email, 'priority': priority})
    return redirect(url_for('index'))

@app.route('/clear')
def clear():
    
    todo_items.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
