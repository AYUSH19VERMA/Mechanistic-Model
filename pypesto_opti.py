import yaml2sbml
import amici
import amici.plotting
import os
import sys
import importlib
import numpy as np
import petab
import pypesto
import numpy as np
import h5py
import pypesto.petab
import pypesto.optimize as optimize
import pypesto.visualize as visualize
import matplotlib.pyplot as plt

#yaml_file_petab = 'Mechanistic_model_petab.yml'
PEtab_dir = './Mechanistic_Model_PEtab/'
PEtab_yaml_name = 'problem.yml'
measurement_table_name = 'measurement.tsv'
model_name = 'Mechanistic_Model_with_observables'

importer = pypesto.petab.PetabImporter.from_yaml(os.path.join(PEtab_dir, PEtab_yaml_name), model_name=model_name)

problem = importer.create_problem()
#petab.lint.lint_problem(problem)-to check if petab file is valid
optimizer = optimize.ScipyOptimizer()
result = optimize.minimize(problem,optimizer=optimizer,n_starts=10)

visualize.parameters(result)
plt.show()
"""
print(result.optimize_result.list[0])
print(result.optimize_result.get_for_key('fval'))

#optimizer_scipy_lbfgsb = optimize.ScipyOptimizer(method='L-BFGS-B')
optimizer_scipy_powell = optimize.ScipyOptimizer(method='Powell')

optimizer_dlib = optimize.DlibOptimizer()
optimizer_pyswarm = optimize.PyswarmOptimizer()

n_starts = 100

# Due to run time we already use parallelization.
# This will be introduced in more detail later.
engine = pypesto.engine.MultiProcessEngine()
history_options = pypesto.HistoryOptions(trace_record=True)

# Scipy: L-BFGS-B
result_lbfgsb = optimize.minimize(problem=problem,
                                  optimizer=optimizer_scipy_lbfgsb,
                                  engine=engine,
                                  history_options=history_options,
                                  n_starts=n_starts)

# Scipy: Powell
result_powell = optimize.minimize(problem=problem,
                              optimizer=optimizer_scipy_powell,
                              engine=engine,
                              history_options=history_options,
                              n_starts=n_starts)


# Dlib
result_dlib = optimize.minimize(problem=problem,
                                optimizer=optimizer_dlib,
                                engine=engine,
                                history_options=history_options,
                                n_starts=n_starts)


# PySwarm
result_pyswarm = optimize.minimize(problem=problem,
                                   optimizer=optimizer_pyswarm,
                                   engine=engine,
                                   history_options=history_options,
                                   n_starts=n_starts)
"""
