from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
root=Tk()
root.geometry("900x500")

Burger = ImageTk.PhotoImage(Image.open("burger1.png "))
burger = Label(root)
burger["image"]=Burger
burger.place(relx=0.7,rely=0.5,anchor=CENTER)

Title=Label(root,text="Borgor Master",font=("times",40,"bold"),fg="Orange")
Title.place(relx=0.22,rely=0.1,anchor=CENTER)

Dish_label=Label(root,text="Select Dish:")
Dish_label.place(relx=0.06,rely=0.2,anchor=CENTER)

dish=["borgor","chugjug","candice cookie"]
dish_select=ttk.Combobox(root,state="readonly",values=dish)
dish_select.place(relx=0.25,rely=0.2,anchor=CENTER)

Toppings_label=Label(root,text="Select Toppings:")
Toppings_label.place(relx=0.08,rely=0.5,anchor=CENTER)

toppings=[]
toppings_select=ttk.Combobox(root,state="readonly",values=toppings)
toppings_select.place(relx=0.25,rely=0.5,anchor=CENTER)

cost_L=Label(root,font=("times",15,"bold"))
cost_L.place(relx=0.2,rely=0.75,anchor=CENTER)

class parent():
    def __init__(self):
        print("uwu making order")
    def menu(dish):
        if dish=="borgor":
            toppings=["nugget","ketchey","sussy meal"]
            toppings_select["values"]=toppings
        elif dish=="chugjug":
            toppings=["mini","fortnitebunger","mega"]
            toppings_select["values"]=toppings
        elif dish=="candice cookie":
            toppings=["chonky","stonky","bonky"]
            toppings_select["values"]=toppings
        else:
            print("enter a dish dum")
    def final_amount(dish,toppings):
        cost=0
        if dish=="borgor":
            cost=cost+10
        if dish=="chugjug":
            cost=cost+15
        if dish=="candice cookie":
            cost=cost+5
        if toppings=="nugget":
            cost=cost+2
        if toppings=="ketchey":
            cost=cost+1
        if toppings=="sussy meal":
            cost=cost+3
        if toppings=="fortnitebunger":
            cost=cost+4
        if toppings=="mega":
            cost=cost+5
        if toppings=="chonky":
            cost=cost+1
        if toppings=="stonky":
            cost=cost+1
        if toppings=="bonky":
            cost=cost+1
        if toppings=="mini":
            cost=cost+3
        cost_L["text"]="this dish will cost you $"+str(cost)
class child1(parent):
    def __init__(self,dish):
        self.new_dish=dish
    def get_menu():
        new_dish=dish_select.get()
        parent.menu(new_dish)
class child2(parent):
    def __init__(self,dish,addons):
        self.new_dish=dish
        self.new_addons=addons
    def get_cost():
        new_dish=dish_select.get()
        addons=toppings_select.get()
        parent.final_amount(new_dish,addons)
child1 = Button(root,text="menu",command=child1.get_menu)
child1.place(relx=0.06,rely=0.3,anchor=CENTER)
child2 = Button(root,text="order",command=child2.get_cost)
child2.place(relx=0.04,rely=0.6,anchor=CENTER)
root.mainloop()