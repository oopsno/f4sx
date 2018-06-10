# encoding: UTF-8

import os


class DotProxy:
    __slots__ = ['identifier', 'parent']

    def __init__(self, identifier, parent):
        self.identifier = identifier
        self.parent = parent

    def __getattr__(self, item):
        return DotProxy(item, self)

    def __call__(self, *args, stack=None):
        if stack is None:
            stack = [self.identifier]
        else:
            stack.insert(0, self.identifier)
        return self.parent(*args, stack=stack or [self.identifier])


class ScriptWriter:
    def __init__(self):
        self._buffer = []

    def scof(self, file=None):
        self.dump(to=file)

    def comment(self, line):
        self._write_line(f'; {line}')

    def _write_line(self, line: str):
        self._buffer.append(line)

    def _write_function_call(self, *args, stack=None):
        if stack is None:
            stack = []
        command = '.'.join(stack)
        args = ' '.join(map(str, args))
        self._write_line(f'{command} {args}')

    def __getattr__(self, item):
        return DotProxy(item, self._write_function_call)

    def dump(self, to=None):
        content = os.linesep.join(self._buffer)
        if to is None:
            print(content)
        else:
            to.write(content)

