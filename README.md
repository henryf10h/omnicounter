# omnicounter

layerZero example. Omnicounter increases the counter's value in the chain B while being called from chain A.

## setup

This repository assumes you have eth-brownie already installed. To start, just do as follows:

Clone this repository

Install package manager for LayerZero's contracts as: 

    brownie pm install henryf10h/lz-solidity-examples@0.0.1

Compile __omnicounter.sol and ILayerZeroEndpoint.sol__

    brownie compile

Deploy **omnicounter.sol** in rinkeby and mumbai:

    brownie run deploy.py --network rinkeby
    brownie run deploy.py --network polygon-test

Set **trustedRemote()** in both chains by:

    brownie run set_trusted_remote_rinkeby.py --network rinkeby
    brownie run set_trusted_remote_mumbai.py --network polygon-test

Call __increaseCounter()__ in both chains by:

    brownie run increase_counter_rinkeby.py --network rinkeby
    brownie run increase_counter_mumbai.py --network polygon-test
    
## note

In our increase_counter_rinkeby.py and mumbai version, we set msg.value manually. If you want to add the exact amount asked by the endpoint, you may call our **estimate_fees_rinkey.py** and **estimate_fees_mumbai.py** scripts and pass those as msg.value in the increaseCounter() method.

    brownie run estimate_fees_rinkeby.py --network rinkeby 
    brownie run estimate_fees_mumbai.py --network polygon-test
