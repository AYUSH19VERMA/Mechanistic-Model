# Getting Started
##● Creating a biochemical reaction network
##● Set of ODEs
##● Assign values to each object in the model
##● Use simulator to solve equations
##More Project Details 
Problem Statement:
###1.	Translating the fungal infection model into the Systems Biology Markup Language (SBML), using software such as yaml2smbl in Python.
###2.	Conducting parameter optimisation of the model with the currently available data using previously developed parameter optimisation tools, such as pyPESTO in Python.
###3.	Developing a reproducible parameter optimisation pipeline that will be applied to the model to compare the performance of optimisation algorithms.
# ODE_Simulations_final.py
ODE file .py file-
The file contains code to simulate ODEs mentioned in in silico fungal persistence paper.
# Copy_of_ODE_Simulations_final.ipynb
ODE simulations file of .ipynb
The notebook contains the code and plots of the in silico fungal persistence paper.
# validate.py
File to check/validate if .yml file is correctly formatted.
# convert_yaml_sbml.py
File to convert yaml(.yml) to sbml(.xml).
# SBML_file.xml
This is the generated sbml file(.xml extension) from the yaml(.yml) file using yaml2sbml.
# Ayush files
All the files required for simulating and validating model.
# Mechanistic_Model_PyPesto
Parameter optimisation of mechanistic model using pypesto

(This is the main folder which is required for the PyPESTO implementation purpose. It contains all the necessary basic files to optimize your model from the start.)
# lotka_pypesto
Parameter optimisation of Lotka Volterra model to implement PyPESTO
# Mechanistic_Model_plots and results.ipynb
Simulated mechanistic model equations and contains plot of model.
# SBML_file.xml
Fungal Infection model into SBML
# amici.ipynb
To implemente Model, solver and trajectory plotting of model in amici.
