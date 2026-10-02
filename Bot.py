import discord
from discord import app_commands
from discord.ext import commands, tasks
import os
import random

TOKEN = os.getenv("MTU1NTUxNDk5Mjg3NzM3MTUxMw.GZ0I1d.i0i8suDJ-wRrSFSXAEFtEOzmB2DPD3EMerNl0o")

# ============ القائمة البيضاء ============
ALLOWED_USERS = [
    1395048157984985120,
    1464246205646241824,
    # ⚠️ ضيف ID تبعك هنا (مهم جداً)
]

# ============ الرسائل اللي تنزل كل فترة ============
MESSAGES = [
    "يلعن امك يا ابن القحبه ",
   " كسمك بزبي تنقز يولد الحرام ",
    "يلعن ابوك وامك يبن القحبه يخو الشرموطه",
    "اخضع لا نياك امك يبن القحبه كسمك كسختك",
  "انيك امك يبن القحبه يخو الشرموطه يلعن امك كسمك",
  "كسمك بزبي تنقز كسختك تتمحن",
  "امك قحبه و زانيه تعرض للكل",
  "امك تخضع اول ما تشوف زبي يبن القحبه كسمك ",
  "انيك الي يعز عليك يبن القحبه يولد زبي",
  "انا ابوك يولد القحبه نكت امك وجبتك كسمك ",
  " يلعن امك واختك وابوك الي بس يشوفون زبي يذوبون",
  " يلعن امك يبن القحبه يخو الشرموطه المصريه ",
  " انيك امك يولد الحرام ",
  " امك تعرض بكسها للكل يبن القحبه ",
  "امك عايبه امك شرموطه يبن القحبه ",
  " امك فاجره امك خاضغه لا زبي ",
  " امك تتمحن احسن من مايا خليفه يبن القواده ",
  " كسمك بزبي يقحبه يمصاص زبي يبن الزواني المخضوعه ",
  " انيك امك ",
  "انيك كسختك",
  " انيك ابوك الديوث الي يخلي امك تتناك عشان فلوس  ",
  " انيك عارك انت واخوياك ",
  " على زبي انت وامك واختك واهلك ",
  " اخضع لي يقحبه ",
  " بس تشوف زبي يقحبه يزاني يمفتوح تذوب ",
  " يلعن امك يا ابن زبي كسمك ",
  " صدر امك كبير يلبيه",
  "امك قحبه يلبيه",
  "امك فاجره يلبيه",
  " امك مصاصه زباب يلبيه",
  " يا ابن القحبه خليت امك 9 اشهر ما ينزل منها دم يبن القحبه",
  " امك صارت تتمحن بقوه يبن القحبه ",
  " بس كنت انت حيوان منوي كنت انيك امك واخليها تهتز ووتتمحن بقوه وتقول خلاص يكفي دادي ",
  " نياك امك هنا يبن القحبه ",
  " اصمل وتعال مكالمه اوريك شلون نكت امك بزبي الكبير ",
  " اصمل ",
  "اصمل ",
  "اصمل يولد الحرام كسمككككك",
  "تعال لا اخليك تتمحن فويس من جمال زبي يبن القحبه",
  " انيك امك يبن الحرام وانيكها قدام ابوك عشان اخليها عبره لك يبن الديوث",
  " اشتري امك بدينار ",
  "ابطح امك يبن القحبه يخو الخاضعه ",
  " اختك شرموطه تتناك مني يبن القحبه",
  " اهلك بس يشوفوني انيك امك يضلهم يستنون عشان اقذف المنوي عليهم يبن الرخيصه",
  " امك تحب تعض زبي يبن القحبه ",
  " امك تتوحش على زبي وتذوب بس تشوفه ",
  " امك بس تمسك زبي تصير تحارب باختك وابوك عشان لا ياخذونه وتضل تمص هي ",
  " افحل امك يبن القحبه",
  " قدامك نياك امك ",
  " قائد القنبله المنويه ",
  " الله يلعن امك يبن القحبه",
  " يا مزغوب يا مفتوح مص لي ",
  " امك قحبه وزانيه يأخذونها ملهى ليلي رقاصه وينيكوها على الدور ",
    # ✏️ عدّل هذي واضيف اللي بدك ياه
]

# ============ الردود المخصصة ============
CUSTOM_REPLIES = {
    "كسمك على كسم نحر": "كسمك انت يبن القحبه يخو الشرموطه لا تسب نياكين امك عشان لا انيك امك",
    "تعال اخضع لي انت ونحر": "يلعن امك يبن القحبه تعال اخضع لا نياكين  امك لا تسوي فحل على نياكين امك",
    "N7R IS COM": "WELCOME F7L",
    "JHNM IS COM": "WELCOME F7L ",
}

CHANNEL_ID = None
INTERVAL_SECONDS = 0.4  # كل  0.4

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


def is_allowed(user_id: int) -> bool:
    return user_id in ALLOWED_USERS


async def check(interaction: discord.Interaction) -> bool:
    if not is_allowed(interaction.user.id):
        await interaction.response.send_message(
            "❌ ما عندك صلاحية لاستخدام هذا البوت", ephemeral=True
        )
        return False
    return True


# ============ الرد التلقائي على الكلمات ============
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if not is_allowed(message.author.id):
        return
    content = message.content.strip()
    if content in CUSTOM_REPLIES:
        await message.channel.send(CUSTOM_REPLIES[content])
    await bot.process_commands(message)


# ============ المهمة الدورية (الرسائل) ============
@tasks.loop(seconds=INTERVAL_SECONDS)
async def send_message():
    if CHANNEL_ID is None:
        return
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        try:
            await channel.send(random.choice(MESSAGES))
        except Exception as e:
            print(f"خطأ: {e}")


@send_message.before_loop
async def before_send():
    await bot.wait_until_ready()


@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
        print("✅ تم تسجيل الأوامر")
    except Exception as e:
        print(f"خطأ: {e}")
    if not send_message.is_running():
        send_message.start()
    print(f"✅ البوت شغال: {bot.user}")


# ============================================
# ============== الأوامر ======================
# ============================================

# ---------- /قناة ----------
@bot.tree.command(name="قناة", description="حدد القناة اللي تنزل فيها الرسائل")
async def set_channel(interaction: discord.Interaction):
    if not await check(interaction):
        return
    global CHANNEL_ID
    CHANNEL_ID = interaction.channel.id
    await interaction.response.send_message(
        f"✅ القناة: {interaction.channel.mention}\n"
        f"⏱️ كل {INTERVAL_SECONDS} ثانية",
        ephemeral=True
    )


# ---------- /ارسل ----------
@bot.tree.command(name="ارسل", description="يبعت رسالة عشوائية الآن")
async def send_now(interaction: discord.Interaction):
    if not await check(interaction):
        return
    await interaction.response.send_message(random.choice(MESSAGES))


# ---------- /إضافة_رسالة ----------
@bot.tree.command(name="إضافة_رسالة", description="أضف رسالة للقائمة")
@app_commands.describe(نص="النص اللي بدك تضيفه")
async def add_message(interaction: discord.Interaction, نص: str):
    if not await check(interaction):
        return
    MESSAGES.append(نص)
    await interaction.response.send_message("✅ تمت الإضافة", ephemeral=True)


# ---------- /الرسائل ----------
@bot.tree.command(name="الرسائل", description="اعرض كل الرسائل")
async def list_messages(interaction: discord.Interaction):
    if not await check(interaction):
        return
    text = "\n".join(f"{i+1}. {m}" for i, m in enumerate(MESSAGES))
    await interaction.response.send_message(
        f"📋 **الرسائل:**\n{text}", ephemeral=True
    )


# ---------- /المدة ----------
@bot.tree.command(name="المدة", description="غيّر المدة بالثواني (الحد الأدنى 60)")
@app_commands.describe(ثواني="عدد الثواني")
async def set_interval(interaction: discord.Interaction, ثواني: int):
    if not await check(interaction):
        return
    global INTERVAL_SECONDS
    if ثواني < 60:
        await interaction.response.send_message(
            "❌ الحد الأدنى 60 ثانية عشان ما ينحظر البوت", ephemeral=True
        )
        return
    INTERVAL_SECONDS = ثواني
    send_message.change_interval(seconds=ثواني)
    await interaction.response.send_message(
        f"✅ صار كل {ثواني} ثانية", ephemeral=True
    )


# ---------- /إضافة_رد ----------
@bot.tree.command(name="إضافة_رد", description="أضف كلمة ورد تلقائي")
@app_commands.describe(كلمة="الكلمة", رد="الرد")
async def add_reply(interaction: discord.Interaction, كلمة: str, رد: str):
    if not await check(interaction):
        return
    CUSTOM_REPLIES[كلمة] = رد
    await interaction.response.send_message(
        f"✅ `{كلمة}` ← `{رد}`", ephemeral=True
    )


# ---------- /إضافة_مستخدم ----------
@bot.tree.command(name="إضافة_مستخدم", description="أضف شخص للقائمة البيضاء")
@app_commands.describe(ايدي="ID الشخص")
async def add_user(interaction: discord.Interaction, ايدي: str):
    if not await check(interaction):
        return
    try:
        uid = int(ايدي)
        if uid in ALLOWED_USERS:
            await interaction.response.send_message("⚠️ موجود أصلاً", ephemeral=True)
            return
        ALLOWED_USERS.append(uid)
        await interaction.response.send_message(f"✅ تم إضافة `{uid}`", ephemeral=True)
    except ValueError:
        await interaction.response.send_message("❌ ID غلط", ephemeral=True)


# ---------- /المسموحين ----------
@bot.tree.command(name="المسموحين", description="اعرض المسموح لهم")
async def list_users(interaction: discord.Interaction):
    if not await check(interaction):
        return
    users = "\n".join(f"• `{uid}`" for uid in ALLOWED_USERS)
    await interaction.response.send_message(
        f"👥 **المسموح لهم:**\n{users}", ephemeral=True
    )


# ---------- /منشن (للأشخاص بالقائمة فقط) ----------
@bot.tree.command(name="منشن", description="منشن للأشخاص اللي بالقائمة")
@app_commands.describe(نص="نص اختياري مع المنشن")
async def mention_all(interaction: discord.Interaction, نص: str = None):
    if not await check(interaction):
        return
    mentions = " ".join(f"<@{uid}>" for uid in ALLOWED_USERS)
    if نص:
        await interaction.response.send_message(f"{mentions}\n{نص}")
    else:
        await interaction.response.send_message(mentions)


# ---------- /منشن_شخص ----------
@bot.tree.command(name="منشن_شخص", description="منشن لشخص معين")
@app_commands.describe(شخص="الشخص اللي بدك تعمله منشن")
async def mention_one(interaction: discord.Interaction, شخص: discord.Member):
    if not await check(interaction):
        return
    await interaction.response.send_message(شخص.mention)


# ============ التشغيل ============
bot.run(TOKEN)
