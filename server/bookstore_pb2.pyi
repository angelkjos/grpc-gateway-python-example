from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Shelf(_message.Message):
    __slots__ = ["id", "theme"]
    ID_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    id: int
    theme: str
    def __init__(self, id: _Optional[int] = ..., theme: _Optional[str] = ...) -> None: ...

class Book(_message.Message):
    __slots__ = ["id", "author", "title"]
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    id: int
    author: str
    title: str
    def __init__(self, id: _Optional[int] = ..., author: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class ListShelvesResponse(_message.Message):
    __slots__ = ["shelves"]
    SHELVES_FIELD_NUMBER: _ClassVar[int]
    shelves: _containers.RepeatedCompositeFieldContainer[Shelf]
    def __init__(self, shelves: _Optional[_Iterable[_Union[Shelf, _Mapping]]] = ...) -> None: ...

class CreateShelfRequest(_message.Message):
    __slots__ = ["shelf"]
    SHELF_FIELD_NUMBER: _ClassVar[int]
    shelf: Shelf
    def __init__(self, shelf: _Optional[_Union[Shelf, _Mapping]] = ...) -> None: ...

class GetShelfRequest(_message.Message):
    __slots__ = ["shelf"]
    SHELF_FIELD_NUMBER: _ClassVar[int]
    shelf: int
    def __init__(self, shelf: _Optional[int] = ...) -> None: ...

class DeleteShelfRequest(_message.Message):
    __slots__ = ["shelf"]
    SHELF_FIELD_NUMBER: _ClassVar[int]
    shelf: int
    def __init__(self, shelf: _Optional[int] = ...) -> None: ...

class ListBooksRequest(_message.Message):
    __slots__ = ["shelf"]
    SHELF_FIELD_NUMBER: _ClassVar[int]
    shelf: int
    def __init__(self, shelf: _Optional[int] = ...) -> None: ...

class ListBooksResponse(_message.Message):
    __slots__ = ["books"]
    BOOKS_FIELD_NUMBER: _ClassVar[int]
    books: _containers.RepeatedCompositeFieldContainer[Book]
    def __init__(self, books: _Optional[_Iterable[_Union[Book, _Mapping]]] = ...) -> None: ...

class CreateBookRequest(_message.Message):
    __slots__ = ["shelf", "book"]
    SHELF_FIELD_NUMBER: _ClassVar[int]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    shelf: int
    book: Book
    def __init__(self, shelf: _Optional[int] = ..., book: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["shelf", "book"]
    SHELF_FIELD_NUMBER: _ClassVar[int]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    shelf: int
    book: int
    def __init__(self, shelf: _Optional[int] = ..., book: _Optional[int] = ...) -> None: ...

class DeleteBookRequest(_message.Message):
    __slots__ = ["shelf", "book"]
    SHELF_FIELD_NUMBER: _ClassVar[int]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    shelf: int
    book: int
    def __init__(self, shelf: _Optional[int] = ..., book: _Optional[int] = ...) -> None: ...
