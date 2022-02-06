from op_data import OpCodeData

type = "unprefixed"
test_opcode = "0x06"
op_parser = OpCodeData(type)
print(op_parser[test_opcode])