import uncertainpy as un

from brunel_network_class import BrunelNetwork
from brunel_network_function import brunel_network

parameterlist = [["J_E", 4, None],
                 ["g", 4, None]]

parameters = un.Parameters(parameterlist)
parameters.set_all_distributions(un.Distribution(0.1).uniform)

# model = BrunelNetwork()
# model = un.Model(brunel_network,
#                  adaptive=False)
model = brunel_network
features = un.NetworkFeatures(features_to_run="all")

uncertainty = un.UncertaintyEstimation(model,
                                       base_model=un.NestModel,
                                       parameters=parameters,
                                       features=features,
                                       CPUs=1)


uncertainty.uncertainty_quantification(plot_condensed=False,
                                       plot_simulator_results=True)
