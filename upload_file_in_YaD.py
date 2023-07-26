import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        header = {'Authorization': 'OAuth ' + self.token}
        folder = requests.get(f'{url}?path=/', headers=header).json()
        d_folder = {}
        pos = 1
        print('0: Корень диска')
        for i in folder['_embedded']['items']:
            if i['type'] == 'dir':
                d_folder[pos] = i['name']
                print(f'{pos}: {d_folder[pos]}')
                pos += 1
        set_folder = int(input('Выберите папку для загрузки: '))

        if set_folder != 0:
            res = requests.get(f'{url}/upload?path=/{d_folder[set_folder]}/'
                               f'{path_to_file.rpartition("/")[2]}',headers=header).json()['href']
        else:
            res = requests.get(f'{url}/upload?path={path_to_file.rpartition("/")[2]}', headers=header).json()['href']

        with open(file_path, 'rb') as f:
            requests.put(res,  files={'file': f})

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите путь к файлу: ').replace('\\', '/')
    token = input('Введите токен для авторизации: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)