# Task Management Django Project
This Django project is a simple task management application that allows users to create, manage, filter, and sort tasks based on their status, priority, and due date.

## Features
- Task Listing: Users can view a list of tasks, which can be filtered by status and sorted by priority or due date.
- Task Management: Users can manage tasks through the Django admin interface.
### Models
#### Task Model
The core model of this project is the Task model, which has the following fields:

- **title**: A brief title of the task.
- **description**: A detailed description of the task.
- **due_date**: The due date for the task.
- **priority**: The priority level of the task, where:
    - 1 = High
    - 2 = Medium
    - 3 = Low
- **status**: The current status of the task, which can be:
    - To Do
    - In Progress
    - Done
### Views
#### Task List View
The `task_list` view is responsible for displaying a list of tasks. It includes functionality to:

- **Filter Tasks**: Users can filter tasks by their status (e.g., To Do, In Progress, Done).
- **Sort Tasks**: Users can sort tasks by priority or due date.
### URL Configuration
The project has a simple URL configuration:

- **/** : Displays the `task_list` view, showing the list of tasks.
### Templates
#### index.html
The `index.html` template displays the list of tasks in a table format. It includes:

UI elements for filtering tasks by status.
Options to sort tasks by priority or due date.