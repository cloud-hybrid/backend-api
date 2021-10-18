import pymongo.errors

from . import *

class CRUD:
    """
    ...
    """

    def __init__(self, collection: String = __name__.split(".").pop()):
        self.collection = Database[collection]
    #
    # @classmethod
    # def construct(cls, Data: Dictionary):
    #     raise NotImplementedError
    #
    # async def gets(self):
    #     configs = []
    #     async for config in self.Collection.find():
    #         configs.append(self.construct(config))
    #     return configs
    #
    # async def get(self, identifier: String):
    #     config = await self.Collection.find_one({"_id": BSON.ObjectId(identifier)})
    #     if config:
    #         return self.construct(config)
    #
    # async def create(self, config_data: Dictionary) -> Dictionary:
    #     config = await self.Collection.insert_one(config_data)
    #     new_config = await self.Collection.find_one({"_id": config.inserted_id})
    #     return self.construct(new_config)
    #
    # async def update(self, identifier: String, data: Dictionary):
    #     Data: Schema.dict = Schema(**Dictionary(data)).dict()
    #     Response = False if not Data else await self.Collection.update_one(
    #         {"_id": BSON.ObjectId(identifier)},
    #         {"$set": Schema(**Dictionary(data)).dict()}
    #     )
    #
    #     return Response if Response is False else Schema(**Dictionary(Data, **{
    #             "ID": identifier})).dict()
    #
    # async def delete(self, identifier: String):
    #     config = await self.Collection.find_one({"_id": BSON.ObjectId(identifier)})
    #     if config:
    #         await self.Collection.delete_one({"_id": BSON.ObjectId(identifier)})
    #         return True
