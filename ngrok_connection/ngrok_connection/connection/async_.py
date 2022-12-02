from .base import BaseNgrokConnection

from aiohttp.client import ClientSession

from ..exceptions import NgrokConnectionError


class AsyncNgrokConnection(BaseNgrokConnection):

    async def load_tunnel_data(self) -> None:
        async with ClientSession() as session:
            try:
                async with session.get(self.ngrok_url) as response:
                    self.data = await response.json()
            except:
                raise NgrokConnectionError(self.ngrok_url)
