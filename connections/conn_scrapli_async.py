from scrapli import AsyncScrapli


class conn_scrapli():
    def __init__(self, device, connection_key):
        self.device = device
        self.connection_key = connection_key

    async def connect(self):
        self.connection = AsyncScrapli(**self.device[self.connection_key])
        await self.connection.open()
        return self.connection

    async def close(self):
        await self.connection.close()