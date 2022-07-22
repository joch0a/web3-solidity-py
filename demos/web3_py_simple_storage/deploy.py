from audioop import add
from os import environ
import os
from solcx import compile_standard, install_solc
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()


# Compile our solidity

install_solc("0.6.0")

compile_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compile_sol, file)

# Get bytecode

bytecode = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# Get ABI

abi = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Ganache connection
# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
# chain_id = 1337
# my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
# private_key = os.getenv("PRIVATE_KEY")  # Add 0x at the beggining

# Rinkeby connection
w3 = Web3(
    Web3.HTTPProvider("https://rinkeby.infura.io/v3/a17b3ebdd1fc49eeb630bd43334e0e94")
)
chain_id = 4
my_address = "0x29F019590900f135B0A6D0F19b65b6379E18e2D6"
private_key = os.getenv("PRIVATE_KEY")  # Add 0x at the beggining

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get latest transaction
nonce = w3.eth.getTransactionCount(my_address)

# Build the contract deploy transaction
# Sign the transaction
# Send the Transaction

transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
        "gasPrice": w3.eth.gas_price,
    }
)

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# Send this send transaction

print("Deploying contract....")

tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Deployed!")

# Contract address & ABI

simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

print(simple_storage.functions.retrieve().call())

print("Updating contract...")

store_transaction = simple_storage.functions.store(15).build_transaction(
    {
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce + 1,
        "gasPrice": w3.eth.gas_price,
    }
)

signed_store_tx = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)
send_store_tx = w3.eth.send_raw_transaction(signed_store_tx.rawTransaction)
send_store_tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)

print("Updated contract!")
print(simple_storage.functions.retrieve().call())
