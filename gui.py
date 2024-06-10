import os
import tkinter as tk
from tkinter import filedialog, messagebox

class ScreenRecorderGUI:
    def __init__(self, master):
        self.master = master
        master.title("Screen Recorder")

        self.record_button = tk.Button(master, text="Record", command=self.record)
        self.record_button.pack()

        self.convert_button = tk.Button(master, text="Convert", command=self.show_convert_page)
        self.convert_button.pack()

    def record(self):
        subprocess.Popen(["python", "screen-recorder.py"])

    def show_convert_page(self):
        self.record_button.pack_forget()
        self.convert_button.pack_forget()
        
        self.file_label = tk.Label(self.master, text="Select .avi file:")
        self.file_label.pack()
        
        self.file_button = tk.Button(self.master, text="Browse", command=self.select_file)
        self.file_button.pack()
        
        self.output_label = tk.Label(self.master, text="Select output format:")
        self.output_label.pack()
        
        self.output_var = tk.StringVar()
        self.output_var.set("mp4")
        self.output_options = ["mp4", "mov", "mkv"]
        self.output_menu = tk.OptionMenu(self.master, self.output_var, *self.output_options)
        self.output_menu.pack()
        
        self.convert_button = tk.Button(self.master, text="Convert", command=self.convert)
        self.convert_button.pack()

    def select_file(self):
        self.file_path = filedialog.askopenfilename(title="Select a recording file", filetypes=[("Video files", "*.avi")])
        if self.file_path:
            messagebox.showinfo("File Selected", f"Selected file: {os.path.basename(self.file_path)}")

    def convert(self):
        if not hasattr(self, 'file_path'):
            messagebox.showerror("Error", "Please select a .avi file.")
            return

        output_dir = "output/converted"
        os.makedirs(output_dir, exist_ok=True)
        
        output_format = self.output_var.get()
        output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(self.file_path))[0] + "." + output_format)
        
        subprocess.run(["ffmpeg", "-i", self.file_path, "-c:v", "libx264", "-preset", "fast", output_file])
        messagebox.showinfo("Conversion Complete", f"File converted successfully! Saved as {output_file}")

root = tk.Tk()
app = ScreenRecorderGUI(root)
root.mainloop()
