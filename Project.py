import customtkinter
import Main
import Save

Load_Project = []
button_list = []
Project_App = customtkinter.CTk()
Start_Y = 85
font = customtkinter.CTkFont(family="MV-crooker", size=26)
Color_Base = "#2E8B57"
Color_Haver = "#006400"

class Project_viewer:
    def __init__(self, Name, Index, color, text, master, x, y, xpos, ypos, Button_x, Button_y, Button_pos_x, Button_pos_y, Text_Posx, Text_Posy, Text_x, Text_y, x_pos, y_pos, Text_Delite):
        self.label = customtkinter.CTkLabel(master=master, text=" ", width=x, height=y, bg_color=color)
        self.label.place(x=xpos, y=ypos)
        self.Text = customtkinter.CTkLabel(master=master, text=f"{Index} -  {Name}", bg_color=color, font=font, width=Text_x, height=Text_y)
        self.Text.place(x=Text_Posx, y=Text_Posy + 18)
        def Open_Project():
            Main.Name_Project = Name
            Main.Project_index = Index
            Main.Project_Main()
        #!def Delite_Project_index():!
        self.Button = customtkinter.CTkButton(master=master, text=text, font=font, width=Button_x, height=Button_y, bg_color= color, fg_color=Color_Base, hover_color=Color_Haver, command=Open_Project)
        self.Button.place(x=Button_pos_x, y=Button_pos_y)

class Button_UI():
    def __init__(self, master, text, font, height, wight, comand, x_pos, y_pos):
        self.Button = customtkinter.CTkButton(master=master, text=text, font=font, fg_color=Color_Base, hover_color=Color_Haver, width=height, height=wight, command=comand)
        self.Button.place(x=x_pos, y=y_pos)

def New_Project_Input_Name():
    Name_Input = customtkinter.CTkInputDialog(text="Name Project", font=font, button_fg_color=Color_Base, button_hover_color=Color_Haver, title="Input Name Project")
    Save_name = Name_Input.get_input()
    if Save_name != "" and (Save_name is not Save.Name_list):
        Save_index = (len(button_list) + 1)
        Save.Save(Save_name, Save_index)
        Project_App.destroy()
    else:
        New_Project_Input_Name()

def Project_View():
    Save.load_Save()
    Project_App.geometry("1500x800")
    Project_App.title("Project Menu")
    for i in range(len(Save.Name_list) // 2):
        button_name = f"Project_viewer_{i}"
        button = Project_viewer(f"{Save.Name_list[i]}", f"{Save.Index_list[i]}", "#323232", "Open", Project_App, 1440, 75, 35, Start_Y + i * 100, 75, 35, 1370, (Start_Y + i * 100) + 16, 45, (Start_Y + i * 100), 45, 35, 1140, (Start_Y + i * 100 + 16), "Dilite Project")
        globals()[button_name] = button
        button_list.append(button)
    Button_Delite_all = Button_UI(Project_App, "Delite all project", font, 35, 45, Delite_all_Project, 1020, 10)
    Button_New_Project = Button_UI(Project_App, "New project", font, 35, 45, New_Project_Input_Name, 1300, 10)
    Project_App.mainloop()

def Delite_all_Project():
    button_list.clear()
    Save.File_delite_All()
    Save.Name_list.clear()
    Project_App.destroy()

Project_View()
