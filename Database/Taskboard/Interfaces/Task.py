import bson
import bson.errors

from . import *

# =============================================================================
# Standard Library
# =============================================================================

import asyncio

import pprint

# =============================================================================
# Internal, Schemas
# =============================================================================

import Database.Taskboard.Collections.Tasks.CRUD
from .. Schemas.Task import (
    Base,
    Create,
    Update,
    Schema,
    Response,
    Success
)

# =============================================================================
# Authentication
# =============================================================================

# from API.ASGI.Authentication.Context import (
#     Interface as Authentication
# )

from fastapi import Depends

# =============================================================================
# Internal, API
# =============================================================================

Index = lambda Object, attribute: Object.__dict__.get(attribute)
Shard = lambda Object: Object.__dict__

class HTTP(Request):
    """
    Application Programming Interface via HTTP(s)
    """

    Endpoint = "/".join([Request.Prefix, "/".join(__module__.split("."))])

    Generator                           = Request.Generator()

    Generator.prefix                    = Endpoint
    Generator.tags                      = Request.Tags + __module__.split(".")

    CRUD = Database.Taskboard.Collections.Tasks.CRUD.Document(__module__.split(".")[1])

    @staticmethod
    @Generator.get("/All",
        name = "Query All Taskboard Configurations",
        response_model = List[Optional[Schema]],
        responses = { 422: {
            "description" : "Type (Schema) Validation Error"
        }}, response_description = "Query Response Return",
        status_code = 200, deprecated = False, summary = "Taskboard C[R]UD (All) Endpoint"
    )
    async def All():
        return await HTTP.CRUD.gets()

    @staticmethod
    @Generator.get("/{ID}",
        name = "Query a Taskboard Configuration",
        response_model = Schema,
        responses = { 422: {
            "description" : "Type (Schema) Validation Error"
        }}, response_description = "Query Response Return",
        status_code = 200, deprecated = False, summary = "Taskboard C[R]UD Endpoint"
    )
    async def Read(ID: String = Query(..., description = "...")) -> Schema:
    # async def Read(ID: String = Query(..., description = "..."), _ = Depends(Authentication.Session)) -> Schema:
        return await HTTP.CRUD.get(ID)

    @staticmethod
    @Generator.post("/Create",
        name = "Create A Taskboard Task Document",
        response_model = Schema,
        responses = { 422: {
            "description" : "Type (Schema) Validation Error"
        }}, response_description = "Query Response Return",
        status_code = 201, deprecated = False, summary = "Taskboard [C]RUD Endpoint"
    )
    async def Create(Configuration: Schema = Schema()) -> Schema:
        Configuration = Configuration.dict()

        debug(Configuration)

        Document: Create = Create(**{
            "Data": Configuration
        })

        Collection = Document.dict()

        debug(Collection)

        Record = await HTTP.CRUD.create(Collection)

        debug(Record)

        return Record

    @staticmethod
    @Generator.put("/Update",
        name = "Mutate A Taskboard Task Document",
        response_model = Schema, responses = { 422: {
            "description" : "Type (Schema) Validation Error"
        }}, response_description = "Query Response Return",
        status_code = 200, deprecated = False, summary = "Taskboard CR[U]D Endpoint"
    )
    async def Update(Data: Update, ID: String = Query(...,
        type = String,
        description = "Non-Relational Database Record Index"
    )):
        try:
            return await HTTP.CRUD.update(data = Data, identifier = ID)
        except bson.errors.InvalidId:
            return Error({"Error": "'ID' must be a 12-byte byte-array || string, or a 24-character hex string"}, status_code = 422)

    @staticmethod
    @Generator.delete("/Drop",
        name = "Delete A Taskboard Task Document",
        response_model = Union[Success, Response],
        responses = { 422: {
            "description" : "Type (Schema) Validation Error"
        }}, response_description = "Query Response Return",
        status_code = 200, deprecated = False, summary = "Taskboard CRU[D] Endpoint"
    )
    async def Drop(ID: String = Query(...)) -> Union[Success, Response, Error]:
        if await HTTP.CRUD.delete(ID):
            return Success(
                Mutation = "Delete",
                Status = 200,
                Message = "Successfully Dropped Collection"
            )
        else:
            return Response(
                "Delete",
                404,
                "Error - Collection Not Found"
            )

Server.API.include_router(HTTP.Generator)

__all__ = [
    "HTTP"
]
