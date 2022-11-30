import database 
import asyncio

async def main():
    db = database.Database()
    await db.connect()
    data = {
        "FileID": "zzz",
        "Division": "Strategy",
        "FileName": "",
        "Cycle": "Aevum",
        "OldData": True,
    }
    i = await db.createEntry(data)

asyncio.run(main())


