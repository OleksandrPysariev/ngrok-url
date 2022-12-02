import requests

from .base import BaseNgrokConnection
from ..exceptions import NgrokConnectionError


class SyncNgrokConnection(BaseNgrokConnection):

    def load_tunnel_data(self) -> None:
        try:
            self.data = requests.get(self.ngrok_url).json()
        except:
            raise NgrokConnectionError(self.ngrok_url)
