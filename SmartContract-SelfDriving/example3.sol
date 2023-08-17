// SPDX-License-Identifier: MIT
// compiler version must be greater than or equal to 0.8.10 and less than 0.9.0
pragma solidity ^0.8.11;
contract navigation_authority{

struct register{
        uint telemetry;
}
mapping (string => register) Info;
function set_Navigation_information(string memory key, uint val) public{
      Info[key] = register(val);
}

function get_Navigation_information(string memory key) public returns(uint){
      return Info[key].telemetry;
}

}
