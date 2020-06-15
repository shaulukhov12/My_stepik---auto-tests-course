import requests

res = requests.get('https://stepic.org/media/attachments/lesson/24472/sample0.html')
print(res.status_code)
print(res.headers)
print(res.content)