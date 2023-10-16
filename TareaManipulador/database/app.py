from DatabaseMySQL import MySQL
from DatabaseMariaDB import MariaDB

if __name__ == "__main__":

    db = MySQL()
    #db = MariaDB()

    db.conexion()

    # Ejemplo de CREATE|
    db.create("TEST", ["id INT AUTO_INCREMENT PRIMARY KEY", "campo1 VARCHAR(255)", "campo2 INT"])

    # Ejemplo de SELECT
    db.select('CLIENTE', ["*"])

    # Ejemplo de INSERT
    db.insert('CLIENTE', {"Nombre": "Juanito", "Apellido1": "Pérez", "Apellido2": "No sé", "Telefono": "123456789", "Email": "arribatxt@example.com"})

    # Ejemplo de UPDATE
    db.update('CLIENTE', {"Nombre": "Juan", "Apellido2":"AlgúnApellidoGenérico", "Email": "amoatxt@example.com"}, "IDCliente = 1")

    # Ejemplo de DELETE
    db.delete('CLIENTE', "IDCliente = 3")
