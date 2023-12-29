
from customtkinter import *
from CTkMessagebox import CTkMessagebox
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class SocialConnectXApp:
    def __init__(self):
        self.app = CTk()
        self.app.minsize(1160, 800)
        self.app.maxsize(1160, 800)
        self.app.title("SocialConnectX")

        # Frames
        self.frameTop = CTkFrame(master=self.app, width=900, height=100, border_width=1, border_color='black',
                                 fg_color='#1a1a1a')
        self.frameMiddle = CTkFrame(master=self.app, width=900, height=500, border_width=1, border_color='black',
                                    fg_color='#4d4d4d')
        self.frameBottom = CTkFrame(master=self.app, width=900, height=200, border_width=0, border_color='black',
                                    fg_color='#333333')
        self.frameBottom2 = CTkFrame(master=self.app, width=900, height=200, border_width=0, border_color='black',
                                     fg_color='#333333')

        self.frameTop.grid(row=0, column=0, sticky="nsew")
        self.frameMiddle.grid(row=1, column=0, sticky="nsew")
        self.frameBottom.grid(row=2, column=0, sticky="nsew")
        self.frameBottom2.grid(row=3, column=0, sticky="nsew")

        # Buttons and Labels
        self.create_top_buttons()
        self.create_bottom_buttons()
        self.create_middle_textboxes()
        self.CodeTextBox = CTkTextbox(master=self.frameMiddle, width=500, height=500, border_width=2,
                                      border_color='black', font=("Courier New", 14,'bold'))
        self.CodeTextBox.grid(row=1, column=1, sticky="nsew", padx=20, pady=8)  # CodeTextBox is a class variable
        self.line_numbers1 = CTkTextbox(master=self.frameMiddle, width=40, height=5, fg_color='#999999',
                                        state='disabled', font=("Courier New", 12,'bold'),activate_scrollbars=False,text_color="black")
        self.line_numbers1.grid(row=1, column=0, sticky='nsew', pady=8,padx=20)
        self.update_line_numbers()
        # To DO tomorrow
        self.CodeTextBox.bind('<KeyRelease>', lambda event: self.update_line_numbers())
        # Initialize history list to store XML content after each edit
        self.history = []
        self.state_snapshots = []
        self.redo_snapshots = []
        self.add_state()
        # Set up event binding for keyboard actions
        self.CodeTextBox.bind("<Key>", self.update_history)
        self.filename = None

    def create_top_buttons(self):
        SaveButton = CTkButton(master=self.frameTop, text="Save", width=70, height=40, border_width=2,
                               border_color='black', font=("Segoe UI", 18,"bold"), command=self.add_state,fg_color="#999999",text_color="black")
        UndoButton = CTkButton(master=self.frameTop, text="Undo", width=70, height=40, border_width=2,
                               border_color='black', font=("Segoe UI", 18,"bold"), command=self.undo,fg_color="#999999",text_color="black")
        RedoButton = CTkButton(master=self.frameTop, text="Redo", width=70, height=40, border_width=2,
                               border_color='black', font=("Segoe UI", 18,"bold"), command=self.redo,fg_color="#999999",text_color="black")
        ImportButton = CTkButton(master=self.frameTop, text="Import", width=70, height=40, border_width=2,
                                 border_color='black', font=("Segoe UI", 18,"bold"), command=self.UploadAction,fg_color="#999999",text_color="black")
        ExportButton = CTkButton(master=self.frameTop, text="Export", width=70, height=40, border_width=2,
                                 border_color='black', font=("Segoe UI", 18,"bold"), command=self.file_save,fg_color="#999999",text_color="black")
        ProgramName = CTkLabel(master=self.frameTop, text="SocialConnectX", width=70, height=40,
                               font=('Segoe UI', 22, 'bold'),text_color="white")

        ImportButton.pack(side="left", padx=10, pady=15)
        ExportButton.pack(side="left", padx=10, pady=15)
        UndoButton.pack(side="right", padx=10, pady=15)
        RedoButton.pack(side="right", padx=10, pady=15)
        SaveButton.pack(side="right", padx=10, pady=15)
        ProgramName.pack(side="right", anchor='center', padx=190, pady=15)

    def create_bottom_buttons(self):
        OptionName = CTkLabel(master=self.frameBottom, text="Options", width=70, height=1,
                              font=('Segoe UI', 22, 'bold'))
        ParseButton = CTkButton(master=self.frameBottom, text="Parse", width=135, height=40, border_width=2,
                                border_color='black', font=("Segoe UI", 18,"bold"),fg_color="#999999",text_color="black")
        Check_and_FixButton = CTkButton(master=self.frameBottom, text="Check and Fix", width=135, height=40,
                                        border_width=2, border_color='black', font=("Segoe UI", 18,"bold"),
                                        command=self.show_error,fg_color="#999999",text_color="black")
        Xml_TO_JSONButton = CTkButton(master=self.frameBottom, text="Xml TO JSON", width=135, height=40, border_width=2,
                                      border_color='black', font=("Segoe UI", 18,"bold"),fg_color="#999999",text_color="black")
        CompressButton = CTkButton(master=self.frameBottom, text="Compresse", width=135, height=40, border_width=2,
                                   border_color='black', font=("Segoe UI", 18,"bold"),fg_color="#999999",text_color="black")
        DecompressButton = CTkButton(master=self.frameBottom, text="Decompress", width=135, height=40, border_width=2,
                                     border_color='black', font=("Segoe UI", 18,"bold"),fg_color="#999999",text_color="black")
        PrettifyButton = CTkButton(master=self.frameBottom2, text="Prettify", width=135, height=40, border_width=2,
                                   border_color='black', font=("Segoe UI", 18,"bold"),fg_color="#999999",text_color="black")
        MinifyButton = CTkButton(master=self.frameBottom2, text="Minify", width=135, height=40, border_width=2,
                                 border_color='black', font=("Segoe UI", 18,"bold"),fg_color="#999999",text_color="black")
        Show_GraphButton = CTkButton(master=self.frameBottom2, text="Show Graph", width=135, height=40, border_width=2,
                                     border_color='black', font=("Segoe UI", 18,"bold"),fg_color="#999999",text_color="black")
        Graph_analysisButton = CTkButton(master=self.frameBottom2, text="Graph analysis", width=135, height=40,
                                         border_width=2, border_color='black', font=("Segoe UI", 18,"bold"),fg_color="#999999",text_color="black")
        Post_SearchButton = CTkButton(master=self.frameBottom2, text="Post Search", width=135, height=40,
                                      border_width=2, border_color='black', font=("Segoe UI", 18,"bold"),fg_color="#999999",text_color="black")

        OptionName.grid(row=1, column=3, sticky="nsew", padx=48, pady=5)
        ParseButton.grid(row=2, column=1, sticky="nsew", padx=48, pady=15)
        Check_and_FixButton.grid(row=2, column=2, sticky="nsew", padx=48, pady=15)
        Xml_TO_JSONButton.grid(row=2, column=3, sticky="nsew", padx=48, pady=15)
        CompressButton.grid(row=2, column=4, sticky="nsew", padx=48, pady=15)
        DecompressButton.grid(row=2, column=5, sticky="nsew", padx=48, pady=15)
        PrettifyButton.grid(row=3, column=1, sticky="nsew", padx=48, pady=15)
        MinifyButton.grid(row=3, column=2, sticky="nsew", padx=48, pady=15)
        Show_GraphButton.grid(row=3, column=3, sticky="nsew", padx=48, pady=15)
        Graph_analysisButton.grid(row=3, column=4, sticky="nsew", padx=48, pady=15)
        Post_SearchButton.grid(row=3, column=5, sticky="nsew", padx=48, pady=15)

    def create_middle_textboxes(self):
        CodeName = CTkLabel(master=self.frameMiddle, text="Xml Code", width=70, height=1,
                            font=('Segoe UI', 18, 'bold'))
        OutputName = CTkLabel(master=self.frameMiddle, text="Output", width=70, height=1,
                              font=('Segoe UI', 18, 'bold'))
        outputTextBox = CTkTextbox(master=self.frameMiddle, width=500, height=500, border_width=2, border_color='black',
                                   font=("Segoe UI", 14,"bold"), state="disabled")
        # self.CodeTextBox.bind('<KeyRelease>', lambda event: self.update_line_numbers(line_numbers2, outputTextBox))
        CodeName.grid(row=0, column=1, sticky="nsew", padx=20, pady=5)
        OutputName.grid(row=0, column=3, sticky="nsew", padx=20, pady=5)
        outputTextBox.grid(row=1, column=3, sticky="nsew", padx=20, pady=8)

    def show_checkmark(self):
        # Show some positive message with the checkmark icon
        CTkMessagebox(message="CTkMessagebox is successfully installed.",
                      icon="check", option_1="Thanks")

    def show_error(self):
        CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")

    def run(self):
        self.app.mainloop()

    def add_state(self):
        # Add the current state to state_snapshots
        current_state = self.CodeTextBox.get(1.0, END)
        self.state_snapshots.append(current_state)
        # Clear the redo_snapshots when a new state is added
        self.redo_snapshots = []

    def undo(self):
        # Check if there are states to undo to
        if len(self.state_snapshots) > 1:
            # Get the last state from state_snapshots and update the text widget
            current_state = self.state_snapshots.pop()
            target_state = self.state_snapshots[-1]
            self.redo_snapshots.append(current_state)
            self.CodeTextBox.delete(1.0, END)
            self.CodeTextBox.insert(END, target_state)

    def redo(self):
        # Check if there are states to redo to
        if self.redo_snapshots:
            # Get the last state from redo_snapshots and update the text widget
            target_state = self.redo_snapshots.pop()
            self.state_snapshots.append(target_state)
            self.CodeTextBox.delete(1.0, END)
            self.CodeTextBox.insert(END, target_state)

    def update_history(self, event):
        # Capture XML content after each edit and add it to history
        current_state = self.CodeTextBox.get(1.0, END)
        self.history.append(current_state)

    def UploadAction(self):
        filetypes = (
            ('text files', '*.xml'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(filetypes=filetypes)
        self.filename = filename

    def file_save(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".xml")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        text2save = str(self.CodeTextBox.get(1.0, END))  # starts from `1.0`, not `0.0`
        f.write(text2save)
        f.close()

    def update_line_numbers(self):
        # Get the current number of lines in the code Text widget
        total_lines1 = int(self.CodeTextBox.index('end-1c').split('.')[0])

        # Update the line numbers in the line_numbers Text widget
        self.line_numbers1.configure(state='normal')
        self.line_numbers1.delete('1.0', 'end')
        for line in range(1, total_lines1 + 1):
            self.line_numbers1.insert('end', str(line) + '\n')
        self.line_numbers1.configure(state='disabled')
        self.line_numbers1.yview(END)



if __name__ == "__main__":
    app = SocialConnectXApp()
    app.run()
