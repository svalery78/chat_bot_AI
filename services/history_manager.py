
class HistoryManager:
    def __init__(self):
        self.chat_histories = {}  # Stores history for each user_id

    def get_history(self, user_id: int) -> list:
        return self.chat_histories.get(user_id, [])

    def add_to_history(self, user_id: int, user_message: str, bot_message: str):
        if user_id not in self.chat_histories:
            self.chat_histories[user_id] = []
        
        # Add user message
        self.chat_histories[user_id].append({"role": "user", "content": user_message})
        # Add bot message
        self.chat_histories[user_id].append({"role": "assistant", "content": bot_message})

        # Keep history to a reasonable length (e.g., last 10 messages)
        # This is a simple in-memory implementation, for production, consider a proper DB
        max_history_length = 10
        if len(self.chat_histories[user_id]) > max_history_length:
            self.chat_histories[user_id] = self.chat_histories[user_id][-max_history_length:]
