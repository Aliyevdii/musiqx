""" 
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|----------------------------------------------------------------------------------------|
                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.

                        ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
|----------------------------------------------------------------------------------------|       
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
"""

'⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'
from ɦǟռɖʟɛʀֆ import *
from ɖօօʍ_ʀօօʍ import *
from ǟʊȶօ_քʊʀɢɛʀ import *
from ʟɨɮʀǟʀʏ_ʀօօʍ import *
'⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'

@Ӽɛʀօռօɨɖ.on_message(
xeronoid_bot_master_filter 
& xerofil.chat(CHAT_ID)
& xerofil.command("volume", prefixes="/"))
async def volume(client, xemsg: xeromsg):
   if len(xemsg.command) < 2:
      await xemsg.reply_chat_action("playing")
      await client.send_animation(
      chat_id=LOGGER_ID,
      animation=xerolink,
      duration=10,
      text=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝘁𝗼 𝗰𝗵𝗮𝗻𝗴𝗲 𝘃𝗼𝗹𝘂𝗺𝗲 𝗼𝗳 𝗮𝘂𝗱𝗶𝗼 𝗯𝗲𝗶𝗻𝗴 𝗽𝗹𝗮𝘆𝗲𝗱 𝘁𝗵𝗲 𝗯𝗼𝘁 𝗯𝘂𝘁 𝗳𝗮𝗶𝗹𝗲𝗱"
      )
      xeronoid_throw = await xemsg.reply_animation(
      xerolink,
      caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝐘𝐨𝐮 𝐟𝐨𝐫𝐠𝐨𝐭 𝐭𝐨 𝐩𝐚𝐬𝐬 𝐯𝐨𝐥𝐮𝐦𝐞 (𝟏-𝟐𝟎𝟎)"
      )
   else:
      await group_calls.set_my_volume(volume=int(xemsg.command[1]))
      await xemsg.reply_chat_action("playing")
      await client.send_animation(
      chat_id=LOGGER_ID,
      animation=xerolink,
      duration=10,
      text=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝘁𝗼 𝗰𝗵𝗮𝗻𝗴𝗲 𝘃𝗼𝗹𝘂𝗺𝗲 𝗼𝗳 𝗮𝘂𝗱𝗶𝗼 𝗯𝗲𝗶𝗻𝗴 𝗽𝗹𝗮𝘆𝗲𝗱 𝘁𝗵𝗲 𝗯𝗼𝘁"
      )
      xeronoid_throw = await xemsg.reply_animation(
      animation=xerolink,
      caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝗩𝗼𝗹𝘂𝗺𝗲 𝗰𝗵𝗮𝗻𝗴𝗲𝗱 𝘁𝗼 {xemsg.command[1]}"
      )
   
   await xeronoid_volume_purge((xeronoid_throw, xemsg), VOLUME_REMOVER)