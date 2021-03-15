import os, re

os.system("clear")
app_name = os.getenv("REPL_SLUG") #input("App Name: ")
color = input("Hex Color: ")
domain = input("Domain Name: ")
description = input("App Description: ")

for filename in ["web/index.html", "static/manifest.json"]:
	with open(filename, 'r+') as f:
			text = f.read()
			text = re.sub('APP_NAME', app_name, text)
			text = re.sub('DOMAIN_NAME.com', domain, text)
			text = re.sub('######', color, text)
			f.seek(0)
			f.write(text)
			f.truncate()