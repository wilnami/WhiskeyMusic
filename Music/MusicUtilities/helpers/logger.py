from Music.config import LOG_GROUP_ID
from Music import app


async def LOG_CHAT(message, what):
    if message.chat.username:
        chatusername = (f"@{message.chat.username}")
    else:
        chatusername = ("Private Group")
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")" 
    logger_text = f"""
__**wilna ada request**__

**dari:** {message.chat.title} [`{message.chat.id}`]
**nama:** {mention} hadeh
**username:** @{message.from_user.username}
**id:** `{message.from_user.id}`
**link:** {chatusername} yekans
**pesan dan kesan:** {message.text}"""
    await app.send_message(LOG_GROUP_ID, f"{logger_text}", disable_web_page_preview=True)
    
