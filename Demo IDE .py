import tkinter as tk
from tkinter import scrolledtext, messagebox
import re

class LLCppjavaPyIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("LLCppjavaPy IDE")
        self.root.geometry("800x600")

        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(expand=True, fill='both')
        self.text_area.bind('<KeyRelease>', self.highlight_syntax)

        self.run_button = tk.Button(self.root, text="Run", command=self.run_code)
        self.run_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_text)
        self.clear_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.text_area.tag_configure("keyword", foreground="red", font=("Arial", 12, "bold"))
        self.text_area.tag_configure("string", foreground="green")
        self.text_area.tag_configure("comment", foreground="gray")

    def highlight_syntax(self, event=None):
        # Xóa tất cả các tag màu cũ
        self.text_area.tag_remove("keyword", "1.0", tk.END)
        self.text_area.tag_remove("string", "1.0", tk.END)
        self.text_area.tag_remove("comment", "1.0", tk.END)

        code = self.text_area.get("1.0", tk.END)
        lines = code.splitlines()

        for line_number, line in enumerate(lines, start=1):
            # Tô màu từ khóa
            for keyword in ["import", "def", "class", "if", "else", "for", "while", "return","in","as","None","False","True"]:
                pattern = r'\b' + re.escape(keyword) + r'\b'
                start_index = f"{line_number}.{line.find(keyword)}"
                end_index = f"{line_number}.{line.find(keyword) + len(keyword)}"
                if line.find(keyword) != -1:
                    self.text_area.tag_add("keyword", start_index, end_index)

            # Tô màu chuỗi
            for match in re.finditer(r'\".*?\"|\'.*?\'', line):
                self.text_area.tag_add("string", f"{line_number}.{match.start()}", f"{line_number}.{match.end()}")

            # Tô màu chú thích
            for match in re.finditer(r'#.*', line):
                self.text_area.tag_add("comment", f"{line_number}.{match.start()}", f"{line_number}.{match.end()}")

        self.text_area.see(tk.END)  # Cuộn xuống cuối

    def run_code(self):
        code = self.text_area.get("1.0", tk.END)
        try:
            exec(code)
            messagebox.showinfo("Success", "Code executed successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    ide = LLCppjavaPyIDE(root)
    root.mainloop()