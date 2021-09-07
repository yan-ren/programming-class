
import java.util.*;

public class TicTacToe {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char nextPlayer = 'x';
        char[] board = startGame();
        boolean isGameOver = false;
        char result = ' ';

        while (!isGameOver) {
            // Get the current player's next move
            getNextMove(sc, nextPlayer, board);
            // Check if game has ended
            result = hasGameEnded(board);
            if (result != ' ') {
                isGameOver = true;
            }
            System.out.println("result: " + result);
            // otherwise
            if (nextPlayer == 'x') {
                nextPlayer = 'o';
            } else {
                nextPlayer = 'x';
            }
        }
        // end game
        printBoard(board);
        if (result == 'x') {
            System.out.println("player x has won");
        } else if (result == 'o') {
            System.out.println("player o has won");
        } else {
            System.out.println("no one wins");
        }
    }

    public static char hasGameEnded(char[] board) {
        // 3-in-a-row, horizontal
        for (int row = 0; row < 3; row++) {
            if ((board[3 * row] == board[3 * row + 1]) && (board[3 * row + 1] == board[3 * row + 2])
                    && board[3 * row] != ' ') {
                return board[3 * row];
            }
        }

        // 3-in-a-row, vertical
        for (int col = 0; col < 3; col++) {
            if ((board[col] == board[col + 3]) && (board[col + 3] == board[col + 6]) && (board[col] != ' ')) {
                return board[col];
            }
        }

        // 3-in-a-row, diagonal
        if ((board[0] == board[4]) && (board[4] == board[8])) {
            return board[0];
        }
        if ((board[2] == board[4]) && (board[4] == board[6])) {
            return board[2];
        }

        // check if board is filled
        boolean isFilled = true;
        for (int i = 0; i < 9; i++) {
            if (board[i] == ' ') {
                isFilled = false;
            }
        }

        if (isFilled) {
            return '-';
        }

        return ' ';
    }

    public static char[] startGame() {
        char[] board = new char[9];
        for (int i = 0; i < board.length; i++) {
            board[i] = ' ';
        }
        return board;
    }

    public static int getNextMove(Scanner sc, char nextPlayer, char[] board) {
        boolean isValid = false;
        int move = -1;
        printBoard(board);

        while (!isValid) {
            // Ask current player for their next move
            System.out.println("It is " + nextPlayer + "'s move, enter a move");
            move = sc.nextInt();
            // Check to see if the selection is valid
            if (move >= 0 && move <= 8 && board[move] == ' ') {
                isValid = true;
                board[move] = nextPlayer;
            }
        }

        return move;
    }

    public static void printBoard(char[] board) {
        for (int i = 0; i < board.length; i++) {
            System.out.print(i + ": " + board[i] + " | ");
            if ((i + 1) % 3 == 0) {
                System.out.println();
            }
        }
    }
}
