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
from ɦʏքɛʋօɨɖʟǟɮ.ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ import *
from ɦʏքɛʋօɨɖʟǟɮ.ʟɪʙʀᴀʀʏ import *
from ɦʏքɛʋօɨɖʟǟɮ.ʜᴏᴍᴇ import *





'|-------------------------------🦋Ӽɛʀօռօɨɖ🦋------------------------------|'
async def Xero_Singing(_, __, XS: XeroSpeak):
    group_call = XePlay.group_call
    if not (group_call and group_call.is_connected):
        return False
    chat_id = int("-100" + str(group_call.full_chat.id))
    if XS.chat.id == chat_id:
        return True
    return False
Xero_Singer = filters.create(Xero_Singing)
'|-------------------------------🦋Ӽɛʀօռօɨɖ🦋------------------------------|'
Known_User = filters.create(lambda _, __, message:(message.from_user and message.from_user.is_contact) or message.outgoing)
'|-------------------------------🦋Ӽɛʀօռօɨɖ🦋------------------------------|'
async def XeroBot_Voixe_Check(_, __, XS: XeroSpeak):
    group_call = XePlay.group_call
    if group_call and group_call.is_connected:
        return True
    return False
Voixe_Check = filters.create(XeroBot_Voixe_Check)
'|-------------------------------🦋Ӽɛʀօռօɨɖ🦋------------------------------|'