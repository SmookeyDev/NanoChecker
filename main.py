from nanolib import generate_seed, generate_account_id
import string, random
import requests

def accounts_balances(accounts):
    data = {"action":"accounts_balances","accounts": accounts}
    response = requests.post('http://api.nanex.cc/', json=data)
    return response.json()

while True:

    seeds = []
    adresses = []

    for n in range(100):
        seed = generate_seed()
        account = generate_account_id(seed, 0).replace("xrb", "nano")
        seeds.append(seed)
        adresses.append(account)

    all_balances = accounts_balances(adresses)\

    try:
        bals = all_balances["balances"]
    except:
        continue

    for address in bals:
        result = f"Account: {address} || Seed: {seeds[adresses.index(address)]} || Balances: (Balance: {bals[address]['balance']}, Pending: {bals[address]['pending']})"
        if int(bals[address]['balance']) > 0 or int(bals[address]['pending']) > 0:
            with open('wallets.txt', 'a') as arq:
                arq.write('{}\n'.format(result))
        print(result)