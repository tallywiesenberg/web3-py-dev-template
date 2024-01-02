"""Test block number easy script"""

from scripts.block_number import get_block_number

def test_get_block_number():
    """Test get block number"""
    assert get_block_number() > 0