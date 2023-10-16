from abc import ABC, abstractmethod

# Clase base abstracta para la base de datos


class Database(ABC):
    @abstractmethod
    def conexion(self):
        pass

    @abstractmethod
    def create(self, table, fields):
        pass

    @abstractmethod
    def select(self, table, fields, condition=""):
        pass

    @abstractmethod
    def insert(self, table, data):
        pass

    @abstractmethod
    def update(self, table, data, condition):
        pass

    @abstractmethod
    def delete(self, table, condition):
        pass
