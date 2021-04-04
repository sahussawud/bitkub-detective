
from etherscan import Etherscan
API_KEY = 'K7ST5DC6VP2Z5ZVWWD1IB3JDB5AHIEV274'
ADDRESS = '0xEcA19B1a87442b0c25801B809bf567A6ca87B1da'
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def main():
    eth = Etherscan(API_KEY, net="ropsten")
    all_dataset = []
    relate_address = [ADDRESS]
        
    while True:
        if relate_address:
            r = eth.get_erc20_token_transfer_events_by_address(address=relate_address[0], startblock=0, endblock=999999999, sort='asc')
            for i in r:
                if i['tokenSymbol'] == 'BKTC' and i['to'] not in relate_address:
                    all_dataset.append(i)
                    relate_address.append(i['to'])
            del relate_address[0]
        else:
            break

    print('No | Tx Address | From | To |  Amount Tranfer')
    for count, value in enumerate(all_dataset, start=1):
        print(count, value['hash'], value['from'], value['to'], int(value['value'])/10**18)


main()
