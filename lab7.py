import tkinter as tk
from tkinter import scrolledtext
from itertools import permutations

def generate_permutations():
    try:
        size = int(entry_size.get())
        if size % 2 != 0 or size < 2:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Ошибка: Размер матрицы должен быть четным числом >= 2.")
            return

        half_size = size // 2
        A = [[f"A{i+1}{j+1}" for j in range(half_size)] for i in range(half_size)]
        B = [[f"B{i+1}{j+1}" for j in range(half_size)] for i in range(half_size)]
        C = [[f"C{i+1}{j+1}" for j in range(half_size)] for i in range(half_size)]
        D = [[f"D{i+1}{j+1}" for j in range(half_size)] for i in range(half_size)]

        submatrices = [A, B, C, D]
        permuted_matrices = list(permutations(submatrices))

        result = ""
        for idx, perm in enumerate(permuted_matrices):
            result += f"Вариант {idx + 1}:\n"
            top_half = [perm[0][i] + perm[1][i] for i in range(half_size)]
            bottom_half = [perm[2][i] + perm[3][i] for i in range(half_size)]
            full_matrix = top_half + bottom_half
            for row in full_matrix:
                result += " ".join(row) + "\n"
            result += "\n"

        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result)

    except ValueError:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Ошибка: Введите корректный размер матрицы (четное число >= 2).")

root = tk.Tk()
root.title("Перестановка подматриц")
root.geometry("600x400")

label_size = tk.Label(root, text="Введите размер квадратной матрицы (четное число >= 2):")
label_size.pack(pady=5)

entry_size = tk.Entry(root)
entry_size.pack(pady=5)

button_generate = tk.Button(root, text="Сгенерировать", command=generate_permutations)
button_generate.pack(pady=10)

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
output_text.pack(pady=10)

root.mainloop()
