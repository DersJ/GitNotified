import json, validators

#TODO: Add input validation
def main():
    data = {}
    print("")
    print("GitNotifier Setup")
    print("Thanks for trying GitNotifier! I just need a few things before we can get started.")
    print("")
    data['domain'] = inputURL()
    print("")
    print("Great! Next, I need the project id for each project which you would like notifications")
    print('This can found by going to the repository page, where "Project-ID" is right under the project name')
    print("To select multiple repos for notification, enter a comma-separated list of ids. For example: 1111, 2222, 3333")
    data['id_list'] = inputIDs()
    print("")
    print("Ok, lastly I need an API access token for your gitlab account. This can be found in the user dropdown menu > Settings > Access Token")
    print("You may need to generate a new token if you haven't yet")
    data['token'] = input("Gitlab API Access Token: ")

    with open("./config.json", 'w') as f:
        json.dump(data, f)

    print("")
    print("Thanks! to finialize setup make sure you've installed the requirements via pip install -r requirements.txt")
    print("then run python notifier.py to start listening for commits and pushing desktop notifications.")

def inputURL():
    url = askForURL()
    while(not validators.url(url)):
        url = askForURL(invalid=True)
    if(url[len(url)-1] != '/'):
        url = url + '/'
    return url
def askForURL(invalid=False):
    if(invalid):
        print("")
        print("Invalid url! Please re-enter. For example: https://example.gitlab.com/")
    else:
        print("Enter your gitlab url. For example: https://example.gitlab.com/")
    return input("Your Gitlab Url: ")

def inputIDs():
    ids = askForIDs()
    invalid = (not validateIDs(ids))
    while(invalid):
        ids = askForIDs(invalid=True)
        invalid = (not validateIDs(ids))

    return ids
def askForIDs(invalid=False):
    if(invalid):
        print("")
        print("Invalid Project Ids, Try again!")
        return input("Project ID(s): ").replace(' ', "").split(',')
    else:
        return input("Project ID(s): ").replace(' ', "").split(',')

def validateIDs(ids):
    if(type(ids) == list):
        valid = True
        for i in ids:
            if(type(i) != str or len(i) <= 0 or not i.isdigit()):
                valid = False
            
    return valid

if __name__ == "__main__":
    main()