from dataclasses import dataclass
from typing import Literal, Union
from utils import load_json_file

@dataclass
class Operand:
    immediate: bool
    name: str
    bytes: int
    value: Union(int, None)
    adjust: Union(Literal["+", "-"], None)

    def create(cls, value):
        return Operand(immediate=cls.immediate,
                       name=cls.name,
                       bytes=cls.bytes,
                       value=value,
                       adjust=cls.adjust)

@dataclass
class Instruction:

    opcode: int
    immediate: bool
    operands: list[Operand]
    cycles: list[int]
    bytes: int
    mnemonic: str
    comment: str = ""

    def create(cls, operands):
        return Instruction(opcode=cls.opcode,
                           immediate=cls.immediate,
                           operands=operands,
                           cycles=cls.cycles,
                           bytes=cls.bytes,
                           mnemonic=cls.mnemonic)

class OpDataParser:
    __op_data = load_json_file()

    def __init__(self, type: str):
        self.type = type
    
    def __getitem__(self, key):
        all_data = load_json_file("Opcodes.json")
        data = all_data[]