# Monty Hall Monte Carlo Simulation

Choose one of three doors. The host knows where the car is, always opens a different door hiding a goat, and offers you the remaining unopened door. Staying wins when your first choice was the car (about one third of rounds). Switching wins when your first choice was a goat (about two thirds).

## Browser visualizer

Open [index.html](index.html) in a modern browser. No installation or server is required.

- **Play one round:** Choose a door, watch the host reveal a goat, then stay or switch.
- **Run the experiment:** Run from 1 to 100 million trials. Progress, win counts, and a convergence chart update as the simulation runs. You can stop a run at any time.
- **Presets:** Choose 1,000, 1 million, 10 million, or 100 million trials.

The large simulation runs in a Web Worker to keep the page responsive. Each trial randomly places the car and chooses a first door. Because the host always reveals an unchosen goat, staying wins exactly when that first choice was the car; switching wins in every other round. The worker counts that equivalent outcome directly. Results differ between runs.

## Python command line

Use Python 3.10 or later:

```sh
python montyhall.py
python montyhall.py --trials 10000000
python montyhall.py --trials 100000 --seed 42
```

The default is 1 million trials. `--seed` makes results reproducible, and `--trials` accepts any positive integer. The Python simulation explicitly models the host opening an eligible goat door, then checks the remaining choice.

Further reading: [Monty Hall problem on MathWorld](https://mathworld.wolfram.com/MontyHallProblem.html).
