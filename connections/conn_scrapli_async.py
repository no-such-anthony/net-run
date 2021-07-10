from scrapli import AsyncScrapli

async def conn_scrapli(device, connection_key):

    connection = AsyncScrapli(**device[connection_key])
    await connection.open()

    return connection