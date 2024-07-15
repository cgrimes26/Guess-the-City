"""
module name: purchase
function name: purchase
overview of this function:
1) Customer interaction for what and how much the want buy.
2) check the user interaction valid or not with exception handelling.
3) calculating the customer purchase product with discount(if discountable)
4) show the last update of the product
5) write the invoice for customer with unique naming
"""


def purchase(List):
    L = List  # assign list with variable name 'L'.
    a_name = input("Please enter your name: ")
    print("\nHello " + a_name + "! Welcome to Best Tees.\nLook at above and select product as your choice.")
    q = {}  # assign empty dictionary with variable name 'q'.
    flag = "Y"
    while flag.upper() == "Y":  # check and go if flag is 'Y' or 'y'.
        product = input("\nWhich products would you like to buy? ")
        product_name = product.upper()  # change the string value in the upper case.
### check the user entered product name with stock of store
        if product_name == L[0][0].upper() \
            or product_name == L[1][0].upper() \
            or product_name == L[2][0].upper() \
            or product_name == L[3][0].upper() \
            or product_name == L[4][0].upper() \
            or product_name == L[5][0].upper() \
            or product_name == L[6][0].upper() \
            or product_name == L[7][0].upper() \
            or product_name == L[8][0].upper() \
            or product_name == L[9][0].upper() \
            or product_name == L[10][0].upper() \
            or product_name == L[11][0].upper() \
            or product_name == L[12][0].upper() \
            or product_name == L[13][0].upper() \
            or product_name == L[14][0].upper() \
            or product_name == L[15][0].upper() \ 
            or product_name == L[16][0].upper() \
            or product_name == L[17][0].upper() \
            or product_name == L[18][0].upper() \
            or product_name == L[19][0].upper() \
            or product_name == L[20][0].upper() \
            or product_name == L[21][0].upper() \
            or product_name == L[22][0].upper() \
            or product_name == L[23][0].upper() \
            or product_name == L[24][0].upper() \
            or product_name == L[25][0].upper() \
            or product_name == L[26][0].upper() \
            or product_name == L[27][0].upper() \
            or product_name == L[28][0].upper() \
            or product_name == L[29][0].upper() \
            or product_name == L[30][0].upper() \
            or product_name == L[31][0].upper() \
            or product_name == L[32][0].upper() \
            or product_name == L[33][0].upper() \
            or product_name == L[35][0].upper() \
            or product_name == L[36][0].upper() \
            or product_name == L[37][0].upper() :
            p = True
            while p == True:
                try:
                    p_quantity = int(input("How many " + product + " do you want to buy: "))
                    p = False
                except:  # executes, if customer entered unexpected value.
                    print("\t\tError!!!\nPlease enter integer value!! ")
            if product_name == L[0][0].upper() and p_quantity <= int(L[0][2]):
                q[product_name] = p_quantity
            elif product_name == L[1][0].upper() and p_quantity <= int(L[1][2]):
                q[product_name] = p_quantity
            elif product_name == L[2][0].upper() and p_quantity <= int(L[2][2]):
                q[product_name] = p_quantity
            elif product_name == L[3][0].upper() and p_quantity <= int(L[3][2]):
                q[product_name] = p_quantity
            elif product_name == L[4][0].upper() and p_quantity <= int(L[4][2]):
                q[product_name] = p_quantity
            elif product_name == L[5][0].upper() and p_quantity <= int(L[5][2]):
                q[product_name] = p_quantity
            elif product_name == L[6][0].upper() and p_quantity <= int(L[6][2]):
                q[product_name] = p_quantity
            elif product_name == L[7][0].upper() and p_quantity <= int(L[7][2]):
                q[product_name] = p_quantity
            elif product_name == L[8][0].upper() and p_quantity <= int(L[8][2]):
                q[product_name] = p_quantity
            elif product_name == L[9][0].upper() and p_quantity <= int(L[9][2]):
                q[product_name] = p_quantity
            elif product_name == L[10][0].upper() and p_quantity <= int(L[10][2]):
                q[product_name] = p_quantity
            elif product_name == L[11][0].upper() and p_quantity <= int(L[11][2]):
                q[product_name] = p_quantity
            elif product_name == L[12][0].upper() and p_quantity <= int(L[12][2]):
                q[product_name] = p_quantity
            elif product_name == L[13][0].upper() and p_quantity <= int(L[13][2]):
                q[product_name] = p_quantity
            elif product_name == L[14][0].upper() and p_quantity <= int(L[14][2]):
                q[product_name] = p_quantity
            elif product_name == L[15][0].upper() and p_quantity <= int(L[15][2]):
                q[product_name] = p_quantity
            elif product_name == L[16][0].upper() and p_quantity <= int(L[16][2]):
                q[product_name] = p_quantity
            elif product_name == L[17][0].upper() and p_quantity <= int(L[17][2]):
                q[product_name] = p_quantity
            elif product_name == L[18][0].upper() and p_quantity <= int(L[18][2]):
                q[product_name] = p_quantity
            elif product_name == L[19][0].upper() and p_quantity <= int(L[19][2]):
                q[product_name] = p_quantity
            elif product_name == L[20][0].upper() and p_quantity <= int(L[20][2]):
                q[product_name] = p_quantity
            elif product_name == L[21][0].upper() and p_quantity <= int(L[21][2]):
                q[product_name] = p_quantity
            elif product_name == L[22][0].upper() and p_quantity <= int(L[22][2]):
                q[product_name] = p_quantity
            elif product_name == L[23][0].upper() and p_quantity <= int(L[23][2]):
                q[product_name] = p_quantity
            elif product_name == L[24][0].upper() and p_quantity <= int(L[24][2]):
                q[product_name] = p_quantity
            elif product_name == L[25][0].upper() and p_quantity <= int(L[25][2]):
                q[product_name] = p_quantity
            elif product_name == L[26][0].upper() and p_quantity <= int(L[26][2]):
                q[product_name] = p_quantity
            elif product_name == L[27][0].upper() and p_quantity <= int(L[27][2]):
                q[product_name] = p_quantity
            elif product_name == L[28][0].upper() and p_quantity <= int(L[28][2]):
                q[product_name] = p_quantity
            elif product_name == L[29][0].upper() and p_quantity <= int(L[29][2]):
                q[product_name] = p_quantity
            elif product_name == L[30][0].upper() and p_quantity <= int(L[30][2]):
                q[product_name] = p_quantity
            elif product_name == L[31][0].upper() and p_quantity <= int(L[31][2]):
                q[product_name] = p_quantity
            elif product_name == L[32][0].upper() and p_quantity <= int(L[32][2]):
                q[product_name] = p_quantity
            elif product_name == L[33][0].upper() and p_quantity <= int(L[33][2]):
                q[product_name] = p_quantity
            elif product_name == L[34][0].upper() and p_quantity <= int(L[34][2]):
                q[product_name] = p_quantity
            elif product_name == L[35][0].upper() and p_quantity <= int(L[35][2]):
                q[product_name] = p_quantity
            elif product_name == L[36][0].upper() and p_quantity <= int(L[36][2]):
                q[product_name] = p_quantity
            elif product_name == L[37][0].upper() and p_quantity <= int(L[37][2]):
                q[product_name] = p_quantity
            else:
                print(
                    "\nSorry!! " + a_name + "!, " + product + " is out of stock.\nWe will add stock of " + product + " later. \nLets hope, you will get this product after next shopping.\n")

            flag = (input(a_name + " do you want buy more products?(Y/N)"))
        else:
            print("sorry!! " + product + " is not available in our store.")
            print("\nChoose from following products please!")
            print("--------------------------------------------")
            print("PRODUCT\t\tPRICE\t\tCOLORS")
            print("--------------------------------------------")
            for i in range(len(L)):
                print(L[i][0], "\t\t", L[i][1], "\t\t", L[i][2], "\t\t", L[i][3], "\t\t", L[i][4], "\t\t", L[i][5], "\t\t", L[i][6], "\t\t", L[i][7], "\t\t", L[i][8], "\t\t", L[i][9], "\t\t", L[i][10],
                "\t\t", L[i][11], "\t\t", L[i][12], "\t\t", L[i][13], "\t\t", L[i][14], "\t\t", L[i][15], "\t\t", L[i][16], "\t\t", L[i][17], "\t\t", L[i][18], "\t\t", L[i][19], "\t\t", L[i][20], 
                "\t\t", L[i][21], "\t\t", L[i][22], "\t\t", L[i][23], "\t\t", L[i][24], "\t\t", L[i][25], "\t\t", L[i][26], "\t\t", L[i][27], "\t\t", L[i][28], "\t\t", L[i][29], "\t\t", L[i][30], 
                "\t\t", L[i][31], "\t\t", L[i][32], "\t\t", L[i][33], "\t\t", L[i][34], "\t\t", L[i][35], "\t\t", L[i][36], "\t\t", L[i][37], "\t\t",)  # print, last updated product name, quantity and price.
            print("--------------------------------------------")

    print("\nYou Chose Items and it's Quantity respectively:\n", q, "\n")
    '''
        In the following operation:
        1) change every string value in the upper case latter.
        2) check what is the product entered by customer.
        3) executes respective condition if product is phone or laptop or hdd entered by customer.
    '''
    f_amount = 0  # final amount
    for keys in q.keys():
        if keys == L[0][0].upper():  # executes this operation if product is phone entered by customer.
            p_price = int(L[0][1])
            p_num = int(q[keys])
            p_amount = (p_price * p_num)
            f_amount += (p_price * p_num)
            print("\nTotal cost for T-shirt(S-XL): ", p_amount)
        elif keys == L[1][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[1][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for T-shirt(2XL): ", l_amount)
        elif keys == L[2][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[2][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for T-shirt(3XL): ", l_amount)
        elif keys == L[3][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[3][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for T-shirt(4XL): ", l_amount)
        elif keys == L[4][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[4][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for T-shirt(S-XL): ", l_amount)
        elif keys == L[5][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[5][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for T-shirt(2XL): ", l_amount)
        elif keys == L[6][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[6][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for T-shirt(3XL): ", l_amount)
        elif keys == L[7][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[7][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for T-shirt(4XL): ", l_amount)
        elif keys == L[8][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[8][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Long-sleeve(S-XL): ", l_amount)
        elif keys == L[9][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[9][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Long-sleeve(2XL): ", l_amount)
        elif keys == L[10][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[10][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Long-sleeve(3XL): ", l_amount)
        elif keys == L[11][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[11][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Long-sleeve(4XL): ", l_amount)
        elif keys == L[12][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[12][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Long-sleeve(S-XL): ", l_amount)
        elif keys == L[13][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[13][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Long-sleeve(2XL): ", l_amount)
        elif keys == L[14][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[14][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Long-sleeve(3XL): ", l_amount)
        elif keys == L[15][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[15][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Long-sleeve(4XL): ", l_amount)
        elif keys == L[16][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[16][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Windbreaker(S-XL): ", l_amount)
        elif keys == L[17][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[17][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Windbreaker(2XL): ", l_amount)
        elif keys == L[18][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[18][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Windbreaker(3XL): ", l_amount)
        elif keys == L[19][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[19][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Windbreaker(4XL): ", l_amount)
        elif keys == L[20][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[20][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Hooded Zipper(S-XL): ", l_amount)
        elif keys == L[21][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[21][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Hooded Zipper(2XL): ", l_amount)
        elif keys == L[22][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[22][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Hooded Zipper(3XL): ", l_amount)
        elif keys == L[23][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[23][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Hooded Zipper(4XL): ", l_amount)
        elif keys == L[24][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[24][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Hoodies(S-XL): ", l_amount)
        elif keys == L[25][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[25][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Hoodies(2XL): ", l_amount)
        elif keys == L[26][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[26][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Hoodies(3XL): ", l_amount)
        elif keys == L[27][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[27][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Hoodies(4XL): ", l_amount)
        elif keys == L[28][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[28][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Hats/Caps: ", l_amount)
        elif keys == L[29][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[29][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Tote bag(s): ", l_amount)
        elif keys == L[30][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[30][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Jersey(S-XL): ", l_amount)
        elif keys == L[31][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[31][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Jersey(2XL): ", l_amount)
        elif keys == L[32][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[32][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Jersey(3XL): ", l_amount)
        elif keys == L[33][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[33][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Jersey(4XL): ", l_amount)
        elif keys == L[34][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[34][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Name on back(all on sizes): ", l_amount)
        elif keys == L[35][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[35][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Number on back(6-in): ", l_amount)
        elif keys == L[36][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[36][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total cost for Number on back(8-in): ", l_amount)
        else:  # executes this operation if product is hdd entered by customer.
            h_price = int(L[37][1])
            h_num = int(q[keys])
            h_amount = (h_price * h_num)
            f_amount += (h_price * h_num)
            print("Total cost for Hand towel: ", h_amount)
    print("\nYour discountable total amount is: ", f_amount)

    '''
        In the following operation:
        1) ask to customer for expected discount % in total purchase amount.
        2) check the total purchase amount which is dcustomer expected discountable or not.
        3) check the total purchase amount which is basic discountable or not.
    '''
    disc = float(input("Please enter your expected discount (%): "))
    dis = 0.0
    if (f_amount >= 5000) and (f_amount < 10000):
        discount = disc
        if discount <= 5.0:
            dis = (discount * f_amount) / 100
            total = float(f_amount - dis)
            print("You got your expected " + str(disc) + "% discount and amount is: ", dis)
        else:
            discount = 5.0
            dis = (discount * f_amount) / 100
            total = float(f_amount - dis)
            print("You did not got your expected " + str(
                disc) + "% discount\nBecause, your totel purchase is not meet the minimum criteria for " + str(
                disc) + "% discount.")
            print("You got basic 5% discount and discounted amount is:", dis)
    elif f_amount >= 10000:
        discount = disc
        if discount <= 10.0:
            dis = (discount * f_amount) / 100
            total = float(f_amount - dis)
            print("You got your expected " + str(disc) + "% discount and amount is: ", dis)
        else:
            discount = 10.0
            dis = (discount * f_amount) / 100
            total = float(f_amount - dis)
            print("You did not got your expected " + str(
                disc) + "% discount\nBecause, your totel purchase is not meet the minimum criteria for " + str(
                disc) + "% discount.")
            print("You got basic 10% discount and discounted amount is:", dis)
    else:
        discount = 0.0
        total = float(f_amount)
        print("You did not got your expected " + str(
            disc) + "% discount\nBecause, your totel purchase is not meet the minimum criteria for " + str(
            disc) + "% discount.")
    print("Your payable amount is: ", total)

    '''
        In the following operation:
        1) write a each unique involve name which includes current date and time with customer name as well.
        2) write a purchase product name and details in file (invoice).
        3) write a discounted amount and final payable amount in file (invoice).
    '''

    import datetime  # import system date and time for create a unique invoive name.
    dt = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day) + "-" + str(datetime.datetime.now().hour) + "-" + str(
        datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
    invoice = str(dt)  # unique invoice
    t = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day)  # date
    d = str(t)  # date
    u = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(
        datetime.datetime.now().second)  # time
    e = str(u)  # time

    file = open(invoice + " (" + a_name + ").txt", "w")  # generate a unique invoive name and open it in write mode.
    file.write("=============================================================")
    file.write("\nBEST TEES\t\t\t\tINVOICE")
    file.write("\n\nInvoice: " + invoice + "\t\tDate: " + d + "\n\t\t\t\t\tTime: " + e + "")
    file.write("\nName of Customer: " + str(a_name) + "")
    file.write("\n=============================================================")
    file.write("\nPARTICULAR\tQUANTITY\tUNIT PRICE\tTOTAL")
    file.write("\n-------------------------------------------------------------")

    for keys in q.keys():  # In this loop, write in a file only those product which is purchase by user.
        if keys == "T-shirt(S-XL)":
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['T-shirt(S-XL)']) + " \t\t " + str(L[0][1]) + " \t\t " + str(p_amount)))
        elif keys == "T-shirt(2XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['T-shirt(2XL)']) + " \t\t " + str(L[1][1]) + " \t\t " + str(l_amount)))
        elif keys == "T-shirt(3XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['T-shirt(3XL)']) + " \t\t " + str(L[2][1]) + " \t\t " + str(l_amount)))
        elif keys == "T-shirt(4XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['T-shirt(4XL)']) + " \t\t " + str(L[3][1]) + " \t\t " + str(l_amount)))
        elif keys == "T-shirt(S-XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['T-shirt(S-XL)']) + " \t\t " + str(L[4][1]) + " \t\t " + str(l_amount)))
        elif keys == "T-shirt(2XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['T-shirt(2XL)']) + " \t\t " + str(L[5][1]) + " \t\t " + str(l_amount)))
        elif keys == "T-shirt(3XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['T-shirt(3XL)']) + " \t\t " + str(L[6][1]) + " \t\t " + str(l_amount)))
        elif keys == "T-shirt(4XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['T-shirt(4XL)']) + " \t\t " + str(L[7][1]) + " \t\t " + str(l_amount)))
        elif keys == "Long-sleeve shirt(S-XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Long-sleeve shirt(S-XL)']) + " \t\t " + str(L[8][1]) + " \t\t " + str(l_amount)))
        elif keys == "Long-sleeve shirt(2XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Long-sleeve shirt(2XL)']) + " \t\t " + str(L[9][1]) + " \t\t " + str(l_amount)))
        elif keys == "Long-sleeve shirt(3XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Long-sleeve shirt(3XL)']) + " \t\t " + str(L[10][1]) + " \t\t " + str(l_amount)))
        elif keys == "Long-sleeve shirt(4XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Long-sleeve shirt(4XL)']) + " \t\t " + str(L[11][1]) + " \t\t " + str(l_amount)))
        elif keys == "Long-sleeve shirt(S-XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Long-sleeve shirt(S-XL)']) + " \t\t " + str(L[12][1]) + " \t\t " + str(l_amount)))
        elif keys == "Long-sleeve shirt(2XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Long-sleeve shirt(2XL)']) + " \t\t " + str(L[13][1]) + " \t\t " + str(l_amount)))
        elif keys == "Long-sleeve shirt(3XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Long-sleeve shirt(3XL)']) + " \t\t " + str(L[14][1]) + " \t\t " + str(l_amount)))
        elif keys == "Long-sleeve shirt(4XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Long-sleeve shirt(4XL)']) + " \t\t " + str(L[15][1]) + " \t\t " + str(l_amount)))
        elif keys == "Winbreaker(S-XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Winbreaker(S-XL)']) + " \t\t " + str(L[16][1]) + " \t\t " + str(l_amount)))
        elif keys == "Windbreaker(2XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Windbreaker(2XL)']) + " \t\t " + str(L[17][1]) + " \t\t " + str(l_amount)))
        elif keys == "Windbreaker(3XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Windbreaker(3XL)']) + " \t\t " + str(L[18][1]) + " \t\t " + str(l_amount)))
        elif keys == "Windbreaker(4XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Windbreaker(4XL)']) + " \t\t " + str(L[19][1]) + " \t\t " + str(l_amount)))
        elif keys == "Hooded Zipper(S-XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Hooded Zipper(S-XL)']) + " \t\t " + str(L[20][1]) + " \t\t " + str(l_amount)))
        elif keys == "Hooded Zipper(2XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Hooded Zipper(2XL)']) + " \t\t " + str(L[21][1]) + " \t\t " + str(l_amount)))
        elif keys == "Hooded Zipper(3XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Hooded Zipper(3XL)']) + " \t\t " + str(L[22][1]) + " \t\t " + str(l_amount)))
        elif keys == "Hooded Zipper(4XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Hooded Zipper(4XL)']) + " \t\t " + str(L[23][1]) + " \t\t " + str(l_amount)))
        elif keys == "Hoodies(S-XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Hoodies(S-XL)']) + " \t\t " + str(L[24][1]) + " \t\t " + str(l_amount)))
        elif keys == "Hoodies(2XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Hoodies(2XL)']) + " \t\t " + str(L[25][1]) + " \t\t " + str(l_amount)))
        elif keys == "Hoodies(3XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Hoodies(3XL)']) + " \t\t " + str(L[26][1]) + " \t\t " + str(l_amount)))
        elif keys == "Hoodies(4XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Hoodies(4XL)']) + " \t\t " + str(L[27][1]) + " \t\t " + str(l_amount)))
        elif keys == "Hats/Caps":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Hats/Caps']) + " \t\t " + str(L[28][1]) + " \t\t " + str(l_amount)))
        elif keys == "Tote bag":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Tote bag']) + " \t\t " + str(L[29][1]) + " \t\t " + str(l_amount)))
        elif keys == "Jersey(S-XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Jersey(S-XL)']) + " \t\t " + str(L[30][1]) + " \t\t " + str(l_amount)))
        elif keys == "Jersey(2XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Jersey(2XL)']) + " \t\t " + str(L[31][1]) + " \t\t " + str(l_amount)))
        elif keys == "Jersey(3XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Jersey(3XL)']) + " \t\t " + str(L[32][1]) + " \t\t " + str(l_amount)))
        elif keys == "(Jersey(4XL)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Jersey(4XL)']) + " \t\t " + str(L[33][1]) + " \t\t " + str(l_amount)))
        elif keys == "Name on back":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Name on back']) + " \t\t " + str(L[34][1]) + " \t\t " + str(l_amount)))
        elif keys == "Number on back(6-in)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Number on back(6-in)']) + " \t\t " + str(L[35][1]) + " \t\t " + str(l_amount)))
        elif keys == "Number on back(8-in)":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['Number on back(8-in)']) + " \t\t " + str(L[36][1]) + " \t\t " + str(l_amount)))
        else:
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['Hand towel']) + " \t\t " + str(L[37][1]) + " \t\t " + str(h_amount)))

    file.write("\n\n-------------------------------------------------------------")
    file.write("\n\t\t\tYour discountable amount: " + str(f_amount))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\t\t   Your " + str(discount) + "% discounted amount is: " + str(dis))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\t\t\t Your payable amount is: " + str(total))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\n\tThank You " + a_name + " for your shopping.\n\t\tSee you again!")
    file.write("\n=============================================================")
    file.close()
    return q
