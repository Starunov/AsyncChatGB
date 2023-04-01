import subprocess

web_resources = ['yandex.ru', 'youtube.com']
container = [('ping', w, '-c', '2') for w in web_resources]

for args in container:
    for line in subprocess.Popen(args, stdout=subprocess.PIPE).stdout:
        resp = line.decode('utf-8')
        print(type(resp), resp)
    print('=' * 100)
