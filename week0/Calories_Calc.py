class CalorieCalculator:
    def __init__(self):
        self.exercise_data = {
            'running': 11.4,  # calories burned per minute per kg
            'cycling': 8.5,
            'swimming': 7.0,
            'walking': 3.8,
            'jumping_jacks': 8.0
        }

    def get_user_input(self):
        self.weight = float(input("Enter your weight in kg: "))
        self.exercise_type = input(
            "Enter the type of exercise (running, cycling, swimming, walking, jumping_jacks): ").lower()
        self.duration = float(input("Enter the duration of exercise in minutes: "))

    def calculate_calories_burned(self):
        if self.exercise_type not in self.exercise_data:
            print("Exercise type not recognized. Please enter a valid exercise type.")
            return 0.0

        calories_per_minute = self.exercise_data[self.exercise_type]
        total_calories_burned = calories_per_minute * self.weight * self.duration
        return total_calories_burned

    def display_result(self, total_calories_burned):
        print(
            f"Total calories burned during {self.duration} minutes of {self.exercise_type}: {total_calories_burned:.2f} calories")


if __name__ == "__main__":
    calculator = CalorieCalculator()
    calculator.get_user_input()
    total_calories_burned = calculator.calculate_calories_burned()
    if total_calories_burned > 0:
        calculator.display_result(total_calories_burned)
