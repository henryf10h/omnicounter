from brownie import network, accounts, config, OmniCounter

# we need end point address

"""
  rinkeby: 
    chainId: 10001
    endpoint: 0x79a63d6d8BBD5c6dfc774dA79bCcD948EAcb53FA

  polygon-test:
    chainId: 10009
    endpoint: 0xf69186dfBa60DdB133E91E9A4B5673624293d8F8

"""

def main():
    net = network.show_active()
    print(net)
    account1 = accounts.add(config['wallets']['from_key'])
    return OmniCounter.deploy(config['networks'][net]['endpoint'],{'from': account1})