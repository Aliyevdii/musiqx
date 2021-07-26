"""⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|
                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.

                        ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
|••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|       
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝"""


from Ӽɛʀօռօɨɖ.ɖօօʍ_ʀօօʍ import *
from Ӽɛʀօռօɨɖ.Ӽɛʀօռօɨɖʍʊֆɨƈ.xmp import *
from Ӽɛʀօռօɨɖ.ʟɨɮʀǟʀʏ_ʀօօʍ import *


async def skip_current_playing():
    xeronoid_voixe = xep.xeronoid_voixe
    xeronoid_music_list = xep.xeronoid_music_list
    if not xeronoid_music_list:
        return
    if len(xeronoid_music_list) == 1:
        await xep.update_start_time()
        return
    client = xeronoid_voixe.client
    download_dir = os.path.join(client.workdir, DEFAULT_DOWNLOAD_DIR)
    xeronoid_voixe.input_filename = os.path.join(
    download_dir,
    f"{xeronoid_music_list[1].audio.file_unique_id}.raw")
    await xep.update_start_time()
    # remove old track from Ӽɛʀօռօɨɖ.xeronoid_music_list
    old_track = xeronoid_music_list.pop(0)
    print(f"• START PLAYING: {xeronoid_music_list[0].audio.title}")
    await xep.send_playlist()
    os.remove(os.path.join(
        download_dir,
        f"{old_track.audio.file_unique_id}.raw")
    )
    if len(xeronoid_music_list) == 1:
        return
    await download_audio(xeronoid_music_list[1])


async def download_audio(xeMsg: XeronoidMessageType):
    xeronoid_voixe = xep.xeronoid_voixe
    client = xeronoid_voixe.client
    raw_file = os.path.join(client.workdir, DEFAULT_DOWNLOAD_DIR,
                            f"{xeMsg.audio.file_unique_id}.raw")
    if not os.path.isfile(raw_file):
        original_file = await xeMsg.download()
        ffmpeg.input(original_file).output(
            raw_file,
            format='s16le',
            acodec='pcm_s16le',
            ac=2,
            ar='48k',
            loglevel='error'
        ).overwrite_output().run()
        os.remove(original_file)