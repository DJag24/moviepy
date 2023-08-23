python
import telegram
import subprocess
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

# Replace YOUR_BOT_TOKEN with your actual bot token
bot = telegram.Bot(token='6035704347:AAFe3bk_NeimNu6jKp6GFANMxbx2vAg68PY')

def trim_video(update, context):
    chat_id = update.message.chat_id
    try:
        # Get the URL of the video
        url = update.message.text.split(' ')[1]
        
        # Download the video using youtube-dl
        command = f"youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' -o video.mp4 -- {url}"
        subprocess.call(command, shell=True)
        
        # Trim the video using moviepy
        clip = VideoFileClip("video.mp4").subclip(10, 20)
        clip.write_videofile("output.mp4")
        
        # Send the trimmed video to the user
        bot.send_video(chat_id=chat_id, video=open("output.mp4", "rb"))
        
        # Delete temporary files
        os.remove("video.mp4")
        os.remove("output.mp4")
    except Exception as e:
        bot.send_message(chat_id=chat_id, text=str(e))

# Replace YOUR_BOT_TOKEN with your actual bot token
updater = telegram.ext.Updater(token='6035704347:AAFe3bk_NeimNu6jKp6GFANMxbx2vAg68PY', use_context=True)
updater.dispatcher.add_handler(telegram.ext.CommandHandler('trim', trim_video))
updater.start_polling()
```
