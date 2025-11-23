import sys
from collections import Counter
from typing import Optional, Dict

from probability_calculator.get_user_input import GetUserInput
from probability_calculator.output_text import OutputText
from probability_calculator.prob_calculator import Hat, experiment


class ProbabilityCalculator:
    """A class to manage probability experiments using a customizable hat of balls.

    This class allows the user to:
    - Create a hat with colored balls.
    - Show the current hat configuration.
    - Run probability experiments based on expected ball draws.

    Attributes:
        hat (Optional[Hat]): The current hat object used for experiments.
        running (bool): Controls the main loop of the menu.
        user_input (GetUserInput): Utility for validated user inputs.
    """

    def __init__(self) -> None:
        """Initialize the probability calculator."""
        self.hat: Optional["Hat"] = None
        self.running: bool = True
        self.user_input = GetUserInput

    def handle_choice(self) -> None:
        """Process user menu choice and invoke related actions."""
        choice = self.user_input.get_user_choice()
        match choice:
            case "1":
                self.create_hat()
            case "2":
                self.show_current_hat()
            case "3":
                self.run_experiment()
            case "0":
                self.running = False
                OutputText.exit_message()
                sys.exit(0)

    def run(self) -> None:
        """Start the main loop of the probability calculator."""
        OutputText.show_welcome_message()
        while self.running:
            OutputText.show_main_menu()
            self.handle_choice()

    def create_hat(self) -> None:
        """Create a hat by asking the user to input ball colors and quantities."""
        balls: Dict[str, int] = {}

        while True:
            color = input("Enter color of ball (empty for finish): ").strip()
            if color == "":
                break

            if color in balls:
                print(f"{color} already added with {balls[color]} balls.")
                print("Please choose a different color or finish.\n")
                continue

            qty = self.user_input.validate_positive_number(
                f"How many balls for {color}? "
            )
            balls[color] = qty

        if balls:
            self.hat = Hat(**balls)
            print("Hat created successfully.")
        else:
            print("Impossible to create new hat.")

    def show_current_hat(self) -> None:
        """Display the distribution of balls in the current hat."""
        if self.hat is None:
            print("No hat created")
            return

        color_count = Counter(self.hat.contents)
        for color, count in color_count.items():
            print(f"{color}: {count}")

    def run_experiment(self) -> None:
        """Run a probability experiment based on user-defined expectations."""
        if self.hat is None:
            print("No hat created")
            return

        expected_balls = self._expected_balls()
        if not expected_balls:
            print("No balls expected, operation aborted.")
            return

        num_balls_drawn = self._num_balls_drawn()
        if num_balls_drawn is None:
            return

        num_experiments = self._nums_experiments()
        if num_experiments is None:
            return

        probability = experiment(
            hat=self.hat,
            expected_balls=expected_balls,
            num_balls_drawn=num_balls_drawn,
            num_experiments=num_experiments
        )

        self._print_probability(probability)

    def _expected_balls(self) -> Optional[Dict[str, int]]:
        """Ask the user which balls and quantities to expect.

        Returns:
            Optional[Dict[str, int]]: A dictionary mapping ball colors to expected quantities,
            or None if no expectations were provided.
        """
        expected_balls: Dict[str, int] = {}

        print("For the purpose of the experiment, we want to know what color ball and quantity you want to extract")

        while True:
            color = input("What color do you want to extract? (blank to confirm)").strip().lower()
            if color == "":
                break

            try:
                quantity = self.user_input.validate_positive_number(
                    f"Quantity of balls {color}: "
                )
                expected_balls[color] = quantity
                print(f"Added {quantity} of {color} balls to the expected\n")

            except ValueError:
                print("Insert a valid number.")

        if expected_balls:
            return expected_balls

        print("No ball expected specified. Operation aborted.")
        return None

    def _num_balls_drawn(self) -> Optional[int]:
        """Ask the user how many balls should be drawn.

        Returns:
            Optional[int]: Number of balls to draw, or None if invalid.
        """
        num_balls_drawn = self.user_input.validate_positive_number(
            "How many balls should be drawn for each experiment? "
        )

        if self.hat and num_balls_drawn > len(self.hat.contents):
            print("Number of balls drawn exceeds number of balls in the hat.")

        return num_balls_drawn

    def _nums_experiments(self) -> Optional[int]:
        """Ask the user for the number of experiments to perform.

        Returns:
            Optional[int]: Number of experiments.
        """
        while True:
            try:
                num_experiments = int(input("How many experiments want to execute? "))
            except ValueError:
                print("Insert a valid integer.")
                continue

            if num_experiments <= 0:
                print("Number of experiments must be greater than 0.")
                continue

            if num_experiments < 1000:
                print(
                    f"Warning: {num_experiments} experiments may yield inaccurate results. "
                    "At least 1000 are recommended."
                )
                confirm = input("Continue? (y/n) ").lower()
                if confirm not in ("y", "yes"):
                    continue

            if num_experiments > 50000:
                print("Warning: This might require more time.")
                confirm = input("Continue? (y/n) ").lower()
                if confirm not in ("y", "yes"):
                    continue

            print(f"{num_experiments} experiments will be performed.")
            return num_experiments

    def _print_probability(self, probability: float) -> None:
        """Print the resulting probability.

        Args:
            probability (float): The probability computed by the experiment.
        """
        percentage = probability * 100

        print("\n" + "=" * 60)
        print("RESULTS")
        print("=" * 60)
        print(f"Percentage: {percentage:.2f}%")