#Реализуйте класс Version, описывающий версию программного обеспечения. При создании экземпляра класс должен принимать один аргумент:

# version — строка из трех целых чисел, разделенных точками и описывающих версию ПО.

from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version):
        self.version = (list(map(int, version.split('.'))) + [0, 0])[:3]

    def __repr__(self):
        return f"{self.__class__.__name__}({'.'.join(map(str, self.version)).__repr__()})"

    def __str__(self):
        return '.'.join(map(str, self.version))

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.version == other.version
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self.version < other.version
        return NotImplemented

print(Version('3.0.3') == Version('1.11.28'))
print(Version('3.0.3') < Version('1.11.28'))
print(Version('3.0.3') > Version('1.11.28'))
print(Version('3.0.3') <= Version('1.11.28'))
print(Version('3.0.3') >= Version('1.11.28'))

print(Version('3') == Version('3.0'))
print(Version('3') == Version('3.0.0'))
print(Version('3.0') == Version('3.0.0'))

versions = [Version('2'), Version('2.1'), Version('1.9.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))