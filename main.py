from pyrogram import Client , filters
import datetime , schedule , asyncio , os , random
import pytz  , logging
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pysondb import db
api_id =00 # need a edit
api_hash ='api-hash' # need a edit
admin =00  # need a edit
session_name = "self-spammer-never-offline"  
chat_id_spam = []
run = [] 
timeSlip = []
app = Client(session_name, api_id, api_hash)
tehran = pytz.timezone('Asia/Tehran')
tehran_time = datetime.now(tehran)  
if os.path.exists("downloads"):
        if os.path.exists("downloads/text.txt"): pass
        else : 
            with open ("downloads/text.txt" , 'w')  as file: file.write("")
        if os.path.exists("downloads/cap.txt"): pass
        else : 
            with open ("downloads/cap.txt" , 'w')  as file: file.write("")
else :
        os.mkdir("downloads")  
        with open ("downloads/text.txt" , 'w')  as file: file.write("")
        with open ("downloads/cap.txt" , 'w')  as file: file.write("")
scheduler = AsyncIOScheduler()
scheduler.start()
@app.on_message(filters.user(admin) , group=1)
async def help(client , message):
    if message.text == "help":
        n1 = "welcome to self ZX"
        n2 = "hello dir"
        n3 = "develpoer : @DevelopGod"
        n4 = "To add text "
        n5 = "`text `Hello @liknat"
        n20 = "To delete texts"
        n21 = "`cleanText`"
        n6 = "To add caption"
        n7 = "`caption `Hallo"
        n8 = "To delete caption"
        n9 = "`cleanCaption`"
        n10 = "To change chat id "
        n11 = "`set_id `-100+ID"
        n27 = "To clean all id"
        n28 = "`cleanid`"
        n29 = "To see id list"
        n30 = "`idlist`"
        n18 = "Set time for spam"
        n19 = "`time `5"
        n12 = "join in the group"
        n13 = "`join `(link)"
        n14 = "left in the group"
        n15 = "`left ` -100+ID"
        n16 = "change name account"
        n22 = "`name `Mohammad"
        n23 = "change bio account"
        n24 = "`bio `Mohammad"
        n25 = "ping command"
        n26 = "`ping`"
        n17 = "it never goes offline"
        texthelp = f"{n1}\n{n2}\n{n3}\n\n{n4}\n{n5}\n{n20}\n{n21}\n{n6}\n{n7}\n{n8}\n{n9}\n{n10}\n{n11}\n{n27}\n{n28}\n{n29}\n{n30}\n{n18}\n{n19}\n{n12}\n{n13}\n{n14}\n{n15}\n{n16}\n{n22}\n{n23}\n{n24}\n{n25}\n{n26}\n\n{n17}"
        await message.reply(f"**{texthelp}**")
@app.on_message(filters.user(admin) , group=2)
async def add_text(client , message):
    if message.text:
        text = message.text.strip()
        if text.startswith("text "):
            content = text[5:]
            with open('downloads/text.txt', 'a') as file:
                file.write(content + '\n')
                await message.reply_text("**TEXTS SAVED!**")
@app.on_message(filters.user(admin) , group=3)
async def changechat_id(client , message):
    if message.text:
        text = message.text.strip()
        if text.startswith("set_id "):
            chat_id = text[7:]
            chat_id_spam.append(chat_id) 
            this_job = scheduler.get_job(job_id="spam")
            if this_job is None:
                scheduler.add_job(spammer, "interval", seconds=timeSlip[0], id="spam")
                await message.reply("**ID SETED!**")
async def spammer(): 
    with open('downloads/text.txt', 'r', encoding="utf-8") as txt:
        lines = txt.readlines()
        text = random.choice(lines).strip()
    with open('downloads/cap.txt', 'r', encoding="utf-8") as cap:
        cap_text = cap.read().strip()
        طtext = cap_text + '\n' + text
    for spam_id in chat_id_spam:
        try:
            await app.send_message(chat_id=spam_id, text=text)
        except:
            pass
@app.on_message(filters.user(admin),group=6)
async def numbercap(client,message):    
    if message.text.startswith("caption"):
            text = message.text.replace("caption", "").strip()
            with open("downloads/cap.txt", "a") as file:
                file.write(text + "\n")
                await message.reply_text("**CAPTION SAVED!**")        
@app.on_message(filters.user(admin),group=7)
async def numberdelcap(client,message):
    if message.text == "cleanCaption":
        with open("downloads/cap.txt", "w") as file:
            file.write("")
            await message.reply("**CAPTIONS CLEAN!**")
@app.on_message(filters.user(admin) , group=8)
async def stopspammer(client , message):
    if message.text.startswith("time "):
        txt = message.text.replace("time ", "") 
        etxt = int(txt)
        timeSlip.append(etxt)
        await message.reply(f"**{txt} second \nOKAY!**")
@app.on_message(filters.user(admin),group=9)
async def deltar(client , message):    
    if message.text == "cleanid":   
        chat_id_spam.clear()
        this_job = scheduler.get_job(job_id="spam")
        if this_job is not None:
            scheduler.remove_job(job_id="spam")
            await message.reply("**ALL ID NOW CLEANED!**")
@app.on_message(filters.user(admin),group=10)
async def listtarget(client , message):    
    if message.text == "idlist":        
        if len(chat_id_spam) == 0:
            txt = "EMPETY!"
        else:
            txt = "\n"
            i = 1
            for spam_id in chat_id_spam:
                txt += f"**\n{i}. `{spam_id}`**"
                i += 1    
        await message.reply(text= txt)
@app.on_message(filters.user(admin),group=11)
async def pingBOT(client , message):
    if message.text == "ping":
        pin = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
        ping = random.choice(pin)
        await message.reply_text(f"**ROBOT ONLINE! \n {ping}s**")
@app.on_message(filters.user(admin),group=12)
async def joinchat(client , message):
    if message.text:
        text = message.text.strip()
        if text.startswith("join "):
            link = text[5:]
            await app.join_chat(chat_id=link)
            await message.reply("JOINED!")
@app.on_message(filters.user(admin),group=13)
async def leftchat(client , message):
    if message.text:
        text = message.text.strip()
        if text.startswith("left "):
            link = text[5:]
            await app.leave_chat(chat_id=link,delete=True)
            await message.reply("LEFTED!")
@app.on_message(filters.user(admin),group=14)
async def changename(client,message):
    if message.text:
        text = message.text.strip()
        if text.startswith("name "):
            nametext = text[5:]
            await app.update_profile(first_name=nametext)
            await message.reply("NAME CHANGED!")
@app.on_message(filters.user(admin),group=15)
async def changebio(client,message):
    if message.text:
        text = message.text.strip()
        if text.startswith("bio "):
            biotext = text[4:]
            await app.update_profile(bio=biotext)
            await message.reply("BIO CHANGED!")
@app.on_message(filters.user(admin),group=16)
async def cleantexts(client,message):
    if message.text == "cleanTexts":
        with open("downloads/text.txt", "w") as file:
            file.write("")
        await message.reply("**TEXTS CLEAN!**")
app.run()
    