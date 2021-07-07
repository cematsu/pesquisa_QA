from json import JSONEncoder


class Object:
    pass


class RequestEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Config:
    @classmethod
    def get_url(cls):
        return 'https://bit.ly/3jOMrR9'