pragma solidity 0.5.14;
pragma experimental ABIEncoderV2;

import { BandChainLib } from "/BandChainLib.sol";
import { IBridge } from "/IBridge.sol";

contract SimplePriceDatabase {
  using BandChainLib for bytes;

  bytes32 public codeHash;
  bytes public params;
  IBridge public bridge;
  
  uint256 public latestPrice;
  uint256 public lastUpdate;

  constructor( 
    bytes32 _codeHash ,
    bytes memory _params,
    IBridge _bridge
  ) public {
    codeHash = _codeHash;
    params = _params;
    bridge = _bridge;
  }

  function update(bytes memory _reportPrice) public {
    IBridge.VerifyOracleDataResult memory result = bridge.relayAndVerify(_reportPrice);
    uint64[] memory decodedInfo = result.data.toUint64List();
    
    require(result.codeHash == codeHash, "INVALID_CODEHASH");
    require(keccak256(result.params) == keccak256(params), "INVALID_PARAMS");
    require(uint256(decodedInfo[1]) > lastUpdate, "TIMESTAMP_MUST_BE_OLDER_THAN_THE_LAST_UPDATE");

    latestPrice = uint256(decodedInfo[0]);
    lastUpdate = uint256(decodedInfo[1]);
  }
}

contract File {
    // Initialize file hash
    string fileHash;

    // Write function
    function set(string memory _fileHash) public {
        fileHash = _fileHash;
    }
    // Read function
    function get() public view returns (string memory) {
        return fileHash;
    }
}