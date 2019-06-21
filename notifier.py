import os, time, sys, json
try:
	import requests, pync
except ImportError as e:
	print("ERROR: "+str(e))
	print("Uh Oh! Looks like a requirement isn't installed! Run pip install -r requirements.txt")
	sys.exit()


def listenForCommits():

	try:
		with open('./config.json') as json_file:  
			data = json.load(json_file)

			access_token = data["token"]
			domain = data["domain"]
			id_list = data["id_list"]

	except FileNotFoundError as e:
		print("ERROR: "+str(e))
		print("Config file not found! Run python setup.py to generate it.")

	current_commit = None
	pync.notify("GitNotifier is running!")

	names = {}
	for repo in id_list:
		response = requests.get("{}/api/v4/projects/{}/".format(domain, repo), headers={"Private-Token": access_token})
		names[repo] = response.json()["name_with_namespace"]
	
	current_commits ={}
	
	while(True):
		for repo in id_list:
			response = requests.get("{}/api/v4/projects/{}/repository/commits/".format(domain, repo), headers={"Private-Token": access_token})
			if(response.status_code == 200):
				data = response.json()[0]
				rec_id = data['short_id']
				if(rec_id != current_commits.get(repo)):
					pync.notify("New commit on {}! Pushed by {}".format(names[repo], data['author_name']), title="GitNotifier", open="{}/projects/{}".format(domain, repo))
					current_commits[repo] = rec_id
			else:
				print("Error! Gitlab api responded with {}".format(response.status_code))
		time.sleep(60)

if __name__ == "__main__":
	listenForCommits()