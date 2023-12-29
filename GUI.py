from customtkinter import *
from CTkMessagebox import CTkMessagebox

class SocialConnectXApp:
    def __init__(self):
        self.app = CTk()
        self.app.minsize(1160, 900)
        self.app.maxsize(1160, 900)
        self.app.title("SocialConnectX")

        # Frames
        self.frameTop = CTkFrame(master=self.app, width=900, height=100, border_width=2, border_color='white', fg_color='transparent')
        self.frameMiddle = CTkFrame(master=self.app, width=900, height=500, border_width=2, border_color='white', fg_color='transparent')
        self.frameBottom = CTkFrame(master=self.app, width=900, height=200, border_width=2, border_color='white', fg_color='transparent')
        self.frameBottom2 = CTkFrame(master=self.app, width=900, height=200, border_width=2, border_color='white', fg_color='transparent')

        self.frameTop.grid(row=0, column=0, sticky="nsew")
        self.frameMiddle.grid(row=1, column=0, sticky="nsew")
        self.frameBottom.grid(row=2, column=0, sticky="nsew")
        self.frameBottom2.grid(row=3, column=0, sticky="nsew")

        # Buttons and Labels
        self.create_top_buttons()
        self.create_bottom_buttons()
        self.create_middle_textboxes()
        self.CodeTextBox = CTkTextbox(master=self.frameMiddle, width=500, height=500, border_width=2, border_color='black', font=("Courier New", 14))
        self.CodeTextBox.grid(row=1, column=1, sticky="nsew", padx=20, pady=8)  # CodeTextBox is a class variable
        self.line_numbers1 = CTkTextbox(master=self.frameMiddle, width=12, height=5, bg_color= 'lightgray', state='disabled',font=("Courier New", 12))
        self.line_numbers1.grid(row=1, column=0, sticky='nsew',pady=8)
        self.update_line_numbers()
        # To DO tomorrow 
        self.CodeTextBox.bind('<KeyRelease>', lambda event: self.update_line_numbers())
        line_numbers_scrollbar = CTkScrollbar(master=self.line_numbers1, command=self.line_numbers1.yview,minimum_pixel_length=2)
        line_numbers_scrollbar.grid(row=0, column=1, sticky='nsew')
        self.line_numbers1.configure(yscrollcommand=line_numbers_scrollbar.set)
        # Initialize history list to store XML content after each edit
        self.history = []
        self.state_snapshots = []
        self.redo_snapshots = []
        self.add_state()
        # Set up event binding for keyboard actions
        self.CodeTextBox.bind("<Key>", self.update_history)
        self.filename = None
        
    def create_top_buttons(self):
        SaveButton = CTkButton(master=self.frameTop, text="Save", width=70, height=40, border_width=2, border_color='black', font=('Helvetica', 18),command=self.add_state)
        UndoButton = CTkButton(master=self.frameTop, text="Undo", width=70, height=40, border_width=2, border_color='black', font=('Helvetica', 18),command=self.undo)
        RedoButton = CTkButton(master=self.frameTop, text="Redo", width=70, height=40, border_width=2, border_color='black', font=('Helvetica', 18),command=self.redo)
        ImportButton = CTkButton(master=self.frameTop, text="Import", width=70, height=40, border_width=2, border_color='black', font=('Helvetica', 18),command= self.UploadAction)
        ExportButton = CTkButton(master=self.frameTop, text="Export", width=70, height=40, border_width=2, border_color='black', font=('Helvetica', 18),command=self.file_save)
        ProgramName = CTkLabel(master=self.frameTop, text="SocialConnectX", width=70, height=40, font=('Helvetica', 22, 'bold'))

        ImportButton.pack(side="left", padx=10, pady=15)
        ExportButton.pack(side="left", padx=10, pady=15)
        UndoButton.pack(side="right", padx=10, pady=15)
        RedoButton.pack(side="right", padx=10, pady=15)
        SaveButton.pack(side="right", padx=10, pady=15)
        ProgramName.pack(side="right", anchor='center', padx=190, pady=15)

    def create_bottom_buttons(self):
       OptionName = CTkLabel(master=self.frameBottom, text="Options", width=70, height=1, font=('Helvetica', 18, 'bold'))
       ParseButton = CTkButton(master=self.frameBottom, text="Parse", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
       Check_and_FixButton = CTkButton(master=self.frameBottom, text="Check and Fix", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18),command=self.show_error)
       Xml_TO_JSONButton = CTkButton(master=self.frameBottom, text="Xml TO JSON", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
       CompressButton = CTkButton(master=self.frameBottom, text="Compresse", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
       DecompressButton = CTkButton(master=self.frameBottom, text="Decompress", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
       PrettifyButton = CTkButton(master=self.frameBottom2, text="Prettify", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
       MinifyButton = CTkButton(master=self.frameBottom2, text="Minify", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
       Show_GraphButton = CTkButton(master=self.frameBottom2, text="Show Graph", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
       Graph_analysisButton = CTkButton(master=self.frameBottom2, text="Graph analysis", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
       Post_SearchButton = CTkButton(master=self.frameBottom2, text="Post Search", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))

       OptionName.grid(row=1, column=3, sticky="nsew", padx=50, pady=5)
       ParseButton.grid(row=2, column=1, sticky="nsew", padx=50, pady=15)
       Check_and_FixButton.grid(row=2, column=2, sticky="nsew", padx=50, pady=15)
       Xml_TO_JSONButton.grid(row=2, column=3, sticky="nsew", padx=50, pady=15)
       CompressButton.grid(row=2, column=4, sticky="nsew", padx=50, pady=15)
       DecompressButton.grid(row=2, column=5, sticky="nsew", padx=50, pady=15)
       PrettifyButton.grid(row=3, column=1, sticky="nsew", padx=50, pady=15)
       MinifyButton.grid(row=3, column=2, sticky="nsew", padx=50, pady=15)
       Show_GraphButton.grid(row=3, column=3, sticky="nsew", padx=50, pady=15)
       Graph_analysisButton.grid(row=3, column=4, sticky="nsew", padx=50, pady=15)
       Post_SearchButton.grid(row=3, column=5, sticky="nsew", padx=50, pady=15)

    def create_middle_textboxes(self):
        CodeName = CTkLabel(master=self.frameMiddle, text="Xml Code", width=70, height=1,font=('Helvetica', 18, 'bold'))
        OutputName = CTkLabel(master=self.frameMiddle, text="Output", width=70, height=1,font=('Helvetica', 18, 'bold'))
        outputTextBox = CTkTextbox(master=self.frameMiddle, width=500, height=500, border_width=2, border_color='black', font=("Courier New", 14), state="disabled")
        # To DO tomorrow 
        line_numbers2 = CTkTextbox(master=self.frameMiddle, width=4, height=20,bg_color= 'lightgray', state='disabled')
        line_numbers2.grid(row=1, column=2, sticky='nsew')
        line_numbers_scrollbar2 = CTkScrollbar(master=line_numbers2, command=line_numbers2.yview,minimum_pixel_length=2)
        line_numbers_scrollbar2.grid(row=0, column=1, sticky='nsew')
        line_numbers2.configure(yscrollcommand=line_numbers_scrollbar2.set)
        # self.CodeTextBox.bind('<KeyRelease>', lambda event: self.update_line_numbers(line_numbers2, outputTextBox))
        CodeName.grid(row=0, column=1, sticky="nsew", padx=20, pady=2)
        OutputName.grid(row=0, column=3, sticky="nsew", padx=20, pady=2)
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
            self.CodeTextBox.delete(1.0,END)
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
        filename = filedialog.askopenfilename(filetypes =filetypes )
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


if __name__ == "__main__":
    app = SocialConnectXApp()
    app.run()
