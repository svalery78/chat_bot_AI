# AI Telegram Bot with OpenRouter

This project implements a Telegram bot that leverages the OpenRouter API to interact with various large language models (LLMs) and generate responses to user queries. The bot is built using Python with `aiogram` for Telegram interaction and `httpx` for API calls.

## Features

*   **Telegram Integration:** Seamless interaction with users via Telegram.
*   **OpenRouter API:** Utilizes OpenRouter for access to multiple LLMs.
*   **Conversation Context:** Remembers previous messages in a dialogue to provide more coherent responses.
*   **Error Handling:** Basic error handling for API calls and message processing.

## Project Structure

The project follows a modular structure:

```
/ai_telegram_bot
├── .env                      # Environment variables (API_KEY, BOT_TOKEN)
├── requirements.txt          # Python dependencies
├── main.py                   # Entry point for the bot
├── /core
│   └── config.py             # Configuration loading
├── /bot
│   └── handlers.py           # Telegram message handlers
├── /services
│   ├── openrouter_client.py  # OpenRouter API client
│   └── history_manager.py    # Manages chat history/context
└── /storage                  # (Optional) For database integration
```

## Setup and Installation

Follow these steps to set up and run the bot:

### 1. Clone the Repository

```bash
git clone <repository_url>
cd ai_telegram_bot
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of the project and add your Telegram Bot Token and OpenRouter API Key:

```
TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
OPENROUTER_API_KEY="YOUR_OPENROUTER_API_KEY"
```

*   **`TELEGRAM_BOT_TOKEN`**: Obtain this from BotFather on Telegram.
*   **`OPENROUTER_API_KEY`**: Get this from the OpenRouter website after signing up.

### 5. Run the Bot

Once everything is set up, you can run the bot:

```bash
python main.py
```

The bot will start polling for messages. You can then interact with it on Telegram.

## Usage

*   Send `/start` to the bot to receive a welcome message.
*   Send any text message to the bot, and it will use the OpenRouter API to generate a response, remembering the conversation context.

## Contributing

(Optional) Information on how others can contribute to your project.

## License

(Optional) Information about the project's license.
