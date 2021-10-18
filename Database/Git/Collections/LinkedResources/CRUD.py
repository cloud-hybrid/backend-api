import abc

from . import *
from .. import Base

class Document(Base.CRUD, abc.ABC):
    """
    ...
    """

    def __init__(self, collection: String = __name__.split(".").pop()):
        super(Document, self).__init__(collection)

    @classmethod
    def construct(cls, Data: Dictionary):
        return {
            **Data,
            **{
                "ID": Data.pop("_id")
            }
        }

    @classmethod
    def get_user(cls, *argv, **kwargs):
        """
        ...
        @Task - Query User data from Username field and instantiate User field inside of Schema with returned response
        """

        raise NotImplementedError
