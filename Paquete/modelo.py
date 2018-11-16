import abc

class PersonaEquipo(object):
    """
        se define la clases abstracta
    """
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, nom):
        self.nombre = nom

    @abc.abstractmethod
    def entrenamiento():
        pass


        