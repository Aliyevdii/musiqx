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
from Ӽɛʀօռօɨɖʍʊֆɨƈ import *
from ƈʊֆȶօʍ_ʄɨʟȶɛʀֆ import *
from ɖօօʍ_ʀօօʍ import *
from ǟʊȶօ_քʊʀɢɛʀ import *
from ʟɨɮʀǟʀʏ_ʀօօʍ import *
'⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝    ••••••••|••••••••    ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'

@Ӽɛʀօռօɨɖ.on_message(
xeronoid_master_filter
& xeronoid_user_filter
& xerofil.command("group", prefixes="/"))
async def list_voice_chat(client, xemsg: xeromsg):
    group_call = xep.group_call
    if group_call and group_call.is_connected:
        xeronoid_chatid = int("-100" + str(group_call.full_chat.id))
        chat = await client.get_chat(xeronoid_chatid)
        await client.send_animation(
        chat_id=LOGGER_ID,
        animation=xerolink,
        duration=10,
        caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝗳𝗼𝗿 𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘄𝗵𝗲𝗮𝘁𝗵𝗲𝗿 𝘁𝗵𝗲 𝗯𝗼𝘁 𝗶𝘀 𝗽𝗹𝘂𝗴𝗴𝗲𝗱 𝗼𝗿 𝗻𝗼𝘁"
        )
        cprint('🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝗳𝗼𝗿 𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘄𝗵𝗲𝗮𝘁𝗵𝗲𝗿 𝘁𝗵𝗲 𝗯𝗼𝘁 𝗶𝘀 𝗽𝗹𝘂𝗴𝗴𝗲𝗱 𝗼𝗿 𝗻𝗼𝘁', 'yellow', attrs=['bold'])
        xeronoid_throw = await xemsg.reply_animation(
        animation=xerolink,
		duration=10,
        caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n🎧 𝗖𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗶𝗻 𝘁𝗵𝗲 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁:\n**{chat.title}**"
        )
    else:
        await client.send_animation(
        chat_id=LOGGER_ID,
        animation=xerolink,
        duration=10,
        caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝗳𝗼𝗿 𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘄𝗵𝗲𝗮𝘁𝗵𝗲𝗿 𝘁𝗵𝗲 𝗯𝗼𝘁 𝗶𝘀 𝗽𝗹𝘂𝗴𝗴𝗲𝗱 𝗼𝗿 𝗻𝗼𝘁"
        )
        cprint('🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝗳𝗼𝗿 𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘄𝗵𝗲𝗮𝘁𝗵𝗲𝗿 𝘁𝗵𝗲 𝗯𝗼𝘁 𝗶𝘀 𝗽𝗹𝘂𝗴𝗴𝗲𝗱 𝗼𝗿 𝗻𝗼𝘁', 'yellow', attrs=['bold'])
        xeronoid_throw = await xemsg.reply_animation(
        animation=xerolink,
		duration=10,
        caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n🎧 𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗵𝗮𝘀 𝗻𝗼𝘁 𝗷𝗼𝗶𝗻𝗲𝗱 𝗮𝗻𝘆 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁 𝘆𝗲𝘁"
        )
        await xeronoid_group_purge((xeronoid_throw, xemsg), GROUP_REMOVER)