#!/usr/bin/env python

import os
import sys
import aiohttp
import asyncio
from PIL import Image


async def download_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


async def download_and_write_file(name):
    content = await download_content("https://this" + str(name) + "doesnotexist.com/")
    fout = open(name, 'wb')
    fout.write(content)
    try:
        Image.open(name)
    except IOError:
        os.rename(name, name + '.html')
        return
    os.rename(name, name + '.jpg')


async def main(args):
    tasks = map(download_and_write_file, args)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # передавайте в качестве аргументов к скрипту вещи, которые хотите найти на https://thisxdoesnotexist.com/
    asyncio.run(main(sys.argv[1:len(sys.argv)]))
