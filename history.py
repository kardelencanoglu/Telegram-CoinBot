import os
import json
import datetime

__history_path = os.path.join('data', 'history.json')


def __converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


def set_history(user, operation):
    user = str(user)
    if os.path.exists(__history_path):
        with open(__history_path, 'r') as file:
            data = json.load(file)
            if data:
                data[user] = operation
                with open(__history_path, 'w') as f:
                    json.dump(data, f, default=__converter)
                return

    with open(__history_path, 'w') as file:
        json.dump({user: operation}, file)


def search_history(user, operation):
    user = str(user)
    if os.path.isfile(__history_path):
        with open(__history_path, 'r') as file:
            data = json.load(file)
            if data:
                if user in data:
                    for i in data[user]:
                        for j in operation:
                            if j == i:
                                # eğer işlem daha önceden var ise False döndür
                                return False

    return True
