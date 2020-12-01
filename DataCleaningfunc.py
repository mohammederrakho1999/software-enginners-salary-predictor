# -*- coding: utf-8 -*-

"""
@author: errakho mohammed
"""

import numpy as np # linear algebra
import pandas as pd # data processing
import glob
import os

#extension ='csv'
#all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
all_filenames = glob.glob(os.path.join("../input/software", "*.csv"))
df = pd.concat([pd.read_csv(f) for f in all_filenames], ignore_index = True)


print(df["Salary Estimate"].value_counts())
print("*"*100)
print(df["Salary Estimate"].isnull().sum())
print(df.info())

# parsing the salary estimate colomn
def Parse_Salary1(df, column, newColumn):
    for val in df[column].values:
        df[newColumn] = df[column].apply(lambda x: 1 if "Per Hour" in str(x) else 0)
    return newColumn


df = df[df["Salary Estimate"].notnull()]

def Parse_Salary2(column):
    for x in df[column]:
        salary = df[column].apply(lambda x: x.split("(")[0])
        salary_net = salary.apply(lambda x: x.replace("Per Hour","").replace("$","").replace("K",""))
    return salary_net

salary_net = Parse_Salary2("Salary Estimate")

def Parse_Salary3(salary_net,newColumn1, newColumn2):
    df[newColumn1] = salary_net.apply(lambda x: int(x.split("-")[0]))
    df[newColumn2] = salary_net.apply(lambda x: int(x.split("-")[1]))
    return newColumn1, newColumn2


df["avr_salary"] = (df["max_salary"] + df["min_salary"]) / 2

def Parse_Javascript(column, newColumn):
    df[newColumn] = df[column].apply(lambda x: 1 if "javascript" in x.lower() else 0)
    return newColumn

    
def Parse_Html(column, newColumn):
    df[newColumn] = df[column].apply(lambda x: 1 if "html" in x.lower() else 0)
    return newColumn


def Parse_Css(column, newColumn):
    df[newColumn] = df[column].apply(lambda x: 1 if "css" in x.lower() else 0)
    return newColumn


def Parse_React(column, newColumn):
    df[newColumn] = df[column].apply(lambda x: 1 if ("react" or "react.js") in x.lower() else 0)
    return newColumn


def Parse_Angular(column, newColumn):
    df[newColumn] = df[column].apply(lambda x: 1 if "angular" in x.lower() else 0 )
    return newColumn


def Parse_Git(column, newColumn):
    df[newColumn] = df[column].apply(lambda x: 1 if "git" in x.lower() else 0)
    return newColumn


def Parse_node(column, newColumn):
    df[newColumn] = df[column].apply(lambda x: 1 if ("node" or "node.js") in x.lower() else 0)
    return newColumn


def Parse_Php(column, newColumn):
    df[newColumn] = df[column].apply(lambda x: 1 if "php" in x.lower() else 0)
    return newColumn


def Parse_Mysql(column, newColumn):
    df[newColumn] = df[column].apply(lambda x: 1 if "java" in x.lower() else 0)
    return newColumn


def Parse_J2ee(column, newColumn):
    df[newColumn] = df[column].apply(lambda x: 1 if "j2ee" in x.lower() else 0)
    return newColumn


def Parse_Net(column,newColumn):
    df[newColumn] = df[column].apply(lambda x: 1 if (".net" or "net") in x.lower() else 0)
    return newColumn


def Parse_Company(column, newColumn):
    df[newColumn] = df[column].apply(lambda x: x[:-4])
    return newColumn


def Parse_Remote_Jobs(column, newColumn):
    df[newColumn] = df[column].apply(lambda x: 1 if x.lower() == "remote" else 0)
    return newColumn


def Parse_Location(column, newColumn):
    for x in df[column].values:
        df[newColumn] = df[column].apply(lambda x: x[-2:])
    return newColumn


def Parse_Year(column, newColumn):
    for val in df[column].values:
        df[newColumn] = df[column].apply(lambda x: 2020 - x)
    return newColumn
