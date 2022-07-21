import re
PORT = 80
FLAG_PART = 0

conf_text = """server {
    listen PORT_THERE default_server;
    location / {
        proxy_pass http://127.0.0.1:5000/flag/FLAG_THERE;
    }
    }"""

for i in range(30):
    result_str = re.sub(r"PORT_THERE",str(PORT+i),conf_text)
    result_str = re.sub(r"FLAG_THERE",str(FLAG_PART+i),result_str)
    print(result_str)
