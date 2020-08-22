import requests
from dotenv import load_dotenv
import os


def wall_post(payload, message, response_save_wall_photo):
    url = 'https://api.vk.com/method/wall.post'

    owner_id = response_save_wall_photo[0]['owner_id']
    from_group = 1
    message = message
    media_id = response_save_wall_photo[0]['id']

    payload.update({'message': message,
                    'from_group': from_group,
                    'attachments': f'photo{owner_id}_{media_id}',
                    'owner_id': -(payload['group_id'])})

    requests.get(url, params=payload)


def save_wall_photo(payload, response_get_wall_upload_server):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'

    photo = response_get_wall_upload_server['photo']
    server = response_get_wall_upload_server['server']
    hash_photo = response_get_wall_upload_server['hash']

    payload.update({'photo': photo,
                    'server': server,
                    'hash': hash_photo})

    return requests.post(url, params=payload).json()['response']


def get_wall_upload_server(payload):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    response = requests.get(url, params=payload).json()

    upload_url = response['response']['upload_url']

    with open('comic.png', 'rb') as file:
        files = {
            'photo': file
        }
        return requests.post(upload_url, files=files).json()


def download_comic(url):
    pic_name = 'comic.png'

    response = requests.get(url)
    response.raise_for_status()

    with open(pic_name, 'wb') as file:
        file.write(response.content)


def get_random_comic():
    response = requests.get('https://c.xkcd.com/random/comic/')
    response.raise_for_status()

    return response.url


def get_comic_pic_and_message():
    response = requests.get(get_random_comic() + 'info.0.json')
    response.raise_for_status()
    response_json = response.json()

    download_comic(response_json['img'])

    return response_json['alt']


def main():
    load_dotenv()

    vk_access_token = os.getenv('VK_ACCESS_TOKEN')

    group_id = 198053823

    payload = {'access_token': vk_access_token,
               'v': '5.122',
               'group_id': group_id}

    message = get_comic_pic_and_message()

    wall_post(payload, message, save_wall_photo(payload, get_wall_upload_server(payload)))


if __name__ == '__main__':
    main()
