from enum import Enum



class Sound(Enum):
    MOVE_UP = 1,
    MOVE_DOWN = 2,
    COLLISION = 3

class Sounds():
    __sounds = {}
    __index = 0

    def __getitem__(self, item):
        if isinstance(item, Sound):
            if item in Sounds.__sounds:
                return Sounds.__sounds[item]
            else:
                return None

    def __setitem__(self, key, value):
        if isinstance(key, Sound):
            Sounds.__sounds[key] = value

    def __iter__(self):
        return self

    def __next__(self):
        if Sounds.__index == len([x for x in Sounds.__sounds]):
            Sounds.__index = 0
            raise StopIteration
        else:
            Sounds.__index += 1
            return Sounds.__sounds[[x for x in Sounds.__sounds][Sounds.__index - 1]]


