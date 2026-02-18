import tkinter as tk
from tkinter import scrolledtext, messagebox

class LLCppjavaPyIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("LLCppjavaPy IDE")
        self.root.geometry("800x600")

        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(expand=True, fill='both')

        self.run_button = tk.Button(self.root, text="Run", command=self.run_code)
        self.run_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_text)
        self.clear_button.pack(side=tk.LEFT, padx=10, pady=10)

    def run_code(self):
        code = self.text_area.get("1.0", tk.END)
        # Giả lập chạy mã, bạn có thể thay thế bằng logic thực tế cho ngôn ngữ LLCppjavaPy
        try:
            exec(code)  # Chạy mã (cẩn thận với exec)
            messagebox.showinfo("Success", "Code executed successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    ide = LLCppjavaPyIDE(root)
    root.mainloop()