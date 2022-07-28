ABI = [       
    {   
        'inputs': [
            {
                'internalType': "address",
                'name': "_lzEndpoint",
                'type': "address"     
            }
        ],
        'name': "constructor",
        'stateMutability': "nonpayable",
        'type': "constructor"
    },
    {
        'anonymous': False,
        'inputs': [
            {
                'indexed': False,
                'internalType': "uint16",
                'name': "_srcChainId",
                'type': "uint16"
            },
            {
                'indexed': False,
                'internalType': "bytes",
                'name': "_srcAddress",
                'type': "bytes"
            },
            {
                'indexed': False,
                'internalType': "uint64",
                'name': "_nonce",
                'type': "uint64"
            },
            {
                'indexed': False,
                'internalType': "bytes",
                'name': "_payload",
                'type': "bytes"
            }
        ],
        'name': "MessageFailed",
        'type': "event"
    },
    {
        'anonymous': False,
        'inputs': [
            {
                'indexed': True,
                'internalType': "address",
                'name': "previousOwner",
                'type': "address"
            },
            {
                'indexed': True,
                'internalType': "address",
                'name': "newOwner",
                'type': "address"
            }
        ],
        'name': "OwnershipTransferred",
        'type': "event"
    },
    {
        'anonymous': False,
        'inputs': [
            {
                'indexed': False,
                'internalType': "uint16",
                'name': "_srcChainId",
                'type': "uint16"
            },
            {
                'indexed': False,
                'internalType': "bytes",
                'name': "_srcAddress",
                'type': "bytes"
            }
        ],
        'name': "SetTrustedRemote",
        'type': "event"
    },
    {
        'inputs': [],
        'name': "counter",
        'outputs': [
            {
                'internalType': "uint256",
                'name': "",
                'type': "uint256"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint16",
                'name': "",
                'type': "uint16"
            },
            {
                'internalType': "bytes",
                'name': "",
                'type': "bytes"
            },
            {
                'internalType': "uint64",
                'name': "",
                'type': "uint64"
            }
        ],
        'name': "failedMessages",
        'outputs': [
            {
                'internalType': "bytes32",
                'name': "",
                'type': "bytes32"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint16",
                'name': "_srcChainId",
                'type': "uint16"
            },
            {
                'internalType': "bytes",
                'name': "_srcAddress",
                'type': "bytes"
            }
        ],
        'name': "forceResumeReceive",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint16",
                'name': "_version",
                'type': "uint16"
            },
            {
                'internalType': "uint16",
                'name': "_chainId",
                'type': "uint16"
            },
            {
                'internalType': "address",
                'name': "",
                'type': "address"
            },
            {
                'internalType': "uint256",
                'name': "_configType",
                'type': "uint256"
            }
        ],
        'name': "getConfig",
        'outputs': [
            {
                'internalType': "bytes",
                'name': "",
                'type': "bytes"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint16",
                'name': "_dstChainId",
                'type': "uint16"
            }
        ],
        'name': "incrementCounter",
        'outputs': [],
        'stateMutability': "payable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint16",
                'name': "_srcChainId",
                'type': "uint16"
            },
            {
                'internalType': "bytes",
                'name': "_srcAddress",
                'type': "bytes"
            }
        ],
        'name': "isTrustedRemote",
        'outputs': [
            {
                'internalType': "bool",
                'name': "",
                'type': "bool"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "lzEndpoint",
        'outputs': [
            {
                'internalType': "contract ILayerZeroEndpoint",
                'name': "",
                'type': "address"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint16",
                'name': "_srcChainId",
                'type': "uint16"
            },
            {
                'internalType': "bytes",
                'name': "_srcAddress",
                'type': "bytes"
            },
            {
                'internalType': "uint64",
                'name': "_nonce",
                'type': "uint64"
            },
            {
                'internalType': "bytes",
                'name': "_payload",
                'type': "bytes"
            }
        ],
        'name': "lzReceive",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint16",
                'name': "_srcChainId",
                'type': "uint16"
            },
            {
                'internalType': "bytes",
                'name': "_srcAddress",
                'type': "bytes"
            },
            {
                'internalType': "uint64",
                'name': "_nonce",
                'type': "uint64"
            },
            {
                'internalType': "bytes",
                'name': "_payload",
                'type': "bytes"
            }
        ],
        'name': "nonblockingLzReceive",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "owner",
        'outputs': [
            {
                'internalType': "address",
                'name': "",
                'type': "address"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "renounceOwnership",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint16",
                'name': "_srcChainId",
                'type': "uint16"
            },
            {
                'internalType': "bytes",
                'name': "_srcAddress",
                'type': "bytes"
            },
            {
                'internalType': "uint64",
                'name': "_nonce",
                'type': "uint64"
            },
            {
                'internalType': "bytes",
                'name': "_payload",
                'type': "bytes"
            }
        ],
        'name': "retryMessage",
        'outputs': [],
        'stateMutability': "payable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint16",
                'name': "_version",
                'type': "uint16"
            },
            {
                'internalType': "uint16",
                'name': "_chainId",
                'type': "uint16"
            },
            {
                'internalType': "uint256",
                'name': "_configType",
                'type': "uint256"
            },
            {
                'internalType': "bytes",
                'name': "_config",
                'type': "bytes"
            }
        ],
        'name': "setConfig",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint16",
                'name': "_version",
                'type': "uint16"
            }
        ],
        'name': "setReceiveVersion",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint16",
                'name': "_version",
                'type': "uint16"
            }
        ],
        'name': "setSendVersion",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint16",
                'name': "_srcChainId",
                'type': "uint16"
            },
            {
                'internalType': "bytes",
                'name': "_srcAddress",
                'type': "bytes"
            }
        ],
        'name': "setTrustedRemote",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "newOwner",
                'type': "address"
            }
        ],
        'name': "transferOwnership",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint16",
                'name': "",
                'type': "uint16"
            }
        ],
        'name': "trustedRemoteLookup",
        'outputs': [
            {
                'internalType': "bytes",
                'name': "",
                'type': "bytes"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    }
]