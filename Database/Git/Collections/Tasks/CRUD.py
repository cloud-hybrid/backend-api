import abc

from . import *
from .. import Base

import pprint
from devtools import debug

class Document(Base.CRUD, abc.ABC):
    """
    ...
    """

    def __init__(self, collection: String):
        super(Document, self).__init__(collection)

        # ... debug(self.collection.name)

    @classmethod
    def construct(cls, Data: Dictionary):
        return {
            **Data,
            **{
                "ID": Data.pop("_id")
            }
        }

    async def gets(self):
        configs = []
        async for config in self.collection.find():
            configs.append(self.construct(config))
        return configs

    async def get(self, identifier: String):
        Data = await self.collection.find_one({"_id": BSON.ObjectId(identifier)})
        if Data is None:
            return None
        else:
            return self.construct(Data)

    async def create(self, config_data: Dictionary) -> Dictionary:
        config = await self.collection.insert_one(config_data)
        new_config = await self.collection.find_one({"_id": config.inserted_id})
        return self.construct(new_config)

    async def update(self, identifier: String, data: Dictionary):
        Data = await self.get(identifier)
        if Data is None:
            return None
        else:
            Response = await self.collection.update_one(
                {"_id": BSON.ObjectId(identifier)},
                {"$set": data}
            )

            return Response

    async def delete(self, identifier: String):
        config = await self.collection.find_one({"_id": BSON.ObjectId(identifier)})
        if config:
            await self.collection.delete_one({"_id": BSON.ObjectId(identifier)})
            return True
