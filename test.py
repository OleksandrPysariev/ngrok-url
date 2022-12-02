import asyncio

from ngrok_connection import AsyncNgrokConnection, SyncNgrokConnection


def sync_test():
    connection = SyncNgrokConnection()
    connection.load_tunnel_data()
    return connection.get_tunnel_url()


async def async_test():
    connection = AsyncNgrokConnection()
    await connection.load_tunnel_data()
    return connection.get_tunnel_url()


async def main():
    real_value = input("Enter real value: ")

    sync_res = sync_test()
    async_res = await async_test()

    print(f"{sync_res = }")
    print(f"{async_res = }")

    assert sync_res == real_value
    assert async_res == real_value


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
