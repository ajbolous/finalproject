import json
import jsonpickle


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = '1'

    def eat(self, amount):
        print self.name

    def __repr__(self):
        return "Person({},{})".format(self.name, self.age)


persons = [Person('ah', 12), Person('zx', 23), Person('a', 2)]


def save(data, filename):
    with open('machines.json', 'w') as fp:
        js = jsonpickle.encode(data)
        fp.write(js)


def load(filename):
    with open(filename) as fp:
        data = fp.read()
        return jsonpickle.decode(data)

persons = load('machines.json')
print persons