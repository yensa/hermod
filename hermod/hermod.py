import logging
from typing import Any

import sqlalchemy
from sqlalchemy.inspection import inspect

from hermod.message import Message
from hermod.message_field import MessageEnum, MessageInteger, MessageString
from hermod.message_relation import MessageRelation

logger = logging.getLogger(__name__)

SQLA_TO_MESSAGE = {
    sqlalchemy.Integer: MessageInteger,
    sqlalchemy.String: MessageString,
    sqlalchemy.Enum: MessageEnum,
}


def model_to_message(model: Any) -> Message:
    info = inspect(model)

    message_name = model.__name__
    fields = []

    for column in info.columns:
        if column.foreign_keys:
            # Avoid adding the foreign keys in the message
            continue

        m_field = SQLA_TO_MESSAGE.get(column.type.__class__)

        if m_field:
            fields.append(m_field(column))

        logger.warning(f"Could not generate a field for {column}")

    for relation in info.relationships:
        fields.append(MessageRelation(relation))

    return Message(message_name, fields)
