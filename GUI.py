from customtkinter import *
from PIL import Image

app = CTk()
app.minsize(1080, 745)
app.maxsize(1080, 745)
app.title("SocialConnectX")


frameTop = CTkFrame(master=app, width=827, height=100, border_width=2, border_color='white', fg_color='transparent')
framemiddle = CTkFrame(master=app, width=827, height=500, border_width=2, border_color='white', fg_color='transparent')
frameBottom = CTkFrame(master=app, width=827, height=200, border_width=2, border_color='white', fg_color='transparent')
frameBottom2 = CTkFrame(master=app, width=827, height=200, border_width=2, border_color='white', fg_color='transparent')

frameTop.grid(row=0, column=0, sticky="nsew")
framemiddle.grid(row=1, column=0, sticky="nsew")
frameBottom.grid(row=2, column=0, sticky="nsew")
frameBottom2.grid(row=3, column=0, sticky="nsew")

SaveButton = CTkButton(master=frameTop, text="Save", width=70, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
UndoButton = CTkButton(master=frameTop, text="Undo", width=70, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
RedoButton = CTkButton(master=frameTop, text="Redo", width=70, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
ImportButton = CTkButton(master=frameTop, text="Import", width=70, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
ExportButton = CTkButton(master=frameTop, text="Export", width=70, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
ProgramName = CTkLabel(master=frameTop, text="SocialConnectX", width=70, height=40, font=('Helvetica', 22, 'bold'))

ImportButton.pack(side="left", padx=10, pady=15)
ExportButton.pack(side="left", padx=10, pady=15)
UndoButton.pack(side="right", padx=10, pady=15)
RedoButton.pack(side="right", padx=10, pady=15)
SaveButton.pack(side="right", padx=10, pady=15)
ProgramName.pack(side="right", anchor='center', padx=190, pady=15)

ParseButton = CTkButton(master=frameBottom, text="Parse", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
Check_and_FixButton = CTkButton(master=frameBottom, text="Check and Fix", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
Xml_TO_JSONButton = CTkButton(master=frameBottom, text="Xml TO JSON", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
CompressButton = CTkButton(master=frameBottom, text="Compresse", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
decompressButton = CTkButton(master=frameBottom, text="Decompress", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
prettifyButton = CTkButton(master=frameBottom2, text="Prettify", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
MinifyButton = CTkButton(master=frameBottom2, text="Minify", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
Show_GraphButton = CTkButton(master=frameBottom2, text="Show Graph", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
Graph_analysisButton = CTkButton(master=frameBottom2, text="Graph analysis", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))
Post_SearchButton = CTkButton(master=frameBottom2, text="Post Search", width=130, height=40, border_width=2, border_color='black', font=('Helvetica', 18))

ParseButton.grid(row=2, column=0, sticky="nsew", padx=40, pady=15)
Check_and_FixButton.grid(row=2, column=1, sticky="nsew", padx=40, pady=15)
Xml_TO_JSONButton.grid(row=2, column=2, sticky="nsew", padx=40, pady=15)
CompressButton.grid(row=2, column=3, sticky="nsew", padx=40, pady=15)
decompressButton.grid(row=2, column=4, sticky="nsew", padx=40, pady=15)
prettifyButton.grid(row=3, column=0, sticky="nsew", padx=40, pady=15)
MinifyButton.grid(row=3, column=1, sticky="nsew", padx=40, pady=15)
Show_GraphButton.grid(row=3, column=2, sticky="nsew", padx=40, pady=15)
Graph_analysisButton.grid(row=3, column=3, sticky="nsew", padx=40, pady=15)
Post_SearchButton.grid(row=3, column=4, sticky="nsew", padx=40, pady=15)

CodeTextBox = CTkTextbox(master=framemiddle, width=500, height=500, border_width=2, border_color='black', font=('Helvetica', 18))
outputTextBox = CTkTextbox(master=framemiddle, width=500, height=500, border_width=2, border_color='black', font=('Helvetica', 18))

CodeTextBox.grid(row=0, column=0, sticky="nsew", padx=20, pady=15)
outputTextBox.grid(row=0, column=1, sticky="nsew", padx=20, pady=15)

app.mainloop()
