from . import *

# =============================================================================
# Standard Library
# =============================================================================

import asyncio

import pprint

# =============================================================================
# Internal, Schemas
# =============================================================================

import Database.Git.Collections.LinkedResources.CRUD

from Database.Git.Schemas.LinkedResource import (
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

class HTTP(Request):
    """
    Application Programming Interface via HTTP(s)
    """

    Generator = Request.Generator(
        prefix = "{0}/{1}".format(
            Request.Prefix, "Linked-Resource"
        ), tags = Request.Tags
    )

    CRUD = Database.Git.Collections.LinkedResources.CRUD.Document()

    @staticmethod
    @Generator.get("/All",
        name = "Query All Git Configurations",
        response_model = List[Optional[Schema]],
        responses = { 422: {
            "description" : "Type (Schema) Validation Error"
        }}, response_description = "Query Response Return",
        status_code = 200, deprecated = False,
        summary = "Git C[R]UD (All) Endpoint")
    async def All():
        configurations = await HTTP.CRUD.gets()
        return [
            Schema(
                **{
                    **configuration, **{
                        "ID": configuration.pop("_id")
                    }
                }
            ) for configuration in configurations
        ]

    @staticmethod
    @Generator.get("/{ID}",
        name = "Query a Git Configuration",
        response_model = Schema,
        responses = { 422: {
            "description" : "Type (Schema) Validation Error"
        }}, response_description = "Query Response Return",
        status_code = 200, deprecated = False,
        summary = "Git C[R]UD Endpoint")
    async def Read(ID: String = Query(..., description = "...")) -> Schema:
        return await HTTP.CRUD.get(ID)

    @staticmethod
    @Generator.post("/Create",
        name = "Create A Git Task Document",
        response_model = Schema,
        responses = { 422: {
            "description" : "Type (Schema) Validation Error"
        }}, response_description = "Query Response Return",
        status_code = 201, deprecated = False,
        summary = "Git [C]RUD Endpoint")
    async def Create(Config: Base = Body(...),
        Token: Optional[String] = Header(None)
    ) -> Schema:
        return await HTTP.CRUD.create(Config.dict())

    @staticmethod
    @Generator.put("/Update",
        name = "Mutate A Git Task Document",
        response_model = Schema, responses = { 422: {
            "description" : "Type (Schema) Validation Error"
        }}, response_description = "Query Response Return",
        status_code = 200, deprecated = False,
        summary = "Git CR[U]D Endpoint")
    async def Update(ID: String = Query(...,
        type = String,
        description = "Non-Relational Database Record Index"
    ), Request: Update = Body(...)):
        """
        ...
        """

        return await HTTP.CRUD.update(
            ID, {
                Key: Value for Key, Value in Request.dict().items()
                    if Value is not None
            }
        )

    @staticmethod
    @Generator.delete("/Drop",
        name = "Delete A Git Task Document",
        response_model = Union[Success, Response],
        responses = { 422: {
            "description" : "Type (Schema) Validation Error"
        }}, response_description = "Query Response Return",
        status_code = 200, deprecated = False,
        summary = "Git CRU[D] Endpoint")
    async def Drop(ID: String = Query(...)
    ) -> Union[Success, Response, Error]:
        """
        ...
        """

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
