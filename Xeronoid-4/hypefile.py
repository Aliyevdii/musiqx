"""⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••| 
                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.

                        ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|        
⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
"""
import os
import subprocess
from sys import platform



XEXO = "⇜⊷•♪ 🦋Ӽɛʀօռօɨɖ🦋 ♪•⊶⇝** by 🔥 ΉYPΣ VӨID LΛB 🔥\n"
print(f"{XEXO}")
print("The bot is going to run in>   "  +   platform.upper())



HEROKU = os.environ.get('HEROKU', None)
if HEROKU is not None and HEROKU == "HEROKU": # For heroku, docker container will do it initially
    subprocess.run("python3 -m Ӽɛʀօռօɨɖ & python3 -m Ӽɛʀօռօɨɖɮօȶ",shell=True)
else: # This is basically for auto downloading reqs in WSL and or Replit
    os.system("pip3 install --upgrade pip;pip3 install -r Ӽɛʀօռօɨɖ.txt;clear")
    subprocess.run("python3 -m Ӽɛʀօռօɨɖ & python3 -m Ӽɛʀօռօɨɖɮօȶ",shell=True)