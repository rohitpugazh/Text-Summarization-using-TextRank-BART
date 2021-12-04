from re import S
import tkinter as tk
from tkinter import scrolledtext
import textranksummary, bartsummary

win = tk.Tk()
win.title("BART-TextRank Summarizer")
win.resizable(0,0)


tk.Label(win, 
          text = "Original Article",
          font = ("Times New Roman", 15), 
          background = 'green', 
          foreground = "white").grid(column = 0, row = 0, padx=10, pady=10)

tk.Label(win, 
          text = "Summarized Article",
          font = ("Times New Roman", 15), 
          background = 'green', 
          foreground = "white").grid(column = 1, row = 0, padx=10, pady=10)

input_text_area = scrolledtext.ScrolledText(win, 
                                      wrap = tk.WORD, 
                                      width = 40, 
                                      height = 20, 
                                      font = ("Times New Roman", 12))
input_text_area.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

output_text_area = scrolledtext.ScrolledText(win, 
                                      wrap = tk.WORD, 
                                      width = 40, 
                                      height = 20, 
                                      font = ("Times New Roman", 12))
output_text_area.grid(row=1, column=1, padx=10, pady=5, sticky=tk.E)


def summarize():
    article=input_text_area.get("1.0","end-1c")
    trs = textranksummary.generate_textrank(article, 6)
    bs = bartsummary.generate_bart(article)
    combined = bs + "" +trs
    combinedsum = bartsummary.generate_bart(combined)
    output_text_area.configure(state='normal')
    output_text_area.delete('1.0', "end")
    output_text_area.insert(tk.INSERT, combinedsum)
    output_text_area.configure(state='disabled')

summarize_button = tk.Button(win, text="Summarize", 
                    command=lambda: summarize()).grid(row=2, column = 0, columnspan=2, pady=10, sticky=tk.S + tk.N)

win.mainloop()