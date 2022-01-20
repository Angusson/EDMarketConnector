"""Utilities for dealing with HTTP."""
from __future__ import annotations

from gzip import compress

__all__ = ['gzip']


def gzip(data: str | bytes, max_size: int = 512, encoding='utf-8') -> tuple[bytes, bool]:
    """
    Compress the given data if the max size is greater than specified.

    :param data: The data to compress
    :param max_size: The max size of data, in bytes, defaults to 512
    :param encoding: The encoding to use if data is a str, defaults to 'utf-8'
    :return: the payload to send, and a bool indicating compression state
    """
    if isinstance(data, str):
        data = data.encode(encoding=encoding)

    if len(data) <= max_size:
        return data, False

    return compress(data), True
