"""
=====================================================================
  GROVE STREET BOT — Discord-бот в стиле GTA: San Andreas
  Библиотека: discord.py 2.x (слэш-команды)
=====================================================================

Что нужно перед запуском:
  1) Python 3.9+
  2) pip install -U discord.py
  3) Создать приложение и бота на https://discord.com/developers/applications
     - Скопировать TOKEN (вкладка Bot)
     - Включить нужные Intents (для этого бота хватает дефолтных)
  4) Пригласить бота на сервер с правом "applications.commands"
  5) Задать токен в переменных окружения хостинга (переменная GROVE_TOKEN).
     В коде токен НЕ хранится — это безопаснее и он не утечёт в git.

Где задать GROVE_TOKEN на популярных хостингах:
  - Railway:  вкладка Variables
  - Render:   Environment -> Environment Variables
  - Replit:   вкладка Secrets (замочек)
  - VPS:      export GROVE_TOKEN="..."  или файл .env

Локальный запуск для теста:
  Linux/Mac:  export GROVE_TOKEN="ваш_токен"  &&  python grove_bot.py
  Windows:    set GROVE_TOKEN=ваш_токен       &&  python grove_bot.py
=====================================================================
"""

import os
import random

import discord
from discord import app_commands
from discord.ext import commands

# ----------------------------- НАСТРОЙКИ -----------------------------
# Токен НЕ хранится в коде. Он задаётся в переменных окружения хостинга
# (переменная GROVE_TOKEN). Так безопаснее и токен не утечёт в git.
TOKEN = os.getenv("GROVE_TOKEN")

# Фирменный зелёный цвет Grove Street для эмбедов
GROVE_GREEN = 0x2E8B3D

# --------------------------- ИНИЦИАЛИЗАЦИЯ ---------------------------
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


# -------------------------- БАЗЫ ФРАЗ/ДАННЫХ -------------------------
CJ_QUOTES = [
    "Ah shit, here we go again.",
    "All we had to do was follow the damn train, CJ!",
    "Grove Street. Home. At least it was before I fucked everything up.",
    "I'm getting too old for this shit.",
    "Ballas gonna regret the day they stepped on Grove turf.",
]

SMOKE_ORDER = [
    "I'll have two number 9s, a number 9 large,",
    "a number 6 with extra dip, a number 7,",
    "two number 45s, one with cheese,",
    "and a large soda. 🥤",
]

BALLAS_DISS = [
    "Балласы носят фиолетовое, потому что даже цвет выбрать нормально не смогли. 💜🤡",
    "Грин Сабер видел твою тачку — сказал, что даже угонять стыдно.",
    "На Грув Стрит ты бы и минуты не простоял, соня.",
    "Тебя даже Биг Смоук не взял бы за напарника. А это уже приговор.",
    "Райдер, конечно, крыса, но даже он лучше тебя.",
]

EIGHTBALL = [
    "Grove Street, home — да, однозначно.",
    "Спроси у Свита, он знает.",
    "Балласы бы не одобрили. Значит — да.",
    "Не сегодня, гомик.",
    "Follow the damn train — то есть нет.",
    "Всё чётко, погнали.",
    "Ah shit... лучше не рискуй.",
]

CHEATS = [
    ("HESOYAM", "Полное здоровье, броня и $250 000"),
    ("BAGUVIX", "Бесконечное здоровье"),
    ("CVWKXAM", "Бесконечный кислород"),
    ("AEZAKMI", "Розыск не растёт"),
    ("LXGIWYL", "Набор оружия (уровень 1)"),
    ("AIYPWZQP", "Джетпак"),
    ("OSRBLHH", "Уровень розыска +2 звезды"),
    ("ASBHGRB", "Спавн танка Rhino"),
    ("YECGAA", "Дать джетпак / полёт"),
    ("CIKGCGX", "Все девушки хотят CJ 😎"),
]

CARS = [
    "Greenwood 🚗", "Sabre 🏎️", "Voodoo 🚙", "BMX 🚲",
    "Rhino (танк) 🪖", "Hydra ✈️", "NRG-500 🏍️", "Sultan 🚗",
]

WEATHERS = [
    "Los Santos — солнце и смог ☀️",
    "San Fierro — туман, ни хрена не видно 🌫️",
    "Las Venturas — жара пустыни 🏜️",
    "Гроза над Гроув Стрит ⛈️",
]


# ----------------------------- СОБЫТИЯ -----------------------------
@bot.event
async def on_ready():
    """Срабатывает при запуске: синхронизируем слэш-команды."""
    try:
        synced = await bot.tree.sync()
        print(f"✅ Залогинились как {bot.user} | команд синхронизировано: {len(synced)}")
    except Exception as e:
        print(f"⚠️ Ошибка синхронизации команд: {e}")

    await bot.change_presence(
        activity=discord.Game(name="Grove Street, home 🏠💚")
    )


# ---------------------------- КОМАНДЫ ------------------------------
@bot.tree.command(name="grove", description="Приветствие в духе Grove Street")
async def grove(interaction: discord.Interaction):
    embed = discord.Embed(
        title="GROVE STREET — HOME 🏠",
        description=f"Добро пожаловать на район, {interaction.user.mention}! "
                    f"Зелёный — цвет семьи. 💚",
        color=GROVE_GREEN,
    )
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="cj", description="Случайная цитата Карла Джонсона")
async def cj(interaction: discord.Interaction):
    quote = random.choice(CJ_QUOTES)
    embed = discord.Embed(title="CJ 🎤", description=quote, color=GROVE_GREEN)
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="bigsmoke", description="Легендарный заказ Биг Смоука")
async def bigsmoke(interaction: discord.Interaction):
    order = "\n".join(SMOKE_ORDER)
    embed = discord.Embed(
        title="Заказ Биг Смоука 🍔",
        description=f"{order}\n\n*«You know what you doin'.»*",
        color=0xE0A800,
    )
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="diss", description="Задиссить Балласов (или обидчика)")
@app_commands.describe(target="Кого дёрнуть (необязательно)")
async def diss(interaction: discord.Interaction, target: discord.Member = None):
    line = random.choice(BALLAS_DISS)
    prefix = f"{target.mention}, " if target else ""
    await interaction.response.send_message(f"{prefix}{line}")


@bot.tree.command(name="8ball", description="Магический шар Grove Street")
@app_commands.describe(question="Твой вопрос")
async def eightball(interaction: discord.Interaction, question: str):
    answer = random.choice(EIGHTBALL)
    embed = discord.Embed(title="🎱 Магический шар", color=GROVE_GREEN)
    embed.add_field(name="Вопрос", value=question, inline=False)
    embed.add_field(name="Ответ", value=answer, inline=False)
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="cheat", description="Случайный чит-код из GTA San Andreas")
async def cheat(interaction: discord.Interaction):
    code, effect = random.choice(CHEATS)
    embed = discord.Embed(title="🎮 Чит-код", color=GROVE_GREEN)
    embed.add_field(name="Код", value=f"`{code}`", inline=True)
    embed.add_field(name="Эффект", value=effect, inline=False)
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="wanted", description="Проверить уровень розыска")
@app_commands.describe(user="Кого проверяем (необязательно)")
async def wanted(interaction: discord.Interaction, user: discord.Member = None):
    stars = random.randint(0, 6)
    target = user or interaction.user
    if stars == 0:
        text = f"{target.mention} чист — копы даже не в курсе. 😎"
    else:
        text = f"{target.mention} в розыске: {'⭐' * stars}\nЛучше валить с района!"
    await interaction.response.send_message(text)


@bot.tree.command(name="spawn", description="Заспавнить случайную тачку/транспорт")
async def spawn(interaction: discord.Interaction):
    car = random.choice(CARS)
    await interaction.response.send_message(f"🚗 На район подкатил: **{car}**")


@bot.tree.command(name="weather", description="Погода в Сан-Андреасе")
async def weather(interaction: discord.Interaction):
    w = random.choice(WEATHERS)
    await interaction.response.send_message(f"🌤️ {w}")


@bot.tree.command(name="ping", description="Проверить, жив ли бот")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"🏓 Понг! Задержка: `{latency}ms`")


@bot.tree.command(name="help", description="Список команд бота")
async def help_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="GROVE STREET BOT — команды 💚",
        color=GROVE_GREEN,
    )
    cmds = {
        "/grove": "Приветствие района",
        "/cj": "Цитата CJ",
        "/bigsmoke": "Заказ Биг Смоука",
        "/diss": "Задиссить кого-нибудь",
        "/8ball": "Магический шар",
        "/cheat": "Случайный чит-код GTA SA",
        "/wanted": "Уровень розыска",
        "/spawn": "Заспавнить тачку",
        "/weather": "Погода в San Andreas",
        "/ping": "Проверить бота",
    }
    for name, desc in cmds.items():
        embed.add_field(name=name, value=desc, inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=True)


# ------------------------------ ЗАПУСК ------------------------------
if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError(
            "❌ Не задан токен! Добавь переменную окружения GROVE_TOKEN "
            "в настройках хостинга (Variables / Environment / Secrets)."
        )
    bot.run(TOKEN)
