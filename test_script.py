import requests

print("--> Sending a GET request to localhost on port 8000...")

try:
    r = requests.get('http://localhost:8000')
    if r.status_code != 201:
        print("--> Status code is:", r.status_code)
        print("--> Test failed!")
        exit(1)    
    else:
        print("--> Status code is:", r.status_code)
        print("--> Content:", r.text)
        print("--> Test succeeded!")
        exit(0)
except Exception as e:
    print("--> Test failed! See below error:\n\n", e, "\n")
    exit(1)