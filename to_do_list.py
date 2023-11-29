import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Task list
        self.tasks = []

        # Create listbox
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
        self.task_listbox.pack(pady=10)

        # Entry for new task
        self.new_task_entry = tk.Entry(root, width=30)
        self.new_task_entry.pack(pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        # Load tasks from file
        self.load_tasks()

        # Populate the listbox with tasks
        self.update_listbox()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.tasks = [line.strip() for line in f]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        new_task = self.new_task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.save_tasks()
            self.update_listbox()
            self.new_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            deleted_task = self.tasks.pop(task_index)
            self.save_tasks()
            self.update_listbox()
            messagebox.showinfo("Task Deleted", f"Task '{deleted_task}' deleted successfully.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        new_task = self.new_task_entry.get()
        if selected_index:
            task_index = selected_index[0]
            self.tasks[task_index] = new_task
            self.save_tasks()
            self.update_listbox()
            messagebox.showinfo("Task Updated", "Task updated successfully.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
