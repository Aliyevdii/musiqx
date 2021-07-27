"""
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••| 
⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝

                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                        ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|        
"""
from xᴇʀᴏꜰɪʟᴇᴛꜱ.butts import MIB,SIB
from ᴘᴜʀɢᴇ_ᴍᴇᴄʜᴀɴɪꜱᴍ import * 
from ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ import *
from xᴇʀᴏꜰɪʟᴇᴛꜱ import *
from ʟɪʙʀᴀʀʏ import *
from ʜᴏᴍᴇ import *



@Client.on_message(
filters.group
& filters.chat(CHAT_ID)
& ~filters.edited
& ~filters.via_bot
& Xero_Singer
& filters.command("sing", prefixes="/"))
async def play_track(client, XS: XeroSpeak):
    group_call = XePlay.group_call
    playlist = XePlay.playlist   
    print("Userbot is now downloading audio and sending to server...")    
    
    
    "Check Wherether audio duration matches with the specified time mentioned in the code"
    if XS.audio:
        if XS.audio.duration > (MAX_MIN * 60):
            reply = await XS.reply_animation(
                animation=xerolink,
                caption=f"{XEXO}🎧 Audio which duration longer than {str(MAX_MIN)} min won't be automatically added to playlist",
                reply_markup = MIB
            )
            await xeronoid_sing_purge(
                (reply,),
                PLAY_REMOVER)
            return
        m_audio = XS
    elif XS.reply_to_message and XS.reply_to_message.audio:
        m_audio = XS.reply_to_message
        if m_audio.audio.duration > (MAX_HOUR * 60 * 60):
            reply = await XS.reply_animation(
                animation=xerolink,
                caption=f"{XEXO}🎧 Audio which duration longer than {str(MAX_HOUR)} hours won't be added to playlist",
                reply_markup = MIB
            )
            await xeronoid_sing_purge(
                (reply,),
                PLAY_REMOVER)
            return
    else:
        await XePlay.send_playlist()
        await XS.delete()
        return
    
    
        
    
    
    "Check Wherether audio is already added in the playlist or not"
    if playlist and playlist[-1].audio.file_unique_id \
            == m_audio.audio.file_unique_id:
        reply = await XS.reply_animation(
            animation=xerolink,
            caption=f"{XEXO}🎧  That music is already added to the xeronoid playlist",
            reply_markup = MIB
            )
        await xeronoid_sing_purge(
            (reply,),
            PLAY_REMOVER)
        return
    
    
        
    
    "Download the raw audio file and send to the server and return"
    playlist.append(m_audio)
    if len(playlist) == 1:
        m_status = await client.send_animation(
            animation=xerolink,
            duration=10,
            chat_id=LOGGER_ID,
            caption=f"{XEXO}🎧 Music has been sent to the server...\nPlease wait"
        )
        
        
        m_status = await XS.reply_animation(
            animation=xerolink,
            caption=f"{XEXO}🎧 Please wait for xeronoid to link with userbot's server...\nGreater audio size, more time to add to server",
            reply_markup = MIB
        )
        await download_audio(playlist[0])
        
        
        group_call.input_filename = os.path.join(
            client.workdir,
            DEFAULT_DOWNLOAD_DIR,
            f"{playlist[0].audio.file_unique_id}.raw"
        )
        await XePlay.update_start_time()
        await m_status.delete()
        
        
        
        
        "Log the audio being transcoded and played in the group..."
        await client.send_animation(
            animation=xerolink,
            duration=10,
            chat_id=LOGGER_ID,
            caption=f"{XEXO}🎧  Xeronoid userbot has started playing:\n{playlist[0].audio.title}"
        )
        # Only userbot is going to log this event. So we need not to worry about Xeronoidbot
        
    await XePlay.send_playlist()
    for track in playlist[:2]:
        await download_audio(track)
    if not XS.audio:
        await XS.delete()
        
