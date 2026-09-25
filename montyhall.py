"""Monte Carlo simulation of the three-door Monty Hall problem."""

from __future__ import annotations

import argparse
import random
from dataclasses import dataclass


@dataclass(frozen=True)
class Results:
    trials: int
    stay_wins: int

    @property
    def switch_wins(self) -> int:
        return self.trials - self.stay_wins


def play_trial(rng: random.Random) -> bool:
    """Play one round; return True if the original choice wins.

    The host always reveals a goat behind a different door, then offers the
    remaining unopened door. Consequently, switching wins exactly when the
    first choice was a goat.
    """
    car = rng.randrange(3)
    first_choice = rng.randrange(3)
    goat_doors = [door for door in range(3) if door != first_choice and door != car]
    revealed = rng.choice(goat_doors)
    switched_choice = 3 - first_choice - revealed  # Doors are numbered 0, 1, 2.
    assert switched_choice != revealed
    assert (switched_choice == car) != (first_choice == car)
    return first_choice == car


def simulate(trials: int, seed: int | None = None) -> Results:
    """Run trials with an optional seed for reproducible results."""
    if trials <= 0:
        raise ValueError("trials must be a positive integer")
    rng = random.Random(seed)
    stay_wins = sum(play_trial(rng) for _ in range(trials))
    return Results(trials=trials, stay_wins=stay_wins)


def positive_integer(value: str) -> int:
    """Validate the command-line trial count."""
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a positive integer") from exc
    if number <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-n", "--trials", type=positive_integer, default=1_000_000,
        help="number of trials (default: 1,000,000)",
    )
    parser.add_argument(
        "--seed", type=int, help="optional seed for reproducible results",
    )
    args = parser.parse_args()
    results = simulate(args.trials, args.seed)

    print(f"Trials:      {results.trials:,}")
    print(
        f"Stay wins:   {results.stay_wins:,} "
        f"({results.stay_wins / results.trials:.2%}; expected 33.33%)"
    )
    print(
        f"Switch wins: {results.switch_wins:,} "
        f"({results.switch_wins / results.trials:.2%}; expected 66.67%)"
    )


if __name__ == "__main__":
    main()
