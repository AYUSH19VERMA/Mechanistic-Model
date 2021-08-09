## Getting Started
When a mathematical model is developed to study disease pathogenesis like fungal infection, the structure of the model is defined based on its biological/clinical literature, which helps in understanding and then conducting the model parameter fitting. For parameter fitting, some recently discovered ready to use a variety of methods are already available. New methods are also being developed continuously in this field. Some methods fit better than others, depending on the model structure and the data availability. 

_ _ _

### More Project Details 
#### Objective:
1. Translating the fungal infection model into the Systems Biology Markup Language (SBML), using software such as yaml2smbl in Python.
2. Conducting parameter optimisation of the model with the currently available data using previously developed parameter optimisation tools, such as pyPESTO in Python.
3.	Developing a reproducible parameter optimisation pipeline that will be applied to the model to compare the performance of optimisation algorithms.

The aim of this project is to compare the performance of different parameter optimisation methods that are available in the systems biology community and develop a computational pipeline that can be used in future modelling work. We are using a mathematical model of fungal infection and the data collected to benchmark different optimisation methods, such as differential evolution, gradient-based methods (e.g. L-BFGS-B and Powell), non-gradient based methods (e.g. Dlib and Pyswarm), and scipy optimizer methods, using pyPESTO in python.

#### Problem statement:
1. Installation of Amici is difficult; it showed errors while installing and importing.
2. PyPESTO Implementation to the model
#### Solution:
All the above problem can be solved by using a software called PyCharm, which is an integrated development environment used in computer programming. This software supports easy installation of packages like amici and implementing pypesto to the model due to its capacity to contain pre installed dependencies for various packages.

---

#### All the files and their functions are described below


