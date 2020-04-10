import sys
import requests

sub_list = open("subdomains.txt").read()
subs = sub_list.splitlines()

for sub in subs:
	url_to_check = f"http://{sub}.{sys.argv[1]}"

	try:
		requests.get(url_to_check)
	except requests.ConnectionError:
		pass
	else:
		print("Valid domain : ",url_to_check)