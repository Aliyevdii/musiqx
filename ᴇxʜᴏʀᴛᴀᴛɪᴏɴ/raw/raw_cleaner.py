from Ӽɛʀօռօɨɖ import *
from ᴠᴏᴋᴀʟɪᴢᴇ import *
from ᴇᴘɪꜱᴛʟᴇ import *
from VEhJU0lTVVNFREZPUlhFUk9OT0lE import *


@Ӽɛռ.on_message(
demon_killer_sigki
& senzo_kryo_ni
& misa_misa
& filters.command(
"raw",
prefixes=DYNO_COMMAND)) 
async def clean_raw_pcm(client, ryui: Message):
    raw_hug = os.path.join(client.workdir, fmedaddyy)
    all_fn: list[str] = os.listdir(raw_hug)
    for track in ʜᴀᴅᴇ.playlist[:2]:
        track_fn = f"{track.audio.file_unique_id}.raw"
        if track_fn in all_fn:
            all_fn.remove(track_fn)
    files = 0
    if all_fn:
        for fn in all_fn:
            if fn.endswith(".raw"):
                files += 1
                os.remove(os.path.join(raw_hug, fn))             
    hawk = await ryui.reply_text(f"""{XE}
                                 
ɴᴜᴍʙᴇʀ ᴏꜰ ᴄʟᴇᴀɴᴇᴅ ᴛᴇᴍᴘ ꜰɪʟᴇ: **{files}**
""")
    await ryui.delete()
    await wait_before_rm((hawk, ryui), Kill_Time)
    return

async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()