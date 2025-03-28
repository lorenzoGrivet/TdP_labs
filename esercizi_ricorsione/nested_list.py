def count_leafs(input_list):
    if len(input_list)==0:
        return 0
    else:
        counter=0
        for element in input_list:
            if type(element)==list:
                counter+=count_leafs(element)

            else:
                counter+=1
        return counter


if __name__=="__main__":
    count_leafs([1,2,3,[1,2,[4,8,8]],[88,99]])
