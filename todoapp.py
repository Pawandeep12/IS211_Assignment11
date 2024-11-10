from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global list to store To-Do items
todo_items = []

@app.route('/')
def index():
    # Display the To-Do list items and the form to add new items
    return render_template('index.html', items=todo_items)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form.get('task')
    email = request.form.get('email')
    priority = request.form.get('priority')
    
    # Simple validation for email and priority
    if not task or not email or priority not in ['Low', 'Medium', 'High']:
        return redirect(url_for('index'))
    
    # Add new item to list if valid
    todo_items.append({'task': task, 'email': email, 'priority': priority})
    return redirect(url_for('index'))

@app.route('/clear')
def clear():
    # Clear the list of To-Do items
    todo_items.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
