import tkinter as tk
from tkinter import messagebox


class SudokuChecker:
    def __init__(self, window):
        self.window = window
        self.window.title("Emmanuel Sudoku Game")
        self.rows = []

        self.instructions_label = tk.Label(window, text="Enter the 9 rows of Sudoku (9 digits per row):", font="20")
        self.instructions_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.entries = []
        for i in range(9):
            row_label = tk.Label(window, text=f"Row {i + 1}:", font="20")
            row_label.grid(row=i + 1, column=0)
            entry = tk.Entry(window, width=10)
            entry.grid(row=i + 1, column=1)
            self.entries.append(entry)

        self.check_button = tk.Button(window, text="Check Sudoku", command=self.validate_sudoku)
        self.check_button.grid(row=10, column=0, columnspan=2, pady=10)

    def check(self, numbers):
        return sorted(list(numbers)) == [chr(x + ord("0")) for x in range(1, 10)]

    def validate_sudoku(self):
        self.rows = []

        for i in range(len(self.entries)):
            entry = self.entries[i]
            row = entry.get()
            if len(row) != 9 or not row.isdigit():
                messagebox.showerror("Input Error", f"Row {i + 1} must contain exactly 9 digits!")
                return
            self.rows.append(row)

        ok = all(self.check(row) for row in self.rows)

        if ok:
            for c in range(9):
                col = [self.rows[r][c] for r in range(9)]
                if not self.check(col):
                    ok = False
                    break

        if ok:
            for r in range(0, 9, 3):
                for c in range(0, 9, 3):
                    sqr = "".join(self.rows[r + i][c:c + 3] for i in range(3))
                    if not self.check(list(sqr)):
                        ok = False
                        break

        if ok:
            messagebox.showinfo("Sudoku Result", "Yes, the Sudoku is valid!")
        else:
            messagebox.showinfo("Sudoku Result", "No, the Sudoku is invalid.")


def main():
    window = tk.Tk()
    SudokuChecker(window)
    window.mainloop()


main()
