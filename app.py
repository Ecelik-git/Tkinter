from tkinter import *
main = Tk()
main.title("Track Monthly Flu Patients")
main.geometry("800x800")
main.configure(bg="light blue")
nameLabel = Label(main, text="Clinic Name", bg="light blue").grid(row=1, column=0, sticky="w")
addressLabel = Label(main, text="Clinic Address", bg="light blue").grid(row=2, column=0, sticky="w")
phoneLabel = Label(main, text="Clinic Phne Number", bg="light blue").grid(row=3, column=0, sticky="w")
nameText = Entry(main, bg="light blue").grid(row=1, column=1, sticky="w")
addressText = Entry(main, bg="light blue").grid(row=2, column=1, sticky="w")
phoneText = Entry(main, bg="light blue").grid(row=3, column=1, sticky="w")
'''background_image = PhotoImage(file='download.jpeg')
background_label = Label(main, image=background_image)
background_label.place(relwidth=1, relheight=1)'''
titleLabel = Label(main, text="YOU CAN ENTER THE NUMBER OF PATIENT OF EACH MONTH", bg="light blue").grid(row=0, column=0, sticky="n")
spinLabel = Label(main, text="Choose Month", bg="light blue").grid(row=5, column=0, sticky="w")
spin = Spinbox(values=('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))
spin.grid(row=6, column=0, sticky="w")
textLabel = Label(main, text="Enter the amount", bg="light blue").grid(row=5, column=1, sticky="w")
textBox = Entry(main)
textBox.grid(row=6, column=1, sticky="w")
amount_list = []
month_list = []
def getInput():
    ay = spin.get()
    amount = int(textBox.get())
    amount_list.append(amount)
    month_list.append(ay)
    print(month_list, amount_list)
    textBox.delete(0, END)
def addition():
    return sum(amount_list)
from statistics import mean
def average():
    return mean(amount_list)
AddButton = Button(main, text="ADD", fg="green", font="bold", bg="yellow", command=getInput)
AddButton.grid(row=7, column=0, sticky="w")
sumLabel = Label(main, text="SUM:", bg="orange")
sumLabel.grid(row=9, column=0, sticky="w")
averageLabel = Label(main, text="AVERAGE:", bg="orange")
averageLabel.grid(row=9, column=1, sticky="w")
def press():
    sumLabel.config(text="SUM: " + str(addition()))
    averageLabel.config(text="AVERAGE: " + str(float(average())))
    r=12
    b= 0
    for i in month_list:
        Label(text=i, bg="light blue").grid(row=r, column=0, sticky="w")
        Label(text=str(amount_list[b]), bg="light blue").grid(row=r, column=1, sticky="w")
        r = r + 1
        b = b + 1
    month = np.array (month_list)
    amount = np.array (amount_list)
    #amount_1= np.array (amount_list)

    fig = Figure(figsize=(6, 6))
    a = fig.add_subplot(111)
    a.scatter(amount,month,color='red')
    #a.plot(amount, color='blue')
    a.invert_yaxis()

    a.set_title ("Monthly Entry", fontsize=16)
    a.set_ylabel("months", fontsize=12)
    a.set_xlabel("number of patients", fontsize=14)

    canvas = FigureCanvasTkAgg(fig, master=main)
    canvas.get_tk_widget().grid(row=r, column=0, sticky="e")
    canvas.draw()
DisplayButton = Button(main, text="Display Data", fg="green", font="bold", bg="yellow", command=press)
DisplayButton.grid(row=7, column=1, sticky="w")
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
#graphButton = Button(main, text="GRAPH", command=plot).grid(row=3, column=2)
show_All_Data = Label(main, text="Below you can see all the data entered", bg="light blue")
show_All_Data.grid(row=10, column=0, sticky="e")
show_data = Label(main, text="by the users", bg="light blue")
show_data.grid(row=10, column=1, sticky="w")
def delete():
    r=12
    items = '                                                 '
    for i in month_list:
        list = Label(text=items, bg="light blue")
        list.grid(row=r, column=0, sticky="w")
        value = Label(text=items, bg="light blue")
        value.grid(row=r, column=1, sticky="w")
        r = r + 1
    sumLabel.config(text="SUM: ")
    averageLabel.config(text="AVERAGE: ")
    del amount_list[:]
    del month_list[:]
    #canvas.delete("fig")
ResetButton = Button(main, text="Reset Data", fg="green", font="bold", bg="yellow", command=delete)
ResetButton.grid(row=8, column=1, sticky="w")
main.mainloop()
