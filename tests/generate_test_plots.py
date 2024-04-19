import os
import numpy as np

# import matplotlib
# matplotlib.use('Agg')

import matplotlib.pyplot as plt

from uncertainpy.plotting import PlotUncertainty
from uncertainpy.plotting.prettyplot import prettyPlot
from uncertainpy.features.spikes import Spikes


folder = os.path.dirname(os.path.realpath(__file__))
test_data_dir = os.path.join(folder, "data")
output_test_dir = os.path.join(folder, "figures")


def generate_plot_uncertainty():
    data_file = "TestingModel1d.h5"

    plot = PlotUncertainty(folder=output_test_dir, logger_level="error")

    plot.load(os.path.join(test_data_dir, data_file))

    plot.plot_all_sensitivities()


def generate_plots_plot_uncertainty_no_sensitivity():
    data_file = "TestingModel1d.h5"

    plot = PlotUncertainty(folder=output_test_dir, logger_level="error")

    plot.load(os.path.join(test_data_dir, data_file))

    plot.plot_all(sensitivity=None)


def generate_plots_plot_uncertainty_sobol_total():
    data_file = "TestingModel1d.h5"

    plot = PlotUncertainty(folder=output_test_dir, logger_level="error")

    plot.load(os.path.join(test_data_dir, data_file))

    plot.plot_all(sensitivity="sobol_total")


def generate_plots_plot_uncertainty_single():
    data_file = "TestingModel1d_single-parameter-a.h5"

    plot = PlotUncertainty(
        folder=os.path.join(output_test_dir, "TestingModel1d_single-parameter-a"),
        logger_level="error",
    )

    plot.load(os.path.join(test_data_dir, data_file))

    plot.plot_all()

    data_file = "TestingModel1d_single-parameter-b.h5"

    plot = PlotUncertainty(
        folder=os.path.join(output_test_dir, "TestingModel1d_single-parameter-b"),
        logger_level="error",
    )

    plot.load(os.path.join(test_data_dir, data_file))

    plot.plot_all()


def generate_simulator_plot_0d():
    data_file = "TestingModel0d.h5"

    plot = PlotUncertainty(folder=output_test_dir, logger_level="error")

    plot.load(os.path.join(test_data_dir, data_file))

    plot.evaluations()


def generate_simulator_plot_1d():
    data_file = "TestingModel1d.h5"

    plot = PlotUncertainty(folder=output_test_dir, logger_level="error")

    plot.load(os.path.join(test_data_dir, data_file))

    plot.evaluations()


def generate_simulator_plot_2d():
    data_file = "TestingModel2d.h5"

    plot = PlotUncertainty(folder=output_test_dir, logger_level="error")

    plot.load(os.path.join(test_data_dir, data_file))

    plot.evaluations()


def generate_spike_plot():
    time = np.arange(0, 10)
    values = np.arange(0, 10) + 10

    prettyPlot(time, values, title="Spike", xlabel="time", ylabel="voltage")
    plt.xlim([min(time), max(time)])

    plt.savefig(os.path.join(output_test_dir, "spike.png"))
    plt.close()


def generate_spikes_plot():
    values = np.load(os.path.join(test_data_dir, "U_test.npy"))
    time = np.load(os.path.join(test_data_dir, "t_test.npy"))

    spikes = Spikes(time, values, xlabel="xlabel", ylabel="ylabel")

    spikes.plot_spikes(os.path.join(output_test_dir, "spikes.png"))

    spikes = Spikes(time, values, xlabel="xlabel", ylabel="ylabel")
    spikes.plot_voltage(os.path.join(output_test_dir, "U_test.png"))

    spikes = Spikes(
        time, values, xlabel="xlabel", ylabel="ylabel", extended_spikes=True
    )

    spikes.plot_spikes(os.path.join(output_test_dir, "spikes_extended.png"))

    values = np.load(os.path.join(test_data_dir, "V_spike.npy"))
    time = np.load(os.path.join(test_data_dir, "t_spike.npy"))

    spikes = Spikes(time, values, xlabel="xlabel", ylabel="ylabel")
    spikes.plot_voltage(os.path.join(output_test_dir, "V_spike.png"))

    values = np.load(os.path.join(test_data_dir, "V_noise.npy"))
    time = np.load(os.path.join(test_data_dir, "t_noise.npy"))

    spikes = Spikes(time, values, xlabel="xlabel", ylabel="ylabel")
    spikes.plot_voltage(os.path.join(output_test_dir, "V_noise.png"))


if __name__ == "__main__":
    generate_plot_uncertainty()
    # generate_simulator_plot()
    generate_simulator_plot_0d()
    generate_simulator_plot_1d()
    generate_simulator_plot_2d()
    generate_spike_plot()
    generate_spikes_plot()
    generate_plots_plot_uncertainty_single()
    generate_plots_plot_uncertainty_no_sensitivity()
    # generate_plots_plot_uncertainty_sobol_total()
