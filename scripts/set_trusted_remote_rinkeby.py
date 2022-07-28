from brownie import network, accounts, config, OmniCounter, Contract
from abi import ABI 

def main():
    account = accounts.add(config['wallets']['from_key'])
    net = network.show_active()
    print(net)
    # https://eth-brownie.readthedocs.io/en/stable/core-contracts.html
    omnicounter = Contract.from_abi("OmniCounter", config['networks'][net]['srcAddress'], ABI)
# set
    omnicounter.setTrustedRemote(config['networks']['polygon-test']['chainId'],config['networks']['polygon-test']['srcAddress'],{'from': account })