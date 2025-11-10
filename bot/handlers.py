import logging
from aiogram import types
from aiogram.filters import CommandStart
from aiogram import Router
from services.openrouter_client import OpenRouterClient
from services.history_manager import HistoryManager

router = Router()
openrouter_client = OpenRouterClient()
history_manager = HistoryManager()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Привет! Я твой AI ассистент. Задай мне вопрос.")

@router.message()
async def text_handler(message: types.Message):
    user_id = message.from_user.id
    user_message = message.text

    chat_history = history_manager.get_history(user_id)
    
    try:
        response = await openrouter_client.generate_response(user_message, chat_history)
        await message.answer(response)
        history_manager.add_to_history(user_id, user_message, response)
    except Exception as e:
        logging.error(f"Error processing message for user {user_id}: {e}")
        await message.answer("Извините, произошла ошибка при обработке вашего запроса. Пожалуйста, попробуйте еще раз.")
