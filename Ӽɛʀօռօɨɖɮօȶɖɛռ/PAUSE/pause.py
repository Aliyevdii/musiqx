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

'⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'
from ɦǟռɖʟɛʀֆ import *
from ɖօօʍ_ʀօօʍ import *
from ǟʊȶօ_քʊʀɢɛʀ import *
from ʟɨɮʀǟʀʏ_ʀօօʍ import *
'⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'

@Ӽɛʀօռօɨɖ.on_message(
xeronoid_bot_master_filter 
& xerofil.chat(CHAT_ID)
& xerofil.command("pause", prefixes="/"))
async def pause_playing(client, xemsg: xeromsg):
    xeroclip.xeronoid_musical_xhat.pause_playout()
    await xeroclip.xeronoid_begin_clock(reset=True)
    await xemsg.reply_chat_action("record_audio")
    await client.send_animation(
    chat_id=LOGGER_ID,
    animation=xerolink,
    duration=10,
    text=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝘁𝗼 𝗽𝗮𝘂𝘀𝗲 𝗮𝘂𝗱𝗶𝗼 𝗯𝗲𝗶𝗻𝗴 𝗽𝗹𝗮𝘆𝗲𝗱 𝗯𝘆 𝘁𝗵𝗲 𝗯𝗼𝘁"
    )
    xemsg.reply_text("𝗜𝗻𝗶𝘁𝗶𝗮𝘁𝗲𝗱 𝘅𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗽𝗮𝘂𝘀𝗲 𝘀𝗲𝗾𝘂𝗲𝗻𝗰𝗲!")
    xeronoid_throw = await xemsg.reply_animation(
    animation=xerolink,
    caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗶𝘀 𝗻𝗼𝘄 𝗽𝗮𝘂𝘀𝗲𝗱 𝗶𝗻 𝘃𝗼𝗶𝗰𝗲𝗰𝗵𝗮𝘁",
    quote=False
    )
    xeroclip.xeronoid_msngr['pause'] = xeronoid_throw
    
    await xeronoid_pause_purge((xemsg, xemsg), PAUSE_REMOVER)
    