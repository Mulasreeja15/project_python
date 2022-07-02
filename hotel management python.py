
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import requests
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog

global bill_str
bill_str = str()
 # ====================== Total Button Code =============
def total_bills():

        # ============ Drinks Items Price ================
        lassi_price = 50
        coffee_price = 20
        tea_price = 10
        juice_price = 30
        shakes_price = 50
        milk_price = 20
        shikanji_price = 15
        redbull_price = 150
        # ================ Food Items Price =================
        roti_price = 5
        dal_makhni_price = 120
        mutter_panner_price = 150
        paratha_price = 40
        mix_veg_price = 70
        omelete_price = 20
        veg_biriyani_price = 120
        rice_price = 50


        # ============Drinks Item quantity =============
        lassi_q = lassi_qty.get()
        coffee_q = coffee_qty.get()
        tea_q = tea_qty.get()
        juice_q = juice_qty.get()
        shakes_q = shakes_qty.get()
        milk_q = milk_qty.get()
        shikanji_q = shikanji_qty.get()
        redbull_q = redbull_qty.get()

        # ===========Food Items quanity ================
        roti_q = roti_qty.get()
        dal_makhni_q = dal_makhni_qty.get()
        mutter_panner_q = mutter_panner_qty.get()
        paratha_q = paratha_qty.get()
        mix_veg_q = mix_veg_qty.get()
        omelete_q = omlete_qty.get()
        veg_biriyani_q = veg_biryani_qty.get()
        rice_q = rice_qty.get()


# ================ Drinks Items Validation =================#
        if lassi_var.get() == 0:
                lassi_q = 0
        elif lassi_var.get() == 1 and lassi_qty.get()== "":
                messagebox.showerror("error","please fill the lassi quantity")
                lassi_q = 0 

        if coffee_var.get() == 0:
                coffee_q = 0
        elif coffee_var.get() == 1 and coffee_qty.get()== "":
                messagebox.showerror("error","please fill the coffee quantity")
                coffee_q = 0    

        if tea_var.get() == 0:
                tea_q = 0
        elif tea_var.get() == 1 and tea_qty.get()== "":
                messagebox.showerror("error","please fill the tea quantity")
                tea_q = 0 

        if juice_var.get() == 0:
                juice_q = 0
        elif juice_var.get() == 1 and juice_qty.get()== "":
                messagebox.showerror("error","please fill the juice quantity")
                juice_q = 0        

        if shakes_var.get() == 0:
                shakes_q = 0
        elif shakes_var.get() == 1 and shakes_qty.get()== "":
                messagebox.showerror("error","please fill the shakes quantity")
                shakes_q = 0 

        if milk_var.get() == 0:
                milk_q = 0
        elif milk_var.get() == 1 and milk_qty.get()== "":
                messagebox.showerror("error","please fill the milk quantity")
                milk_q = 0                              

        if shikanji_var.get() == 0:
                shikanji_q = 0
        elif shikanji_var.get() == 1 and shikanji_qty.get()== "":
                messagebox.showerror("error","please fill the shikanji quantity")
                shikanji_q = 0       

        if redbull_var.get() == 0:
                redbull_q = 0
        elif redbull_var.get() == 1 and redbull_qty.get()== "":
                messagebox.showerror("error","please fill the redbull quantity")
                redbull_q = 0    


        # ====== Food Items Validation ============
        if roti_var.get() == 0:  
                roti_q = 0
        elif roti_var.get() == 1 and roti_qty.get() == "":
                messagebox.showerror("erroe","please fill the roti quantity")
                roti_q = 0

        if dal_makhni_var.get() == 0:  
                dal_makhni_q = 0
        elif dal_makhni_var.get() == 1 and dal_makhni_qty.get() == "":
                messagebox.showerror("erroe","please fill the dal makhni quantity")
                dal_makhni_q = 0      

        if mutter_panner_var.get() == 0:  
                mutter_panner_q = 0
        elif mutter_panner_var.get() == 1 and mutter_panner_qty.get() == "":
                messagebox.showerror("erroe","please fill the mutter panner quantity")
                mutter_panner_q = 0    

        if paratha_var.get() == 0:  
                paratha_q = 0
        elif paratha_var.get() == 1 and paratha_qty.get() == "":
                messagebox.showerror("erroe","please fill the paratha quantity")
                paratha_q = 0   

        if mix_veg_var.get() == 0:  
                mix_veg_q = 0
        elif mix_veg_var.get() == 1 and mix_veg_qty.get() == "":
                messagebox.showerror("erroe","please fill the mix veg quantity")
                mix_veg_q = 0  

        if omlete_var.get() == 0:  
                omelete_q = 0
        elif omlete_var.get() == 1 and omlete_qty.get() == "":
                messagebox.showerror("erroe","please fill the omelete quantity")
                omelete_q = 0       

        if veg_biryani_var.get() == 0:  
                veg_biriyani_q = 0
        elif veg_biryani_var.get() == 1 and veg_biryani_qty.get() == "":
                messagebox.showerror("erroe","please fill the veg biriyani quantity")
                veg_biriyani_q = 0             

        if rice_var.get() == 0:  
                rice_q = 0
        elif rice_var.get() == 1 and rice_qty.get() == "":
                messagebox.showerror("erroe","please fill the rice quantity")
                rice_q = 0      


        # =============== Total Drinks Items Price ==============
        total_lassi_price = lassi_price * int(lassi_q)
        total_coffee_price = coffee_price * int(coffee_q)
        total_tea_price = tea_price * int(tea_q)
        total_juice_price = juice_price * int(juice_q)
        total_shakes_price = shakes_price * int(shakes_q)
        total_milk_price = milk_price * int(milk_q)
        total_shikanji_price = shikanji_price * int(shikanji_q)
        total_redbull_price = redbull_price * int(redbull_q)
        total_roti_price = roti_price * int(roti_q)
        total_dal_makhni_price = dal_makhni_price * int(dal_makhni_q)
        total_mutter_panner_price = mutter_panner_price * int(mutter_panner_q)
        total_paratha_price = paratha_price * int(paratha_q)
        total_mix_veg_price = mix_veg_price * int(mix_veg_q)
        total_omlete_price = omelete_price * int(omelete_q)
        total_veg_biryani_price = veg_biriyani_price * int(veg_biriyani_q)
        total_rice_price = rice_price * int(rice_q)
        #=========================== total foods cost ============================================#
        total_foods_cost = total_roti_price + total_dal_makhni_price + total_mutter_panner_price +total_paratha_price + total_mix_veg_price + total_omlete_price + total_veg_biryani_price + total_rice_price
        total_drinks_cost = total_lassi_price + total_coffee_price + total_tea_price + total_juice_price + total_shakes_price + total_milk_price + total_shikanji_price + total_redbull_price

        if foods_cost.get() != "":
              foods_cost.delete(0,"end")
              foods_cost.insert("end",int(total_foods_cost))
        else :
              foods_cost.insert("end",int(total_foods_cost))

        if drinks_cost.get() != "":
                drinks_cost.delete(0, "end")
                drinks_cost.insert("end", total_drinks_cost)
        else:
                drinks_cost.insert("end", total_drinks_cost)

        if service_charge_cost.get() != "":
              service_charge_cost.delete(0,"end")
              service_charge_cost.insert(0,"10")
        else :
              service_charge_cost.insert(0,"10")


        fc = int(foods_cost.get())
        dc = int(drinks_cost.get())



        total_paid_tax = fc+dc
        total_paid_tax = total_paid_tax * 8/100




        
        if paid_tax_cost.get() != "":
              paid_tax_cost.delete(0,"end")
              paid_tax_cost.insert(0,total_paid_tax)
        else :
              paid_tax_cost.insert(0,total_paid_tax)

        total_sub_cost = fc+dc+int(service_charge_cost.get())

        if sub_total_cost.get() != "":
              sub_total_cost.delete(0,"end")
              sub_total_cost.insert(0,total_sub_cost)
        else :
              sub_total_cost.insert(0,total_sub_cost)

        if total_cost_cost.get() != "":
                total_cost_cost.delete(0, "end")
                total_cost_cost.insert(0, total_sub_cost + total_paid_tax)
        else:
                total_cost_cost.insert(0, total_sub_cost + total_paid_tax)



#============================================ total bill reciept ===============================================#
        date = datetime.now().date()
        if bill_details.get(1.0,"end")!="":
               bill_details.delete(1.0,"end")
               global bill_str
               bill_str = f"bill no-{random.randint(100,1000)} {date}\n\
===items(q) Amount=== \n\
Lassi({str(lassi_q)}) {str(int(lassi_q)*lassi_price)}\n\
coffee({str(coffee_q)}) {str(int(coffee_q)*coffee_price)}\n\
tea({str(tea_q)}) {str(int(tea_q)* tea_price)}\n\
juice({str(juice_q)}) {str(int(juice_q)* juice_price)}\n\
shakes({str(shakes_q)}) {str(int(shakes_q)* shakes_price)}\n\
milk({str(milk_q)}) {str(int(milk_q)* milk_price)}\n\
shikanji({str(shikanji_q)}) {str(int(shikanji_q)* shikanji_price)}\n\
redbull({str(redbull_q)}) {str(int(redbull_q)* redbull_price)}\n\
Roti({str(roti_q)}) {str(int(roti_q)*roti_price)}\n\
Dal Makhani({str(dal_makhni_q)}) {str(int(dal_makhni_q)*dal_makhni_price)}\n\
Mutter Panner({str(mutter_panner_q)}) {str(int(mutter_panner_q)*mutter_panner_price)}\n\
Paratha({str(paratha_q)}) {str(int(paratha_q)*paratha_price)}\n\
Mix Veg({str(mix_veg_q)}) {str(int(mix_veg_q)*mix_veg_price)}\n\
Omlete({str(omelete_q)}) {str(int(omelete_q)*omelete_price)}\n\
Veg Biryani({str(veg_biriyani_q)}) {str(int(veg_biriyani_q)*veg_biriyani_price)}\n\
Rice({str(rice_q)}) {str(int(rice_q)*rice_price)}\n\
-----------------------\n\
COST OF FOOD : {str(fc+dc)}\n\
SERVICE COST : {str(10)}\n\
TAX : {str(total_paid_tax)}\n\
-----------------------\n\
TOTAL BILL : {str(total_sub_cost + total_paid_tax)}"
               bill_details.insert(
                       1.0, bill_str)
                       


#===========================end ========================

def save():
        root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
        if root.filename is None:
                   return
        file_save = str(bill_details.get(1.0,END))
        root.filename.write(file_save)
        root.filename.close()

        #==================== end =======================#

        
#========================================= drinks checkbutton validation ==========================#

def lassi_chk():
        if lassi_var.get()== 1:
                lassi_qty['state']="normal"
                lassi_qty ['bg'] = '#00ff00'
                lassi_qty['fg'] = "white"
        else:
                lassi_qty['state'] = "disabled"


def coffee_chk():
        if coffee_var.get()== 1:
                coffee_qty['state']="normal"
                coffee_qty ['bg'] = '#00ff00'
                coffee_qty['fg'] = "white"
        else:
                coffee_qty['state'] = "disabled"

def tea_chk():
        if tea_var.get()== 1:
                tea_qty['state']="normal"
                tea_qty ['bg'] = '#00ff00'
                tea_qty['fg'] = "white"
        else:
                tea_qty['state'] = "disabled"

def juice_chk():
        if juice_var.get()== 1:
                juice_qty['state']="normal"
                juice_qty ['bg'] = '#00ff00'
                juice_qty['fg'] = "white"
        else:
                juice_qty['state'] = "disabled"


def shakes_chk():
        if shakes_var.get()== 1:
                shakes_qty['state']="normal"
                shakes_qty ['bg'] = '#00ff00'
                shakes_qty['fg'] = "white"
        else:
                shakes_qty['state'] = "disabled"


def milk_chk():
        if milk_var.get()== 1:
                milk_qty['state']="normal"
                milk_qty ['bg'] = '#00ff00'
                milk_qty['fg'] = "white"
        else:
                milk_qty['state'] = "disabled"


def shikanji_chk():
        if shikanji_var.get()== 1:
                shikanji_qty['state']="normal"
                shikanji_qty ['bg'] = '#00ff00'
                shikanji_qty['fg'] = "white"
        else:
                shikanji_qty['state'] = "disabled"

def redbull_chk():
        if redbull_var.get()== 1:
                redbull_qty['state']="normal"
                redbull_qty ['bg'] = '#00ff00'
                redbull_qty['fg'] = "white"
        else:
                redbull_qty['state'] = "disabled"


                #=======================end====================3
#=========================== foods checkbutton validation=============================#


def roti_chk():
        if roti_var.get()== 1:
                roti_qty['state']="normal"
                roti_qty ['bg'] = '#00ff00'
                roti_qty['fg'] = "white"
        else:
                roti_qty['state'] = "disabled"

def dal_makhni_chk():
        if dal_makhni_var.get()== 1:
                dal_makhni_qty['state']="normal"
                dal_makhni_qty ['bg'] = '#00ff00'
                dal_makhni_qty['fg'] = "white"
        else:
                dal_makhni_qty['state'] = "disabled"
                
def mutter_panner_chk():
        if mutter_panner_var.get()== 1:
                mutter_panner_qty['state']="normal"
                mutter_panner_qty ['bg'] = '#00ff00'
                mutter_panner_qty['fg'] = "white"
        else:
                mutter_panner_qty['state'] = "disabled"


def paratha_chk():
        if paratha_var.get()== 1:
                paratha_qty['state']="normal"
                paratha_qty ['bg'] = '#00ff00'
                paratha_qty['fg'] = "white"
        else:
                paratha_qty['state'] = "disabled"


def mix_veg_chk():
        if mix_veg_var.get()== 1:
                mix_veg_qty['state']="normal"
                mix_veg_qty ['bg'] = '#00ff00'
                mix_veg_qty['fg'] = "white"
        else:
                mix_veg_qty['state'] = "disabled"

def omlete_chk():
        if omlete_var.get()== 1:
                omlete_qty['state']="normal"
                omlete_qty ['bg'] = '#00ff00'
                omlete_qty['fg'] = "white"
        else:
                omlete_qty['state'] = "disabled"

def veg_biryani_chk():
        if veg_biryani_var.get()== 1:
                veg_biryani_qty['state']="normal"
                veg_biryani_qty ['bg'] = '#00ff00'
                veg_biryani_qty['fg'] = "white"
        else:
                veg_biryani_qty['state'] = "disabled"

def rice_chk():
        if rice_var.get()== 1:
                rice_qty['state']="normal"
                rice_qty ['bg'] = '#00ff00'
                rice_qty['fg'] = "white"
        else:
               rice_qty['state'] = "disabled"


#======#calculator code#=======#

def nine():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end" )
                result.insert("end","9")
        else:
                result.insert("end", "9")


def eight():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","8")

        else:
                result.insert("end","8")

def seven():
       if 'error' in result.get() or '=' in result.get():
               result.delete(0,"end")
               result.insert("end","7")

       else:
               result.insert("end","7")

def six():
    

      if 'error' in result.get() or '=' in result.get():
               result.delete(0,"end")
               result.insert("end","6")

      else:    
               result.insert("end","6")
               
def five():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end" )
                result.insert("end","5")
        else:
                result.insert("end", "5")


def four():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end" )
                result.insert("end","4")
        else:
                result.insert("end","4")

def three():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end" )
                result.insert("end","3")
        else:
                result.insert("end","3")
def two():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end" )
                result.insert("end","2")
        else:
                result.insert("end","2")
def one():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end" )
                result.insert("end","1")
        else:
                result.insert("end","1")
def zero():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end" )
                result.insert("end","0")
        else:
                result.insert("end", "0")


def plus():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","+")

        else:
                result.insert("end","+")

def minus():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end" )
                result.insert("end","-")
        else:
                result.insert("end", "-")

def mul():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","*")
        else:
                result.insert("end", "*")

def divide():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end" )
                result.insert("end","/")
        else:
                result.insert("end", "/")

def equal():
        if result.get()== "":
                result.insert("end","error")
        elif result.get()[0] == "0" or result.get()[0] == "+" or result.get()[0]:
                result.delete(0,"end")
                result.insert("end","error")
        elif 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")


        else:

                res = result.get()
                res = eval(res)
                result.insert("end","=")
                result.insert("end",res)


def clear():
        result.delete(0,"end")


def send():
        root= tk.Tk()
        root.geometry('600x800')
        root['bg']="white"


        frame4= Frame(root,width=300,height=60,relief=RIDGE,borderwidth=5,bg='#248aa2',highlightbackground="white",highlightcolor="white",highlightthickness=2)
        frame4.place(x=0,y=0)

        l2 = Label(frame4,text="Send Bill" , font=('robot',22,'bold'),bg='#248aa2',fg="#ffffff")
        l2.place(x=85,y=1)
        
        frame5= Frame(root,width=300,height=340,relief=RIDGE,borderwidth=5,bg='#248aa2',highlightbackground="white",highlightcolor="white",highlightthickness=2)
        frame5.place(x=0,y=55)

        innerframe5= Frame(root,width=285,height=325,relief=RIDGE,borderwidth=5,bg='#248aa2',highlightbackground="white",highlightcolor="white",highlightthickness=2)
        innerframe5.place(x=0,y=0)

        l3 = LabelFrame(innerframe5,text="Send Bill Through Sms" , width=270, height=310,font=('verdana',10,'bold'),fg='#248aa2',relief=RIDGE,highlightbackground="white")
        l3.place(x=2,y=2)


        l4 = Label(innerframe5,text="Phone Number" , font=('verdana',10,'bold'))
        l4.place(x=40,y=40)


        number = Entry(innerframe5,width=30,borderwidth=2)
        number.place(x=40,y=70)


        l5 = Label(innerframe5,text="Bill Details" , font=('verdana',10,'bold'))
        l5.place(x=40,y=100)

        bill_message = ScrolledText(innerframe5, width=23, height=9, borderwidth=4, relief=SUNKEN, font=('courier','9',''))
        bill_message.place(x=40,y=120)

        if bill_message.get(1.0,"end") != "":
                bill_message.delete(1.0,"end")
                bill_message.insert(1.0, bill_str)
        else:
                bill_message.insert(1.0, bill_str)


        def send_bill():
                ph_number = number.get()
                messages = bill_details.get("1.0","end-1c")


                if ph_number == "":
                        messagebox.showerror("Error",'Please fill the phone number')
                elif messages == "":
                        messagebox.showerror("Error",'Bill details is empty')
                else:
                        url = "https://www.fast2sms.com/dev/bulk"
                        api =""#go to fast2sms.com signup to get the free api
                        querystring= {"authorization":api,"sender_id":"FSTSMS","message": "NO message"}

                        headers = {
                                 'cache-control': "no-cache"
                                 }
                        requests.request("GET",url,headers=headers,params=querystring)

                        messagebox.showinfo("Send SMS",'Bill has been send to you successfully')

                root.mainloop()


        send_msg = Button(innerframe5,text="Send Bill",relief=RAISED ,borderwidth=2,font=('impact',8,'bold'),bg='#248aa2',fg="White",padx=20,command=send_bill)
        send_msg.place(x=60,y=280)


            #=============end===========#

   #===========exit button code======================#

def exit():
        message = messagebox.askquestion('Notepad', 'Do you want to exit the application' )
        if message == "yes" :
                 
                 root.destroy()
        else:

                 "return"



                #-------end------#
#==========clear button code==========#

def cleared_bill():
                     #====drinks====#
    


         lassi_qty.delete(0,'end')
         lassi.deselect()
         lassi_qty['state'] = "disabled"
         coffee_qty.delete(0,'end')
         coffee.deselect()
         coffee_qty['state'] = "disabled"
         tea_qty.delete(0,'end')
         tea.deselect()
         tea_qty['state'] = "disabled"
         juice_qty.delete(0,'end')
         juice.deselect()
         juice_qty['state'] = "disabled"
         shakes_qty.delete(0,'end')
         shakes.deselect()
         shakes_qty['state'] = "disabled"
         milk_qty.delete(0,'end')
         milk.deselect()
         milk_qty['state'] = "disabled"
         shikanji_qty.delete(0,'end')
         shikanji.deselect()
         shikanji_qty['state'] = "disabled"
         redbull_qty.delete(0,'end')
         redbull.deselect()
         redbull_qty['state'] = "disabled"



                       #==============food==========#
         roti_qty.delete(0,'end')
         roti.deselect()
         roti_qty['state'] = "disabled"
         dal_makhni_qty.delete(0,'end')
         dal_makhni.deselect()
         dal_makhni_qty['state'] = "disabled"
         mutter_panner_qty.delete(0,'end')
         mutter_panner.deselect()
         mutter_panner_qty['state'] = "disabled"
         mix_veg_qty.delete(0,'end')
         mix_veg.deselect()
         mix_veg_qty['state'] = "disabled"
         omlete_qty.delete(0,'end')
         omlete.deselect()
         omlete_qty['state'] = "disabled"
         veg_biryani_qty.delete(0,'end')
         veg_biryani.deselect()
         veg_biryani_qty['state'] = "disabled"
         rice_qty.delete(0,'end')
         rice.deselect()
         rice_qty['state'] = "disabled"


           #===========total costs======#
         drinks_cost.delete(0,'end')
         foods_cost.delete(0,'end')
         service_charge_cost.delete(0,'end')
         paid_tax_cost.delete(0,'end')
         sub_total_cost.delete(0,'end')
         total_cost_cost.delete(0,'end')
         #============Bill Details=============#

         bill_details.delete(1.0,'end')
 #======end=========#




         #============= main window code =================#

root = tk.Tk()
root.geometry("650x400")
root.maxsize(650,390)
root.minsize(650,390)
root.title("Hotel Management System")


frame = Frame(root,width=650,height=70,relief=RIDGE,borderwidth=5,bg='#248aa2')
frame.place(x=0,y=0)


l1= Label(frame,text="Hotel Management System",font=('roboto',30,'bold'),bg='#ff5733',fg ="#ffffff")
l1.place(x=10,y=4)


frame1 = Frame(root,width=650,height=700,relief=RIDGE,borderwidth=5,bg='#4933FF')
frame1.place(x=0,y=70)

innerframe1 = Frame(frame1, width=150, height=220, relief=RIDGE, borderwidth=3, bg='#248aa2')
innerframe1.place(x=0,y=0)

drinks = LabelFrame(innerframe1,text="Drinks",width=135,height=205,borderwidth=3,font=('verdana',10,'bold'),fg='#248aa2',relief=RIDGE,highlightbackground="white")
drinks.place(x=2,y=2)


lassi_var = IntVar()
lassi = Checkbutton(drinks, text="Lassi", variable=lassi_var, font=('verdana',8,'bold'), onvalue=1, offvalue=0, command=lassi_chk)
lassi.place(x=2,y=2)



lassi_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state='disabled')
lassi_qty.place(x=74,y=2)
lassi_qty.insert(0,"0")



coffee_var = IntVar()
coffee = Checkbutton(drinks,text="coffee",variable=coffee_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=coffee_chk)
coffee.place(x=2,y=22)


coffee_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state='disabled')
coffee_qty.place(x=74,y=22)


tea_var = IntVar()
tea = Checkbutton(drinks,text="tea",variable=tea_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=tea_chk)
tea.place(x=2,y=44)


tea_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state='disabled')
tea_qty.place(x=74,y=44)



juice_var = IntVar()
juice = Checkbutton(drinks,text="juice",variable=juice_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=juice_chk)
juice.place(x=2,y=66)
juice_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state='disabled')
juice_qty.place(x=74,y=66)




shakes_var = IntVar()
shakes= Checkbutton(drinks,text="shakes",variable=shakes_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=shakes_chk)
shakes.place(x=2,y=88)
shakes_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state='disabled')
shakes_qty.place(x=74,y=88)

milk_var = IntVar()
milk = Checkbutton(drinks,text="milk",variable=milk_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=milk_chk)
milk.place(x=2,y=110)
milk_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state='disabled')
milk_qty.place(x=74,y=110)

shikanji_var = IntVar()
shikanji= Checkbutton(drinks,text="shikani",variable=shikanji_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=shikanji_chk)
shikanji.place(x=2,y=132)
shikanji_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state='disabled')
shikanji_qty.place(x=74,y=132)

redbull_var = IntVar()
redbull= Checkbutton(drinks,text="redbull",variable=redbull_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=redbull_chk)
redbull.place(x=2,y=154)
redbull_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state='disabled')
redbull_qty.place(x=74,y=154)

innerframe2 = Frame(frame1,width=290,height=220,relie=RIDGE,borderwidth=3,bg='#248aa2')
innerframe2.place(x=151,y=0)


foods = LabelFrame(innerframe2,text ="Foods",width=275,height=205,borderwidth=3,font=('verdana',10,'bold'),fg='#248aa2',relief=RIDGE,highlightbackground="white")
foods.place(x=2,y=2)

              

roti_var = IntVar()
roti = Checkbutton(foods,text="roti",variable=roti_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=roti_chk)
roti.place(x=2,y=2)
roti_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state='disabled')
roti_qty.place(x=140,y=2)


dal_makhni_var = IntVar()
dal_makhni= Checkbutton(foods,text="dal_makhni",variable=dal_makhni_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=dal_makhni_chk)
dal_makhni.place(x=2,y=22)
dal_makhni_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state='disabled')
dal_makhni_qty.place(x=140,y=22)

mutter_panner_var = IntVar()
mutter_panner = Checkbutton(foods,text="mutter_panner",variable=mutter_panner_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=mutter_panner_chk)
mutter_panner.place(x=2,y=44)
mutter_panner_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state='disabled')
mutter_panner_qty.place(x=140,y=44)

paratha_var = IntVar()
paratha = Checkbutton(foods,text="paratha",variable=paratha_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=paratha_chk)
paratha.place(x=2,y=66)
paratha_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state='disabled')
paratha_qty.place(x=140,y=66)


mix_veg_var = IntVar()
mix_veg = Checkbutton(foods,text="mix_veg",variable=mix_veg_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=mix_veg_chk)
mix_veg.place(x=2,y=88)
mix_veg_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state='disabled')
mix_veg_qty.place(x=140,y=88)



omlete_var = IntVar()
omlete = Checkbutton(foods,text="omlete",variable=omlete_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=omlete_chk)
omlete.place(x=2,y=110)
omlete_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state='disabled')
omlete_qty.place(x=140,y=110)


veg_biryani_var = IntVar()
veg_biryani = Checkbutton(foods,text="veg_biryani",variable=veg_biryani_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=veg_biryani_chk)
veg_biryani.place(x=2,y=132)
veg_biryani_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state='disabled')
veg_biryani_qty.place(x=140,y=132)




rice_var = IntVar()
rice = Checkbutton(foods,text="rice",variable=rice_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=rice_chk)
rice.place(x=2,y=154)
rice_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state='disabled')
rice_qty.place(x=140,y=154)


#=====================================================================================================================================#

frame2= Frame(root,width=450,height=90,relief=RIDGE,borderwidth=5,bg='#FF3358')
frame2.place(x=0,y=300)


innerframe3 = Frame(frame2,width=440,height=80,relief=RIDGE,borderwidth=3,bg='#FF3358')
innerframe3.place(x=0,y=0)


cost_of_drinks = Label(innerframe3,text="cost of drinks",font=('verdana' ,8, 'bold'))
cost_of_drinks.place(x=2,y=2)
drinks_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
drinks_cost.place(x=130,y=0)

cost_of_foods = Label(innerframe3,text="cost of foods",font=('verdana' ,8, 'bold'))
cost_of_foods.place(x=2,y=24)
foods_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
foods_cost.place(x=130,y=22)


service_charge= Label(innerframe3,text="service charge",font=('verdana' ,8, 'bold'))
service_charge.place(x=2,y=46)
service_charge_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
service_charge_cost.place(x=130,y=44)


paid_tax = Label(innerframe3,text="paid tax ",font=('verdana' ,8, 'bold'))
paid_tax.place(x=250,y=2)
paid_tax_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
paid_tax_cost.place(x=330,y=0)

sub_total = Label(innerframe3,text="sub total",font=('verdana' ,8, 'bold'))
sub_total.place(x=250,y=24)
sub_total_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
sub_total_cost.place(x=330,y=22)



total_cost = Label(innerframe3,text="total cost",font=('verdana' ,8, 'bold'))
total_cost.place(x=250,y=46)
total_cost_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
total_cost_cost.place(x=330,y=44)




frame3 = Frame(root,width=200,height=320,relief=RIDGE,borderwidth=5)
frame3.place(x=450,y=70)



innerframe4 = Frame(root,width=200,height=320,relief=RIDGE,borderwidth=5,bg='#33FF49')
innerframe4.place(x=450,y=70)



result = Entry(innerframe4,width=28,relief=SUNKEN,borderwidth=3)
result.place(x=2,y=0)


nine= Button(innerframe4,text="9",padx=15,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=nine)
nine.place(x=0,y=24)


eight= Button(innerframe4,text="8",padx=15,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=eight)
eight.place(x=48,y=24)

seven= Button(innerframe4,text="7",padx=15,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=seven)
seven.place(x=96,y=24)


plus= Button(innerframe4,text="+",padx=6,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=plus)
plus.place(x=144,y=24)



six= Button(innerframe4,text="6",padx=15,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=six)
six.place(x=0,y=50)



five= Button(innerframe4,text="5",padx=15,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=five)
five.place(x=48,y=50)


four= Button(innerframe4,text="4",padx=15,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=four)
four.place(x=96,y=50)

minus= Button(innerframe4,text="-",padx=15,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=minus)
minus.place(x=144,y=50)


three = Button(innerframe4,text="3",padx=15,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=three)
three.place(x=0,y=76)

two= Button(innerframe4,text="2",padx=15,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=two)
two.place(x=48,y=76)


one= Button(innerframe4,text="1",padx=15,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=one)
one.place(x=96,y=76)


multiply = Button(innerframe4,text="*",padx=7,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=mul)
multiply.place(x=144,y=76)

zero= Button(innerframe4,text="0",padx=15,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=zero)
zero.place(x=0,y=102)


clear= Button(innerframe4,text="C",padx=15,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=clear)
clear.place(x=48,y=102)

equal= Button(innerframe4,text="=",padx=15,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=equal)
equal.place(x=96,y=102)


divide = Button(innerframe4,text="/",padx=7,relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white", command=divide)
divide.place(x=144,y=102)



bill_details = ScrolledText(innerframe4,width=23,height=9,relief=SUNKEN,borderwidth=3,font=('courier','9',''))
bill_details.place(x=0,y=130)


total= Button(innerframe4,text="Total",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white",command=total_bills)
total.place(x=0,y=275)


Save= Button(innerframe4,text="Save",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white",command=save)
Save.place(x=43,y=275)


Send= Button(innerframe4,text="Send",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white",command=send)
Send.place(x=82,y=275)


exit = Button(innerframe4,text="Exit",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white",command=exit)
exit.place(x=124,y=275)

clr= Button(innerframe4,text="C",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#FB3C25', fg="white",command=cleared_bill)
clr.place(x=160,y=275)


root.mainloop()

