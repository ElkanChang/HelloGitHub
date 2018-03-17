#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse

class Config():
    '''Parse configuration'''
    def __init__(self,config_file):
        '''check config file format and store config value'''
        self._config = {}
        with open(config_file) as c_file:
            for line in c_file:
                line = line.split("=")
                config_item = line[0].strip()
                config_value = line[1].strip()
                try:
                    float(config_value)
                    self._config[config_item] = config_value
                except ValueError:
                    print('config file format error.')
                    sys.exit()

    def get_config(self,item):
        '''get specific config value'''
        return self._config[item]

class UserData():
    '''handle user data and calculate final salary
       then write result to output file'''
    def __init__(self,user_data_file):
        '''check file format and store correct content'''
        self.userdata = {}
        with open(user_data_file) as u_file:
            for line in u_file:
                line = line.split(",")
                work_num = line[0].strip()
                salary_before = line[1].strip()
                try:
                    int(salary_before)
                    self.userdata[work_num] = salary_before
                except ValueError:
                    print('User data file format error.')
                    sys.exit()

    def calculator(self):
        '''calculate final salary
           final_salary = salary_before - insurance - tax
           tax = tax_income * tax_rate - deduction
           tax_income = (1 - insurance_rate) * salary_before - 3500'''
        final_salary_dict = {}

        cardinal_max = config_info.get_config("JiShuH")
        cardinal_min = config_info.get_config("JiShuL")
        pension = config_info.get_config("YangLao")
        medical = config_info.get_config("YiLiao")
        unemployment = config_info.get_config("ShiYe")
        injury = config_info.get_config("GongShang")
        maternity = config_info.get_config("ShengYu")
        accumulation = config_info.get_config("GongJiJin")
        common_items = (pension + medical + unemployment +
                        injury + maternity +accumulation)

        for work_num in self.userdata.keys():
            salary_before = self.userdata[work_num]
            if salary_before < cardinal_min:
                insurance = cardinal_min * common_items
            elif salary_before > cardinal_max:
                insurance = cardinal_max * common_items
            else:
                insurance = salary_before * common_items
            tax_income = salary_before - insurance - 3500
            if tax_income <=0:
                tax_rate = 0
                deduction = 0
            elif tax_income <= 1500:
                tax_rate = 0.03
                deduction = 0
            elif 1500 < tax_income <= 4500:
                tax_rate = 0.1
                deduction = 105
            elif 4500 < tax_income <= 9000:
                tax_rate = 0.2
                deduction = 555
            elif 9000 < tax_income <= 35000:
                tax_rate = 0.25
                deduction = 1005
            elif 35000 < tax_income <= 55000:
                tax_rate = 0.3
                deduction = 2755
            elif 55000 < tax_income <= 80000:
                tax_rate = 0.35
                deduction = 5505
            elif tax_income > 80000:
                tax_rate = 0.45
                deduction = 13505
            tax = tax_income * tax_rate - deduction
            final_salary = salary_before - insurance - tax
            insurance_2f = format(insurance,'.2f')
            tax_2f = format(tax,'.2f')
            final_salary_2f = format(final_salary,'.2f')
            final_salary_dict[work_num] = ("{0},{1},{2},{3},{4}".format(
                                          work_num,before_salary,insurance_2f,
                                          tax_2f,final_salary_2f))
        return final_salary_dict

    def dump_to_flie(self,result_file,final_result):
        '''write result in CSV format'''
#        final_result = self.calculator()
        with open(result_file,"w") as r_file:
            for i in final_result.values():
                r_file.write( i + "\n")

def main():
    parser = argparse.ArgumentParser(description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-c','--config',help='config file',dest='cfg')
    parser.add_argument('-d','--data',help='user data file',dest='dat')
    parser.add_argument('-o','--outdir',help='output directory',dest='outd')
    args = parser.parse_args()

    config_info = Config(args.cfg)
    calc = UserData(args.dat)
    calc_result = calc.calculator()
    calc.dump_to_file(args.outd,calc_result)

if __name__ == '__main__':
    if len(sys.argv) != 7:
        print('Parameter Error')
        sys.exit()
    else:
        main()
