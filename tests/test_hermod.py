#!/usr/bin/env python
"""Tests for `hermod` package."""
# pylint: disable=redefined-outer-name

import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

from hermod.hermod import model_to_message
from hermod.message import Message

Base = declarative_base()


class TypeEnum(enum.Enum):
    TYPE_A = 0
    TYPE_B = 1
    TYPE_C = 2


class ModelA(Base):
    __tablename__ = "model_a"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(Enum(TypeEnum))
    power = Column(Integer)

    model_b_id = Column(Integer, ForeignKey("model_b.id"))
    model_b = relationship("ModelB", back_populates="model_as")


class ModelB(Base):
    __tablename__ = "model_b"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    model_as = relationship("ModelA", back_populates="model_b")


class TestModelToMessage:
    def test_model_a(self):
        result = model_to_message(ModelA)

        with open("tests/data/model_a.proto", "r") as f:
            expected = f.read()

        assert isinstance(result, Message)
        assert result.to_string() == expected.strip()

    def test_model_b(self):
        result = model_to_message(ModelB)

        with open("tests/data/model_b.proto", "r") as f:
            expected = f.read()

        assert isinstance(result, Message)
        assert result.to_string() == expected.strip()
