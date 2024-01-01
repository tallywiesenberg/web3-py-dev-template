from brownie import network

def main() -> None:

    print(network.web3.eth.block_number)