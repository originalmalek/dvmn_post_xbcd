import requests
from dotenv import load_dotenv
import os


def post_comic(vk_token, group_id, message, response_save_wall_photo):

    url = 'https://api.vk.com/method/wall.post'

    owner_id = response_save_wall_photo[0]['owner_id']
    from_group = 1
    message = message
    media_id = response_save_wall_photo[0]['id']

    payload = {'access_token': vk_token,
               'v': '5.122',
               'group_id': group_id,
               'message': message,
               'from_group': from_group,
               'attachments': f'photo{owner_id}_{media_id}',
               'owner_id': -group_id}

    response = requests.get(url, params=payload)
    response.raise_for_status()


def save_wall_photo(vk_token, group_id, response_get_wall_upload_server):

    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    photo = response_get_wall_upload_server['photo']
    server = response_get_wall_upload_server['server']
    hash_photo = response_get_wall_upload_server['hash']

    payload = {'access_token': vk_token,
               'v': '5.122',
               'group_id': group_id,
               'photo': photo,
               'server': server,
               'hash': hash_photo}
    response = requests.post(url, params=payload)
    response.raise_for_status()

    return response.json()['response']


def get_wall_upload_server(vk_token, group_id):
    payload = {'access_token': vk_token,
               'v': '5.122',
               'group_id': group_id}

    url = 'https://api.vk.com/method/photos.getWallUploadServer'

    response = requests.get(url, params=payload).json()

    upload_url = response['response']['upload_url']

    with open('comic.png', 'rb') as file:
        files = {
            'photo': file
        }
        response = requests.post(upload_url, files=files)
        response.raise_for_status()

        return response.json()


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
    response_xkcd = response.json()

    download_comic(response_xkcd['img'])

    return response_xkcd['alt']


def main():
    load_dotenv()

    vk_token = os.getenv('VK_ACCESS_TOKEN')

    group_id = 198053823

    message = get_comic_pic_and_message()

    post_comic(vk_token, group_id, message,
               save_wall_photo(vk_token, group_id,
                               get_wall_upload_server(vk_token, group_id)))


if __name__ == '__main__':
    main()
