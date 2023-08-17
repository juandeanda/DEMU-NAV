// SPDX-License-Identifier: MIT
// compiler version must be greater than or equal to 0.8.10 and less than 0.9.0
pragma solidity ^0.8.11;
contract navigation_authority{

bool owner = false;
bool authority = false;
bool system = false; 

struct register{
        uint data;
        string name;
    }
mapping (string => register) Info;
function set_authority_status(bool navigation) public{
    authority = navigation;
}
function set_owner_status(bool navigation) public{
    owner = navigation;
}
function set_authority_system(bool navigation) public{
    system = navigation;
}
function Navigation() public returns(bool){
    bool aux = false;
    if(owner && authority && system){
        aux = true;
    }
    return aux;
 }
 function set_Navigation_emergency (string memory key,string memory name) public returns(bool){
    bool aux = false;
    if(owner && system){
        aux = true;
    }
    Info[key] = register(block.timestamp,name);
    return aux;
 }
}
