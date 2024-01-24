# Реализуйте класс Config, который соответствует шаблону синглтон и описывает конфигурационный объект с фиксированными параметрами. При создании экземпляра класс не должен принимать никаких аргументов.
#
# При первом вызове класса Config должен создаваться и возвращаться экземпляр этого класса, а при последующих вызовах должен возвращаться экземпляр, созданный при первом вызове.
#
# Экземпляр класса Config должен иметь четыре атрибута:
#
# program_name — атрибут со строковым значением GenerationPy
# environment — атрибут со строковым значением release
# loglevel — атрибут со строковым значением verbose
# version — атрибут со строковым значением 1.0.0

class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.program_name = 'GenerationPy'
        self.environment = 'release'
        self.loglevel = 'verbose'
        self.version = '1.0.0'

config = Config()

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)


config1 = Config()
config2 = Config()
config3 = Config()

print(config1 is config2)
print(config1 is config3)