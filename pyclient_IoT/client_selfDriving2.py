from web3 import Web3
from web3.middleware import geth_poa_middleware
import json


class Client:
	def __init__(self,http):
		self.w3 = Web3(Web3.HTTPProvider(http))
		self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
		print("web3 is connected : " , self.w3.isConnected())
	def reedkey(self,datadir):
		with open(datadir) as keyfile:
			encrypted_key = keyfile.read()
			key = self.w3.eth.account.decrypt(encrypted_key, '')
		return key
	def connected(self,abi,key,address,robot_caller,msn):
		caller = self.w3.eth.accounts[0]
		private_key = key
		nonce = self.w3.eth.getTransactionCount(caller)
		# Initialize address nonce
		nonce = self.w3.eth.getTransactionCount(caller)
		nonce2 = self.w3.eth.getTransactionCount(caller)
		Val = self.w3.eth.contract(address=address,abi=abi)
		Chain_id = self.w3.eth.chain_id
		call_function = Val.functions.set_Navigation_information(robot_caller,msn).buildTransaction({"chainId": Chain_id, "from": caller, "nonce": nonce})
		# Sign transaction
		signed_tx = self.w3.eth.account.sign_transaction(call_function, private_key=private_key)
		# Send transaction
		send_tx = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
		# Wait for transaction receipt
		tx_receipt = self.w3.eth.wait_for_transaction_receipt(send_tx)
		print(tx_receipt,"1") # Optional

	def telemetry_informatio(self,abi,key,address,robot_caller):
		caller = self.w3.eth.accounts[0]
		private_key = key
		nonce = self.w3.eth.getTransactionCount(caller)
		# Initialize address nonce
		nonce = self.w3.eth.getTransactionCount(caller)
		nonce2 = self.w3.eth.getTransactionCount(caller)
		Val = self.w3.eth.contract(address=address,abi=abi)
		result = Val.functions.get_Navigation_information(robot_caller).call()
		print(result)
