# A simple to do list application 
# This project involves basic concepts such as user input, basic control flow and data storage
# The program will provide a simple menu for adding tasks, showing tasks, removing tasks and exiting the application

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the to-do list.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed from the to-do list.')
        else:
            print(f'Task "{task}" not found in the to-do list.')

    def show_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('\nTo-Do List:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

def main():
    todo_list = ToDoList()

    while True:
        print('\nOptions:')
        print('1. Add Task')
        print('2. Remove Task')
        print('3. Show Tasks')
        print('4. Exit')

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            task = input('Enter the task to remove: ')
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print('Exiting the to-do list application. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

if __name__ == "__main__":
    main()
