import tkinter as tk
from tkinter import ttk

def add_new_task():
    new_task = entry_task.get()
    if new_task:
        list_tasks.insert(tk.END, f"{len(list_tasks.get(0, tk.END))+1}. {new_task}")
        entry_task.delete(0, tk.END)

def delete_selected_task():
    selected_task_index = list_tasks.curselection()
    if selected_task_index:
        list_tasks.delete(selected_task_index)
        update_task_list()

def update_selected_task():
    selected_task_index = list_tasks.curselection()
    if selected_task_index:
        updated_text = entry_task.get()
        list_tasks.delete(selected_task_index)
        list_tasks.insert(selected_task_index, f"{selected_task_index[0]+1}. {updated_text}")
        entry_task.delete(0, tk.END)

def clear_task_entry(event):
    entry_task.delete(0, tk.END)

def update_task_list():
    tasks = list_tasks.get(0, tk.END)
    list_tasks.delete(0, tk.END)
    for index, task in enumerate(tasks, start=1):
        list_tasks.insert(tk.END, f"{index}. {task.split('. ', 1)[1]}")

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400+400+100")
root.configure(bg='#F5F5F5')

style = ttk.Style()

style.configure("TButton", padding=6, relief="flat", font=('Arial', 10), background='#4285F4', foreground='#000000')
style.configure("TEntry", padding=6, relief="flat", font=('Arial', 10))
style.configure("TListbox", padding=6, relief="flat", font=('Arial', 10), background='#E0E0E0', selectbackground='#B4D7FF', selectforeground='#000000')

list_tasks = tk.Listbox(root)
list_tasks.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

entry_task = ttk.Entry(root, font=("Arial", 10), width=30)
entry_task.insert(0, "Add your task here...")
entry_task.bind("<FocusIn>", clear_task_entry)
entry_task.pack(pady=10, padx=10)

button_add = ttk.Button(root, text="Add Task", command=add_new_task)
button_delete = ttk.Button(root, text="Delete Task", command=delete_selected_task)
button_update = ttk.Button(root, text="Update Task", command=update_selected_task)

button_add.pack(pady=5, padx=10, side=tk.LEFT)
button_delete.pack(pady=5, padx=10, side=tk.LEFT)
button_update.pack(pady=5, padx=10, side=tk.LEFT)

root.mainloop()
