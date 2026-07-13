# 💚 Grove Street Bot

Discord-бот в стиле **GTA: San Andreas** на `discord.py` (слэш-команды).

## Команды
| Команда | Что делает |
|---|---|
| `/grove` | Приветствие района |
| `/cj` | Случайная цитата CJ |
| `/bigsmoke` | Легендарный заказ Биг Смоука |
| `/diss` | Задиссить Балласов или чела |
| `/8ball` | Магический шар |
| `/cheat` | Случайный чит-код GTA SA |
| `/wanted` | Уровень розыска |
| `/spawn` | Заспавнить тачку |
| `/weather` | Погода в San Andreas |
| `/ping`, `/help` | Служебные |

## Запуск

Токен **не хранится в коде** — он задаётся в переменной окружения `GROVE_TOKEN`.

### На хостинге
1. Залей репозиторий на GitHub и подключи к хостингу (Railway / Render / Replit и т.п.).
2. В настройках хостинга добавь переменную окружения:
   - `GROVE_TOKEN` = токен твоего бота
3. Хостинг сам поставит зависимости из `requirements.txt` и запустит `python grove_bot.py`
   (для Railway/Render/Heroku есть `Procfile` с worker-процессом).

### Локально
```bash
pip install -r requirements.txt
export GROVE_TOKEN="твой_токен"   # Windows: set GROVE_TOKEN=твой_токен
python grove_bot.py
```

## Где взять токен
[Discord Developer Portal](https://discord.com/developers/applications) → New Application →
Bot → Reset Token. При приглашении бота включи scope `bot` и `applications.commands`.

> ⚠️ Никогда не коммить токен в git. Файл `.env` уже в `.gitignore`.
