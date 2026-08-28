import uuid
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field


class RetailerSession(BaseModel):
    session_id: str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
    retailer: str
    country: str
    locale: str
    user_agent: str
    cookies: Dict[str, str] = Field(default_factory=dict)
    success_count: int = 0
    failure_count: int = 0
    blocked_count: int = 0
    is_retired: bool = False

    def record_success(self):
        self.success_count += 1

    def record_failure(self, is_blocked: bool = False):
        self.failure_count += 1
        if is_blocked:
            self.blocked_count += 1
        if self.blocked_count >= 3 or self.failure_count >= 6:
            self.is_retired = True


class SessionManager:
    """Manages isolated sessions per retailer-country target and enforces session retirement."""

    def __init__(self):
        self._sessions: Dict[str, RetailerSession] = {}

    def get_or_create_session(
        self,
        retailer: str,
        country: str,
        locale: str,
        user_agent: str
    ) -> RetailerSession:
        key = f"{retailer.lower()}_{country.upper()}"
        session = self._sessions.get(key)
        if session is None or session.is_retired:
            session = RetailerSession(
                retailer=retailer,
                country=country,
                locale=locale,
                user_agent=user_agent
            )
            self._sessions[key] = session
        return session
