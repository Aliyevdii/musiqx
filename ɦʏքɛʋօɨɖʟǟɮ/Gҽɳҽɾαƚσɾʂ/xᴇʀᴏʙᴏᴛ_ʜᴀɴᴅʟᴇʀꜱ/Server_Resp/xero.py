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
from 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯.xᴇʀᴏꜰɪʟᴇᴛꜱ.butts import MIB,SIB
from 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯.ᴘᴜʀɢᴇ_ᴍᴇᴄʜᴀɴɪꜱᴍ import * 
from 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯.ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ import *
from 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯.ʟɪʙʀᴀʀʏ import *
from 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯.ʜᴏᴍᴇ import *


@Client.on_message(
filters.command("xero", prefixes="/"))
async def pong(client, XS: XeroSpeak):
    await XS.reply_chat_action("typing")

    start = datetime.now()
    end = datetime.now()
    delta_energy1 = (end - start).seconds
    delta_energy2= (end - start).microseconds
    
    await client.send_animation(
        animation=xerolink,
        duration=10,
        chat_id=LOGGER_ID,
        caption=f"{XEXO}🎧 𝗦𝗲𝗿𝘃𝗲𝗿 𝗿𝗲𝘀𝗽𝗼𝗻𝘀𝗲 𝘁𝗶𝗺𝗲 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗳𝗲𝘁𝗰𝗵𝗲𝗱 𝗮𝗻𝗱 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝘁𝗼 𝘁𝗵𝗲 𝘂𝘀𝗲𝗿"
		)
 
    zeto = await XS.reply_animation(
        xerolink,
        caption=f"""{XEXO}
        |   𝚂𝚎𝚛𝚟𝚎𝚛 𝚛𝚎𝚜𝚙𝚘𝚗𝚜𝚎 𝚝𝚒𝚖𝚎 𝚒𝚜   |
                📡 **{delta_energy1}** `𝙨𝙚𝙘𝙤𝙣𝙙𝙨` 
                📡 **{delta_energy2}** `𝙢𝙞𝙘𝙧𝙤𝙨𝙚𝙘𝙤𝙣𝙙𝙨`""",
        reply_markup = MIB) 


    # Let's Clean this also lol.....
    await delete_server(
        (zeto,  XS),
         SERVER_REMOVER)
    return 