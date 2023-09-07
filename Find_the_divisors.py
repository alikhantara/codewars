def print_factors(x):
   fin_list = []
   for i in range(1, x + 1):
        if x % i == 0:
                fin_list.append(i)
                #return(fin_list)
                print(fin_list)

num = 27

print_factors(num)