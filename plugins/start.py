from pyrogram import Client, filters, enums
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message, ReplyKeyboardMarkup,\
    KeyboardButton
from config import prefix, developer, get_bot_information 
from database import get_db_botname
from plugins.commands import command2
from plugins.general import confirm_user


@Client.on_message(filters.command("start", prefix) & filters.user(developer))
async def startsudo(c: Client, m: Message):
    await confirm_user(c, m)
    if m.chat.type == enums.ChatType.PRIVATE:
        t = """↯︙ اهلا بك عزيزي ↫ ⦗ {await get_Rank(user_data2)} ⦘
– – – – – –
↯︙ يمكنك التحكم في بوت
↯︙ عبر الازرار في الاسفل"""
        keyboard = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton("استخدم الازرار في الاسفل")],
            [KeyboardButton("تعطيل التواصل ")] +
            [KeyboardButton("تفعيل التواصل ")],
            [KeyboardButton("تعطيل الاذاعه ")] +
            [KeyboardButton("تفعيل الاذاعه ")],
            [KeyboardButton("تعطيل اليوتيوب ")] +
            [KeyboardButton("تفعيل اليوتيوب ")],
            [KeyboardButton("المطورين ")],
            [KeyboardButton("اذاعه خاص ")] +
            [KeyboardButton("اذاعه بالمجموعات ")],
            [KeyboardButton("اذاعه بالتوجيه خاص ")] +
            [KeyboardButton("اذاعه بالتوجيه للمجموعات ⁦")],
            [KeyboardButton("اذاعه موجهه بالتثبيت ⁦")] +
            [KeyboardButton("اذاعه بالتثبيت ")],
            [KeyboardButton("الاحصائيات ")],
            [KeyboardButton("المشتركين ⁦")] +
            [KeyboardButton("الجروبات ")],
            [KeyboardButton("حذف الاعضاء الفيك ")] +
            [KeyboardButton("حذف الجروبات الفيك ")],
            [KeyboardButton("حذف رد عام ")] +
            [KeyboardButton("اضف رد عام ")],
            [KeyboardButton("الردود العامه ")],
            [KeyboardButton("قائمه الكتم العام ")] +
            [KeyboardButton("قائمه الحظر العام ")],
            [KeyboardButton("ضع اسم للبوت ")],
            [KeyboardButton("معلومات السيرفر ")] +
            [KeyboardButton("سرعه السيرفر ")],
            [KeyboardButton("جلب نسخه احتياطيه اساسيه ")],
            [KeyboardButton("رفع نسخه احتياطيه ")],
            [KeyboardButton("الاصدار ⁦")] +
            [KeyboardButton("تحديث السورس ")],
            [KeyboardButton("رستر البوت ")],
            [KeyboardButton("الغاء ⁦")],
        ],
            resize_keyboard=True,
            one_time_keyboard=False
        )
        await m.reply_text(t, reply_markup=keyboard, parse_mode=enums.ParseMode.MARKDOWN)
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(" ابدأ محادثة", url=f"https://t.me/{get_bot_information()[1]}?start=start")]])
        await m.reply_text("مرحبا! أنا فالكيري. لاكتشاف وظائفي ، ابدأ محادثة معي.", reply_markup=keyboard)


@Client.on_message(filters.command("start", prefix) & ~filters.user(developer))
async def start(c: Client, m: Message):
    await confirm_user(c, m)
    if m.chat.type == enums.ChatType.PRIVATE:
        botname = get_db_botname() or "فالكيري"
        x = f"""
↯︙ اهلا بك عزيزي ( {first_name + last_name} )
↯︙ في بوت ( {botname} )
↯︙ لحمايه المجموعات ومميزات خدميه اخرى
↯︙ للبدء ارفع البوت مشرف وارسل تفعيل
↯︙ سيتم رفع الادمنيه ومالك المجموعه تلقائيا
        """
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("الاوامر ", callback_data="commandss")] + [InlineKeyboardButton(" حول", callback_data="infos")], [InlineKeyboardButton("تغير اللغه ", callback_data="chlang")], [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ", url=f"https://t.me/{get_bot_information()[1]}?startgroup=dream")]])
        async for photo in c.get_chat_photos(get_bot_information()[1], limit=1):
            await m.reply_photo(photo.file_id, caption=x, reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(" ابدأ محادثة", url=f"https://t.me/{get_bot_information()[1]}?start=start")]])
        await m.reply_text("مرحبا! أنا فالكيري. لاكتشاف وظائفي ، ابدأ محادثة معي.", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^start_back$"))
async def start_back(c: Client, m: CallbackQuery):
    botname = get_db_botname() or "فالكيري"
    x = f"""
↯︙ اهلا بك عزيزي المستخدم
↯︙ في بوت ( {botname} )
↯︙ لحمايه المجموعات ومميزات خدميه اخرى
↯︙ للبدء ارفع البوت مشرف وارسل تفعيل
↯︙ سيتم رفع الادمنيه ومالك المجموعه تلقائيا
    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("الاوامر ", callback_data="commandss")] + [InlineKeyboardButton(" حول", callback_data="infos")], [InlineKeyboardButton("تغير اللغه ", callback_data="chlang")], [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ", url=f"https://t.me/{get_bot_information()[1]}?startgroup=dream")]])
    async for photo in c.get_chat_photos(get_bot_information()[1], limit=1):
        await m.message.edit_text(x, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^infos$"))
async def infos(c: Client, m: CallbackQuery):
    res = """
- [ل مـشاعركـم ؟](t.me/ee_re1)
- [𝗔𝗦𝗞 𝗧𝗢 𝗠𝗘](t.me/hhthth)
- [Hasnen | حسنين](t.me/hhthth)

For the first time, Source Zero was launched 
        """
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("« عوده", callback_data="start_back")]])
    await m.message.edit_text(res, reply_markup=keyboard, disable_web_page_preview=True, parse_mode=enums.ParseMode.MARKDOWN)


@Client.on_callback_query(filters.regex("^commandss$"))
async def commandsss(c: Client, m: CallbackQuery):
    await command2(c, m)
