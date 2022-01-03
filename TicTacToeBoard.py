class TicTacToeBoard:
    """
    A class to hold a TicTacToe board

    Attributes
    ----------
    board : list
        Matrix to hold board

    Methods
    -------
    display_board(self)
        Displays matrix in a nice format
    play_turn(self, letter)
        Performs the actions of a turn
    insert_letter(self, letter, row, col)
        Inserts letter into matrix board
    check_available(self, row, col)
        Checks if spot if available
    check_winner(self)
        Checks to see if the game should end
    """

    def __init__(self):
        """
        Construct a TicTacToe board as a matrix
        """
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def display_board(self):
        """
        Displays matrix in a nice format
        """
        print("-------")
        for i in range(len(self.board)):
            string = "|"
            for j in range(len(self.board[i])):
                string = string + self.board[i][j] + "|"
            print(string)
            print("-------")

    def play_turn(self, letter):
        """
        Performs the actions of a turn

        :param letter: Letter to insert next into matrix
        :type letter: str
        """
        while True:
            row = input("Which row would you like to place your "+letter+"? 1, 2, or 3? ")
            while (row != "1") & (row != "2") & (row != "3"):   # Validate input
                row = input("Enter a valid row number. 1, 2, or 3: ")
            row = int(row)
            col = input("Which column would you like to place your "+letter+"? 1, 2, or 3? ")
            while (col != "1") & (col != "2") & (col != "3"):   # Validate input
                col = input("Enter a valid column number. 1, 2, or 3: ")
            col = int(col)
            if self.check_available(row-1, col-1):
                break

        self.insert_letter(letter, row-1, col-1)
        self.display_board()

    def insert_letter(self, letter, row, col):
        """
        Inserts letter into matrix board

        :param letter: Letter to insert into matrix board
        :type letter: str
        :param row: Row number of matrix
        :type row: int
        :param col: Column number of matrix
        :type col: int
        """
        self.board[row][col] = letter

    def check_available(self, row, col):
        """
        Checks if spot if available

        :param row: Row number of matrix
        :type row: int
        :param col: Column number of matrix
        :type col: int
        :return: Status of spot. True: available
        :rtype: bool
        """
        if self.board[row][col] == " ":
            return True
        print("That space is already occupied.")
        return False

    def check_winner(self):
        """
        Checks to see if the game should end

        :return: Status of game. True: Winner exists
        :rtype: bool
        """
        # For each row, check if all elements are the same
        for row in self.board:
            first = row[0]
            acrossC = 0
            for i in range(len(row)):
                if (row[i] == first) & (first != " "):
                    acrossC += 1
            if acrossC == 3:
                string = "Three {}'s in a row! We have a winner!"
                print(string.format(first))
                return True

        # For each column, check if all elements are the same
        downCF = downCS = downCT = 0
        first = self.board[0][0]
        second = self.board[0][1]
        third = self.board[0][2]
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if j == 0:
                    if (self.board[i][j] == first) & (first != " "):
                        downCF += 1
                        if downCF == 3:
                            string = "Three {}'s in a row! We have a winner!"
                            print(string.format(first))
                            return True
                elif j == 1:
                    if (self.board[i][j] == second) & (second != " "):
                        downCS += 1
                        if downCS == 3:
                            string = "Three {}'s in a row! We have a winner!"
                            print(string.format(second))
                            return True
                elif j == 2:
                    if (self.board[i][j] == third) & (third != " "):
                        downCT += 1
                        if downCT == 3:
                            string = "Three {}'s in a row! We have a winner!"
                            print(string.format(third))
                            return True

        # For both diagonals, check if all elements are the same
        middle = self.board[1][1]
        if (self.board[0][0] == middle) & (self.board[2][2] == middle) & (middle != " "):
            string = "Three {}'s in a row! We have a winner!"
            print(string.format(middle))
            return True
        elif (self.board[0][2] == middle) & (self.board[2][0] == middle) & (middle != " "):
            string = "Three {}'s in a row! We have a winner!"
            print(string.format(middle))
            return True

        # Check if game is over by turns
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == " ":
                    count += 1
                    break
        if count == 0:
            print("There was no winner...")
            return True

        # Game is not over
        return False
