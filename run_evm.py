
import binascii

from simple_evm import VM

code_hex = '60806040526004361061006c5763ffffffff7c010000000000000000000000000000000000000000000000000000000060003504166312065fe08114610071578063455259cb14610098578063858af522146100ad57806395dd7a55146100c2578063afc874d2146100d9575b600080fd5b34801561007d57600080fd5b506100866100ee565b60408051918252519081900360200190f35b3480156100a457600080fd5b506100866100f3565b3480156100b957600080fd5b506100866100f7565b3480156100ce57600080fd5b506100d76100fc565b005b3480156100e557600080fd5b506100d7610139565b333190565b3a90565b602a90565b6000805b7f80000000000000000000000000000000000000000000000000000000000000008110156101355760003b9150600101610100565b5050565b604080517f08c379a000000000000000000000000000000000000000000000000000000000815260206004820152600e60248201527f616c776179732072657665727473000000000000000000000000000000000000604482015290519081900360640190fd00a165627a7a72305820645df686b4a16d5a69fc6d841fc9ad700528c14b35ca5629e11b154a9d3dff890029'
code_bytes = binascii.unhexlify(code_hex)
msg_bytes = b'\x12\x06\x5f\xe0'

m = VM(code_bytes, msg_bytes)
pc = None
while pc != m.pc:
    pc = m.pc
    m.step()
