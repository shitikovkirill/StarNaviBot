import requests


class Post:

    id = None
    errors = []

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
            data=post_data
        )

        rdata = response.json()
        if response.status_code == 201:
            self.id = rdata["id"]
        else:
            self.errors.append({"status": response.status_code, "response_data": rdata})

        return response.status_code, rdata

    def like(self, url, token):
        response = requests.post(
            url=url,
            headers={'Authorization': f"Bearer {token}"},
        )

        rdata = response.json()
        if response.status_code != 200:
            self.errors.append({"status": response.status_code, "response_data": rdata})

        return response.status_code, rdata

    def __repr__(self):
        return f"Post: id {self.id}, title {self.title}"

