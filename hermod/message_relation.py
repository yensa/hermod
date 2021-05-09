from hermod.message_field import MessageField


class MessageRelation(MessageField):
    @property
    def typename(self) -> str:
        return self.column.entity.class_.__name__

    @property
    def column_name(self) -> str:
        return self.column.key

    def to_string(self, index: int, indent: str = "") -> str:
        is_repeated = self.column.uselist

        super_ = super().to_string(index=index, indent="")

        return indent + ("repeated " + super_ if is_repeated else super_)
