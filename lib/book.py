#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count  

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            self._page_count = None
        else:
            self._page_count = value

    def turn_page(self):
        if self._page_count is not None:
            print("Flipping the page...wow, you read fast!")
        else:
            print("Unable to flip pages, invalid page count.")
