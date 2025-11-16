# simple-to-do-list
1.Project Overview
>>This is a simple console-based To-Do List Application built using Python.
>>The app allows users to add, view, and remove tasks, and it stores all tasks in a text file so that data is saved even after the program is closed.
2.Objective
>>Implement a basic to-do list manager using core Python concepts.
3. Tools Used
>>Python
>>VS Code / Terminal
4. Deliverable
>>A single Python file: todo.py
5.Features
>>View tasks
>> Add new tasks
>> Remove existing tasks
>>Persistent storage using a text file (tasks.txt)
6. How It Works
>> Tasks are stored in a Python list.
>> When the app starts, it loads tasks from tasks.txt.
>> After adding or removing tasks, the program saves them back to the file.
>> This ensures the task list remains available every time the program is reopened.
7. How to Run
>> Make sure Python is installed.
>> Save the file as todo.py
>> Open terminal and run:
>> python todo.py
8. Sample Menu
--- TO-DO LIST MENU ---
1. View Tasks
2. Add Task
3. Remove Task
4. Exit
9.File Structure
project-folder
>>todo.py
>>tasks.txt   (auto-created)
10.Code Summary
The program uses:
>> open() to read/write the tasks file
>> Lists to store tasks
>> A while loop to display a menu and take user input
>> Exception handling for invalid inputs
