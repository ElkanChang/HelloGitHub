#!/usr/bin/env python3

# real_tax_money = salary - insurance - 3500
# real_tax = real_tax_money * tax_rate - some_num

import sys

def real_salary(**kw):
    final_salary_dict = {}
    for p in kw.keys():
        try:
            int(p)
        except ValueError:
            print('Parameter Error')
            sys.exit()
        p_salary = kw[p]
        real_tax_money = 0.835 * p_salary - 3500
        if real_tax_money <=0:
            tax_rate = 0
            some_num = 0
        elif real_tax_money <= 1500:
            tax_rate = 0.03
            some_num = 0
        elif real_tax_money > 1500 and real_tax_money <= 4500:
            tax_rate = 0.1
            some_num = 105
        elif real_tax_money > 4500 and real_tax_money <= 9000:
            tax_rate = 0.2
            some_num = 555
        elif real_tax_money > 9000 and real_tax_money <= 35000:
            tax_rate = 0.25
            some_num = 1005
        elif real_tax_money > 35000 and real_tax_money <= 55000:
            tax_rate = 0.3
            some_num = 2755
        elif real_tax_money > 55000 and real_tax_money <= 80000:
            tax_rate = 0.35
            some_num = 5505
        elif real_tax_money > 80000:
            tax_rate = 0.45
            some_num = 13505
        else:
            print("I don't know what you want to do")

        real_tax = real_tax_money * tax_rate - some_num
        final_salary = 0.835 * p_salary - real_tax
        final_salary_dict[p] = format(final_salary,'.2f')

    for a in final_salary_dict.keys():
        b = final_salary_dict[a]
        print("{0}:{1}".format(a,b))

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Parameter Error")
        sys.exit()
    else:
        salary_info = sys.argv[1:]

        salary_dict = {}

        try:
            for ind in salary_info:
                ind = ind.split(":")
                num = ind[0]
                salary = int(ind[1])
                salary_dict[num] = salary
        except ValueError:
            print ("Parameter Error")
            sys.exit()

#    print(salary_dict)
#    print(type(salary_dict))
    real_salary(**salary_dict)

