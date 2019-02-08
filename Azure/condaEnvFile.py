# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 03:44:18 2019

Create Enviroment File for Azure Container Services
https://docs.microsoft.com/en-us/azure/machine-learning/service/tutorial-deploy-models-with-aml#create-environment-file

@author: msdsadmin
"""

from azureml.core.conda_dependencies import CondaDependencies 

myenv = CondaDependencies()
myenv.add_conda_package("scikit-learn")

with open("myenv.yml","w") as f:
    f.write(myenv.serialize_to_string())