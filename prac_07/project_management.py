import csv
from datetime import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.percent_complete}% "


class ProjectManagement:
    def __init__(self):
        self.projects = []

    def load_projects(self):
        with open("project.csv", "r") as in_file:
            for line in in_file:
                values = line.strip().split(",")
                project = Project(*values)
                self.projects.append(project)

    def save_projects(self):
        with open("project.csv", "w") as f:
            for project in self.projects:
                f.write(f"{project.name},{project.start_date},{project.priority},{project.cost_estimate},{project.percent_complete}\n")

    def display_projects(self, completed=False):
        if completed:
            completed_projects = [p for p in self.projects if p.percent_complete == 100]
            print("Completed projects: ")
            for p in completed_projects:
                print(f"  {p}")
        else:
            incomplete_projects = [p for p in self.projects if p.percent_complete != 100]
            print("Incomplete projects: ")
            for p in incomplete_projects:
                print(f"  {p}")

    def filter_projects_by_date(self):
        date_str = input("Show projects that start after date (dd/mm/yyyy): ")
        try:
            date = datetime.strptime(date_str, '%d/%m/%Y').date()
        except ValueError:
            print("Invalid date format")
            return

        filtered_projects = [p for p in self.projects if p.start_date > date]
        for p in filtered_projects:
            print(f"  {p}")

    def add_project(self):
        print("Let's add a new project")
        name = input("Name: ")
        start_date = input("Start date (dd/mm/yyyy): ")
        priority = input("Priority: ")
        cost_estimate = input("Cost estimate: $")
        percent_complete = input("Percent complete: ")
        self.projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))

    def update_project(self):
        self.display_projects()
        choice = input("Project choice: ")
        try:
            choice = int(choice)
            project = self.projects[choice]
        except (ValueError, IndexError):
            print("Invalid choice")
            return

        percent_complete = input("New Percentage: ")
        project.percent_complete = percent_complete

        priority = input("New Priority: ")
        project.priority = priority