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
from Ӽɛʀօռօɨɖ.ɖօօʍ_ʀօօʍ import *
from Ӽɛʀօռօɨɖ.ǟʊȶօ_քʊʀɢɛʀ import *
from Ӽɛʀօռօɨɖ.ʟɨɮʀǟʀʏ_ʀօօʍ import *
from Ӽɛʀօռօɨɖ.Ӽɛʀօռօɨɖʍʊֆɨƈ import *
from Ӽɛʀօռօɨɖ.ƈʊֆȶօʍ_ʄɨʟȶɛʀֆ import *
'|••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|'




'|••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|'
@Client.on_message(
xero_basic_fils
& xero_self_fils
& xero_xemp_fils
& filters.command("off", prefixes=DYNO_COMMANDK))
async def leave_voice_chat(_, m: Message):
    xeronoid_voixe = xep.xeronoid_voixe
    xep.xeronoid_music_list.clear()
    xeronoid_voixe.input_filename = ''
    await xeronoid_voixe.stop()
    await m.delete()
'|••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|'