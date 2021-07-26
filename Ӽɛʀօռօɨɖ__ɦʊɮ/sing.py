"""⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••| 
                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.

                        ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|        
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝"""
from ɖօօʍ_ʀօօʍ import *
from ǟʊȶօ_քʊʀɢɛʀ import *
from ʟɨɮʀǟʀʏ_ʀօօʍ import *
from Ӽɛʀօռօɨɖʍʊֆɨƈ import *
from ƈʊֆȶօʍ_ʄɨʟȶɛʀֆ import *





@Ӽɛʀօռօɨɖ.on_message(
filters.group
& ~filters.edited
& xero_xemp_fils
& filters.command("sing", prefixes=DYNO_COMMANDK) | filters.audio)
async def play_track(client, xeMsg: XeronoidMessageType):
    xeronoid_voixe = xep.xeronoid_voixe
    xeronoid_music_list = xep.xeronoid_music_list
    # check audio
    if xeMsg.audio:
        if xeMsg.audio.duration > (MAX_MIN * 60):
            reply = await xeMsg.reply_text(
                f"{emoji.ROBOT} audio which duration longer than "
                f"{str(MAX_MIN)} min won't be automatically "
                "added to xeronoid_music_list"
            )
            await delay_sing_messages((reply,), PLAY_REMOVER)
            return
        m_audio = xeMsg
    elif xeMsg.reply_to_message and xeMsg.reply_to_message.audio:
        m_audio = xeMsg.reply_to_message
        if m_audio.audio.duration > (MAX_HOUR * 60 * 60):
            reply = await xeMsg.reply_text(
                f"{emoji.ROBOT} audio which duration longer than "
                f"{str(MAX_HOUR)} hours won't be added to xeronoid_music_list"
            )
            await delay_sing_messages((reply,), PLAY_REMOVER)
            return
    else:
        await xep.send_playlist()
        await xeMsg.delete()
        return
    # check already added
    if xeronoid_music_list and xeronoid_music_list[-1].audio.file_unique_id \
            == m_audio.audio.file_unique_id:
        reply = await xeMsg.reply_text(f"{emoji.ROBOT} already added")
        await delay_sing_messages((reply, xeMsg), PLAY_REMOVER)
        return
    # add to xeronoid_music_list
    xeronoid_music_list.append(m_audio)
    if len(xeronoid_music_list) == 1:
        m_status = await xeMsg.reply_text(
            f"{emoji.INBOX_TRAY} downloading and transcoding..."
        )
        await download_audio(xeronoid_music_list[0])
        xeronoid_voixe.input_filename = os.path.join(
            client.workdir,
            DEFAULT_DOWNLOAD_DIR,
            f"{xeronoid_music_list[0].audio.file_unique_id}.raw"
        )
        await xep.update_start_time()
        await m_status.delete()
        print(f"- START PLAYING: {xeronoid_music_list[0].audio.title}")
    await xep.send_playlist()
    for track in xeronoid_music_list[:2]:
        await download_audio(track)
    if not xeMsg.audio:
        await xeMsg.delete()
