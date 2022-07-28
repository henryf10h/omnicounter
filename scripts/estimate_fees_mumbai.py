from brownie import accounts, config, network, Contract, interface
from abi import ABI 

# send link
# interface.LinkTokenInterface(link_token)

# https://layerzero.gitbook.io/docs/guides/code-examples/estimating-message-fees
# https://layerzero.gitbook.io/docs/guides/advanced/relayer-adapter-parameters

def main():
    net = network.show_active()
    account = accounts.add(config['wallets']['from_key'])
    omnicounter = Contract.from_abi("OmniCounter", config['networks'][net]['srcAddress'], ABI)
    print(omnicounter)
    endpoint = interface.ILayerZeroEndpoint(config['networks'][net]['endpoint'])
    estimate_fees=endpoint.estimateFees(config['networks']['rinkeby']['chainId'],config['networks']['rinkeby']['srcAddress'],"0x",False,"0x00010000000000000000000000000000000000000000000000000000000000030d40",{'from':account})
    print(estimate_fees)