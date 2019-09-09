import requests

from lib.error import BotRequestError


class Post:

    id = None

    def __init__(self, title: str, text: str):
        self.title = title
        self.text = text

    def publish(self, url, token):
        post_data = {
            'title': self.title,
            'description': self.text
        }

        response = requests.post(
            url=url,
            headers={'Authorization': f"Bearer {token}"},
            json=post_data
        )

        if response.status_code == 201:
            rdata = response.json()
            self.id = rdata["id"]
        else:
            raise BotRequestError(f"Status: {response.status_code}, response_data: {response.text}")

        return response.status_code, rdata

    def like(self, url_template, token):
        response = requests.post(
            url=url_template.format(self.id),
            headers={'Authorization': f"Bearer {token}"},
        )

        if response.status_code != 200:
            raise BotRequestError(f"Status: {response.status_code}, response_data: {response.text}")
        rdata = response.json()

        return response.status_code, rdata

    def __repr__(self):
        return f"Post: id {self.id}, title {self.title}"

