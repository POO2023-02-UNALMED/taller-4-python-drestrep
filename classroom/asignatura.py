class Asignatura:

    def __init__(self, nombre, salon=1):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        return self._nombre + " remoto"
