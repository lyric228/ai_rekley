from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram import Bot, Dispatcher, Router, F
from ai import *


ai = Ai()
router = Router()
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💡 Идеи 💡"), KeyboardButton(text="🔧 Техники 🔧")],
        [KeyboardButton(text="📝 Задания 📝"), KeyboardButton(text="📚 Материалы 📚")],
        [KeyboardButton(text="✨ Вдохновение ✨"), KeyboardButton(text="🤝 Сообщество 🤝")],
        [KeyboardButton(text="🆘 Помощь 🆘")],
    ],
    resize_keyboard=True
)


@router.message(CommandStart())
async def handle_start(msg: Message):
    await msg.answer(f"Привет, {msg.chat.first_name}!\nЯ — Ре-Клей, ваш творческий проводник в мир коллажа. Я помогу вам совершить первые шаги в новом хобби или создать новые, уникальные работы, найти вдохновение.", reply_markup=main_keyboard)
    if messages.get(msg.chat.id) is None:
        messages[msg.chat.id] = []
        ai.add_msg(msg.chat.id, SYSTEM_ROLE, BASE_SYSTEM_PROMPT)
    
@router.message(F.contains("Идеи"))
async def handle_kb_idea(msg: Message):
    pass
    
@router.message(F.contains("Техники"))
async def handle_kb_techniques(msg: Message):
    pass
    
@router.message(F.contains("Задания"))
async def handle_kb_tasks(msg: Message):
    pass
    
@router.message(F.contains("Материалы"))
async def handle_kb_materials(msg: Message):
    pass
    
@router.message(F.contains("Вдохновение"))
async def handle_kb_inspiration(msg: Message):
    pass
    
@router.message(F.contains("Сообщество"))
async def handle_kb_community(msg: Message):
    pass
    
@router.message(F.contains("Помощь"))
async def handle_kb_help(msg: Message):
    pass
    
@router.message(F.text)
async def handle_msg(msg: Message):
    wait_msg = await msg.answer("Думаю...")
    answer = ai.ask(msg.chat.id, msg.text)
    await wait_msg.edit_text(answer)
