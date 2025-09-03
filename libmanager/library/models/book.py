
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Book:
    """책 정보를 표현하는 데이터 클래스.
    - 인스턴스 변수: title(str), author(str), year(int)
    - 클래스 변수: book_count(int) — 생성될 때마다 +1
    - __str__는 "{title} by {author} ({year})" 형식 반환
    - @classmethod from_dict(cls, data: Dict[str, Any]) -> Book 구현
    """
    book_count: int = 0

    def __init__(self, title, author, year):
        self.title: str = title
        self.author: str = author
        self.year: int = year
        Book.book_count += 1

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.year})"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Book":
        return cls(
            title = data.get("title", ""),
            author = data.get("author", ""),
            year = data.get("year", 0)
        )
