# Tic Tac Toe Web App

This repository contains a simple Tic Tac Toe (〇×ゲーム) web application built with Flask. Users can choose to play as X or O and compete against the computer. Regardless of who selects a symbol, **O always makes the first move**. If you pick X, the computer starts; choosing O lets you go first.

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```

Access `http://localhost:5000` in your browser to play.

## Deployment to Render

The project includes a `render.yaml` configuration. When you create a new Web Service on Render, it will automatically install dependencies and run the app using Gunicorn.

## Computer Strategy

The computer uses the **minimax algorithm** to determine its moves. This algorithm explores all possible moves of the game tree and assumes both players play optimally. Each board state is scored as follows:

- `+1` if the computer wins
- `-1` if the player wins
- `0` for a tie

The computer selects the move with the highest score to maximize its chance of winning or forcing a draw. This approach ensures the computer never loses if played correctly.

