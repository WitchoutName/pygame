from enum import Enum


class Group(Enum):
    DEFAULT = 1
    ENEMIES = 2,
    CLOUDS = 3,
    ROCKETS = 4


class Groups:
    __groups = {}
    __index = 0

    def __getitem__(self, item):
        if isinstance(item, Group):
            if item in Groups.__groups:
                return Groups.__groups[item]
            else:
                return None

    def __setitem__(self, key, value):
        if isinstance(key, Group):
            Groups.__groups[key] = value

    def __iter__(self):
        return self

    def __next__(self):
        if Groups.__index == len([x for x in Groups.__groups]):
            Groups.__index = 0
            raise StopIteration
        else:
            Groups.__index += 1
            return Groups.__groups[[x for x in Groups.__groups][Groups.__index - 1]]