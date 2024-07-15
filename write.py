def over_write(List, Dictionary):   # an overwrite function
    L = List    # assign list with variable name 'L'
    d = Dictionary    # assign Dictionary with variable name 'd'
    """
    Update quantity of product after customer purchased some quantity of any product.
    And print remaining stock products.
    """
    for keys in d.keys():
        if keys == "T-shirt(S-XL)":
            L[0][2] = str(int(L[0][2])-d['T-shirt(S-XL'])
        elif keys == "T-shirt(2XL)":
            L[1][2] = str(int(L[1][2])-d['T-shirt(2XL)'])
        elif keys == "T-shirt(3XL)":
            L[2][2] = str(int(L[2][2])-d['T-shirt(3XL)'])
        elif keys == "T-shirt(4XL)":
            L[3][2] = str(int(L[3][2])-d['T-shirt(4XL)'])
        elif keys == "T-shirt(S-XL)":
            L[4][2] = str(int(L[4][2])-d['T-shirt(S-XL)'])
        elif keys == "T-shirt(2XL)":
            L[5][2] = str(int(L[5][2])-d['T-shirt(2XL)'])
        elif keys == "T-shirt(3XL)":
            L[6][2] = str(int(L[6][2])-d['T-shirt(3XL)'])
        elif keys == "T-shirt(4XL)":
            L[7][2] = str(int(L[7][2])-d['T-shirt(4XL)'])
        elif keys == "Long-sleeve(S-XL)":
            L[8][2] = str(int(L[8][2])-d['Long-sleeve(S-XL)'])
        elif keys == "Long-sleeve(2XL)":
            L[9][2] = str(int(L[9][2])-d['Long-sleeve(2XL)'])
        elif keys == "Long-sleeve(3XL)":
            L[10][2] = str(int(L[10][2])-d['Long-sleeve(3XL)'])
        elif keys == "Long-sleeve(4XL)":
            L[11][2] = str(int(L[11][2])-d['Long-sleeve(4XL)'])
        elif keys == "Long-sleeve(S-XL)":
            L[12][2] = str(int(L[12][2])-d['Long-sleeve(S-XL)'])
        elif keys == "Long-sleeve(2XL)":
            L[13][2] = str(int(L[13][2])-d['Long-sleeve(2XL)'])
        elif keys == "Long-sleeve(3XL)":
            L[14][2] = str(int(L[14][2])-d['Long-sleeve(3XL)'])
        elif keys == "Long-sleeve(4XL)":
            L[15][2] = str(int(L[15][2])-d['Long-sleeve(4XL)'])
        elif keys == "Windbreaker(S-XL)":
            L[16][2] = str(int(L[16][2])-d['Windbreaker(S-XL)'])
        elif keys == "Windbreaker(2XL)":
            L[17][2] = str(int(L[17][2])-d['Windbreaker(2XL)'])
        elif keys == "Windbreaker(3XL)":
            L[18][2] = str(int(L[18][2])-d['Windbreaker(3XL)'])
        elif keys == "Windbreaker(4XL)":
            L[19][2] = str(int(L[19][2])-d['Windbreaker(4XL)'])
        elif keys == "Hooded Zipper(S-XL)":
            L[20][2] = str(int(L[20][2])-d['Hooded Zipper(S-XL)'])
        elif keys == "Hooded Zipper(2XL)":
            L[21][2] = str(int(L[21][2])-d['Hooded Zipper(2XL)'])
        elif keys == "Hooded Zipper(3XL)":
            L[22][2] = str(int(L[22][2])-d['Hooded Zipper(3XL)'])
        elif keys == "Hooded Zipper(4XL)":
            L[23][2] = str(int(L[23][2])-d['Hooded Zipper(4XL)'])
        elif keys == "Hoodies(S-XL)":
            L[24][2] = str(int(L[24][2])-d['Hoodies(S-XL)'])
        elif keys == "Hoodies(2XL)":
            L[25][2] = str(int(L[25][2])-d['Hoodies(2XL)'])
        elif keys == "Hoodies(3XL)":
            L[26][2] = str(int(L[26][2])-d['Hoodies(3XL)'])
        elif keys == "Hoodies(4XL)":
            L[27][2] = str(int(L[27][2])-d['Hoodies(4XL)'])
        elif keys == "Hats/Caps":
            L[28][2] = str(int(L[28][2])-d['Hats/Caps'])
        elif keys == "Tote bag(s)":
            L[29][2] = str(int(L[29][2])-d['Tote bag(s)'])
        elif keys == "Jersey(S-XL)":
            L[30][2] = str(int(L[30][2])-d['Jersey(S-XL)'])
        elif keys == "Jersey(2XL)":
            L[31][2] = str(int(L[31][2])-d['Jersey(2XL)'])
        elif keys == "Jersey(3XL)":
            L[32][2] = str(int(L[32][2])-d['Jersey(3XL)'])
        elif keys == "Jersey(4XL)":
            L[33][2] = str(int(L[33][2])-d['Jersey(4XL)'])
        elif keys == "Name on back(all sizes)":
            L[34][2] = str(int(L[34][2])-d['Name on back (all sizes)'])
        elif keys == "Number on back(6-in)":
            L[35][2] = str(int(L[35][2])-d['Number on back(6-in)'])
        elif keys == "Number on back(8-in)":
            L[36][2] = str(int(L[36][2])-d['Number on back(8-in)'])
        else:
            L[2][2] = str(int(L[37][2])-d['Hand towel'])
    print("\nRemaining Stock Products:\n",L)
        
    files = open("products.txt", "w")  # opens stock file (products.txt) file in write mode.
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return
