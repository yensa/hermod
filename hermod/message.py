from typing import List

from hermod.message_field import MessageField


class Message:
    def __init__(self, name: str, fields: List[MessageField]):
        self.name = name
        self.fields = fields

    def to_string(self) -> str:
        message = [f"message {self.name}" " {"]
        for i, field in enumerate(self.fields):
            message.append(field.to_string(i + 1, indent="    "))
        message.append("}")

        return "\n".join(message)
