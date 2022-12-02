class Error(Exception):
    """Base class for other exceptions"""

    pass


class NgrokConnectionError(Error):
    def __init__(self, url: str):
        self.url = url
        super().__init__(f"Ngrok did not respond to {self.url}")


class NgrokNoTunnelError(Error):
    def __init__(self):
        super().__init__("Ngrok has no open tunnels")


class TunnelNotFoundError(Error):
    def __init__(self, index: int):
        super().__init__(f"Tunnel not found with index {index}")


class DataNotLoadedError(Error):
    def __init__(self):
        super().__init__("Data not loaded. Please, use load_tunnel_data before using this method")
