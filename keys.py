from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.core import x

SelectParams('testnet')

######################################################################
#
# TODO: Fill this in with address secret key for BTC testnet3
#
# Create address in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

# Only to be imported by alice.py
# Alice should have coins!!
alice_secret_key_BTC = CBitcoinSecret(
    'cRPvmToaY7ovbFDmsULLWfnTFF9X9GyHZ3tfcSbFDwtcskb77BMo')

# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret(
    'cP1QCDjQ7HuxPMKHYvyVrGYLCTRRvHpnWcR2rAEy63gdBC3Z1VPt')

######################################################################
#
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=$YOURTOKEN
#
# Send coins with
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=<YOURTOKEN>

# curl -d '{"address": "C1Hj6QcscPy4CqHNLje6CnRM3sKhiZ1q7b", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=$YOURTOKEN

# Only to be imported by alice.py
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('7be8d4f70b1659e49a24ccabefe56641777769f164808d72057173ffa469b4fa'))

# Only to be imported by bob.py
# Bob should have coins!!
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('5891578bf2d34207990d947b959d84763bfb7b242c254301da3f8ab612088186'))

# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)

alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
