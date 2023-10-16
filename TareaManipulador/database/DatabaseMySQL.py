from DatabaseAbstract import Database
import mysql.connector

# Implementación concreta para MySQL usando mysql-connector-python


class MySQL(Database):
    def __init__(self):
        self.connection = None

    def conexion(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                port=3307,
                user='root',
                password='root',
                database='TallerMecanico'
            )
            # if self.connection.is_connected():
            print("Connected to MySQL")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def create(self, table, fields):
        try:
            cursor = self.connection.cursor()

            # Verificar si la tabla ya existe
            cursor.execute(f"SHOW TABLES LIKE '{table}'")
            table_exists = cursor.fetchone()

            if table_exists:
                print(f"La tabla '{table}' ya existe en la base de datos.")
            else:
                if fields:
                    field_definitions = ', '.join(fields)
                    query = f"CREATE TABLE {table} ({field_definitions})"
                else:
                    query = f"CREATE TABLE {
                        table} (id INT AUTO_INCREMENT PRIMARY KEY)"

                cursor.execute(query)
                self.connection.commit()
                print(f"Tabla '{table}' creada con éxito.")

        except mysql.Error as err:
            print(f"Error al crear la tabla: {err}")

    def select(self, table, fields, condition=""):
        try:
            cursor = self.connection.cursor()

            # Crear la consulta SQL
            if fields:
                field_list = ', '.join(fields)
                query = f"SELECT {field_list} FROM {table}"
            else:
                query = f"SELECT * FROM {table}"

            if condition:
                query += f" WHERE {condition}"

            # Ejecutar la consulta SQL
            cursor.execute(query)

            # Obtener los resultados
            result = cursor.fetchall()

            # Imprimir los resultados
            for row in result:
                print(row)

        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return None

    def insert(self, table, data):
        try:
            cursor = self.connection.cursor()

            columns = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            cursor.execute(query, tuple(data.values()))

            self.connection.commit()
            print(f"Datos insertados en la tabla '{table}'.")

        except mysql.connector.Error as err:
            print(f"Error al insertar datos: {err}")

    def update(self, table, data, condition):
        try:
            cursor = self.connection.cursor()

            set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
            query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
            cursor.execute(query, tuple(data.values()))

            self.connection.commit()
            print(f"Datos actualizados en la tabla '{table}'.")

        except mysql.connector.Error as err:
            print(f"Error al actualizar datos: {err}")

    def delete(self, table, condition):
        try:
            cursor = self.connection.cursor()

            query = f"DELETE FROM {table} WHERE {condition}"
            cursor.execute(query)

            self.connection.commit()
            print(f"Registros eliminados de la tabla '{table}'.")

        except mysql.connector.Error as err:
            print(f"Error al eliminar registros: {err}")
