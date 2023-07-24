import requests

def most_inelligent(name1, name2, name3):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    resp = requests.get(url)
    json_data = resp.json()
    intel = 0
    name = ''
    for data in json_data:
        if name1.title() == data['name'] or \
                name2.title() == data['name'] or \
                name3.title() == data['name']:
            if intel < data["powerstats"]["intelligence"]:
                intel = data["powerstats"]["intelligence"]
                name = data['name']
                print(f'У "{name}" - {intel} интеллекта')
            else:
                print(f"У \"{data['name']}\" - {data['powerstats']['intelligence']} интеллекта")
    print(f'\nСамый умный - "{name}"')
most_inelligent('Captain America', 'Thanos', 'Hulk')