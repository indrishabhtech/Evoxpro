import os
import asyncio
import yt_dlp

from ... import app
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch


@app.on_message(filters.command(["song"], ["/", "!", "."]))
async def song(client: app, message: Message):
    aux = await message.reply_text("**🔄 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 ...**")
    if len(message.command) < 2:
        return await aux.edit(
            "**🤖 𝐆𝐢𝐯𝐞 🙃 𝐌𝐮𝐬𝐢𝐜 💿 𝐍𝐚𝐦𝐞 😍\n💞 𝐓𝐨 🔊 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 🥀 𝐒𝐨𝐧𝐠❗**"
        )
    try:
        song_name = message.text.split(None, 1)[1]
        vid = VideosSearch(song_name, limit = 1)
        song_title = vid.result()["result"][0]["title"]
        song_link = vid.result()["result"][0]["link"]
        ydl_opts = {
            "format": "mp3/bestaudio/best",
            "verbose": True,
            "geo-bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3"
                }
            ],
            "outtmpl": f"downloads/{song_title}",
        }
        await aux.edit("**𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ...**")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(song_link)
        await aux.edit("**𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ...**")
        await message.reply_audio(f"downloads/{song_title}.mp3")
        try:
            os.remove(f"downloads/{song_title}.mp3")
        except:
            pass
        await aux.delete()
    except Exception as e:
        await aux.edit(f"**Error:** {e}")


######


@app.on_message(filters.command(["song"], ["/", "!", "."]))
async def download_instareels(c: app, m: Message):
    try:
        reel_ = m.command[1]
    except IndexError:
        await m.reply_text("Give me an link to download it...")
        return
    if not reel_.startswith("https://www.instagram.com/reel/"):
        await m.reply_text("In order to obtain the requested reel, a valid link is necessary. Kindly provide me with the required link.")
        return
    OwO = reel_.split(".",1)
    Reel_ = ".dd".join(OwO)
    try:
        await m.reply_video(Reel_)
        return
    except Exception:
        try:
            await m.reply_photo(Reel_)
            return
        except Exception:
            try:
                await m.reply_document(Reel_)
                return
            except Exception:
                await m.reply_text("I am unable to reach to this reel.")


  
