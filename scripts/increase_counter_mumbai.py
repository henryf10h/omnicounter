from brownie import network, accounts, config, OmniCounter, Contract, interface
from abi import ABI 

#Increase the counter
def main():
    account = accounts.add(config['wallets']['from_key'])
    net = network.show_active()
    print(net)
    omnicounter = Contract.from_abi("OmniCounter", config['networks'][net]['srcAddress'], ABI)
    #endpoint = interface.ILayerZeroEndpoint(config['networks'][net]['endpoint'])
    #estimate_fees = endpoint.estimateFees(config['networks']['rinkeby']['chainId'],config['networks']['rinkeby']['srcAddress'],"0x",False,"0x00010000000000000000000000000000000000000000000000000000000000030d40",{'from':account})
#increment counter. If in rinkeby, set destId of polygon.
    omnicounter.incrementCounter(config['networks']['rinkeby']['chainId'],{'from': account, 'amount' : 100000000000000000,'gas_limit':210000,"allow_revert":True })

#https://eth-brownie.readthedocs.io/en/stable/core-gas.html