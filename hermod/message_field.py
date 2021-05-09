from typing import Any, Mapping

SQLAColumn = Any
EnumMember = Any


class MessageField:
    typename = None

    def __init__(self, column: SQLAColumn):
        self.column = column

    @property
    def column_name(self) -> str:
        return self.column.name

    def to_string(self, index: int = 1, indent: str = "") -> str:
        return f"{indent}{self.typename} {self.column_name} = {index};"


class MessageInteger(MessageField):
    typename = "int32"


class MessageString(MessageField):
    typename = "string"


class MessageEnum(MessageField):
    @property
    def typename(self) -> str:
        return self.column.type.python_type.__name__

    @property
    def enum_values(self) -> Mapping[str, EnumMember]:
        return self.column.type.enum_class.__members__

    def to_string(self, index: int = 1, indent: str = "") -> str:
        enum = [f"{indent}enum {self.typename}" " {"]

        for enum_name, enum_value in self.enum_values.items():
            enum.append(f"{indent}    {enum_name} = {enum_value.value};")

        enum.append(f"{indent}" "}")
        enum.append(super().to_string(index, indent=indent))

        return "\n".join(enum)
