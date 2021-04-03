  
# from etherscan.accounts import Account
# import json

# with open('./api_key.json', mode='r') as key_file:
#     key = json.loads(key_file.read())['key']

# address = '0xEcA19B1a87442b0c25801B809bf567A6ca87B1da'

# api = Account(address=address, api_key=key)
# # transactions = api.get_all_transactions(offset=10000, sort='asc',
# #                                         internal=False)
# # transactions = api.get_transaction_page(page=1, offset=10000, sort='des', erc20=True)
# print(api.get_transaction_page(erc20=True))

# # print(transactions[0])
from etherscan import Etherscan

eth = Etherscan('K7ST5DC6VP2Z5ZVWWD1IB3JDB5AHIEV274', net="ropsten")

all_dataset = []
relate_address = ['0xEcA19B1a87442b0c25801B809bf567A6ca87B1da']
    
while True:
    if relate_address:
        r = eth.get_erc20_token_transfer_events_by_address(address=relate_address[0], startblock=0, endblock=999999999, sort='asc')
        for i in r:
            if i['tokenSymbol'] == 'BKTC' and i['to'] not in relate_address:
                all_dataset.append(i)
                relate_address.append(i['to'])
                print(i, relate_address)
        del relate_address[0]
    
print(all_dataset)