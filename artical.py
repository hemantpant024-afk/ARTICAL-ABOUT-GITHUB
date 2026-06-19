class GitHub:
    def __init__(self):
        self.Title = "GitHub and Its Basic Command"

    def github_info(self):
        print("GitHub")
        print("=== TITLE - GitHub and its basic command ===\n")
        print("Github is a web-based platform used for\n" 
        " version contoral project mangement and back-up\n")

class GitCommand:
    def show_command(self):
        print("basic command of github")
        print("1. git init")   # get new repo to use.
        print("2. git add")    # to add new folder to remote. 
        print("3. git commit -m 'message'")   #use to track folder.
        print("4. git status")  # use to check status of folder.
        print("5. git push")    # use to push folder local to remote.
        print("6. git pull")    # use to remove folder to remote.

# create object
g1 = GitHub()
g2 = GitCommand()

#Call methods
g1.github_info()
g2.show_command()