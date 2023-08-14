from dataclasses import dataclass
from typing import List


@dataclass
class Usage:
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


@dataclass
class Message:
    role: str
    content: str


@dataclass
class UserMessage:
    message: Message
    account_id: str


@dataclass
class Choice:
    message: Message
    index: int
    finish_reason: str


@dataclass
class OpenAiResponse:
    id: str
    object: str
    created: int
    model: str
    usage: Usage
    choices: List[Choice]

    def get_top_message(self) -> Message:
        return self.__get_top_choice().message

    def get_tokens(self) -> int:
        return self.usage.total_tokens

    def __get_top_choice(self) -> Choice:
        return self.choices[0]
