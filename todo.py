```python
# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Creating a database connection
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# Creating a table for tasks
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks
    (id INTEGER PRIMARY KEY AUTOINCREMENT, task_name TEXT, done INTEGER)
''')
conn.commit()

# Function to add new task
def add_task():
    task_name = task_entry.get()
    if task_name:
        cursor.execute('INSERT INTO tasks (task_name, done) VALUES (?, 0)', (task_name,))
        conn.commit()
        task_entry.delete(0, tk.END)
        update_task_list()

# Function to delete task
def delete_task():
    try:
        task_id = int(task_list.curselection()[0])
        task_text = task_list.get(task_id)
        cursor.execute('DELETE FROM tasks WHERE task_name=?', (task_text,))
        conn.commit()
        update_task_list()
    except IndexError:
        messagebox.showwarning('Error', 'Select a task to delete')

# Function to mark task as done
def mark_task_as_done():
    try:
        task_id = int(task_list.curselection()[0])
        task_text = task_list.get(task_id)
        cursor.execute('UPDATE tasks SET done=1 WHERE task_name=?', (task_text,))
        conn.commit()
        update_task_list()
    except IndexError:
        messagebox.showwarning('Error', 'Select a task to mark as done')

# Function to update task list
def update_task_list():
    task_list.delete(0, tk.END)
    cursor.execute('SELECT task_name, done FROM tasks')
    tasks = cursor.fetchall()
    for task in tasks:
        if task[1] == 1:
            task_list.insert(tk.END, f'[X] {task[0]}')
        else:
            task_list.insert(tk.END, f'[ ] {task[0]}')

# Creating the main window
root = tk.Tk()
root.title('Todo App')

# Creating task entry field
task_label = tk.Label(root, text='Task Name')
task_label.pack()
task_entry = tk.Entry(root)
task_entry.pack()

# Creating buttons for adding, deleting, and marking tasks as done
button_frame = tk.Frame(root)
button_frame.pack()
add_button = tk.Button(button_frame, text='Add Task', command=add_task)
add_button.pack(side=tk.LEFT)
delete_button = tk.Button(button_frame, text='Delete Task', command=delete_task)
delete_button.pack(side=tk.LEFT)
done_button = tk.Button(button_frame, text='Mark as Done', command=mark_task_as_done)
done_button.pack(side=tk.LEFT)

# Creating task list
task_list = tk.Listbox(root)
task_list.pack()

# Updating task list on startup
update_task_list()

# Running the application
if __name__ == '__main__':
    root.mainloop()
```