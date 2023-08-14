import openai

from open_ai_response import OpenAiResponse


class OpenAiClient:

    def __init__(self, api_key: str):
        self._api_key = api_key
        openai.api_key = api_key

    def chat_completion(
            self,
            prompt: str,
            model="gpt-3.5-turbo",
            temperature=1,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    ) -> OpenAiResponse:
        self._require_api_key()
        messages = [
            {
                "role": 'user',
                "content": prompt
            }
        ]

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
        )

        return OpenAiResponse(**response)

    def get_model_list(self):
        self._require_api_key()
        return openai.Model.list()

    def _require_api_key(self) -> None:
        if self._api_key is None:
            raise ValueError('OpenAI API key is required')
