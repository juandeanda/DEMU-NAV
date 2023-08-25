# DEMU-NAV
A new IoT-BlockChain-Smart Contract Framework for communication in self-driving vehicles

## Dependence
```
geth=1.10.13-stable-7a0c19f8
python=3.8
ubuntu=20.04.3 LTS
```
## Installation
```
$ git clone https://github.com/juandeanda/DEMU-NAV.git
```
# Insatll dependence and run
```
$ cd DEMU-NAV
$ make install_ubuntu
$ make run
```
## Software description

### Self-driving Blockchain
In principle, we will analyze the needs demanded by the self-driving
blockchain: first, the navigation network invokes a regulatory authority,
then the self-driving blockchain coincides with the concept of permissioned
blockchain. Second, the network has a private character since it must safe-
guard the information of its transactions. Third, according to its environ-
mental characteristics, the network must be open or closed; for example,
in an Industrial environment, it will be closed, while, in city navigation, it
will be open.

* Self-driving permissioned blockchain: the authority controls and
generates the initial characteristics of the blockchain; in technical terms, the Genesis blockchain, which has the levels of mining complexity, set of administrative accounts, transaction controllers, accounts corresponding to administrators with a permission value, meaning by permission value the amount allowed to grant transactions.

* Crypto-security: The main elements are to safeguard the exchange
of information from level 2 to level 3 since levels 2 and 3
contain the private and administrative domain data, in contrast to the
public domain; consequently, mining must be dynamic considering the
level of complexity at a minimum in the public domain and high in
level 2 and 3 transactions. Therefore, the navigation authority will
build the genesis block, thus defining the dynamic degree of mining by
streamlining the network transaction records.

* Self-driving net authentication: Self-driving net members con-
tain different human actors. First, the navigation control author-
ity, which has an organizational representative; second, legal prox-
ies of the autonomous vehicles; third, human contact or interaction
members, e.g., hospital representatives, school principal, among oth-
ers; consequently, we have described human-to-human interaction ac-
tors, which represents our current world. In another scenario, Au-
tonomous Vehicle Artificial Intelligence (Autonomous-IA) represents a
new paradigm in navigation systems; it needs inclusion, as it gener-
ates different combinations Autonomous-IA-Human, Autonomous-IA-
Autonomous-IA, Autonomous-IA-Autonomous-IA, Autonomous-IA-Authority.
Therefore, DEMU-NAV generates a set of accounts considering the dif-
ferent roles, such as Authority, Legal Proxy, Contact Member, and
Autonomous-IA, each with different crypto-signatures.

* Self-driving Smart Contract: Following the framework, Smart contracts allow to adapt the concept of three levels of interaction. Public approach, Smart Contracts have public functions that do not generate transaction costs and are free for consultation if an instruction allows access to the information
