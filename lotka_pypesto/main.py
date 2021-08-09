# The file implemets PyPESTO with the Lotka Volterra Model. A detailed .yml extension(for PEtab file) is used as input and outputs the optimized parameters value 
# for the most optimized optimizer along with some matplotlib plots. Following is the step by step information of what has been implemented in the file.
# 1. import necessary packages
# 2. import .yml file extension and measurement.tsv(data file) to generate PEtab file
# 3. import PEtab problem, define optimizer and run. Output is saved in result variable
# 4. visualize the parameters value by the absimilarly, ove optimizer, printing the parameters value
# 5. similarly, the process is followed(3 and 4) for other optimizers like differentialEvolution, scipy, dlib, pyswarm
# 6. time analysis of different optimizers for each run
# 7. parameter profiling to check the optimizer performance

import yaml2sbml
import matplotlib.pyplot as plt
import os
import numpy as np
import pypesto.petab
import pypesto.optimize as optimize
import pypesto.visualize as visualize
import pypesto

yaml_file_petab = 'Lotka_Volterra_PEtab.yml'
PEtab_dir = './Lotka_Volterra_PEtab/'
PEtab_yaml_name = 'problem.yml'
measurement_table_name = 'measurement_table.tsv'
model_name = 'Lotka_Volterra_with_observables'

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
                           n_starts=10)


visualize.parameters(result)
'#plt.show()'
'#print(result.optimize_result.list[0])'
"#print(result.optimize_result.get_for_key('fval'))"

optimizer_scipy_lbfgsb = optimize.ScipyOptimizer(method='L-BFGS-B')
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

optimizer_results = [result_lbfgsb, result_powell]#, result_dlib, result_pyswarm]
optimizer_names = ['Scipy: L-BFGS-B', 'Scipy: Powell']#, 'Dlib', 'pyswarm']

pypesto.visualize.waterfall(optimizer_results, legends=optimizer_names)
#plt.show()

print('Average Run time per start:')
print('-------------------')

for optimizer_name, optimizer_result in zip(optimizer_names, optimizer_results):
    t = np.sum(optimizer_result.optimize_result.get_for_key('time'))/n_starts
    print(f'{optimizer_name}: {t:f} s')

import pypesto.profile as profile

result = profile.parameter_profile(problem=problem,
                                   result=result,
                                   optimizer=optimizer_scipy_lbfgsb)

# adapt x_labels..
x_labels = [f'Log10({name})' for name in problem.x_names]

visualize.profiles(result, x_labels = x_labels, show_bounds=True)
ax = pypesto.visualize.profile_cis(result, confidence_level=0.95, show_bounds=True)

ax.set_xlabel('Log10(Parameter value)')
#plt.show()

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
