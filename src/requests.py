import requests
from typing import Any, Dict, Optional
from abc import ABC, abstractmethod

class BaseRequest(ABC):
    def __init__(
        self,
        base_url: str,
        default_headers: Optional[Dict[str, str]] = None,
        timeout: int = 10
    ):
        self.base_url = base_url.rstrip("/")
        self.default_headers = default_headers or {}
        self.timeout = timeout


    def _build_url(self, path: str) -> str:
        path = path.lstrip("/")
        return f"{self.base_url}/{path}"
    
    @abstractmethod
    def get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        pass



class HelloTicketsAPIClient(BaseRequest):

    def get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        url = self._build_url(path)
        merged_headers = {**self.default_headers, **(headers or {})}

        response = requests.get(
            url,
            params=params,
            headers=merged_headers,
            timeout=self.timeout
        )

        # Raise for non‑2xx responses
        response.raise_for_status()
        return response