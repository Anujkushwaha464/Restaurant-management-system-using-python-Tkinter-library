from tkinter import*
from   PIL import ImageTk, Image
from tkinter import filedialog,messagebox
import random
import time
import requests



def reset():
    textReceipt.delete(1.0, END)
    tv_roti.set('0')
    tv_dal.set('0')
    tv_mixsabji.set('0')
    tv_paneer.set('0')
    tv_rice.set('0')
    tv_rayta.set('0')
    tv_chola.set('0')
    tv_chicken.set('0')
    tv_fish.set('0')
    tv_mutton.set('0')

    tv_samosa.set('0')
    tv_pizza.set('0')
    tv_patties.set('0')
    tv_noodles.set('0')
    tv_frenchfries.set('0')
    tv_momos.set('0')
    tv_cholebhathure.set('0')
    tv_burger.set('0')
    tv_chaat.set('0')
    tv_pakora.set('0')

    tv_badamshake.set('0')
    tv_chocolateshake.set('0')
    tv_milkshake.set('0')
    tv_faluda.set('0')
    tv_lassi.set('0')
    tv_tea.set('0')
    tv_coffe.set('0')
    tv_colddrinks.set('0')
    tv_shikanji.set('0')
    tv_fruitshake.set('0')

    tv_chocolate.set('0')
    tv_pineapple.set('0')
    tv_strawberry.set('0')
    tv_blackforest.set('0')
    tv_kitkat.set('0')
    tv_masaladosa.set('0')
    tv_idli.set('0')
    tv_uttapam.set('0')
    tv_biryani.set('0')
    tv_bonda.set('0')

    txtroti.config(state=DISABLED)
    txtdal.config(state=DISABLED)
    txtmixsabji.config(state=DISABLED)
    txtfish.config(state=DISABLED)
    txtpaneer.config(state=DISABLED)
    txtrice.config(state=DISABLED)
    txtchola.config(state=DISABLED)
    txtrayta.config(state=DISABLED)
    txtchicken.config(state=DISABLED)
    txtmutton .config(state=DISABLED)

    txtsamosa.config(state=DISABLED)
    txtpizza.config(state=DISABLED)
    txtpatties.config(state=DISABLED)
    txtnoodles.config(state=DISABLED)
    txtfrenchfries.config(state=DISABLED)
    txtmomos.config(state=DISABLED)
    txtcholebhathure.config(state=DISABLED)
    txtburger.config(state=DISABLED)
    txtbhelpuri.config(state=DISABLED)
    txtpakora.config(state=DISABLED)

    txtbadamshake.config(state=DISABLED)
    txtchocolateshake.config(state=DISABLED)
    txtmilkshake.config(state=DISABLED)
    txtfaluda.config(state=DISABLED)
    txtlassi.config(state=DISABLED)
    txttea.config(state=DISABLED)
    txtcoffe.config(state=DISABLED)
    txtcolddrinks.config(state=DISABLED)
    txtshinkanji.config(state=DISABLED)
    txtfruitshake.config(state=DISABLED)

    txtchocolate.config(state=DISABLED)
    txtpineapple.config(state=DISABLED)
    txtstrawberry.config(state=DISABLED)
    txtblackforest.config(state=DISABLED)
    txtkitkat.config(state=DISABLED)
    txtmasaladosa.config(state=DISABLED)
    txtidli.config(state=DISABLED)
    txtuttapam.config(state=DISABLED)
    txtbiryani.config(state=DISABLED)
    txtbonda.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)
    var31.set(0)
    var32.set(0)
    var33.set(0)
    var34.set(0)
    var35.set(0)
    var36.set(0)
    var37.set(0)
    var38.set(0)
    var39.set(0)
    var40.set(0)

    costoffoodvar.set('')
    costoffastfoodvar.set('')
    costofdrinksvar.set('')
    costofcakesvar.set('')
    costofotherfoodvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')

def send():
    if textReceipt.get(1.0,END) =='\n':
        pass
    else:
        def send_msg():
            message=textarea.get(1.0,END)
            number=numberfield.get()
            auth='0cCezjbBP9KO3ETZkrI1RVJgD7aXUN4nxuw6HG2QLd8oqpfhlte1KVuIZtAhx8ElGydRU6F0pQgjqNor'
            url='https://www.fast2sms.com/dev/bulkV2'

            params={
                'authorization': auth,
                'message': message,
                'numbers': number,
                'sender-id': 'FSTSMS',
                'route': 'p',
                'language': 'english'
            }
            response=requests.get(url,params=params)
            dic=response.json()
            result=dic.get('return')
            if result==True:
                messagebox.showinfo('Send Successfully', 'Message sent succesfully')
            else:
                messagebox.showerror('Error', 'Something went wrong')

        root2 = Toplevel()

        root2.title("Send Bill")
        root2.config(bg='silver')
        root2.geometry('485x690+0+0')

        logoImage = PhotoImage(file='sender.png')
        label = Label(root2, image=logoImage, bg='red4')
        label.pack(pady=5)

        numberLabel = Label(root2, text='Mobile Number', font=('arial', 18, 'bold underline'), bg='pink', fg='white')
        numberLabel.pack(pady=5)

        numberfield = Entry(root2, font=('helvetica', 22, 'bold'), bd=3, width=24)
        numberfield.pack(pady=5)

        billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='pink', fg='white')
        billLabel.pack(pady=5)

        textarea = Text(root2, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
        textarea.pack(pady=5)
        # textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')
        # if costoffoodvar.get() != '0 Rs':
        #     textarea.insert(END, f'Cost Of Food\t\t\t{priceofFood}Rs\n')
        # if costoffastfoodvar.get() != '0 Rs':
        #     textarea.insert(END, f'Cost Of FastFood\t\t\t{priceofFastFood}Rs\n')
        # if costofdrinksvar.get() != '0 Rs':
        #     textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n')
        # if costofcakesvar.get() != '0 Rs':
        #     textarea.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n')
        # if costofotherfoodvar.get() != '0 Rs':
        #     textarea.insert(END, f'Cost Of OtherFood\t\t\t{priceofOtherFood}Rs\n')
        # textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n')
        # textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
        textarea.insert(END, 'Dear user,\n')
        textarea.insert(END, f'Rs:{subtotalofItems + 50}.00 successfully paid in\n Asquire Restaurant ( Agra ).\n-sent via ASFRSMS')

        sendButton = Button(root2, text='SEND', font=('arial', 19, 'bold'), bg='white', fg='red4', bd=7, relief=GROOVE
                            , command=send_msg)
        sendButton.pack(pady=5)

        root2.mainloop()


def save():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url == None:
            pass
        else:

            bill_data = textReceipt.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information', 'Your Bill Is Succesfully Saved')


def receipt():
    global billnumber, date
    if costoffoodvar.get() != '' or costoffastfoodvar.get() != ' 'or costofdrinksvar.get() != ''\
            or costofcakesvar.get() != '' or  costofotherfoodvar.get() != '':
        textReceipt.delete(1.0, END)
        x = random.randint(100, 10000)
        billnumber = 'BILL' + str(x)
        date = time.strftime('%d/%m/%Y')
        textReceipt.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n')
        textReceipt.insert(END, '--------------------------------------------------------\n\n')
        textReceipt.insert(END,'\t\tAsquire Restaurant\t\t\t\n')
        textReceipt.insert(END,'\t Add- rambagh, hathras road, Agra\t\t\t\n')
        textReceipt.insert(END,'\tPincode-282006, Uttar Pradesh\t\t\n\n')
        textReceipt.insert(END, '--------------------------------------------------------\n')
        textReceipt.insert(END, '********************************************\n')
        textReceipt.insert(END, 'Items:\t\t Cost Of Items(Rs)\n')
        textReceipt.insert(END, '********************************************\n')
        if tv_roti.get() != '0':
            textReceipt.insert(END, f'Roti\t\t\t{int(tv_roti.get())*5}\n\n')
        if tv_dal.get() != '0':
            textReceipt.insert(END, f'Daal\t\t\t{int(tv_dal.get())*60}\n\n')
        if tv_mixsabji.get() != '0':
            textReceipt.insert(END, f'mixsabji\t\t\t{int(tv_mixsabji.get())*60}\n\n')
        if tv_paneer.get() != '0':
            textReceipt.insert(END, f'paneer:\t\t\t{int(tv_paneer.get()) * 120}\n\n')
        if tv_rice.get() != '0':
            textReceipt.insert(END, f'rice:\t\t\t{int(tv_rice.get()) * 40}\n\n')
        if tv_rayta.get() != '0':
            textReceipt.insert(END, f'rayta:\t\t\t{int(tv_rayta.get()) * 30}\n\n')
        if tv_chola.get() != '0':
            textReceipt.insert(END, f'Chola:\t\t\t{int(tv_chola.get()) * 90}\n\n')
        if tv_chicken.get() != '0':
            textReceipt.insert(END, f'Chicken:\t\t\t{int(tv_chicken.get()) * 150}\n\n')
        if tv_fish.get() != '0':
            textReceipt.insert(END, f'fish:\t\t\t{int(tv_fish.get()) * 150}\n\n')
        if tv_mutton.get() != '0':
            textReceipt.insert(END, f'Mutton:\t\t\t{int(tv_mutton.get()) * 250}\n\n')

        if tv_samosa.get() != '0':
            textReceipt.insert(END, f'Samosa:\t\t\t{int(tv_samosa.get()) * 10}\n\n')
        if tv_pizza.get() != '0':
            textReceipt.insert(END, f'Pizza:\t\t\t{int(tv_pizza.get())*220}\n\n')
        if tv_patties.get() != '0':
            textReceipt.insert(END, f'Patties:\t\t\t{int(tv_patties.get()) * 20}\n\n')
        if tv_noodles.get() != '0':
            textReceipt.insert(END, f'Noodles:\t\t\t{int(tv_noodles.get()) * 50}\n\n')
        if tv_frenchfries.get() != '0':
            textReceipt.insert(END, f'Noodles:\t\t\t{int(tv_frenchfries.get()) * 50}\n\n')
        if tv_momos.get() != '0':
            textReceipt.insert(END, f'Momos:\t\t\t{int(tv_momos.get()) * 30}\n\n')
        if tv_cholebhathure.get() != '0':
            textReceipt.insert(END, f'Cholebhathure:\t\t\t{int(tv_cholebhathure.get())*50}\n\n')
        if tv_burger.get() != '0':
            textReceipt.insert(END, f'Burger:\t\t\t{int(tv_burger.get()) * 50}\n\n')
        if tv_chaat.get() != '0':
            textReceipt.insert(END, f'Chaat :\t\t\t{int(tv_chaat.get()) * 30}\n\n')
        if tv_pakora.get() != '0':
            textReceipt.insert(END, f'Pakora:\t\t\t{int(tv_pakora.get()) * 20}\n\n')

        if tv_badamshake.get() != '0':
            textReceipt.insert(END, f'Badamshake :\t\t\t{int(tv_badamshake.get()) * 80}\n\n')
        if tv_chocolateshake.get() != '0':
            textReceipt.insert(END, f'Chocolsteshake :\t\t\t{int(tv_chocolateshake.get()) * 60}\n\n')
        if tv_milkshake.get() != '0':
            textReceipt.insert(END, f'Milkshake :\t\t\t{int(tv_milkshake.get()) * 50}\n\n')
        if tv_faluda.get() != '0':
            textReceipt.insert(END, f'Faluda :\t\t\t{int(tv_faluda.get()) * 60}\n\n')
        if tv_lassi.get() != '0':
            textReceipt.insert(END, f'Lassi :\t\t\t{int(tv_lassi.get()) * 50}\n\n')
        if tv_tea.get() != '0':
            textReceipt.insert(END, f'Tea :\t\t\t{int(tv_tea.get()) * 10}\n\n')
        if tv_coffe.get() != '0':
            textReceipt.insert(END, f'Coffee :\t\t\t{int(tv_coffe.get()) * 20}\n\n')
        if tv_colddrinks.get() != '0':
            textReceipt.insert(END, f'Colddrinks :\t\t\t{int(tv_colddrinks.get()) * 40}\n\n')
        if tv_shikanji.get() != '0':
            textReceipt.insert(END, f'shikanji :\t\t\t{int(tv_shikanji.get()) * 10}\n\n')
        if tv_fruitshake.get() != '0':
            textReceipt.insert(END, f'Fruitshake :\t\t\t{int(tv_fruitshake.get()) * 60}\n\n')

        if tv_chocolate.get() != '0':
            textReceipt.insert(END, f'Chocolate:\t\t\t{int(tv_chocolate.get()) * 400}\n\n')
        if tv_pineapple.get() != '0':
            textReceipt.insert(END, f'Pineapple:\t\t\t{int(tv_pineapple.get()) * 300}\n\n')
        if tv_strawberry.get() != '0':
            textReceipt.insert(END, f'Strawberry:\t\t\t{int(tv_strawberry.get()) * 300}\n\n')
        if tv_blackforest.get() != '0':
            textReceipt.insert(END, f'Blackforest:\t\t\t{int(tv_blackforest.get()) * 400}\n\n')
        if tv_kitkat.get() != '0':
            textReceipt.insert(END, f'Kitkat:\t\t\t{int(tv_kitkat.get()) * 300}\n\n')

        if tv_masaladosa.get() != '0':
            textReceipt.insert(END, f'Masaladosa:\t\t\t{int(tv_masaladosa.get()) * 50}\n\n')
        if tv_idli.get() != '0':
            textReceipt.insert(END, f'Idli:\t\t\t{int(tv_idli.get()) * 50}\n\n')
        if tv_uttapam.get() != '0':
            textReceipt.insert(END, f'Uttapam :\t\t\t{int(tv_uttapam.get()) * 60}\n\n')
        if tv_biryani.get() != '0':
            textReceipt.insert(END, f'Biryani :\t\t\t{int(tv_biryani.get()) * 100}\n\n')
        if tv_bonda.get() != '0':
            textReceipt.insert(END, f'Bonda :\t\t\t{int(tv_bonda.get()) * 40}\n\n')

        textReceipt.insert(END, '********************************************\n')
        if costoffoodvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
        if costoffastfoodvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of FastFood\t\t\t{priceofFastFood}Rs\n\n')
        if costofdrinksvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if costofcakesvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')
        if costofotherfoodvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Food\t\t\t{priceofOtherFood}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, '--------------------------------------------------------\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')
        textReceipt.insert(END, '--------------------------------------------------------\n')

    else:
        messagebox.showerror('Error', 'No Item Is selected')


def totalcost():
    global priceofFood,priceofFastFood, priceofDrinks, priceofCakes, priceofOtherFood, subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
            var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
            var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
            var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
            var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
            var26.get() != 0 or var27.get() != 0 or var28.get() != 0 or var29.get() != 0 or var30.get() != 0 or \
            var31.get() != 0 or var32.get() != 0 or var33.get() != 0 or var34.get() != 0 or var35.get() != 0 or \
            var36.get() != 0 or var37.get() != 0 or var38.get() != 0 or var39.get() != 0 or var40.get() != 0 :

        item1 = int(tv_roti.get())
        item2 = int(tv_dal.get())
        item3 = int(tv_mixsabji.get())
        item4 = int(tv_paneer.get())
        item5 = int(tv_rice.get())
        item6 = int(tv_rayta.get())
        item7 = int(tv_chola.get())
        item8 = int(tv_chicken.get())
        item9 = int(tv_fish.get())
        item10= int(tv_mutton.get())

        item11 = int(tv_samosa.get())
        item12 = int(tv_pizza.get())
        item13 = int(tv_patties.get())
        item14 = int(tv_noodles.get())
        item15 = int(tv_frenchfries.get())
        item16 = int(tv_momos.get())
        item17 = int(tv_cholebhathure.get())
        item18 = int(tv_burger.get())
        item19 = int(tv_chaat.get())
        item20 = int(tv_pakora.get())

        item21 = int(tv_badamshake.get())
        item22 = int(tv_chocolateshake.get())
        item23 = int(tv_milkshake.get())
        item24 = int(tv_faluda.get())
        item25 = int(tv_lassi.get())
        item26 = int(tv_tea.get())
        item27 = int(tv_coffe.get())
        item28 = int(tv_colddrinks.get())
        item29 = int(tv_shikanji.get())
        item30 = int(tv_fruitshake.get())

        item31 = int(tv_chocolate.get())
        item32 = int(tv_pineapple.get())
        item33 = int(tv_strawberry.get())
        item34 = int(tv_blackforest.get())
        item35 = int(tv_kitkat.get())

        item36 = int(tv_masaladosa.get())
        item37 = int(tv_idli.get())
        item38 = int(tv_uttapam.get())
        item39 = int(tv_biryani.get())
        item40 = int(tv_bonda.get())

        priceofFood=(item1*5)+(item2*60)+(item3*60)+(item4*120)+(item5*40)+(item6*30)+(item7*90)\
                    +(item8*150)+(item9*150)+(item10*250)
        priceofFastFood=(item11*10)+(item12*220)+(item13*20)+(item14*50)+(item15*30)+(item16*20)\
                      +(item17*50)+(item18*50)+(item19*30)+(item20*20)
        priceofDrinks=(item21*80) + (item22 * 60) + (item23 * 50) + ( item24 * 60)+ (item25 * 50) + (item26 * 10)\
                                    + (item27 * 20)+(item28 * 40) + (item29 * 10) + (item30 * 60)
        priceofCakes=(item31*400) + (item32 * 300) + (item33 * 300) + ( item34 * 400)+ (item35 * 300)
        priceofOtherFood=(item36 * 50) + (item37 * 50)+(item38 * 60) + (item39 * 100) + (item40 * 40)

        costoffoodvar.set(str(priceofFood) + ' Rs')
        costoffastfoodvar.set(str(priceofFastFood)+'Rs')
        costofdrinksvar.set(str(priceofDrinks) + ' Rs')
        costofcakesvar.set(str(priceofCakes) + ' Rs')
        costofotherfoodvar.set(str(priceofOtherFood) + ' Rs')
        subtotalofItems = priceofFood +priceofFastFood+ priceofDrinks + priceofCakes+priceofOtherFood
        subtotalvar.set(str(subtotalofItems) + ' Rs')
        servicetaxvar.set('50 Rs')
        tottalcost = subtotalofItems + 50
        totalcostvar.set(str(tottalcost) + ' Rs')

    else:
        messagebox.showerror('Error', 'No Item Is selected')



#functions
def roti():
    if var1.get()==1:
        txtroti.config(state=NORMAL)
        txtroti.delete(0,END)
        txtroti.focus()
    else:
        txtroti.config(state=DISABLED)
        tv_roti.set('0')
def dal():
    if var2.get()==1:
        txtdal.config(state=NORMAL)
        txtdal.delete(0,END)
        txtdal.focus()
    else:
        txtdal.config(state=DISABLED)
        tv_dal.set('0')
def sabji():
    if var3.get()==1:
        txtmixsabji.config(state=NORMAL)
        txtmixsabji.delete(0,END)
        txtmixsabji.focus()
    else:
        txtmixsabji.config(state=DISABLED)
        tv_mixsabji.set('0')
def paneer():
    if var4.get()==1:
        txtpaneer.config(state=NORMAL)
        txtpaneer.delete(0,END)
        txtpaneer.focus()
    else:
        txtpaneer.config(state=DISABLED)
        tv_paneer.set('0')
def chola():
    if var5.get()==1:
        txtchola.config(state=NORMAL)
        txtchola.delete(0,END)
        txtchola.focus()
    else:
        txtchola.config(state=DISABLED)
        tv_chola.set('0')
def pulav_rice():
    if var6.get()==1:
        txtrice.config(state=NORMAL)
        txtrice.delete(0,END)
        txtrice.focus()
    else:
        txtrice.config(state=DISABLED)
        tv_rice.set('0')
def rayta():
    if var7.get()==1:
        txtrayta.config(state=NORMAL)
        txtrayta.delete(0,END)
        txtrayta.focus()
    else:
        txtrayta.config(state=DISABLED)
        tv_rayta.set('0')
def chicken():
    if var8.get()==1:
        txtchicken.config(state=NORMAL)
        txtchicken.delete(0,END)
        txtchicken.focus()
    else:
        txtchicken.config(state=DISABLED)
        tv_chicken.set('0')
def fishsabji():
    if var9.get()==1:
        txtfish.config(state=NORMAL)
        txtfish.delete(0,END)
        txtfish.focus()
    else:
        txtfish.config(state=DISABLED)
        tv_fish.set('0')
def mutton():
    if var10.get()==1:
        txtmutton.config(state=NORMAL)
        txtmutton.delete(0,END)
        txtmutton.focus()
    else:
        txtmutton.config(state=DISABLED)
        tv_mutton.set('0')
def samosa():
    if var11.get()==1:
        txtsamosa.config(state=NORMAL)
        txtsamosa.delete(0,END)
        txtsamosa.focus()
    else:
        txtsamosa.config(state=DISABLED)
        tv_samosa.set('0')
def pizza():
    if var12.get()==1:
        txtpizza.config(state=NORMAL)
        txtpizza.delete(0,END)
        txtpizza.focus()
    else:
        txtpizza.config(state=DISABLED)
        tv_pizza.set('0')
def patties():
    if var13.get()==1:
        txtpatties.config(state=NORMAL)
        txtpatties.delete(0,END)
        txtpatties.focus()
    else:
        txtpatties.config(state=DISABLED)
        tv_patties.set('0')
def noodles():
    if var14.get()==1:
        txtnoodles.config(state=NORMAL)
        txtnoodles.delete(0,END)
        txtnoodles.focus()
    else:
        txtnoodles.config(state=DISABLED)
        tv_noodles.set('0')
def frenchfries():
    if var15.get()==1:

        txtfrenchfries.config(state=NORMAL)
        txtfrenchfries.delete(0,END)
        txtfrenchfries.focus()
    else:
        txtfrenchfries.config(state=DISABLED)
        tv_frenchfries.set('0')
def momos():
    if var16.get()==1:
        txtmomos.config(state=NORMAL)
        txtmomos.delete(0,END)
        txtmomos.focus()
    else:
        txtmomos.config(state=DISABLED)
        tv_momos.set('0')
def cholebhathure():
    if var17.get()==1:
        txtcholebhathure.config(state=NORMAL)
        txtcholebhathure.delete(0,END)
        txtcholebhathure.focus()
    else:
        txtcholebhathure.config(state=DISABLED)
        tv_cholebhathure.set('0')
def burger():

    if var18.get()==1:
        txtburger.config(state=NORMAL)
        txtburger.delete(0,END)
        txtburger.focus()
    else:
        txtburger.config(state=DISABLED)
        tv_burger.set('0')
def bhelpuri():
    if var19.get()==1:
        txtbhelpuri.config(state=NORMAL)
        txtbhelpuri.delete(0,END)
        txtbhelpuri.focus()
    else:
        txtbhelpuri.config(state=NORMAL)
        tv_chaat.set('0')
def pakora():
    if var20.get()==1:
        txtpakora.config(state=NORMAL)
        txtpakora.delete(0,END)
        txtpakora.focus()
    else:
        txtpakora.config(state=DISABLED)
        tv_pakora.set('0')
def badam():
    if var21.get()==1:
        txtbadamshake.config(state=NORMAL)
        txtbadamshake.delete(0,END)
        txtbadamshake.focus()
    elif var21.get()==0:
        txtbadamshake.config(state=DISABLED)
        tv_badamshake.set('0')
def chocolateshake():
    if var22.get()==1:
        txtchocolateshake.config(state=NORMAL)
        txtchocolateshake.delete(0,END)
        txtchocolateshake.focus()
    elif var22.get()==0:
        txtchocolateshake.config(state=DISABLED)
        tv_chocolateshake.set('0')
def milkshake():
    if var23.get()==1:
        txtmilkshake.config(state=NORMAL)
        txtmilkshake.delete(0,END)
        txtmilkshake.focus()
    elif var23.get()==0:
        txtmilkshake.config(state=DISABLED)
        tv_milkshake.set('0')
def faluda():
    if var24.get()==1:
        txtfaluda.config(state=NORMAL)
        txtfaluda.delete(0,END)
        txtfaluda.focus()
    elif var24.get()==0:
        txtfaluda.config(state=DISABLED)
        tv_faluda.set('0')
def lassi():
    if var25.get()==1:
        txtlassi.config(state=NORMAL)
        txtlassi.delete(0, END)
        txtlassi.focus()
    else:
        txtlassi.config(state=DISABLED)
        tv_lassi.set('0')
def tea():
    if var26.get()==1:
        txttea.config(state=NORMAL)
        txttea.delete(0, END)
        txttea.focus()
    else:
        txttea.config(state=DISABLED)
        tv_tea.set('0')
def coffe():
    if var27.get()==1:
        txtcoffe.config(state=NORMAL)
        txtcoffe.delete(0, END)
        txtcoffe.focus()
    else:
        txtcoffe.config(state=DISABLED)
        tv_coffe.set('0')
def colddrinks():
    if var28.get()==1:
        txtcolddrinks.config(state=NORMAL)
        txtcolddrinks.delete(0, END)
        txtcolddrinks.focus()
    else:
        txtcolddrinks.config(state=DISABLED)
        tv_colddrinks.set('0')
def shikanji():
    if var29.get()==1:
        txtshinkanji.config(state=NORMAL)
        txtshinkanji.delete(0, END)
        txtshinkanji.focus()
    else:
        txtshinkanji.config(state=DISABLED)
        tv_shikanji.set('0')
def fruitshake():
    if var30.get()==1:
        txtfruitshake.config(state=NORMAL)
        txtfruitshake.delete(0, END)
        txtfruitshake.focus()
    else:
        txtfruitshake.config(state=DISABLED)
        tv_fruitshake.set('0')
def chocalate():
    if var31.get()==1:
        txtchocolate.config(state=NORMAL)
        txtchocolate.delete(0, END)
        txtchocolate.focus()
    else:
        txtchocolate.config(state=DISABLED)
        tv_chocolate.set('0')
def pineapple():
    if var32.get()==1:
        txtpineapple.config(state=NORMAL)
        txtpineapple.delete(0, END)
        txtpineapple.focus()
    else:
        txtpineapple.config(state=DISABLED)
        tv_pineapple.set('0')
def strawberry():
    if var33.get()==1:
        txtstrawberry.config(state=NORMAL)
        txtstrawberry.delete(0, END)
        txtstrawberry.focus()
    else:
        txtstrawberry.config(state=DISABLED)
        tv_strawberry.set('0')
def blackforest():
    if var34.get()==1:
        txtblackforest.config(state=NORMAL)
        txtblackforest.delete(0, END)
        txtblackforest.focus()
    else:
        txtblackforest.config(state=DISABLED)
        tv_blackforest.set('0')

def kitkat():
    if var35.get()==1:
        txtkitkat.config(state=NORMAL)
        txtkitkat.delete(0, END)
        txtkitkat.focus()
    else:
        txtkitkat.config(state=DISABLED)
        tv_kitkat.set('0')
def masaladosa():
    if var36.get()==1:
        txtmasaladosa.config(state=NORMAL)
        txtmasaladosa.delete(0, END)
        txtmasaladosa.focus()
    else:
        txtmasaladosa.config(state=DISABLED)
        tv_masaladosa.set('0')
def idli():
    if var37.get()==1:
        txtidli.config(state=NORMAL)
        txtidli.delete(0, END)
        txtidli.focus()
    else:
        txtidli.config(state=DISABLED)
        tv_idli.set('0')
def uttapam():
    if var38.get()==1:
        txtuttapam.config(state=NORMAL)
        txtuttapam.delete(0, END)
        txtuttapam.focus()
    else:
        txtuttapam.config(state=DISABLED)
        tv_uttapam.set('0')
def biryani():
    if var39.get()==1:
        txtbiryani.config(state=NORMAL)
        txtbiryani.delete(0, END)
        txtbiryani.focus()
    else:
        txtbiryani.config(state=DISABLED)
        tv_biryani.set('0')
def bonda():
    if var40.get()==1:
        txtbonda.config(state=NORMAL)
        txtbonda.delete(0,END)
        txtbonda.focus()

    else:
        txtbonda.config(state=DISABLED)
        tv_bonda.set('0')

win=Tk()
win.geometry("1260x700+0+0")
#win.resizable(0,0)

win.title("Restorent mangement system Created by ANUJ kushwaha")

topframe=Frame(win,relief=RIDGE,bd=7)
topframe.pack(side=TOP)
topleftframe=Frame(topframe)
topleftframe.pack(side=LEFT)
topmidframe=Frame(topframe)
topmidframe.pack(side=LEFT)
toprightframe=Frame(topframe)
toprightframe.pack(side=LEFT)

logoImage =ImageTk.PhotoImage(Image.open('newb3.png'))
label=Label(topmidframe,image=logoImage)
label.pack()


menuframe=Frame(win,bd=7,relief=RIDGE,bg='purple')
menuframe.pack(side=LEFT)
costframe=LabelFrame(menuframe,bd=4,relief=RIDGE,pady=5)
costframe.pack(side=BOTTOM)
foodframe=LabelFrame(menuframe,bd=4,relief=RIDGE,text='Food',font=('Toledo Heavy',20,'bold'))
foodframe.pack(side=LEFT)
fastfoodframe=LabelFrame(menuframe,bd=4,relief=RIDGE,text='Fastfood',font=('Toledo Heavy',20,'bold'))
fastfoodframe.pack(side=LEFT)
drinksframe=LabelFrame(menuframe,bd=4,relief=RIDGE,text='Drinks',font=('Toledo Heavy',20,'bold'))
drinksframe.pack(side=LEFT)

foodframe1=LabelFrame(menuframe,bd=4,relief=RIDGE)
foodframe1.pack(side=LEFT)
cakesframe=LabelFrame(foodframe1,text='Top_Cakes',relief=RIDGE,bd=4,font=('Toledo Heavy',20,'bold'))
cakesframe.pack(side=TOP)
southindiafood=LabelFrame(foodframe1,text='OtherFood',bd=4,relief=RIDGE,font=('Toledo Heavy',20,'bold'))
southindiafood.pack(side=BOTTOM)

rightframe=Frame(win,bd=10,relief=RIDGE,)
rightframe.pack(side=RIGHT)
calculatorframe=LabelFrame(rightframe,bd=5,relief=RIDGE)
calculatorframe.pack(side=TOP)
receiptframe=LabelFrame(rightframe,bd=5,relief=RIDGE)
receiptframe.pack(side=TOP)
buttonframe=Frame(rightframe,bd=5,relief=RIDGE)
buttonframe.pack(side=BOTTOM)

#variable define

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()
var29=IntVar()
var30=IntVar()
var31=IntVar()
var32=IntVar()
var33=IntVar()
var34=IntVar()
var35=IntVar()
var36=IntVar()
var37=IntVar()
var38=IntVar()
var39=IntVar()
var40=IntVar()


tv_roti=StringVar()
tv_dal=StringVar()
tv_mixsabji=StringVar()
tv_paneer=StringVar()
tv_chola=StringVar()
tv_rice=StringVar()
tv_rayta=StringVar()
tv_chicken=StringVar()
tv_fish=StringVar()
tv_mutton=StringVar()
tv_samosa=StringVar()
tv_pizza=StringVar()
tv_patties=StringVar()
tv_noodles=StringVar()
tv_frenchfries=StringVar()
tv_momos=StringVar()
tv_cholebhathure=StringVar()
tv_burger=StringVar()
tv_chaat=StringVar()
tv_pakora=StringVar()
tv_badamshake=StringVar()
tv_chocolateshake=StringVar()
tv_milkshake=StringVar()
tv_faluda=StringVar()
tv_lassi=StringVar()
tv_tea=StringVar()
tv_coffe=StringVar()
tv_colddrinks=StringVar()
tv_shikanji=StringVar()
tv_fruitshake=StringVar()
tv_chocolate=StringVar()
tv_pineapple=StringVar()
tv_strawberry=StringVar()
tv_blackforest=StringVar()
tv_kitkat=StringVar()
tv_masaladosa=StringVar()
tv_idli=StringVar()
tv_uttapam=StringVar()
tv_biryani=StringVar()
tv_bonda=StringVar()

costoffoodvar=StringVar()
costoffastfoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
costofotherfoodvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

tv_roti.set('0')
tv_dal.set('0')
tv_mixsabji.set('0')
tv_paneer.set('0')
tv_rice.set('0')
tv_chola.set('0')
tv_rayta.set('0')
tv_chicken.set('0')
tv_fish.set('0')
tv_mutton.set('0')

tv_samosa.set('0')
tv_pizza.set('0')
tv_patties.set('0')
tv_noodles.set('0')
tv_frenchfries.set('0')
tv_momos.set('0')
tv_cholebhathure.set('0')
tv_burger.set('0')
tv_chaat.set('0')
tv_pakora.set('0')

tv_badamshake.set('0')
tv_chocolateshake.set('0')
tv_milkshake.set('0')
tv_faluda.set('0')
tv_lassi.set('0')
tv_tea.set('0')
tv_coffe.set('0')
tv_colddrinks.set('0')
tv_shikanji.set('0')
tv_fruitshake.set('0')

tv_chocolate.set('0')
tv_pineapple.set('0')
tv_strawberry.set('0')
tv_blackforest.set('0')
tv_kitkat.set('0')

tv_masaladosa.set('0')
tv_idli.set('0')
tv_uttapam.set('0')
tv_biryani.set('0')
tv_bonda.set('0')

#functions



#Many functions
def checkin():
    root2 = Tk()
    root2.title("Send Bill")
    #root2.config(bg='pink')
    root2.geometry('485x620+50+50')

    logoImage = ImageTk.PhotoImage(file='sender.png')
    label = Label(root2, image=logoImage, bg='white')
    label.pack(pady=5)


    lblname=Label(root2,text='Customer name:',font=('Verdana',15,'bold'))
    lblname.grid(row=0,column=0)
    name = Entry(root2, font=('Verdana', 15, 'bold'), bd=3, width=10)
    name.grid(row=0,column=1)
    numberLabel = Label(root2, text='Mobile Number:', font=('Verdana', 15, 'bold'))
    numberLabel.grid(row=1,column=0)
    numberfield = Entry(root2, font=('Verdana', 15, 'bold'), bd=3, width=10)
    numberfield.grid(row=1,column=1)
    root2.mainloop()
buttoncheckin = Button(topleftframe, text='Check-in', bd=7,bg='green', fg='white', font=('Toledo Heavy', 15, 'bold'), command=checkin)
buttoncheckin.pack(side=LEFT)

def price():
    win1 = Tk()
    win1.geometry("650x680+0+0")
    win1.title("Price List")
    priceframe=Frame(win1,relief=RIDGE,bd=2)
    priceframe.pack(side=TOP)
    food1frame = LabelFrame(priceframe, relief=RIDGE, text='Food Products',fg='red', bd=10, font=('Times new roman',20,'bold'))
    food1frame.pack(side=LEFT)
    food2frame = LabelFrame(priceframe, relief=RIDGE, text='Food Products', bd=10, font=('Times new roman', 20, 'bold'))
    food2frame.pack(side=RIGHT)
    price1frame=Frame(win1, relief=RIDGE, bd=2)
    price1frame.pack(side=TOP)
    food3frame = LabelFrame(price1frame, relief=RIDGE, text='Food Products', bd=10, font=('Times new roman', 20, 'bold'))
    food3frame.pack(side=LEFT)
    food4frame = LabelFrame(price1frame, relief=RIDGE, text='Food Products', bd=10, font=('Times new roman', 20, 'bold'))
    food4frame.pack(side=RIGHT)

    #food1frame
    lblrestaurant = Label(food1frame, font=('Lucida Console', 20, 'bold'), text="Products", bg="wheat", fg="blue", bd=5)
    lblrestaurant.grid(row=0, column=0,padx=20)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="Price",bg="wheat", fg="blue", anchor=W)
    lblrestaurant.grid(row=0, column=3)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="Roti", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=0)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="50", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=3)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="Dal", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=0)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="60", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=3)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="Mixsabji", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=0)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="250", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=3)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="Paneer", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=0)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="50", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=3)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="Chola", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=0)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="75", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=3)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="Rice", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=0)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="45", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=3)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="Rayta", fg="red", anchor=W)
    lblrestaurant.grid(row=7, column=0)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="45", fg="red", anchor=W)
    lblrestaurant.grid(row=7, column=3)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="Chicken", fg="red", anchor=W)
    lblrestaurant.grid(row=8, column=0)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="45", fg="red", anchor=W)
    lblrestaurant.grid(row=8, column=3)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="Mutton", fg="red", anchor=W)
    lblrestaurant.grid(row=9, column=0)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="45", fg="red", anchor=W)
    lblrestaurant.grid(row=9, column=3)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="Fish", fg="red", anchor=W)
    lblrestaurant.grid(row=10, column=0)
    lblrestaurant = Label(food1frame, font=('Lucida Console', 15, 'bold'), text="45", fg="red", anchor=W)
    lblrestaurant.grid(row=10, column=3)

    #food2frame
    lblrestaurant = Label(food2frame, font=('Lucida console', 20, 'bold'), text="Products", bg="darkblue", fg="white",  bd=5)
    lblrestaurant.grid(row=0, column=0, padx=20)
    lblrestaurant = Label(food2frame, font=('Lucida Console', 20, 'bold'), text="Price", bg="darkblue", fg="white",anchor=W)
    lblrestaurant.grid(row=0, column=3)
    lblrestaurant = Label(food2frame, font=('Lucida Console', 15, 'bold'), text="Samosa", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=0)
    lblrestaurant = Label(food2frame, font=('Lucida Console', 15, 'bold'), text="50", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=3)
    lblrestaurant = Label(food2frame, font=('Lucida Console', 15, 'bold'), text="Pizza", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=0)
    lblrestaurant = Label(food2frame, font=('Lucida Console', 15, 'bold'), text="60", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=3)
    lblrestaurant = Label(food2frame, font=('Lucida Console', 15, 'bold'), text="Patties", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=0)
    lblrestaurant = Label(food2frame, font=('Lucida Console', 15, 'bold'), text="250", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=3)
    lblrestaurant = Label(food2frame, font=('Lucida Console', 15, 'bold'), text="Noodles", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=0)
    lblrestaurant = Label(food2frame, font=('Lucida Console', 15, 'bold'), text="50", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=3)
    lblrestaurant = Label(food2frame, font=('Lucida Console', 15, 'bold'), text="Momos", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=0)
    lblrestaurant = Label(food2frame, font=('Lucida Console', 15, 'bold'), text="75", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=3)
    lblrestaurant = Label(food2frame, font=('Lucida Console', 15, 'bold'), text="choleBhathure", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=0)
    lblrestaurant = Label(food2frame, font=('Lucida Console', 15, 'bold'), text="45", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=3)
    #food3frame
    lblrestaurant = Label(food3frame, font=('Verdana', 14, 'bold'), text="DISH", bg="black", fg="yellow",bd=5)
    lblrestaurant.grid(row=0, column=0, padx=20)
    lblrestaurant = Label(food3frame, font=('Verdana', 15, 'bold'), text="PRICE", bg="darkblue", fg="white",anchor=W)
    lblrestaurant.grid(row=0, column=3)
    lblrestaurant = Label(food3frame, font=('Lucida Console', 15, 'bold'), text="Badamshake", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=0)
    lblrestaurant = Label(food3frame, font=('Lucida Console', 15, 'bold'), text="80", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=3)
    lblrestaurant = Label(food3frame, font=('Lucida Console', 15, 'bold'), text="Chocolateshake", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=0)
    lblrestaurant = Label(food3frame, font=('Lucida Console', 15, 'bold'), text="60", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=3)
    lblrestaurant = Label(food3frame, font=('Lucida Console', 15, 'bold'), text="Milkshake", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=0)
    lblrestaurant = Label(food3frame, font=('Lucida Console', 15, 'bold'), text="50Rs", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=3)
    lblrestaurant = Label(food3frame, font=('Lucida Console', 15, 'bold'), text="Faluda", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=0)
    lblrestaurant = Label(food3frame, font=('Lucida Console', 15, 'bold'), text="60 rs", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=3)
    lblrestaurant = Label(food3frame, font=('Lucida Console', 15, 'bold'), text="Lassi ", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=0)
    lblrestaurant = Label(food3frame, font=('Lucida Console', 15, 'bold'), text="75 rs", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=3)
    lblrestaurant = Label(food3frame, font=('Lucida Console', 15, 'bold'), text="Tea", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=0)
    lblrestaurant = Label(food3frame, font=('Lucida Console', 15, 'bold'), text="10 rs", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=3)
    #food4frame
    lblrestaurant = Label(food4frame, font=('Verdana', 14, 'bold'), text="DISH", bg="black", fg="yellow",bd=5)
    lblrestaurant.grid(row=0, column=0, padx=20)
    lblrestaurant = Label(food4frame, font=('Verdana ', 15, 'bold'), text="PRICE", bg="black", fg="yellow",anchor=W)
    lblrestaurant.grid(row=0, column=3)
    lblrestaurant = Label(food4frame, font=('Lucida Console', 15, 'bold'), text=" Chocolate", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=0)
    lblrestaurant = Label(food4frame, font=('Lucida Console', 15, 'bold'), text="400 rs", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=3)
    lblrestaurant = Label(food4frame, font=('Lucida Console', 15, 'bold'), text=" Strawberry", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=0)
    lblrestaurant = Label(food4frame, font=('Lucida Console', 15, 'bold'), text="300 rs", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=3)
    lblrestaurant = Label(food4frame, font=('Lucida Console', 15, 'bold'), text="  Pineapple", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=0)
    lblrestaurant = Label(food4frame, font=('Lucida Console', 15, 'bold'), text="300 rs", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=3)
    lblrestaurant = Label(food4frame, font=('Lucida Console', 15, 'bold'), text="Blackforest", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=0)
    lblrestaurant = Label(food4frame, font=('Lucida Console', 15, 'bold'), text="400 rs", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=3)
    lblrestaurant = Label(food4frame, font=('Lucida Console', 15, 'bold'), text="kitkat", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=0)
    lblrestaurant = Label(food4frame, font=('Lucida Console', 15, 'bold'), text="300 rs", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=3)
    lblrestaurant = Label(food4frame, font=('Lucida Console', 15, 'bold'), text="Masaladosa", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=0)
    lblrestaurant = Label(food4frame, font=('Lucida Console', 15, 'bold'), text="50 rs", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=3)
    win1.mainloop()
btnprice=Button(toprightframe,bd=7,fg="white",font=('Toledo Heavy' ,15,'bold'),text="Price", bg="green",command=price)
btnprice.pack(side=RIGHT)

#foodframe_itremp
#photo=ImageTk.PhotoImage(Image.open('roti.png'))
roti=Checkbutton(foodframe,text='Roti',fg='green',font=('Verdana',15,'bold'),command=roti,onvalue=1,offvalue=0,variable=var1)
roti.grid(row=0,column=0,sticky=W)
dal=Checkbutton(foodframe,text='Dal',fg='green',font=('Verdana',15,'bold'),command=dal,onvalue=1,offvalue=0,variable=var2)
dal.grid(row=1,column=0,sticky=W)
sabji=Checkbutton(foodframe,fg='green',text='MixSabji',font=('Verdana',15,'bold'),command=sabji,onvalue=1,offvalue=0,variable=var3)
sabji.grid(row=2,column=0,sticky=W)
paneer=Checkbutton(foodframe,fg='green',text='Paneer',font=('Verdana',15,'bold'),command=paneer,onvalue=1,offvalue=0,variable=var4)
paneer.grid(row=3,column=0,sticky=W)
chola=Checkbutton(foodframe,fg='green',text='Chola',font=('Verdana',15,'bold'),command=chola,onvalue=1,offvalue=0,variable=var5)
chola.grid(row=4,column=0,sticky=W)
pulav_rice=Checkbutton(foodframe,text='Rice',fg='green',font=('Verdana',15,'bold'),command=pulav_rice,onvalue=1,offvalue=0,variable=var6)
pulav_rice.grid(row=5,column=0,sticky=W)
rayta=Checkbutton(foodframe,text='Rayta',fg='green',font=("Verdana",15,'bold'),command=rayta,onvalue=1,offvalue=0,variable=var7)
rayta.grid(row=6,column=0,sticky=W)
chicken=Checkbutton(foodframe,fg='red',text='Chicken',font=('Verdana',15,'bold'),command=chicken,onvalue=1,offvalue=0,variable=var8)
chicken.grid(row=7,column=0,sticky=W)
fishsabji=Checkbutton(foodframe,text='Fish',fg='red',font=('Verdana',15,'bold'),command=fishsabji,onvalue=1,offvalue=0,variable=var9)
fishsabji.grid(row=8,column=0,sticky=W)
mutton=Checkbutton(foodframe,text='Mutton',fg='red',font=("Verdana",15,'bold'),command=mutton,onvalue=1,offvalue=0,variable=var10)
mutton.grid(row=9,column=0,sticky=W)
#foodentry
txtroti=Entry(foodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_roti)
txtroti.grid(row=0,column=1)
txtdal=Entry(foodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_dal)
txtdal.grid(row=1,column=1)
txtmixsabji=Entry(foodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_mixsabji)
txtmixsabji.grid(row=2,column=1)
txtpaneer=Entry(foodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_paneer)
txtpaneer.grid(row=3,column=1)
txtchola=Entry(foodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_chola)
txtchola.grid(row=4,column=1)
txtrice=Entry(foodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_rice)
txtrice.grid(row=5,column=1)
txtrayta=Entry(foodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_rayta)
txtrayta.grid(row=6,column=1)
txtchicken=Entry(foodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_chicken)
txtchicken.grid(row=7,column=1)
txtfish=Entry(foodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_fish)
txtfish.grid(row=8,column=1)
txtmutton=Entry(foodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_mutton)
txtmutton.grid(row=9,column=1)

#fastfood items in food frame


samosa=Checkbutton(fastfoodframe,text='Samosa',fg='green',font=('Verdana',15,'bold'),command=samosa,onvalue=1,offvalue=0,variable=var11)
samosa.grid(row=0,column=2,sticky=W)
pizza=Checkbutton(fastfoodframe,text='Pizza',fg='green',font=('Verdana',15,'bold'),command=pizza,onvalue=1,offvalue=0,variable=var12)
pizza.grid(row=1,column=2,sticky=W)
patties=Checkbutton(fastfoodframe,text='Patties',fg='green',font=('Verdana',15,'bold'),command=patties,onvalue=1,offvalue=0,variable=var13)
patties.grid(row=2,column=2,sticky=W)
noodles=Checkbutton(fastfoodframe,text='Noodles',fg='green',font=('Verdana',15,'bold'),command=noodles,onvalue=1,offvalue=0,variable=var14)
noodles.grid(row=3,column=2,sticky=W)
frenchfries=Checkbutton(fastfoodframe,text='Frenchfries',fg='green',font=('Verdana',15,'bold'),command=frenchfries,onvalue=1,offvalue=0,variable=var15)
frenchfries.grid(row=4,column=2,sticky=W)
momos=Checkbutton(fastfoodframe,text='Momos',fg='green',font=('Verdana',15,'bold'),command=momos,onvalue=1,offvalue=0,variable=var16)
momos.grid(row=5,column=2,sticky=W)
cholebhathure=Checkbutton(fastfoodframe,text='Cholebhathure',fg='green',font=('Verdana',15,'bold'),command=cholebhathure,onvalue=1,offvalue=0,variable=var17)
cholebhathure.grid(row=6,column=2,sticky=W)
burger=Checkbutton(fastfoodframe,text='Burger',fg='green',font=('Verdana',15,'bold'),onvalue=1,command=burger,offvalue=0,variable=var18)
burger.grid(row=7,column=2,sticky=W)
bhelpuri=Checkbutton(fastfoodframe,text='Bhelpuri/Chaat',fg='green',font=('Verdana',15,'bold'),command=bhelpuri,onvalue=1,offvalue=0,variable=var19)
bhelpuri.grid(row=8,column=2,sticky=W)
pakora=Checkbutton(fastfoodframe,text='Pakora',fg='green',font=('Verdana',15,'bold'),command=pakora,onvalue=1,offvalue=0,variable=var20)
pakora.grid(row=9,column=2,sticky=W)

txtsamosa=Entry(fastfoodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_samosa)
txtsamosa.grid(row=0,column=3)
txtpizza=Entry(fastfoodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_pizza)
txtpizza.grid(row=1,column=3)
txtpatties=Entry(fastfoodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_patties)
txtpatties.grid(row=2,column=3)
txtnoodles=Entry(fastfoodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_noodles)
txtnoodles.grid(row=3,column=3)
txtfrenchfries=Entry(fastfoodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_frenchfries)
txtfrenchfries.grid(row=4,column=3)
txtmomos=Entry(fastfoodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_momos)
txtmomos.grid(row=5,column=3)
txtcholebhathure=Entry(fastfoodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_cholebhathure)
txtcholebhathure.grid(row=6,column=3)
txtburger=Entry(fastfoodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_burger)
txtburger.grid(row=7,column=3)
txtbhelpuri=Entry(fastfoodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_chaat)
txtbhelpuri.grid(row=8,column=3)
txtpakora=Entry(fastfoodframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_pakora)
txtpakora.grid(row=9,column=3)


#drinks/shakes in food frames
#functions

badam=Checkbutton(drinksframe,text='Badamshake',fg='blue',font=('Verdana',15,'bold'),command=badam,onvalue=1,offvalue=0,variable=var21)
badam.grid(row=0,column=4,sticky=W)
chocolateshake=Checkbutton(drinksframe,text='Chocoshake',fg='blue',font=('Verdana',15,'bold'),command=chocolateshake,onvalue=1,offvalue=0,variable=var22)
chocolateshake.grid(row=1,column=4,sticky=W)
milkshake=Checkbutton(drinksframe,text='Milkshake',fg='blue',font=('Verdana',15,'bold'),command=milkshake,onvalue=1,offvalue=0,variable=var23)
milkshake.grid(row=2,column=4,sticky=W)
faluda=Checkbutton(drinksframe,text='Faluda',fg='blue',font=('Verdana',15,'bold'),command=faluda,onvalue=1,offvalue=0,variable=var24)
faluda.grid(row=3,column=4,sticky=W)
lassi=Checkbutton(drinksframe,text='Lassi',fg='blue',font=('Verdana',15,'bold'),command=lassi,onvalue=1,offvalue=0,variable=var25)
lassi.grid(row=4,column=4,sticky=W)
tea=Checkbutton(drinksframe,text='Tea',fg='blue',font=('Verdana',15,'bold'),command=tea,onvalue=1,offvalue=0,variable=var26)
tea.grid(row=5,column=4,sticky=W)
coffe=Checkbutton(drinksframe,text='Coffee',fg='blue',font=('Verdana',15,'bold'),command=coffe,onvalue=1,offvalue=0,variable=var27)
coffe.grid(row=6,column=4,sticky=W)
colddrinks=Checkbutton(drinksframe,text='Colddrinks',fg='blue',font=('Verdana',15,'bold'),command=colddrinks,onvalue=1,offvalue=0,variable=var28)
colddrinks.grid(row=7,column=4,sticky=W)
shikanji=Checkbutton(drinksframe,text='Shikanji',fg='blue',font=('Verdana',15,'bold'),command=shikanji,onvalue=1,offvalue=0,variable=var29)
shikanji.grid(row=8,column=4,sticky=W)
fruitshake=Checkbutton(drinksframe,text='Fruitshake',fg='blue',font=('Verdana',15,'bold'),command=fruitshake,onvalue=1,offvalue=0,variable=var30)
fruitshake.grid(row=9,column=4,sticky=W)

txtbadamshake=Entry(drinksframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_badamshake)
txtbadamshake.grid(row=0,column=5)
txtchocolateshake=Entry(drinksframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_chocolateshake)
txtchocolateshake.grid(row=1,column=5)
txtmilkshake=Entry(drinksframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_milkshake)
txtmilkshake.grid(row=2,column=5)
txtfaluda=Entry(drinksframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_faluda)
txtfaluda.grid(row=3,column=5)
txtlassi=Entry(drinksframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_lassi)
txtlassi.grid(row=4,column=5)
txttea=Entry(drinksframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_tea)
txttea.grid(row=5,column=5)
txtcoffe=Entry(drinksframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_coffe)
txtcoffe.grid(row=6,column=5)
txtcolddrinks=Entry(drinksframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_colddrinks)
txtcolddrinks.grid(row=7,column=5)
txtshinkanji=Entry(drinksframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_shikanji)
txtshinkanji.grid(row=8,column=5)
txtfruitshake=Entry(drinksframe,width=3,font=('Verdana',15,'bold'),state=DISABLED,bd=5,textvariable=tv_fruitshake)
txtfruitshake.grid(row=9,column=5)

#Cakes and south indian famous food



chocolate=Checkbutton(cakesframe,text='chocolate',fg='red4',font=('Verdana',13,'bold'),command=chocalate,onvalue=1,offvalue=0,variable=var31)
chocolate.grid(row=0,column=6,sticky=W)
pineapple=Checkbutton(cakesframe,text='Pineapple',fg='red4',font=('Verdana',13,'bold'),command=pineapple,onvalue=1,offvalue=0,variable=var32)
pineapple.grid(row=1,column=6,sticky=W)
strawberry=Checkbutton(cakesframe,text='Strawberry',fg='red4',font=('Verdana',13,'bold'),command=strawberry,onvalue=1,offvalue=0,variable=var33)
strawberry.grid(row=2,column=6,sticky=W)
blackforest=Checkbutton(cakesframe,text='Blackforest',fg='red4',font=('Verdana',13,'bold'),command=blackforest,onvalue=1,offvalue=0,variable=var34)
blackforest.grid(row=3,column=6,sticky=W)
kitkat=Checkbutton(cakesframe,text='Kitkat',fg='red4',font=('Verdana',13,'bold'),command=kitkat,onvalue=1,offvalue=0,variable=var35)
kitkat.grid(row=4,column=6,sticky=W)
masaladosa=Checkbutton(southindiafood,text='Masaladosa',font=('Verdana',13,'bold'),command=masaladosa,onvalue=1,offvalue=0,variable=var36)
masaladosa.grid(row=0,column=6,sticky=W)
idli=Checkbutton(southindiafood,text='Idli',font=('Verdana',13,'bold'),command=idli,onvalue=1,offvalue=0,variable=var37)
idli.grid(row=1,column=6,sticky=W)
uttapam=Checkbutton(southindiafood,text='Uttapam',font=('Verdana',13,'bold'),command=uttapam,onvalue=1,offvalue=0,variable=var38)
uttapam.grid(row=2,column=6,sticky=W)
biryani=Checkbutton(southindiafood,text='Biryani',font=('Verdana',13,'bold'),command=biryani,onvalue=1,offvalue=0,variable=var39)
biryani.grid(row=3,column=6,sticky=W)
bonda=Checkbutton(southindiafood,text='Bonda',font=('Verdana',13,'bold'),command=bonda,onvalue=1,offvalue=0,variable=var40)
bonda.grid(row=4,column=6,sticky=W)

txtchocolate=Entry(cakesframe,state=DISABLED,cursor='hand2',width=3,font=('Verdana',13,'bold'),bd=5,textvariable=tv_chocolate)
txtchocolate.grid(row=0,column=7)
txtpineapple=Entry(cakesframe,state=DISABLED,cursor='hand2',width=3,font=('Verdana',13,'bold'),bd=5,textvariable=tv_pineapple)
txtpineapple.grid(row=1,column=7)
txtstrawberry=Entry(cakesframe,state=DISABLED,cursor='hand2',width=3,font=('Verdana',13,'bold'),bd=5,textvariable=tv_strawberry)
txtstrawberry.grid(row=2,column=7)
txtblackforest=Entry(cakesframe,state=DISABLED,cursor='hand2',width=3,font=('Verdana',13,'bold'),bd=5,textvariable=tv_blackforest)
txtblackforest.grid(row=3,column=7)
txtkitkat=Entry(cakesframe,state=DISABLED,width=3,cursor='hand2',font=('Verdana',13,'bold'),bd=5,textvariable=tv_kitkat)
txtkitkat.grid(row=4,column=7)
txtmasaladosa=Entry(southindiafood,state=DISABLED,width=3,font=('Verdana',13,'bold'),bd=5,textvariable=tv_masaladosa)
txtmasaladosa.grid(row=0,column=7)
txtidli=Entry(southindiafood,state=DISABLED,width=3,font=('Verdana',13,'bold'),bd=5,textvariable=tv_idli)
txtidli.grid(row=1,column=7)
txtuttapam=Entry(southindiafood,state=DISABLED,width=3,font=('Verdana',13,'bold'),bd=5,textvariable=tv_uttapam)
txtuttapam.grid(row=2,column=7)
txtbiryani=Entry(southindiafood,state=DISABLED,width=3,font=('Verdana',13,'bold'),bd=5,textvariable=tv_biryani)
txtbiryani.grid(row=3,column=7)
txtbonda=Entry(southindiafood,state=DISABLED,width=3,font=('Verdana',13,'bold'),bd=5,textvariable=tv_bonda)
txtbonda.grid(row=4,column=7)

#foodcost and subtotal and total cost
co_food=Label(costframe,text='Cost of food:',fg='purple4',state=NORMAL,font=('Verdana',15,'bold'))
co_food.grid(row=0,column=0,padx=30)
txtco_food=Entry(costframe,state='readonly',width=12,font=('Verdana',15,'bold'),textvariable=costoffoodvar,bd=5,cursor='hand2')
txtco_food.grid(row=0,column=1)
co_fastfood=Label(costframe,text='cost of Fastfood:',fg='purple4',state=NORMAL,font=('Verdana',15,'bold'))
co_fastfood.grid(row=1,column=0,padx=30)
txtco_fastfood=Entry(costframe,state='readonly',width=12,font=('Verdana',15,'bold'),textvariable=costoffastfoodvar,bd=5,cursor='hand2')
txtco_fastfood.grid(row=1,column=1)
co_drinks=Label(costframe,text='Cost of Drinks:',fg='purple4',state=NORMAL,font=('Verdana',15,'bold'))
co_drinks.grid(row=2,column=0,padx=30)
txtco_drinks=Entry(costframe,state='readonly',width=12,font=('Verdana',15,'bold'),textvariable=costofdrinksvar,bd=5,cursor='hand2')
txtco_drinks.grid(row=2,column=1)
co_cakes=Label(costframe,text='Cost of Cakes:',fg='purple4',state=NORMAL,font=('Verdana',15,'bold'))
co_cakes.grid(row=3,column=0,padx=30)
txtco_cakes=Entry(costframe,state='readonly',width=12,font=('Verdana',15,'bold'),textvariable=costofcakesvar,bd=5,cursor='hand2')
txtco_cakes.grid(row=3,column=1)
co_otherfood=Label(costframe,text='Cost of OtherFood:',fg='purple4',state=NORMAL,font=('Verdana',15,'bold'))
co_otherfood.grid(row=0,column=2,padx=30)
txtco_otherfood=Entry(costframe,state='readonly',width=12,font=('Verdana',15,'bold'),textvariable=costofotherfoodvar,bd=5,cursor='hand2')
txtco_otherfood.grid(row=0,column=3)
lblsubtotal=Label(costframe,text='Sub-total :',fg='purple4',font=('Verdana',15,'bold'),bd=5,state=NORMAL)
lblsubtotal.grid(row=1,column=2,padx=30)
txtsubtotal=Entry(costframe,state='readonly',width=12,font=('Verdana',15,'bold'),textvariable=subtotalvar,bd=5,cursor='hand2')
txtsubtotal.grid(row=1,column=3)
lblservice=Label(costframe,text='Service-tax :',fg='purple4',font=('Verdana',15,'bold'),bd=5,state=NORMAL)
lblservice.grid(row=2,column=2,padx=30)
txtservice=Entry(costframe,state='readonly',width=12,font=('Verdana',15,'bold'),textvariable=servicetaxvar,bd=5,cursor='hand2')
txtservice.grid(row=2,column=3)
lbltotal=Label(costframe,text='Total-Bill :',fg='purple4',font=('Verdana',15,'bold'),bd=5,state=NORMAL)
lbltotal.grid(row=3,column=2,padx=30)
txttotal=Entry(costframe,state='readonly',width=12,font=('Verdana',15,'bold'),textvariable=totalcostvar,bd=5,cursor='hand2')
txttotal.grid(row=3,column=3)
#rightframe calculator and buttons and reciepts

buttonTotal=Button(buttonframe,text='Total',font=('Verdana',13,'bold'),fg='white',bg='purple',bd=3,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=0)
buttonReceipt=Button(buttonframe,text='Receipt',font=('Verdana',13,'bold'),fg='white',bg='purple',bd=3,padx=5,command=receipt)
buttonReceipt.grid(row=0,column=1)
buttonSave=Button(buttonframe,text='Save',font=('Verdana',13,'bold'),fg='white',bg='purple',bd=3,padx=5,command=save)
buttonSave.grid(row=0,column=2)
buttonSend=Button(buttonframe,text='Send',font=('Verdana',13,'bold'),fg='white',bg='purple',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)
buttonReset=Button(buttonframe,text='Reset',font=('Verdana',13,'bold'),fg='white',bg='purple',bd=3,padx=5,command=reset)
buttonReset.grid(row=0,column=4)
textReceipt=Text(receiptframe,font=('Verdana',10,'bold'),bg='black',fg='yellow',bd=3,width=44,height=16)
textReceipt.grid(row=0,column=0)

operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''

calculatorField=Entry(calculatorframe,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)
button7=Button(calculatorframe,text='7',font=('arial',16,'bold'),fg='white',bg='coral',bd=6,width=6,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)
button8=Button(calculatorframe,text='8',font=('arial',16,'bold'),fg='white',bg='coral',bd=6,width=6,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)
button9=Button(calculatorframe,text='9',font=('arial',16,'bold'),fg='white',bg='coral',bd=6,width=6
               ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)
buttonPlus=Button(calculatorframe,text='+',font=('arial',16,'bold'),fg='white',bg='coral',bd=6,width=6
                  ,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)
button4=Button(calculatorframe,text='4',font=('arial',16,'bold'),fg='white',bg='coral',bd=6,width=6
               ,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)
button5=Button(calculatorframe,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)
button6=Button(calculatorframe,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)
buttonMinus=Button(calculatorframe,text='-',font=('arial',16,'bold'),fg='white',bg='coral',bd=6,width=6
                   ,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)
button1=Button(calculatorframe,text='1',font=('arial',16,'bold'),fg='white',bg='coral',bd=6,width=6
               ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)
button2=Button(calculatorframe,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)
button3=Button(calculatorframe,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)
buttonMult=Button(calculatorframe,text='*',font=('arial',16,'bold'),fg='white',bg='coral',bd=6,width=6
                  ,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)
buttonAns=Button(calculatorframe,text='Ans',font=('arial',16,'bold'),fg='white',bg='green',bd=6,width=6,
                 command=lambda:answer())
buttonAns.grid(row=4,column=0)
buttonClear=Button(calculatorframe,text='Clear',font=('arial',16,'bold'),fg='white',bg='red3',bd=6,width=6
                   ,command=lambda:clear())
buttonClear.grid(row=4,column=1)
button0=Button(calculatorframe,text='0',font=('arial',16,'bold'),fg='white',bg='coral',bd=6,width=6
               ,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)
buttonDiv=Button(calculatorframe,text='/',font=('arial',16,'bold'),fg='white',bg='coral',bd=6,width=6,
                 command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)


win.mainloop()