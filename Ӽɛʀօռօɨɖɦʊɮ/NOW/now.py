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
xeronoid_master_filter
& xeronoid_chat_check
& xerofil.command("now", prefixes="/"))
async def show_current_playing_time(_, xemsg: xeromsg):
    start_time = xeroclip.start_time
    xeronoid_music_list = xeroclip.xeronoid_music_list
    if not start_time:
        await xemsg.reply_chat_action("find_location")
        cprint('🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝗳𝗼𝗿 𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘄𝗵𝗶𝗰𝗵 𝘀𝗼𝗻𝗴 𝗶𝘀 𝗯𝗲𝗶𝗻𝗴 𝗽𝗹𝗮𝘆𝗲𝗱 𝗯𝘆 𝘁𝗵𝗲 𝗯𝗼𝘁', 'yellow', attrs=['reverse'])
        xeronoid_throw = await xemsg.reply_animation(
        animation=xerolink,
        caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n🎧 𝗨𝗻𝗸𝗻𝗼𝘄𝗻 𝗼𝗿 𝗻𝗼 𝗳𝗶𝗹𝗲𝘀 𝘆𝗲𝘁 𝗶𝗻 𝘅𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝘀𝗲𝗿𝘃𝗲𝗿"
        )
        await xeronoid_current_purge((xeronoid_throw, xemsg), CURRENT_REMOVER)
        return
    utcnow = datetime.utcnow().replace(microsecond=0)
    if xeroclip.xeronoid_msngr.get('current') is not None:
        await xeroclip.xeronoid_msngr['current'].delete()
    xeroclip.xeronoid_msngr['current'] = await xeronoid_music_list[0].reply_animation(
        animation=xerolink,
        caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n🎧 {utcnow - start_time} {timedelta(seconds=xeronoid_music_list[0].audio.duration)}",
        disable_notification=True
        )
    await xeronoid_current_purge((xemsg), CURRENT_REMOVER)