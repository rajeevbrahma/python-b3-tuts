list_1 = [1,2,[3,4,5],{6,7,8},(9,10,11),{'a':12,'b':13},'hello']

for list_element in list_1:
    # print (list_element)
    # print (type(list_element))
    
    # if type(list_element) != int:
    #     for inner_list_element in list_element:
    #         print (inner_list_element)

    if type(list_element) == int:
        print (list_element)

    elif type(list_element) == dict:
        for inner_list_element in list_element:
            print (inner_list_element,"-",list_element[inner_list_element])

    else:
        for inner_list_element in list_element:
            print (inner_list_element)
