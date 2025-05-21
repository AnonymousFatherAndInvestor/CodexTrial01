# Tic Tac Toe Web App

This repository contains a simple Tic Tac Toe (〇×ゲーム) web application built with Flask. Users can choose to play as X or O and compete against the computer.

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```
   For a production-like environment (or when deploying), use Gunicorn:
   ```bash
   gunicorn app:app
   ```

Access `http://localhost:5000` in your browser to play.

## Deployment to Render

The project includes a `render.yaml` configuration and a `Procfile`. When you create a new Web Service on Render, it will automatically install dependencies and run the app using Gunicorn.

### Turn Order

O always moves first. If you choose X, the computer starts as O and makes the first move automatically. When you choose O, you take the first turn.

## Computer Strategy

The computer uses the **minimax algorithm** to determine its moves. This algorithm explores all possible moves of the game tree and assumes both players play optimally. Each board state is scored as follows:

- `+1` if the computer wins
- `-1` if the player wins
- `0` for a tie

The computer selects the move with the highest score to maximize its chance of winning or forcing a draw. This approach ensures the computer never loses if played correctly.

