from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QMessageBox, QComboBox
from PyQt5.QtGui import QFont

from recipes import get_recipes

class RecipeSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Recipe Recommendation System')
        self.layout = QVBoxLayout()
        self.recipes = get_recipes()  # Assuming get_recipes() retrieves recipes
        self.initUI()

    def initUI(self):
        self.title_label = QLabel('Recipe Recommendation System', self)
        self.title_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.layout.addWidget(self.title_label)

        self.intro_label = QLabel(
            'Recipe Recommendation Expert System is an intelligent application that uses artificial intelligence techniques to suggest recipes to users based on your specific needs and preferences. '
            'It considers factors such as allergic status, preferred cuisine type, and meal type being prepared.',
            self
        )
        self.intro_label.setWordWrap(True)
        self.layout.addWidget(self.intro_label)

        self.start_button = QPushButton('START', self)
        self.start_button.clicked.connect(self.start_program)
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)
        self.show()

    def start_program(self):
        self.clear_layout()

        self.allergy_label = QLabel('Select allergens you are allergic to:', self)
        self.layout.addWidget(self.allergy_label)

        self.peanut_allergy = QCheckBox('Peanuts', self)
        self.shellfish_allergy = QCheckBox('Shellfish', self)
        self.soy_allergy = QCheckBox('Soy', self)
        self.egg_allergy = QCheckBox('Eggs', self)
        self.layout.addWidget(self.peanut_allergy)
        self.layout.addWidget(self.shellfish_allergy)
        self.layout.addWidget(self.soy_allergy)
        self.layout.addWidget(self.egg_allergy)

        self.none_allergy = QCheckBox('None', self)
        self.layout.addWidget(self.none_allergy)

        self.allergy_button = QPushButton('NEXT', self)
        self.allergy_button.clicked.connect(self.check_allergy)
        self.layout.addWidget(self.allergy_button)

        self.allergy_how_why_button = QPushButton('How/Why', self)
        self.allergy_how_why_button.clicked.connect(self.show_allergy_info)
        self.layout.addWidget(self.allergy_how_why_button)

    def show_allergy_info(self):
        QMessageBox.information(self, "Allergy Information",
                                "How: Asking about allergies filters out recipes with allergens, narrows options, and personalizes recommendations.\n\n"
                                "Why: This ensures user safety, enhances relevance, builds trust, and meets regulatory requirements.")

    def check_allergy(self):
        self.allergies = []
        if self.peanut_allergy.isChecked():
            self.allergies.append('Peanuts')
        if self.shellfish_allergy.isChecked():
            self.allergies.append('Shellfish')
        if self.soy_allergy.isChecked():
            self.allergies.append('Soy')
        if self.egg_allergy.isChecked():
            self.allergies.append('Eggs')
        if self.none_allergy.isChecked():
            self.allergies = ['None']

        # Check if no allergies are selected and "None" is not checked
        if not self.allergies and not self.none_allergy.isChecked():
            QMessageBox.warning(self, "No Allergies Selected",
                                "Please select at least one allergy or choose 'None' if you have no allergies.")
            return

        allergy_summary = 'You are allergic to ' + ', '.join(self.allergies) if self.allergies[
                                                                                    0] != 'None' else 'You have no allergies.'
        self.show_summary(allergy_summary)

        self.veggie_label = QLabel('Are you vegetarian or non-vegetarian?', self)
        self.layout.addWidget(self.veggie_label)

        self.veggie_combo = QComboBox(self)
        self.veggie_combo.addItem("Vegetarian")
        self.veggie_combo.addItem("Non-Vegetarian")
        self.layout.addWidget(self.veggie_combo)

        self.veggie_button = QPushButton('NEXT', self)
        self.veggie_button.clicked.connect(self.select_veggie)
        self.layout.addWidget(self.veggie_button)

        self.veggie_how_why_button = QPushButton('How/Why', self)
        self.veggie_how_why_button.clicked.connect(self.show_veggie_info)
        self.layout.addWidget(self.veggie_how_why_button)

        self.setLayout(self.layout)

    def show_veggie_info(self):
        QMessageBox.information(self, "Vegetarian Information",
                                "Knowing whether you are vegetarian helps the system tailor the recipes to your dietary choices.")

    def select_veggie(self):
        self.veggie_choice = self.veggie_combo.currentText()

        veggie_summary = f'You selected {self.veggie_choice}.'
        self.show_summary(veggie_summary)

        if self.veggie_choice == "Vegetarian":
            self.eggs_label = QLabel('Do you consume eggs?', self)
            self.layout.addWidget(self.eggs_label)

            self.eggs_combo = QComboBox(self)
            self.eggs_combo.addItem("Yes")
            self.eggs_combo.addItem("No")
            self.layout.addWidget(self.eggs_combo)

            self.eggs_button = QPushButton('NEXT', self)
            self.eggs_button.clicked.connect(self.select_eggs)
            self.layout.addWidget(self.eggs_button)

            self.eggs_how_why_button = QPushButton('How/Why', self)
            self.eggs_how_why_button.clicked.connect(self.show_eggs_info)
            self.layout.addWidget(self.eggs_how_why_button)
        else:
            self.select_preferences()

        self.setLayout(self.layout)

    def show_eggs_info(self):
        QMessageBox.information(self, "Egg Consumption Information",
                                "Knowing whether you consume eggs helps the system classify you as a lacto-ovo vegetarian (consume eggs) or a lacto vegetarian (do not consume eggs).")

    def select_eggs(self):
        self.eggs_choice = self.eggs_combo.currentText()

        if 'Eggs' in self.allergies and self.eggs_choice == 'Yes':
            QMessageBox.warning(self, "Inconsistent Selection",
                                "You cannot be allergic to eggs and also consume them. Please revise your selection.")
            return

        eggs_summary = f'You selected to {"consume" if self.eggs_choice == "Yes" else "not consume"} eggs.'
        self.show_summary(eggs_summary)

        self.select_preferences()

        self.setLayout(self.layout)

    def select_preferences(self):
        self.clear_layout()

        self.pref_cuisine_label = QLabel('Select your preferred cuisine type:', self)
        self.layout.addWidget(self.pref_cuisine_label)

        self.cuisine_combo = QComboBox(self)
        self.cuisine_combo.addItem("Western")
        self.cuisine_combo.addItem("Asian")
        # Add more cuisine types as needed
        self.layout.addWidget(self.cuisine_combo)

        self.pref_meal_label = QLabel('Select your preferred meal type:', self)
        self.layout.addWidget(self.pref_meal_label)

        self.meal_combo = QComboBox(self)
        self.meal_combo.addItem("Breakfast")
        self.meal_combo.addItem("Lunch")
        self.meal_combo.addItem("Dinner")
        self.meal_combo.addItem("Dessert")
        # Add more meal types as needed
        self.layout.addWidget(self.meal_combo)

        self.pref_button = QPushButton('SHOW RECIPES', self)
        self.pref_button.clicked.connect(self.show_recipes)
        self.layout.addWidget(self.pref_button)

        self.pref_how_why_button = QPushButton('How/Why', self)
        self.pref_how_why_button.clicked.connect(self.show_pref_info)
        self.layout.addWidget(self.pref_how_why_button)

        self.setLayout(self.layout)

    def show_pref_info(self):
        QMessageBox.information(self, "Preference Information",
                                "Knowing your preferred cuisine and meal type helps the system recommend recipes that you'll enjoy.")

    def show_recipes(self):
        self.cuisine_choice = self.cuisine_combo.currentText()
        self.meal_choice = self.meal_combo.currentText()

        preference_summary = f'You selected {self.cuisine_choice} cuisine and {self.meal_choice} meal.'
        self.show_summary(preference_summary)

        self.clear_layout()

        self.recipe_label = QLabel('Recommended Recipes:', self)
        self.layout.addWidget(self.recipe_label)

        self.recipe_list = QComboBox(self)
        filtered_recipes = self.filter_recipes()

        if filtered_recipes:
            for recipe in filtered_recipes:
                self.recipe_list.addItem(recipe["name"])
            self.layout.addWidget(self.recipe_list)

            self.select_recipe_button = QPushButton('SELECT RECIPE', self)
            self.select_recipe_button.clicked.connect(self.show_recipe_details)
            self.layout.addWidget(self.select_recipe_button)

            self.recipe_how_why_button = QPushButton('How/Why', self)  # Fix the closing double quote here
            self.recipe_how_why_button.clicked.connect(self.show_recipe_info)
            self.layout.addWidget(self.recipe_how_why_button)
        else:
            no_recipe_label = QLabel("No recipes available. Please click 'RESTART' to start over.", self)
            self.layout.addWidget(no_recipe_label)

            self.restart_button = QPushButton('RESTART', self)
            self.restart_button.clicked.connect(self.restart_program)
            self.layout.addWidget(self.restart_button)

        self.setLayout(self.layout)

    def show_recipe_info(self):
        # Constructing the combined information message
        allergies_info = ", ".join(self.allergies) if self.allergies[0] != 'None' else "None"
        veggie_info = self.veggie_choice
        if self.veggie_choice == "Vegetarian":
            veggie_info += " (Lacto-Ovo)" if self.eggs_choice == "Yes" else " (Lacto)"
        cuisine_info = self.cuisine_choice
        meal_info = self.meal_choice

        how_info = (
            f"Recommended recipes are based on:\n"
            f" - Allergies: {allergies_info}\n"
            f" - Vegetarian status: {veggie_info}\n"
            f" - Preferences: {cuisine_info} cuisine, {meal_info} meal\n\n"
            f"The recipes recommended are based on your preferences and dietary restrictions."
        )

        # Display the combined information in a single message box
        QMessageBox.information(self, "Recipe Recommendation Details", how_info)

    def filter_recipes(self):
        filtered_recipes = []
        for recipe in self.recipes:
            if self.cuisine_choice != recipe["cuisine"]:
                continue
            if self.meal_choice != recipe["meal"]:
                continue
            if self.allergies[0] != 'None' and any(
                    allergen in self.allergies for allergen in recipe["allergens"]):
                continue
            if self.veggie_choice == "Vegetarian" and "Meat" in recipe["allergens"]:
                continue
            if self.veggie_choice == "Vegetarian" and self.eggs_choice == "No" and "Eggs" in recipe[
                "allergens"]:
                continue
            filtered_recipes.append(recipe)
        return filtered_recipes

    def show_recipe_details(self):
        selected_recipe = self.recipe_list.currentText()
        if not selected_recipe:  # Check if no recipe is selected
            QMessageBox.warning(self, "No Recipe Selected", "Please select a recipe.")
        else:
            recipe_details = next((recipe for recipe in self.recipes if recipe["name"] == selected_recipe),
                                  None)
            if recipe_details:
                # Determine vegetarian type based on allergens
                if "Meat" in recipe_details['allergens']:
                    veg_type = "Non-Vegetarian"
                elif "Eggs" in recipe_details['allergens']:
                    veg_type = "Lacto-Ovo-Vegetarian"
                else:
                    veg_type = "Lacto-Vegetarian"

                details_msg = (
                        f"Recipe: {recipe_details['name']}\n"
                        f"Cuisine: {recipe_details['cuisine']}\n"
                        f"Meal: {recipe_details['meal']}\n"
                        f"Allergens: {', '.join(recipe_details['allergens'])}\n"
                        f"Vegetarian Type: {veg_type}\n\n"
                        f"Ingredients:\n- {', '.join(recipe_details['ingredients'])}\n\n"
                        f"Steps:\n" + "\n".join(
                    f"{i + 1}. {step}" for i, step in enumerate(recipe_details['steps']))
                )
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Recipe Details")
                msg_box.setText(details_msg)
                msg_box.setStandardButtons(QMessageBox.NoButton)
                back_button = msg_box.addButton("Back", QMessageBox.AcceptRole)
                restart_button = msg_box.addButton("Restart", QMessageBox.AcceptRole)  # Add restart button
                msg_box.exec_()

                if msg_box.clickedButton() == restart_button:
                    self.start_program()  # Restart the program on button click
            else:
                QMessageBox.warning(self, "Recipe Not Found", "Selected recipe details not found.")

            self.setLayout(self.layout)

    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def show_summary(self, summary):
        summary_label = QLabel(summary, self)
        summary_label.setWordWrap(True)
        self.layout.addWidget(summary_label)

        self.setLayout(self.layout)

    def restart_program(self):
        self.clear_layout()
        self.initUI()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = RecipeSystem()
    sys.exit(app.exec_())
