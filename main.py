import testing
import graham
import jarvis   
import quickhull 
import distributions

from pathlib import Path
import multiprocessing

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


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
        print(f"Saved Numeric Results of '{algorithm_title}' with Generator '{generatorName}' at: '{number_res_path}'")

    plt.legend()
    plt.ylabel('Time milliseconds')    
    plt.xlabel('Number of Points')
    plt.title(generatorName)
    ax = fig.gca()
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))    
    fileName = generatorName.replace(" ", "_").lower()
    fig_path = results_path / f"{fileName}.png"
    fig.savefig(fig_path, dpi=fig.dpi)
    print(f"Saved Figure of Generator '{generatorName}' at: '{fig_path}'")

def main():
    algorithms = [graham.graham_scan, jarvis.jarvis_march, quickhull.quickhull]
    generators1 = [
        distributions.UniformDistribution,
        distributions.BoxDistribution,
        distributions.RepeatedOrderedDistribution,
        distributions.RepeatedInvertedDistribution,
        distributions.RepeatedShuffledDistribution,
        distributions.LineOrderedDistribution, # Not recommended above 32k due to numerical instability
        distributions.LineInvertedDistribution, # Not recommended above 32k due to numerical instability
        distributions.LineShuffledDistribution, # Not recommended above 32k due to numerical instability
        ]
    sizes1 = [2**i for i in range(2, 15)]

    # These generators require smaller tests
    generators2 = [
        distributions.SquaredOrderedDistribution, # Not recommended above 1000 due to numerical instability
        distributions.SquaredInvertedDistribution, # Not recommended above 1000 due to numerical instability
        distributions.SquaredShuffledDistribution, # Not recommended above 1000 due to numerical instability
        ]
    sizes2 = [2**i for i in range(2, 11)]

    generators3 = [
        distributions.NGonDistribution, # Not recommended above 10000 due to time
        distributions.Log2OrderedDistribution, # Not recommended above 10000 due to time
        distributions.Log2InvertedDistribution, # Not recommended above 10000 due to time
        distributions.Log2ShuffledDistribution, # Not recommended above 10000 due to time
    ]
    sizes3 = [2**i for i in range(2, 14)]

    tests = [
        (sizes1, generators1),
        (sizes2, generators2),
        (sizes3, generators3),
    ]

    attempts = 10

    cpus_to_use = int(multiprocessing.cpu_count() / 2)

    with multiprocessing.Pool(processes=cpus_to_use) as pool:
        tasks = []
        
        for sizes, generators in tests:
            tasks = tasks + [pool.apply_async(plotGenerator, args=(name, attempts, generator, sizes, algorithms)) for name, generator in generators]
        
        for task in tasks:
            task.get()            
    

if __name__ == "__main__":
    main()