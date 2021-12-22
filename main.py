import time
from datetime import datetime as dt


host_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.netflix.com", "www.facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Закрыт!")

        file = open(host_path,  "r+")
        content = file.read()

        for website in website_list:
            pass
        else:
            file.write(redirect + " " + website + "\n")
        
    else:
        print("Открыт!")

        file = open(host_path, "r+")
        content = file.readlines()
        file.seek(0)

        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
            file.truncate()

    time.sleep(5)


