from ..util import *


class Evaluatable(ABC):
    """
    represent evaluation component for an evaluatable object
    """

    def __init__(self) -> None:
        pass

    @abstract
    def eval(self):
        raise NotImplementedError