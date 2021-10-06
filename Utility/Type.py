import enum
import datetime
import typing
import dataclasses

Integer = int
Float = float
Array = bytearray
List = typing.List
String = typing.AnyStr
Bytes = typing.ByteString
Address = memoryview
Dictionary = typing.Dict
Optional = typing.Optional
Tuple = typing.Tuple
Union = typing.Union

Generic = typing.Any

Type = dataclasses.dataclass(init = False, frozen = True, unsafe_hash = True, repr = True)

@Type
class Base:
    Type: Type = Type

    Integer: Integer = Integer
    Float: Float = Float
    Array: Array = Array

    String: String = String
    Bytes: Bytes = Bytes
    Address: Address = Address
    Dictionary: Dictionary = Dictionary
    Tuple: Tuple = Tuple
    Union: Union = Union

    Optional: Generic = Optional

    @property
    def __repr__(self) -> str:
        return str(self)
