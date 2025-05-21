from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "replace_this_secret"

EMPTY = " "


def initialize_game(symbol):
    session['board'] = [EMPTY] * 9
    session['player_symbol'] = symbol
    session['computer_symbol'] = 'O' if symbol == 'X' else 'X'
    session['winner'] = None
    if symbol == 'X':
        # Computer is O and should make the first move
        session['turn'] = 'computer'
        computer_move()
        session['turn'] = 'player'
    else:
        session['turn'] = 'player'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start():
    symbol = request.form.get('symbol', 'X').upper()
    if symbol not in ('X', 'O'):
        symbol = 'X'
    initialize_game(symbol)
    return redirect(url_for('play'))

def check_winner(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in lines:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    if EMPTY not in board:
        return 'Tie'
    return None


def minimax(board, player, computer):
    winner = check_winner(board)
    if winner == player:
        return -1, None
    elif winner == computer:
        return 1, None
    elif winner == 'Tie':
        return 0, None

    best_score = -2
    best_move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = computer
            score, _ = minimax(board, player, 'O' if computer == 'X' else 'X')
            score = -score
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                best_move = i
    return best_score, best_move


def computer_move():
    board = session['board']
    _, move = minimax(board[:], session['player_symbol'], session['computer_symbol'])
    if move is not None:
        board[move] = session['computer_symbol']


@app.route('/play')
def play():
    board = session.get('board')
    if board is None:
        return redirect(url_for('index'))

    move = request.args.get('move')
    if move is not None and session['turn'] == 'player':
        idx = int(move)
        if board[idx] == EMPTY:
            board[idx] = session['player_symbol']
            session['turn'] = 'computer'
            winner = check_winner(board)
            if winner is None:
                computer_move()
                session['turn'] = 'player'
            else:
                session['winner'] = winner
    winner = session.get('winner')
    if winner is None:
        winner = check_winner(board)
        if winner:
            session['winner'] = winner
    return render_template('play.html', board=board, winner=session.get('winner'))


@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    import os
    debug = os.getenv("FLASK_ENV") != "production"
    app.run(debug=debug, host="127.0.0.1", port=5000)