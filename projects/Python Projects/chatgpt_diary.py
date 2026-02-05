import os
from tkinter import Tk, Label, Entry, Button, Text, filedialog, Scrollbar, END, messagebox, Toplevel
from datetime import datetime

class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diary Application")
        self.root.geometry("500x500")

        # Label for Diary Filename
        Label(root, text="Diary File Name:").pack(pady=5)
        self.filename_entry = Entry(root, width=50)
        self.filename_entry.pack(pady=5)

        # Entry for Diary Text
        Label(root, text="Diary Entry:").pack(pady=5)
        self.entry_text = Text(root, width=60, height=10)
        self.entry_text.pack(pady=5)

        # Buttons for Actions
        Button(root, text="Submit Entry", command=self.save_entry).pack(pady=10)
        Button(root, text="Browse Entries", command=self.browse_entries).pack(pady=10)

        # Status Label
        self.status_label = Label(root, text="")
        self.status_label.pack(pady=5)

    def save_entry(self):
        filename = self.filename_entry.get().strip()
        if not filename:
            messagebox.showerror("Error", "Please enter a file name!")
            return
        
        entry_text = self.entry_text.get("1.0", END).strip()
        if not entry_text:
            messagebox.showerror("Error", "Diary entry cannot be empty!")
            return

        # Add date to the entry
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry_with_date = f"[{current_date}]\n{entry_text}\n\n"

        # Save the entry
        filepath = filename + ".txt"
        with open(filepath, "a") as file:
            file.write(entry_with_date)

        # Clear the text area and notify user
        self.entry_text.delete("1.0", END)
        self.status_label.config(text="Entry saved successfully!", fg="green")

    def browse_entries(self):
        # Let the user choose a diary file
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return  # User canceled

        # Open the selected file and display its contents
        self.show_entries(file_path)

    def show_entries(self, file_path):
        top = Toplevel(self.root)
        top.title(f"Viewing Entries - {os.path.basename(file_path)}")
        top.geometry("500x400")

        Label(top, text=f"Entries in {os.path.basename(file_path)}:").pack(pady=5)
        
        # Scrollable text area
        scrollbar = Scrollbar(top)
        scrollbar.pack(side="right", fill="y")
        
        text_area = Text(top, wrap="word", yscrollcommand=scrollbar.set)
        text_area.pack(expand=True, fill="both")
        scrollbar.config(command=text_area.yview)

        # Load entries into text area
        with open(file_path, "r") as file:
            content = file.read()
            text_area.insert("1.0", content)

        # Make text area read-only
        text_area.config(state="disabled")


if __name__ == "__main__":
    root = Tk()
    app = DiaryApp(root)
    root.mainloop()
