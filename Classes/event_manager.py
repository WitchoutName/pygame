from enum import Enum


class Event(Enum):
    ADDENEMY = 1
    ADDCLOUD = 2


class Events:
    __events = {}
    __index = 0

    def __getitem__(self, item):
        if isinstance(item, Event):
            if item in Events.__events:
                return Events.__events[item]
            else:
                return None

    def __setitem__(self, key, value):
        if isinstance(key, Event):
            Events.__events[key] = value

    def __iter__(self):
        return self

    def __next__(self):
        if Events.__index == len([x for x in Events.__events]):
            Events.__index = 0
            raise StopIteration
        else:
            Events.__index += 1
            return Events.__events[[x for x in Events.__events][Events.__index - 1]]

