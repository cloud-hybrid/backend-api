#!/usr/bin/env python3

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

# Owner:   Jacob B. Sanders
# Source:  gitlab.cloud-technology.io
# License: BSD 3-Clause License

"""
...
"""

from . import *

import boto3
import boto3.s3.transfer
import botocore.exceptions

AWS = boto3.Session()

# =============================================================================
# API - HTTP Application Programming Interface
# =============================================================================

class HTTP(Request):
    """
    Application Programming Interface via HTTP(s)

    Generator is a Wrapper around FastAPI's Router
    """

    Endpoint = Request.Prefix + __module__.split(".")[-2]

    Generator = Request.Generator()

    Generator.prefix                    = Endpoint
    Generator.tags                      = Request.Tags + __module__.split(".")[1:-1]

    @staticmethod
    @Generator.get("/Meta-Keys")
    async def Methods(region = AWS.region_name):
        Client = boto3.client("s3", region_name = region)
        Resource = boto3.resource("s3", region_name = region)

        methods = [ * vars(Client.meta).get("_method_to_api_mapping").keys() ]

        extensions = [_ for _ in dir(Resource) if _[0] != "_"]

        Data = {*extensions, *methods}

        return Data

    @staticmethod
    @Generator.get("/Buckets")
    async def Buckets(region = AWS.region_name):
        Client = boto3.client("s3", region_name = region)
        Resource = boto3.resource("s3", region_name = region)
        Iterator = Client.list_buckets()

        Data = {
            "Total": None,
            "Buckets": [],
            "Region": region
        }

        for Bucket in Iterator["Buckets"]:
            Object = {
                "Bucket": Bucket["Name"],
                "Creation": Bucket["CreationDate"]
            }

            Data["Buckets"].append(Object)

        Data["Total"] = len(Data["Buckets"])

        return Data

    # @staticmethod
    # @Generator.get("/Buckets/Objects")
    # async def bucketsObjects(region = AWS.region_name):
    #     Client = boto3.client("s3", region_name = region)
    #     Resource = boto3.resource("s3", region_name = region)
    #     Iterator = Client.list_buckets()
    #
    #     Data = {
    #         "Total": None,
    #         "Buckets": [],
    #         "Region": region
    #     }
    #
    #     for Bucket in Iterator["Buckets"]:
    #         Limit = "/"
    #         Cursor = ""
    #
    #         Paginator = Client.get_paginator("list_objects")
    #         Pagination = Paginator.paginate(Bucket = Bucket["Name"])
    #
    #         # for File in Pagination.search("Contents"):
    #         #     if File:
    #         #         Blob = {
    #         #             "File": File["Key"],
    #         #             # "Modification": File["LastModified"],
    #         #             "Size": File["Size"],
    #         #             "Class": File["StorageClass"]
    #         #         }
    #         #         pprint.pprint(Blob)
    #
    #         Folders = [Folder for Folder in Pagination.search("CommonPrefixes") if Folder]
    #
    #         debug(Folders)
    #
    #         #
    #         # debug([Files, Folders])
    #
    #         Object = {
    #             "Bucket": Bucket["Name"],
    #             "Creation": Bucket["CreationDate"],
    #             "Objects": {
    #                 "Files": None,
    #                 "Folders": Folders
    #             }
    #         }
    #
    #         Data["Buckets"].append(Object)
    #
    #     Data["Total"] = len(Data["Buckets"])
    #
    #     return Data

    # @staticmethod
    # @Generator.post("/Upload-File",
    #     name = "S3 Upload File",
    #     response_model = Optional[Dictionary]
    # )
    # async def Upload(Input: Request.Upload = File(...), Authorization: Optional[String] = Header(...)):
    #     Type = Database.User.Schemas.Nexus.Information
    #
    #     Client = boto3.client("s3")
    #
    #     JWT = Authorization.split(" ")[-1]
    #
    #     Account = await Authorizer.Information(JWT)
    #
    #     User: Type = Request.Table(Account, Database.User.Schemas.Nexus.Information)
    #
    #     Type = Input.content_type
    #     Name = Input.filename
    #     Directory = tempfile.tempdir
    #
    #     Public = "{0}/{1}".format(
    #         User.Username, Name
    #     )
    #
    #     Target = "{0}/{1}/{2}".format(
    #         User.ID, User.Username, Name
    #     )
    #
    #     with tempfile.NamedTemporaryFile(delete = True, dir = Directory) as File:
    #         File.write(await Input.read())
    #
    #         Percentage = Thread.Percentage(File.name)
    #
    #         Response = Client.upload_file(File.name, HTTP.Bucket, Target,
    #             Callback = Percentage
    #         )
    #
    #         File.close()
    #
    #     return {
    #         "Status": "Complete",
    #         "Return": 0,
    #         "Error": Response,
    #         "Account": User,
    #         "Type": Type,
    #         "Name": Name,
    #         "Directory": Public
    #     }
    #
    # @staticmethod
    # @Generator.post("/Upload-Files",
    #     name = "S3 Upload File(s)",
    #     response_model = Optional[Dictionary]
    # )
    # async def Uploads(Input: List[UploadFile] = File(...), Authorization: Optional[String] = Header(None)):
    #     """
    #     ...
    #     """
    #
    #     Type = Database.User.Schemas.Nexus.Information
    #
    #     Client = boto3.client("s3")
    #
    #     JWT = Authorization.split(" ")[-1]
    #
    #     Account = await Authorizer.Information(JWT)
    #
    #     User: Type = Request.Table(Account, Database.User.Schemas.Nexus.Information)
    #
    #     for Upload in Input:
    #         Type = Upload.content_type
    #         Name = Upload.filename
    #         Directory = tempfile.tempdir
    #
    #         Target = "{0}/{1}/{2}".format(
    #             User.ID, User.Username, Name
    #         )
    #
    #         with tempfile.NamedTemporaryFile(delete = True, dir = Directory) as File:
    #             File.write(await Upload.read())
    #
    #             Percentage = Thread.Percentage(File.name)
    #             Response = Client.upload_file(File.name, HTTP.Bucket, Target,
    #                 Callback = Percentage
    #             )
    #
    #             File.close()
    #
    #     return {
    #         "Status": "Complete",
    #         "Return": 0,
    #         "Error": Response,
    #         "Account": User
    #     }

    @classmethod
    def createBucket(cls, name: String, region = AWS.region_name):
        """Create an S3 bucket in a specified region

        :param bucket_name: Bucket to create
        :param region: String region to create bucket in, e.g., 'us-west-2'
        :return: True if bucket created, else Exception
        """

        Client = boto3.client("S3", region_name = region)

        try:
            Client.create_bucket(
                Bucket = name,
                CreateBucketConfiguration = {
                    "LocationConstraint": region
                }
            )

        except Exception as Error:
            raise Error

        return True

    @classmethod
    def createBucketFolder(cls, folder: String, bucket: String, region = AWS.region_name):
        """
        ...
        """

        Client = boto3.client("S3", region_name = region)

        try:
            Client.put_object(Bucket = bucket, ContentType = "x-directory", Key = (folder + "/"))
        except Exception as Error:
            raise Error
        return True

Server.Application.API.include_router(HTTP.Generator)

__all__ = ["HTTP"]
