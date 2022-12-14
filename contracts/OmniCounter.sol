// SPDX-License-Identifier: MIT

pragma solidity 0.8.4;
pragma abicoder v2;

import "@layerzero/contracts/lzApp/NonblockingLzApp.sol";

contract OmniCounter is NonblockingLzApp {
    uint public counter;

    constructor(address _lzEndpoint) NonblockingLzApp(_lzEndpoint) {}

    function _nonblockingLzReceive(uint16, bytes memory, uint64, bytes memory) internal override {
        // _nonblockingLzReceive is how we provide custom logic to lzReceive()
        // in this case, increment a counter when a message is received.
        counter += 1;
    }

    function incrementCounter(uint16 _dstChainId) public payable {
        // _lzSend calls endpoint.send()
        _lzSend(_dstChainId, bytes(""), payable(msg.sender), address(0x0), bytes(""));
    }
}