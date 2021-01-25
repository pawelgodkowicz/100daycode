import json


class LoadQuizData:

    def __init__(self, path):
        self.path = path
        with open(self.path) as json_file:
            data = json.load(json_file)
            data = data['results']
        self.data = data


class Question:

    def __init__(self, category, text, answer):
        self.category = category
        self.text = text
        self.answer = answer