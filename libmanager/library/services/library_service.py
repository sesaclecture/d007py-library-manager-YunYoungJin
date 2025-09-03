
from __future__ import annotations
from typing import Iterable, List
from library.models.book import Book
from library.services.base_service import BaseService


class LibraryService(BaseService):
    """도서 목록을 메모리에서 관리하는 서비스."""

    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        # 제목으로 책 삭제 (없으면 ValueError)
        for idx, book in enumerate(self._books):
            if book.title == title:
                del self._books[idx]
                return
        raise ValueError

    def list_books(self) -> Iterable[Book]:
        return list(self._books)

    def find_book(self, title: str) -> Book:
        # 제목으로 책 찾기 (없으면 ValueError)
        for book in self._books:
            if book.title == title:
                return book
        raise ValueError
