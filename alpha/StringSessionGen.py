import asyncio

from pyrogram import Client


async def create_session() -> None:  # pylint: disable=missing-function-docstring
    async with Client(
            ":memory:",
            api_id=input("Enter Telegram APP ID: "),
            api_hash=input("Enter Telegram API HASH: ")
    ) as alpha:
        print("\nprocessing...")
        await alpha.send_message(
            "me", f"your `STRING_SESSION` is\n\n`{await alpha.export_session_string()}`")
        print("String_Session is sent to you Telegram saved messages.")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(create_session())