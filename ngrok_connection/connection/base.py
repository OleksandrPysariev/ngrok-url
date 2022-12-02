from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

from ngrok_connection.exceptions import DataNotLoadedError, TunnelNotFoundError


class BaseNgrokConnection(ABC):

    def __init__(
            self,
            ngrok_host: str = "http://localhost",
            ngrok_port: int = 4040
    ):
        self.ngrok_host = ngrok_host
        self.ngrok_port = ngrok_port
        self.data: Optional[Dict[str, Union[List[dict], Any]]] = None

    @property
    def ngrok_url(self):
        return f"{self.ngrok_host}:{self.ngrok_port}/api/tunnels"

    @abstractmethod
    def load_tunnel_data(self) -> None:
        raise NotImplementedError

    @property
    def tunnels(self) -> list[dict]:
        if not self.data:
            raise DataNotLoadedError()

        return self.data["tunnels"]

    def get_tunnel_url(self, tunnel_index: int = 0) -> str:
        tunnels = self.tunnels
        if tunnel_index >= len(tunnels):
            raise TunnelNotFoundError(tunnel_index)

        return tunnels[tunnel_index]["public_url"]
