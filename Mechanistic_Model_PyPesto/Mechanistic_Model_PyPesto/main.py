# The file implemets PyPESTO with the Mechanistic Model. A detailed .yml extension(for PEtab file) is used as input and outputs the optimized parameters value 
# for the most optimized optimizer along with some matplotlib plots. Following is the step by step information of what has been implemented in the file.
# 1. import necessary packages
# 2. import .yml file extension and measurement.tsv(data file) to generate PEtab file
# 3. import PEtab problem, define optimizer and run. Output is saved in result variable
# 4. visualize the parameters value by the absimilarly, ove optimizer, printing the parameters value
# 5. similarly, the process is followed(3 and 4) for other optimizers like differentialEvolution, scipy, dlib, pyswarm
# 6. time analysis of different optimizers for each run
# 7. parameter profiling to check the optimizer performance


import time
import yaml2sbml
import matplotlib.pyplot as plt
import os
import numpy as np
import pypesto.petab
import pypesto.optimize as optimize
import pypesto.visualize as visualize
import pypesto
import pypesto.profile as profile
import amici
s = time.time()

yaml_file_petab = 'Mechanistic_model_petab.yml'
PEtab_dir = './Mechanistic_Model_PEtab/'
PEtab_yaml_name = 'problem.yml'
measurement_table_name = 'measurement.tsv'
model_name = 'Mechanistic_Model_with_observables'

yaml2sbml.yaml2petab(yaml_file_petab,
                     PEtab_dir,
                     model_name,
                     PEtab_yaml_name,
                     measurement_table_name)


# import PEtab problem
importer = pypesto.petab.PetabImporter.from_yaml(os.path.join(PEtab_dir, PEtab_yaml_name),
                                                 model_name=model_name)
problem = importer.create_problem()

optimizer = optimize.ScipyOptimizer()
result = optimize.minimize(problem,
                           optimizer=optimizer,
                           n_starts=50)


visualize.parameters(result)
plt.show()
print("RESULT FOR SCIPY DEFAULT OPTIMIZER:", result.optimize_result.list[0])
print(result.optimize_result.get_for_key('fval'))

optimizer_scipy_lbfgsb = optimize.ScipyOptimizer(method='L-BFGS-B',options={'maxiter': 10})
optimizer_scipy_powell = optimize.ScipyOptimizer(method='Powell',options={'maxiter': 10})
optimizer_dlib = optimize.DlibOptimizer(options={'maxiter': 10})
optimizer_pyswarm = optimize.PyswarmOptimizer(options={'maxiter': 10})
optimizer_diffEvolution = optimize.ScipyDifferentialEvolutionOptimizer(options={'maxiter': 10})

n_starts = 50

# Due to run time we already use parallelization.
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

result_diffEvolution = optimize.minimize(problem=problem,
                                         optimizer=optimizer_diffEvolution,
                                         engine=engine,
                                         history_options=history_options,
                                         n_starts=n_starts)

optimizer_results = [result, result_lbfgsb, result_powell, result_dlib, result_pyswarm, result_diffEvolution]
optimizer_names = ['Scipy', 'Scipy: L-BFGS-B', 'Scipy: Powell', 'Dlib', 'pyswarm', 'differentialEvolution']

pypesto.visualize.waterfall(optimizer_results, legends=optimizer_names)
plt.show()

print('Average Run time per start:')
print('-------------------')

for optimizer_name, optimizer_result in zip(optimizer_names, optimizer_results):
    t = np.sum(optimizer_result.optimize_result.get_for_key('time'))/n_starts
    print(f'{optimizer_name}: {t:f} s')



result = profile.parameter_profile(problem=problem,
                                   result=result,
                                   optimizer=optimizer)

# adapt x_labels..
x_labels = [f'Log10({name})' for name in problem.x_names]

visualize.profiles(result, x_labels = x_labels, show_bounds=True)
ax = pypesto.visualize.profile_cis(result, confidence_level=0.95, show_bounds=True)

ax.set_xlabel('Log10(Parameter value)')
plt.show()

import pypesto.sample as sample

n_samples = 10000

sampler = sample.AdaptiveMetropolisSampler()

result = sample.sample(problem,
                       n_samples=n_samples,
                       sampler=sampler,
                       result=result)

print(result.sample_result['trace_x'])

sample.geweke_test(result=result)
result.sample_result['burn_in']
sample.effective_sample_size(result=result)
result.sample_result['effective_sample_size']

# scatter plots
ax = visualize.sampling_scatter(result)

# marginals
ax = visualize.sampling_1d_marginals(result)

plt.show()

e = time.time()
print(e-s)
plt.show()
