from project_management import ProjectManagement


def main():
    project_manager = ProjectManagement()
    project_manager.load_projects()

    print(menu())
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == 'L':
            project_manager.load_projects()
        elif choice == 'S':
            project_manager.save_projects()
        elif choice == "D":
            project_manager.display_projects()
        elif choice == "F":
            project_manager.filter_projects_by_date()
        elif choice == "A":
            project_manager.add_project()
        elif choice == "U":
            project_manager.update_project()
        else:
            print("Invalid menu choice")
        print(menu())
        choice = input(">>>").upper()


def menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


if __name__ == '__main__':
    main()