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
from ɦʏքɛʋօɨɖʟǟɮ.xᴇʀᴏꜰɪʟᴇᴛꜱ.butts import MIB,SIB
from ɦʏքɛʋօɨɖʟǟɮ.ᴘᴜʀɢᴇ_ᴍᴇᴄʜᴀɴɪꜱᴍ import * 
from ɦʏքɛʋօɨɖʟǟɮ.ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ import *
from ɦʏքɛʋօɨɖʟǟɮ.xᴇʀᴏꜰɪʟᴇᴛꜱ import *
from ɦʏքɛʋօɨɖʟǟɮ.ʟɪʙʀᴀʀʏ import *
from ɦʏքɛʋօɨɖʟǟɮ.ʜᴏᴍᴇ import *


@Client.on_message(
filters.group
& Xero_Singer
& Known_User
& ~filters.edited
& filters.command("resume", prefixes=DYNO_COMMANDK)
)
async def resume_playing(_, XS: XeroSpeak):
    '|-------------------------------🦋Ӽɛʀօռօɨɖ🦋------------------------------|'
    XePlay.group_call.resume_playout()
    reply = await XS.reply_animation(
        animation=xerolink,
        caption=f"{XEXO}🎧 𝗥𝗲𝘀𝘂𝗺𝗲𝗱 𝗠𝘂𝘀𝗶𝗰 𝗶𝗻 𝗩𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝘁...",
        reply_markup = MIB    )
    '|-------------------------------🦋Ӽɛʀօռօɨɖ🦋------------------------------|'
    if XePlay.msg.get('pause') is not None:
        await XePlay.msg['pause'].delete()
    await XS.delete()
    '|-------------------------------🦋Ӽɛʀօռօɨɖ🦋------------------------------|'
    await xeronoid_resume_purge(
        (reply, XS),
        RESUME_REMOVER)

