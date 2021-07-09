from conn_scrapli_async import conn_scrapli


async def get_connection(device, connection_type, connection_key):
    if connection_type == 'scrapli-async':
        return await conn_scrapli(device, connection_key)
    return None

async def close_connection(connection, connection_type):
    if connection_type == 'scrapli-async':
        await connection.close()
