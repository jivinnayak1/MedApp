from tkinter import *

window = Tk()
window.geometry("400x400")
window.config(bg="lightblue")
window.title("Medical Care app")

welcome = Label(window,text="Welcome to MedCare",font=("Alice",15,"bold"),bg="lightblue",fg="black")
welcome.pack(side="top")

Name_Text = Label(window,text="Enter the Patient's Name",font=("Alice",11,"bold"),bg="lightblue",fg="black")
Name_Text.pack()

Name_Input = Entry(window,font=("Alice",11,"bold"))
Name_Input.pack()

Age_Text = Label(window,text="Enter the Patient's Age",font=("Alice",11,"bold"),bg="lightblue",fg="black")
Age_Text.pack()

Age_Input = Entry(window,font=("Alice",11,"bold"))
Age_Input.pack()

Issue_Text = Label(window,text="Please State the Issue",font=("Alice",11,"bold"),bg="lightblue",fg="black")
Issue_Text.pack()

Issue_Input = Entry(window,font=("Alice",11,"bold"))
Issue_Input.pack()

Doctor_Label = Label(window,text="Select Your Doctor",font=("Alice",11,"bold"),bg="lightblue",fg="black")
Doctor_Label.pack()

Doc_List = ["Dr.Jay","Dr.Lee","Dr.Jyoti","Dr.Subhadeep","Dr.Jivin","Dr.Arjun"]
Selected_Doctor = StringVar()
Selected_Doctor.set(Doc_List[0])

Doc_Menu = OptionMenu(window,Selected_Doctor,*Doc_List)
Doc_Menu.pack()

Time_Label = Label(window,text="Select Your Time Slot",font=("Alice",11,"bold"),bg="lightblue",fg="black")
Time_Label.pack()

Time_List = ["2pm","3pm","4pm","5pm","6pm","7pm","8pm","9pm","11pm","12am","1am"]
Selected_Time = StringVar()
Selected_Time.set(Time_List[0])

Time_Menu = OptionMenu(window,Selected_Time,*Time_List)
Time_Menu.pack()

def ConfirmBooking():
    p_name = Name_Input.get()
    s_doctor = Selected_Doctor.get()
    s_time = Selected_Time.get()
    Confirm_Label.config(text=f"Consultation Booked Succesfully.\nDoctor Name: {s_doctor}\nPatient Name:{p_name}\nTime:{s_time}")

Confirm = Button(window,text="Confirm Booking",font=("Alice",10,"bold"),bg="blue",fg="black",command=ConfirmBooking)
Confirm.pack(padx=10,pady=5)

Confirm_Label = Label(window,font=("Alice",10,"bold"),bg="lightblue",fg="black")
Confirm_Label.pack()
window.mainloop()