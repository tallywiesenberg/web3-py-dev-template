"""
Get the current block number
"""
from telliot_core.apps.telliot_config import TelliotConfig

def get_block_number() -> None:

    cfg = TelliotConfig()

    return cfg.get_endpoint().web3.eth.get_block_number()
