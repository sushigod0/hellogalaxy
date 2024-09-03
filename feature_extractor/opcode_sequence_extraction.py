#opcode sequence extraction from bytecode
from feature_extractor.opcode_dict import opcode_dict
def opcode_sequence_extraction(string):
  # string = row['bytecode']
  string = string.upper()
  # opcode_count = 0
  opcode_list = []
  i = 0
  while i < len(string):
    # print("value of i is {}".format(i) )
    stack = string[i:i+2]
    opcode = opcode_dict()[stack]
    # print(opcode)
    opcode_list.append(opcode)
    # print(opcode)
    if len(opcode) > 4 and opcode[:4] == 'PUSH':
      push = int(opcode[4:])
      # print(push)
      if push > 0:
        i+= (push*2)
    i +=2

  return opcode_list