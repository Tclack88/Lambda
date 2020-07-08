from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

node = "http://localhost:5000"

@app.route('/')
def root():
    return render_template('base.html')

@app.route("/new_transaction", methods = ['GET','POST'])
def show_transaction():
    sender, recipient, amount = request.values['sender'], request.values['recipient'], request.values['amount']
    post_data = {'sender':sender, 'recipient':recipient, 'amount':amount}

    r = requests.post(url=node + "/new_transaction", json=post_data)
    data = r.json() # returns a JSON with 'message' and 'chain'
    message = data['message']
    # parse chain into readable transaction history
    chain = data['chain']
    users = {}
    return_string = ''
    for i, c in enumerate(chain):
        return_string += f'\nBLOCK {i + 1}:\n' # starts at 0, we want it to start at 1:
        transactions = c['transactions']
        if transactions: # i.e. if not an empty list (genesis block)
            return_string += f'-- transactions --'
            for transaction in transactions:
                s = transaction['sender']
                r = transaction['recipient']
                a = float(transaction['amount'])
                if s == '0': # if a coin was mined, sender (s) gave coin to miner, show.
                    users[r] = users.get(r,0) + 1
                    return_string += f'\n{r} forged 1 new coin--total:{users.get(r,1)} coins'
                else: # otherwise another transaction occured
                    users[s] = users.get(s, 0) - a
                    users[r] = users.get(r, 0) + a
                    return_string += f'\n {s} paid {r} {a} coin(s)'
            return_string += f'\nTOTAL: {users}\n\n'
    text = return_string.split('\n')
    return render_template('new_transaction.html', message=message, text=text)

# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
