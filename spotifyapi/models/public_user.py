"""Provide the simplified artist model."""
from .user import User


class PublicUser(User):
    """A simplified artist. This is the same as Artist but matches the Spotify API naming scheme."""

    def __init__(self, data):
        super().__init__(data)
