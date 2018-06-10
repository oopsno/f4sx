# encoding: UTF-8

from typing import Union


class ObjectID:
    def __init__(self, oid: Union[int, str, 'ObjectID']):
        self.object_id = self._to_int(oid)

    def __int__(self):
        return self.object_id

    def __add__(self, other):
        try:
            return ObjectID(self.object_id + self._to_int(other))
        except TypeError:
            raise TypeError(f'Cannot add ObjectID with {other!r}')

    def __radd__(self, other):
        return self + other

    def __str__(self):
        return hex(self.object_id)[2:].upper()

    def __repr__(self):
        return f'ObjectID({str(self)!r})'

    @staticmethod
    def _to_int(what) -> int:
        if isinstance(what, int):
            return what
        elif isinstance(what, str):
            return int(what, base=16)
        elif isinstance(what, ObjectID):
            return int(what)
        else:
            raise TypeError(f'Cannot cast {what:!r} into int')

    @classmethod
    def range(cls, first, last=None, step=1):
        if last is None:
            return [ObjectID(first)]
        for object_id in range(cls._to_int(first), cls._to_int(last) + 1, step):
            yield ObjectID(object_id)

