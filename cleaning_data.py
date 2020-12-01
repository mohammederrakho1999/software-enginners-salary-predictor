# -*- coding: utf-8 -*-
"""
@author: errakho mohammed
"""
import pandas as pd
import numpy as np

from DataCleaningfunc import *


newColumn = Parse_Salary1(df, "Salary Estimate", "Per Hour")

salary_net = Parse_Salary2("Salary Estimate")

newColumn1,newColumn2 = Parse_Salary3(salary_net, "min_salary", "max_salary")

Parse_Javascript("Job Description","javascript")
Parse_Html("Job Description","html")

Parse_Css("Job Description", "css")

Parse_React("Job Description", "react")

Parse_Angular("Job Description", "angular")

Parse_Git("Job Description", "git")

Parse_node("Job Description","node")

Parse_Php("Job Description", "php")

Parse_Mysql("Job Description", "mysql")

Parse_J2ee("Job Description", "j2ee")

Parse_Net("Job Description","net")

Parse_Company("Company Name","new")

Parse_Remote_Jobs("Location","Remote")

Parse_Location("Location", "State")

Parse_year("Founded", "age")

df.to_csv("software_enginners_data_cleaned.csv", index = False)