#get the list of opcodes
import pandas as pd 
def opcode_dict():
    opcode = pd.read_csv('feature_extractor/data/Opcode List.csv')
    opcode_dict = opcode.set_index('uint8')['Mnemonic'].to_dict()
    return opcode_dict