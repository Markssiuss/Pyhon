import time
from datetime import datetime as dt

# Pointing to local temp, to work with real one we should change hosts_temp calls to hosts_path and run as adminitrator
hosts_temp ="WebsiteBlocker\\hosts"
hosts_path="C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"
website_list = ["facebook.com", "www.facebook.com"]

while True:
    if ((dt(dt.now().year,dt.now().month,dt.now().day,dt.now().hour) < dt(dt.now().year,dt.now().month,dt.now().day,19)) and
            (dt(dt.now().year,dt.now().month,dt.now().day,8) < dt(dt.now().year,dt.now().month,dt.now().day,dt.now().hour))):
        print("Working hours")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write("\n" + redirect + " " + website)
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                ToCheck = redirect + " " + website
                if ToCheck in content:
                    content = content.replace(ToCheck,"")
            file.seek(0)
            file.write(content.rstrip() + "\n")
            file.truncate()
        print("Fun hours...")
    time.sleep(300)

# We can schedule it in Windows => change extension to pyw to be calle from pythonw. Open task scheduler, create task, run with highest privileges 
# (if neede, but in this case yes), triggers (at startup for example)