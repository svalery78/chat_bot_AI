
import httpx
from core.config import OPENROUTER_API_KEY

class OpenRouterClient:
    def __init__(self):
        self.api_key = OPENROUTER_API_KEY
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"

    async def generate_response(self, prompt: str, history: list) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        messages = history + [{"role": "user", "content": prompt}]

        data = {
            "model": "deepseek/deepseek-chat-v3-0324:free", #"openai/gpt-3.5-turbo", # or any other model from OpenRouter
            "messages": messages
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.api_url, headers=headers, json=data)
                response.raise_for_status()
                return response.json()["choices"][0]["message"]["content"]
            except httpx.HTTPStatusError as e:
                return f"Ошибка API: {e}"
            except Exception as e:
                return f"Произошла ошибка: {e}"

