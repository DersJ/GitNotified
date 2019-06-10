import json

#TODO: Add input validation
def main():
    data = {}
    print("")
    print("GitNotifier Setup")
    print("Thanks for trying GitNotifier! I just need a few things before we can get started.")
    print("")
    print("Enter your gitlab domain. For example: https://example.gitlab.com/")
    data['domain'] = input("Your Gitlab Domain: ")
    print("")
    print("Great! Next, I need the project id for each project which you would like notifications")
    print('This can found by going to the repository page, where "Project-ID" is right under the project name')
    print("To select multiple repos for notification, enter a comma-separated list of ids. For example: 1111, 2222, 3333")
    data['id_list'] = input("Project ID(s): ").split(',')
    print("")
    print("Ok, lastly I need an API access token for your gitlab account. This can be found in the user dropdown menu > Settings > Access Token")
    print("You may need to generate a new token if you haven't yet")
    data['token'] = input("Gitlab API Access Token: ")

    with open("config.json", 'w') as f:
        json.dump(data, f)

    print("")
    print("Thanks! to finialize setup make sure you've installed the requirements via pip install -r requirements.txt")
    print("then run python notifier.py to start listening for commits and pushing desktop notifications.")

if __name__ == "__main__":
    main()