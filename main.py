from environment import Environment
from open_ai_client import OpenAiClient


def main() -> None:
    environment = Environment()
    client = OpenAiClient(environment.OPEN_AI_API_KEY)
    response = client.chat_completion("Hello, how are you?")
    print(response.get_top_message())


if __name__ == '__main__':
    main()
