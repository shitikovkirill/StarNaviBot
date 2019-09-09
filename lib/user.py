import requests


class User:

    id = None
    token = None
    errors = []

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def sing_up(self, url):
        data = {"username": self.name, "email": self.email, "password": self.password}
        code, rdata = self.__send_request(url, 201, data)
        self.id = rdata['id']
        return code, rdata

    def login(self, url):
        data = {"username": self.name, "password": self.password}
        code, rdata = self.__send_request(url, 200, data)
        self.token = rdata["token"]
        return code, rdata

    def __send_request(self, url, status, data):
        response = requests.post(url=url, data=data)
        rdata = response.json()

        if response.status_code != status:
            self.errors.append({"status": response.status_code, "response_data": rdata})

        return response.status_code, rdata

    def __repr__(self):
        return f"User: id {self.id}, name {self.name}"
