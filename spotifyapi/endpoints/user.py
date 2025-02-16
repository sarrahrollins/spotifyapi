"""Provide the user endpoint."""
from typing import Optional
from .base import EndpointBase
from ..models import Token, PublicUser, PrivateUser


class UserEndpoint(EndpointBase):
    """Endpoints for retrieving information about a user’s profile."""
    def __init__(self, token: Token):
        super().__init__(token)

        self._user = f"{self._base_url}"

    def get_current_user(self) -> PrivateUser:
        """Get detailed profile information about the current user (including the current user’s username).

        Returns:
            The current user's profile information.
        """
        response = self._get(f"{self._user}/me")

        return PrivateUser(response.json())

    def get_user(self, id: str) -> PublicUser:
        """Get public profile information about a Spotify user.

        Args:
            id: The user’s Spotify user ID.

        Returns:
            The profile information of the specified user_id.
        """
        response = self._get(f"{self._user}/users/{id}")

        return PublicUser(response.json())
