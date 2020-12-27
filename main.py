import testing
import graham
import jarvis    
import utils
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path

def plotGenerator(generatorName, attempts, generator, sizes, algorithms):
    results = testing.testGenerator(attempts, generator, sizes, algorithms)
    fileName = generatorName.replace(" ", "_").lower()
    results_path = Path("results") / fileName
    results_path.mkdir(parents=True, exist_ok=True)
    fig = plt.figure()
    for i in range(len(algorithms)):
        times = results[algorithms[i].__name__]
        time_ms = list(map(lambda t: t / 1000000, times.values()))
        numbers = list(times.keys())

        algorithm_title = algorithms[i].__name__.replace("_", " ").title()
        plt.plot(numbers, time_ms, label=algorithm_title)

        number_res_path = results_path / f"{algorithms[i].__name__}.txt"
        with open(number_res_path, "w") as f:
            print("Number of Points | Time ms", file=f)
            for k in range(len(time_ms)):
                print(f"{numbers[k]} | {time_ms[k]}", file=f)
        print(f"Saved Numeric Results of '{algorithm_title}' at: '{number_res_path}'")

    plt.legend()
    plt.ylabel('Time milliseconds')    
    plt.xlabel('Number of Points')
    plt.title(generatorName)
    ax = fig.gca()
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))    
    fileName = generatorName.replace(" ", "_").lower()
    fig_path = results_path / f"{fileName}.png"
    fig.savefig(fig_path, dpi=fig.dpi)
    print(f"Saved Figure at: '{fig_path}'")

def main():
    algorithms = [graham.graham_scan, jarvis.jarvis_march]
    generators = [("Uniform Distribution", utils.generateUniformPoints)]
    sizes = [2**i for i in range(2, 18)]
    attempts = 10

    for name, generator in generators:
        plotGenerator(name, attempts, generator, sizes, algorithms)
    

if __name__ == "__main__":
    main()