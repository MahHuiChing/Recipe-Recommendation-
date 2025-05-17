
def get_recipes():
    recipes = [
        {
            "name": "Western Veggie Omelette",
            "cuisine": "Western",
            "meal": "Breakfast",
            "allergens": ["Shellfish"],
            "ingredients": [
                "2 eggs",
                "1/4 cup milk",
                "1/4 cup diced bell peppers",
                "1/4 cup diced onions",
                "1/4 cup diced tomatoes",
                "1/4 cup shredded cheese",
                "Salt and pepper to taste",
                "1 tbsp olive oil"
            ],
            "steps": [
                "In a bowl, whisk together eggs and milk. Season with salt and pepper.",
                "Heat olive oil in a non-stick skillet over medium heat.",
                "Add diced bell peppers, onions, and tomatoes. Sauté until vegetables are tender.",
                "Pour egg mixture over the vegetables in the skillet. Cook until the edges start to set.",
                "Sprinkle shredded cheese evenly over the omelette.",
                "Fold the omelette in half and cook for another minute until cheese melts and eggs are fully cooked.",
                "Serve hot with toast or your favorite breakfast sides."
            ],
            "vegetarian": True,
            "eggs": True
        },
        {"name": "Western Caprese Salad",
        "cuisine": "Western",
        "meal": "Lunch",
        "allergens": ["Shellfish"],
        "ingredients": [
            "2 large tomatoes, sliced",
            "1 ball fresh mozzarella cheese, sliced",
            "1/4 cup fresh basil leaves",
            "2 tbsp extra virgin olive oil",
            "1 tbsp balsamic vinegar",
            "Salt and pepper to taste"
        ],
        "steps": [
            "Arrange tomato and mozzarella slices alternately on a serving platter.",
            "Tuck fresh basil leaves between the slices.",
            "Drizzle olive oil and balsamic vinegar over the salad.",
            "Season with salt and pepper to taste.",
            "Serve immediately as a refreshing and light lunch."
        ],
        "vegetarian": True,
        "eggs": False
    },
    {
        "name": "Western Veggie Wrap",
        "cuisine": "Western",
        "meal": "Lunch",
        "allergens": ["Shellfish"],
        "ingredients": [
            "1 large flour tortilla",
            "1/2 cup hummus",
            "1/4 cup shredded carrots",
            "1/4 cup sliced cucumber",
            "1/4 cup baby spinach leaves",
            "1/4 cup diced tomatoes",
            "Salt and pepper to taste"
        ],
        "steps": [
            "Spread hummus evenly over the tortilla.",
            "Layer shredded carrots, sliced cucumber, spinach leaves, and diced tomatoes on top of the hummus.",
            "Season with salt and pepper.",
            "Roll the tortilla tightly into a wrap.",
            "Slice in half diagonally and serve as a satisfying lunch option."
        ],
        "vegetarian": True,
        "eggs": False
    },
        {
            "name": "Western Veggie Stir-Fry",
            "cuisine": "Western",
            "meal": "Dinner",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 cup broccoli florets",
                "1 cup sliced bell peppers",
                "1 cup sliced mushrooms",
                "1/2 cup sliced carrots",
                "1/4 cup diced onions",
                "2 cloves garlic, minced",
                "1/4 cup soy sauce",
                "1 tbsp sesame oil",
                "Salt and pepper to taste",
                "Cooked rice or noodles for serving"
            ],
            "steps": [
                "Heat sesame oil in a large skillet or wok over medium-high heat.",
                "Add minced garlic and diced onions, sauté until fragrant.",
                "Add broccoli florets, bell peppers, mushrooms, and carrots. Stir-fry until vegetables are tender-crisp.",
                "Drizzle soy sauce over the vegetables, season with salt and pepper to taste, and toss to combine.",
                "Serve hot over cooked rice or noodles."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Western Quinoa Stuffed Bell Peppers",
            "cuisine": "Western",
            "meal": "Dinner",
            "allergens": ["Shellfish"],
            "ingredients": [
                "4 large bell peppers, tops cut off and seeds removed",
                "1 cup cooked quinoa",
                "1 cup black beans, drained and rinsed",
                "1 cup corn kernels",
                "1/2 cup diced tomatoes",
                "1/4 cup chopped fresh cilantro",
                "1 tsp cumin",
                "1/2 tsp chili powder",
                "Salt and pepper to taste",
                "1/2 cup shredded cheese (optional)"
            ],
            "steps": [
                "Preheat oven to 375°F (190°C).",
                "In a large bowl, combine cooked quinoa, black beans, corn kernels, diced tomatoes, cilantro, cumin, and chili powder.",
                "Season with salt and pepper to taste.",
                "Stuff each bell pepper with the quinoa mixture.",
                "If using, sprinkle shredded cheese on top of each stuffed bell pepper.",
                "Place stuffed bell peppers upright in a baking dish. Cover with foil.",
                "Bake for 25-30 minutes or until bell peppers are tender and filling is heated through.",
                "Serve hot as a nutritious and satisfying dinner."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Western Veggie Pizza",
            "cuisine": "Western",
            "meal": "Dinner",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 pre-made pizza dough",
                "1/2 cup marinara sauce",
                "1 cup shredded mozzarella cheese",
                "1/2 cup sliced bell peppers",
                "1/2 cup sliced mushrooms",
                "1/4 cup sliced red onions",
                "1/4 cup sliced black olives",
                "1/4 cup fresh basil leaves",
                "1 tbsp olive oil",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Preheat oven to 425°F (220°C).",
                "Roll out pizza dough on a lightly floured surface to desired thickness.",
                "Transfer dough to a pizza pan or baking sheet.",
                "Spread marinara sauce evenly over the dough, leaving a small border around the edges.",
                "Sprinkle shredded mozzarella cheese over the sauce.",
                "Top with sliced bell peppers, mushrooms, red onions, and black olives.",
                "Drizzle olive oil over the toppings, season with salt and pepper.",
                "Bake in the preheated oven for 12-15 minutes or until crust is golden and cheese is bubbly.",
                "Remove from oven, sprinkle fresh basil leaves on top.",
                "Slice and serve hot as a delicious homemade dinner."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Classic Apple Crisp",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Shellfish"],
            "ingredients": [
                "6 cups sliced apples (about 6 medium)",
                "1/2 cup granulated sugar",
                "1 tsp ground cinnamon",
                "1/2 cup old-fashioned oats",
                "1/2 cup all-purpose flour",
                "1/2 cup packed brown sugar",
                "1/4 cup unsalted butter, softened",
                "Vanilla ice cream or whipped cream (optional, for serving)"
            ],
            "steps": [
                "Preheat oven to 350°F (175°C).",
                "In a large bowl, toss sliced apples with granulated sugar and cinnamon.",
                "Transfer apple mixture to a greased 9x13-inch baking dish.",
                "In a separate bowl, combine oats, flour, brown sugar, and softened butter until crumbly.",
                "Sprinkle oat mixture evenly over the apples in the baking dish.",
                "Bake for 40-45 minutes or until the topping is golden brown and apples are tender.",
                "Remove from oven and let cool slightly.",
                "Serve warm with vanilla ice cream or whipped cream, if desired."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Chocolate Chip Cookies",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 cup unsalted butter, softened",
                "1 cup granulated sugar",
                "1 cup packed brown sugar",
                "2 large eggs",
                "1 tsp vanilla extract",
                "3 cups all-purpose flour",
                "1 tsp baking soda",
                "1/2 tsp salt",
                "2 cups semisweet chocolate chips"
            ],
            "steps": [
                "Preheat oven to 350°F (175°C).",
                "In a large bowl, cream together softened butter, granulated sugar, and brown sugar until smooth.",
                "Beat in eggs, one at a time, then stir in vanilla extract.",
                "Combine flour, baking soda, and salt; gradually stir into the creamed mixture.",
                "Fold in chocolate chips.",
                "Drop by rounded spoonfuls onto ungreased cookie sheets.",
                "Bake for 10-12 minutes or until edges are golden brown.",
                "Remove from oven and let cookies cool on baking sheets for a few minutes before transferring to wire racks to cool completely."
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Lemon Bars",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 cup unsalted butter, softened",
                "1/2 cup powdered sugar",
                "2 cups all-purpose flour",
                "4 large eggs",
                "2 cups granulated sugar",
                "1/3 cup fresh lemon juice",
                "1/4 cup all-purpose flour",
                "1/2 tsp baking powder",
                "Powdered sugar for dusting"
            ],
            "steps": [
                "Preheat oven to 350°F (175°C).",
                "In a mixing bowl, cream together softened butter and powdered sugar.",
                "Gradually add 2 cups flour, mixing until crumbly.",
                "Press mixture into the bottom of an ungreased 9x13-inch baking pan.",
                "Bake crust for 20 minutes in the preheated oven, or until golden.",
                "Meanwhile, whisk together eggs, granulated sugar, lemon juice, 1/4 cup flour, and baking powder until well combined.",
                "Pour lemon mixture over the baked crust.",
                "Return to the oven and bake for an additional 25 minutes, or until the lemon topping is set.",
                "Remove from oven and let cool completely in the pan on a wire rack.",
                "Once cooled, dust with powdered sugar and cut into squares."
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Mango Sticky Rice",
            "cuisine": "Asian",
            "meal": "Dessert",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 cup glutinous rice (sticky rice)",
                "1 cup coconut milk",
                "1/2 cup granulated sugar",
                "1/4 tsp salt",
                "2 ripe mangoes, peeled and sliced",
                "Toasted sesame seeds for garnish (optional)"
            ],
            "steps": [
                "Rinse sticky rice under cold water until the water runs clear.",
                "In a saucepan, combine sticky rice with enough water to cover. Bring to a boil, then reduce heat to low, cover, and simmer for 20 minutes or until rice is tender and water is absorbed.",
                "In another saucepan, combine coconut milk, sugar, and salt. Heat over medium heat until sugar is dissolved.",
                "Pour half of the coconut milk mixture over the cooked sticky rice and stir to combine. Let it sit for 10 minutes to allow the rice to absorb the coconut milk.",
                "To serve, spoon sticky rice onto plates, top with sliced mangoes, and drizzle with the remaining coconut milk mixture.",
                "Garnish with toasted sesame seeds if desired.",
                "Serve warm or at room temperature."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Matcha Green Tea Mochi",
            "cuisine": "Asian",
            "meal": "Dessert",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 cup mochiko (sweet rice flour)",
                "1/4 cup granulated sugar",
                "1 tbsp matcha green tea powder",
                "3/4 cup water",
                "Cornstarch or potato starch for dusting",
                "Red bean paste (anko) for filling (optional)"
            ],
            "steps": [
                "In a microwave-safe bowl, whisk together mochiko, sugar, matcha powder, and water until smooth.",
                "Cover with plastic wrap and microwave on high for 2 minutes. Stir well, then microwave for an additional 1-2 minutes until the mixture is thick and translucent.",
                "Let the mochi mixture cool slightly until it is safe to handle.",
                "Dust a clean surface with cornstarch or potato starch.",
                "Scoop spoonfuls of mochi mixture onto the dusted surface. Flatten each portion into a circle.",
                "Place a small amount of red bean paste (if using) in the center of each circle.",
                "Fold the edges of the mochi over the filling, pinching to seal.",
                "Roll each mochi ball in more cornstarch or potato starch to prevent sticking.",
                "Serve immediately or store in an airtight container."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Thai Coconut Pandan Pancakes (Khanom Buang)",
            "cuisine": "Asian",
            "meal": "Dessert",
            "allergens": ["Shellfish"],
            "ingredients": [
                "For the pancakes:",
                "1 cup rice flour",
                "1/4 cup all-purpose flour",
                "1/4 cup tapioca starch",
                "1/2 cup coconut milk",
                "1/2 cup water",
                "1/4 cup granulated sugar",
                "1/4 tsp salt",
                "Green food coloring (optional)",
                "For the filling:",
                "1 cup shredded coconut, sweetened",
                "1/2 cup granulated sugar",
                "1/4 cup water",
                "1/4 tsp salt",
                "Pandan leaves extract or pandan paste (for coloring and flavor)"
            ],
            "steps": [
                "To make the filling, combine shredded coconut, sugar, water, salt, and pandan extract/paste in a saucepan over medium heat.",
                "Cook, stirring frequently, until the mixture thickens and becomes sticky. Remove from heat and let it cool.",
                "To make the pancakes, whisk together rice flour, all-purpose flour, tapioca starch, coconut milk, water, sugar, and salt in a bowl until smooth.",
                "If desired, add a few drops of green food coloring to the batter for a vibrant color.",
                "Heat a non-stick skillet over medium heat. Pour a small amount of batter into the skillet and swirl to coat the bottom evenly.",
                "Cook until the edges of the pancake start to lift and the bottom is lightly golden. Flip and cook the other side briefly.",
                "Remove from skillet and fold into a cone shape. Spoon the coconut filling into the cone.",
                "Repeat with the remaining batter and filling.",
                "Serve warm as a traditional Thai dessert."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
    "name": "Japanese Dorayaki (Red Bean Pancake)",
    "cuisine": "Asian",
    "meal": "Dessert",
    "allergens": ["Shellfish"],
    "ingredients": [
        "1 cup all-purpose flour",
        "1/2 cup granulated sugar",
        "1/2 tsp baking powder",
        "2 large eggs",
        "1/2 cup milk",
        "1/2 tsp vanilla extract",
        "Red bean paste (anko) for filling",
        "Vegetable oil for cooking"
    ],
    "steps": [
        "In a bowl, whisk together flour, sugar, and baking powder.",
        "In another bowl, whisk eggs, milk, and vanilla extract until smooth.",
        "Gradually add the wet ingredients to the dry ingredients, mixing until just combined.",
        "Heat a non-stick skillet or griddle over medium heat and lightly grease with vegetable oil.",
        "Pour a small amount of batter onto the skillet to form small pancakes (about 3-4 inches in diameter).",
        "Cook until bubbles form on the surface, then flip and cook the other side until golden brown.",
        "Remove pancakes from skillet and let cool slightly.",
        "Spread red bean paste onto one pancake, then sandwich with another pancake.",
        "Repeat with the remaining pancakes and red bean paste.",
        "Serve warm or at room temperature."
    ],
    "vegetarian": True,
    "eggs": True
    },
    {
    "name": "Thai Mango Sticky Rice Pancakes",
    "cuisine": "Asian",
    "meal": "Dessert",
    "allergens": ["Shellfish"],
    "ingredients": [
        "1 cup glutinous rice (sticky rice)",
        "1 cup coconut milk",
        "1/4 cup granulated sugar",
        "1/4 tsp salt",
        "2 ripe mangoes, peeled and thinly sliced",
        "1 cup all-purpose flour",
        "1/4 cup tapioca starch",
        "1/4 cup coconut milk",
        "1/2 cup water",
        "1/4 cup granulated sugar",
        "1/4 tsp salt",
        "Green food coloring (optional)",
        "Toasted sesame seeds for garnish (optional)"
    ],
    "steps": [
        "In a saucepan, combine glutinous rice with enough water to cover. Bring to a boil, then reduce heat to low, cover, and simmer for 20 minutes or until rice is tender and water is absorbed.",
        "In another saucepan, combine coconut milk, sugar, and salt. Heat over medium heat until sugar is dissolved.",
        "Pour half of the coconut milk mixture over the cooked sticky rice and stir to combine. Let it sit for 10 minutes to allow the rice to absorb the coconut milk.",
        "To make the pancakes, whisk together all-purpose flour, tapioca starch, coconut milk, water, sugar, salt, and green food coloring (if using) until smooth.",
        "Heat a non-stick skillet over medium heat. Pour a small amount of batter onto the skillet and swirl to coat the bottom evenly.",
        "Cook until the edges of the pancake start to lift and the bottom is lightly golden. Flip and cook the other side briefly.",
        "Remove from skillet and let cool slightly.",
        "To serve, spoon sticky rice onto each pancake, top with sliced mangoes, and fold into a cone shape.",
        "Garnish with toasted sesame seeds if desired.",
        "Serve warm or at room temperature."
    ],
    "vegetarian": True,
    "eggs": False
    },
        {
            "name": "Vegetarian Pad Thai",
            "cuisine": "Asian",
            "meal": "Dinner",
            "allergens": ["Shellfish"],
            "ingredients": [
                "8 oz rice noodles",
                "2 tbsp vegetable oil",
                "1 cup tofu, cubed",
                "1/2 cup sliced bell peppers",
                "1/2 cup bean sprouts",
                "1/4 cup chopped peanuts",
                "2 cloves garlic, minced",
                "2 eggs, beaten (optional)",
                "For the sauce:",
                "3 tbsp soy sauce",
                "2 tbsp tamarind paste",
                "2 tbsp brown sugar",
                "1 tbsp rice vinegar",
                "1/4 tsp red pepper flakes (optional)"
            ],
            "steps": [
                "Cook rice noodles according to package instructions. Drain and set aside.",
                "In a small bowl, whisk together soy sauce, tamarind paste, brown sugar, rice vinegar, and red pepper flakes.",
                "Heat vegetable oil in a large skillet or wok over medium-high heat.",
                "Add tofu and cook until golden brown. Add minced garlic and cook until fragrant.",
                "If using eggs, push tofu to one side of the skillet and pour beaten eggs into the other side. Scramble until cooked through.",
                "Add bell peppers and bean sprouts to the skillet. Stir-fry for 2-3 minutes.",
                "Add cooked rice noodles and sauce mixture to the skillet. Toss everything together until well combined and heated through.",
                "Serve hot, garnished with chopped peanuts.",
                "Enjoy your Vegetarian Pad Thai!"
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Tofu and Vegetable Stir-Fry",
            "cuisine": "Asian",
            "meal": "Dinner",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 block tofu, drained and cubed",
                "2 cups mixed vegetables (bell peppers, broccoli, carrots, snow peas)",
                "2 tbsp soy sauce",
                "1 tbsp hoisin sauce",
                "1 tbsp sesame oil",
                "2 cloves garlic, minced",
                "1 tbsp ginger, minced",
                "2 green onions, chopped",
                "1/4 cup vegetable broth",
                "1 tbsp cornstarch mixed with 2 tbsp water",
                "Cooked rice or noodles for serving"
            ],
            "steps": [
                "In a small bowl, combine soy sauce, hoisin sauce, sesame oil, minced garlic, minced ginger, and chopped green onions.",
                "Heat a large skillet or wok over medium-high heat. Add tofu cubes and cook until golden brown on all sides. Remove from skillet and set aside.",
                "In the same skillet, add mixed vegetables and stir-fry for 3-4 minutes until tender-crisp.",
                "Return tofu to the skillet. Add vegetable broth and the soy sauce mixture. Bring to a simmer.",
                "Stir in the cornstarch slurry to thicken the sauce.",
                "Serve hot over cooked rice or noodles.",
                "Enjoy your Tofu and Vegetable Stir-Fry!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetable Spring Rolls with Peanut Sauce",
            "cuisine": "Asian",
            "meal": "Dinner",
            "allergens": ["Shellfish", "Peanuts"],
            "ingredients": [
                "10 spring roll wrappers",
                "2 cups mixed shredded vegetables (carrots, cucumber, lettuce, bell peppers)",
                "1/2 cup cooked vermicelli noodles",
                "1/4 cup fresh mint leaves",
                "1/4 cup fresh cilantro leaves",
                "For the peanut sauce:",
                "1/4 cup peanut butter",
                "2 tbsp soy sauce",
                "1 tbsp rice vinegar",
                "1 tbsp honey",
                "1/2 tsp sesame oil",
                "Water (as needed to thin the sauce)"
            ],
            "steps": [
                "Prepare the peanut sauce by whisking together peanut butter, soy sauce, rice vinegar, honey, and sesame oil. Add water gradually until desired consistency is reached. Set aside.",
                "Fill a shallow dish with warm water. Dip one spring roll wrapper into the water for a few seconds until softened.",
                "Lay wrapper flat and fill with a small handful of shredded vegetables, vermicelli noodles, mint leaves, and cilantro leaves.",
                "Fold the sides of the wrapper over the filling, then roll tightly.",
                "Repeat with remaining wrappers and filling.",
                "Serve spring rolls with peanut sauce for dipping.",
                "Enjoy your Vegetable Spring Rolls with Peanut Sauce!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetarian Thai Green Curry",
            "cuisine": "Asian",
            "meal": "Dinner",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 tbsp vegetable oil",
                "2 tbsp Thai green curry paste",
                "1 can (14 oz) coconut milk",
                "1 cup vegetable broth",
                "1 block tofu, cubed",
                "1 cup mixed vegetables (bell peppers, bamboo shoots, snow peas)",
                "1 tbsp soy sauce",
                "1 tbsp brown sugar",
                "Fresh basil leaves for garnish",
                "Cooked jasmine rice for serving"
            ],
            "steps": [
                "Heat vegetable oil in a large pot over medium heat. Add Thai green curry paste and stir-fry for 1-2 minutes until fragrant.",
                "Add coconut milk and vegetable broth. Bring to a simmer.",
                "Add tofu cubes and mixed vegetables. Simmer for 10-15 minutes until vegetables are tender and tofu is heated through.",
                "Stir in soy sauce and brown sugar.",
                "Serve hot over cooked jasmine rice, garnished with fresh basil leaves.",
                "Enjoy your Vegetarian Thai Green Curry!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Japanese Vegetable Tempura",
            "cuisine": "Asian",
            "meal": "Dinner",
            "allergens": ["Shellfish"],
            "ingredients": [
                "Assorted vegetables (e.g., sweet potato, bell peppers, broccoli)",
                "1 cup all-purpose flour",
                "1/4 cup cornstarch",
                "1/2 tsp baking powder",
                "Ice-cold water",
                "Vegetable oil for frying",
                "Tempura dipping sauce (store-bought or homemade)"
            ],
            "steps": [
                "Prepare vegetables by slicing into thin pieces.",
                "In a bowl, whisk together all-purpose flour, cornstarch, and baking powder.",
                "Gradually add ice-cold water to the flour mixture, whisking until the batter is smooth and thick enough to coat the back of a spoon.",
                "Heat vegetable oil in a deep fryer or large pot to 350°F (180°C).",
                "Dip vegetables into the batter, shaking off excess, and carefully place into the hot oil.",
                "Fry until golden brown and crispy, about 2-3 minutes per side.",
                "Remove tempura from oil and drain on paper towels.",
                "Serve hot with tempura dipping sauce.",
                "Enjoy your Japanese Vegetable Tempura!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Korean Bibimbap (Vegetarian Version)",
            "cuisine": "Asian",
            "meal": "Dinner",
            "allergens": ["Shellfish"],
            "ingredients": [
                "2 cups cooked white rice",
                "1 cup assorted vegetables (e.g., spinach, carrots, bean sprouts, mushrooms)",
                "1/2 cup kimchi (optional)",
                "2 eggs, fried or poached (optional)",
                "For the sauce:",
                "2 tbsp gochujang (Korean red chili paste)",
                "1 tbsp sesame oil",
                "1 tbsp soy sauce",
                "1 tbsp honey",
                "1 clove garlic, minced"
            ],
            "steps": [
                "Prepare the sauce by whisking together gochujang, sesame oil, soy sauce, honey, and minced garlic. Set aside.",
                "In a large skillet, stir-fry assorted vegetables until tender-crisp.",
                "Divide cooked rice among serving bowls. Arrange stir-fried vegetables and kimchi (if using) on top.",
                "Drizzle with prepared sauce.",
                "Top with fried or poached eggs (if desired).",
                "Mix everything together before eating.",
                "Enjoy your Korean Bibimbap!"
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Vegetable Fried Rice",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": ["Shellfish"],
            "ingredients": [
                "2 cups cooked rice, chilled",
                "1 cup mixed vegetables (peas, carrots, bell peppers)",
                "1/2 cup diced tofu",
                "2 eggs, beaten",
                "2 tbsp soy sauce",
                "1 tbsp sesame oil",
                "2 cloves garlic, minced",
                "1/2 cup green onions, chopped",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Heat sesame oil in a large skillet or wok over medium-high heat.",
                "Add minced garlic and sauté until fragrant.",
                "Add mixed vegetables and stir-fry for 2-3 minutes until tender.",
                "Push vegetables to one side of the skillet. Pour beaten eggs into the other side and scramble until cooked through.",
                "Add diced tofu and cooked rice. Stir-fry for another 3-4 minutes.",
                "Stir in soy sauce, green onions, salt, and pepper.",
                "Serve hot.",
                "Enjoy your Vegetable Fried Rice!"
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Vegetarian Sushi Rolls",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": ["Shellfish"],
            "ingredients": [
                "3 sheets nori (seaweed)",
                "1 cup sushi rice, cooked and seasoned",
                "1/2 cucumber, julienned",
                "1/2 avocado, sliced",
                "1/4 cup carrots, julienned",
                "1/4 cup bell peppers, julienned",
                "Soy sauce, pickled ginger, and wasabi for serving"
            ],
            "steps": [
                "Lay a sheet of nori on a bamboo sushi mat or plastic wrap.",
                "Spread a thin layer of sushi rice evenly over the nori, leaving a small border at the top edge.",
                "Arrange cucumber, avocado, carrots, and bell peppers in a line across the center of the rice.",
                "Roll the sushi tightly using the sushi mat, applying gentle pressure as you roll.",
                "Slice the roll into bite-sized pieces using a sharp knife.",
                "Serve with soy sauce, pickled ginger, and wasabi.",
                "Enjoy your Vegetarian Sushi Rolls!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Tofu Stir-Fry with Cashew Nuts",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 block tofu, cubed",
                "1/2 cup cashew nuts",
                "1 cup broccoli florets",
                "1/2 cup bell peppers, sliced",
                "2 tbsp soy sauce",
                "1 tbsp hoisin sauce",
                "1 tbsp rice vinegar",
                "1 tbsp sesame oil",
                "2 cloves garlic, minced",
                "1/2 tsp red pepper flakes (optional)",
                "Cooked rice for serving"
            ],
            "steps": [
                "Heat sesame oil in a large skillet or wok over medium-high heat.",
                "Add minced garlic and stir-fry until fragrant.",
                "Add tofu cubes and cashew nuts. Cook until tofu is golden brown.",
                "Add broccoli florets and bell peppers. Stir-fry for 3-4 minutes until vegetables are tender-crisp.",
                "In a small bowl, whisk together soy sauce, hoisin sauce, rice vinegar, and red pepper flakes.",
                "Pour sauce over the tofu and vegetables. Stir well to combine.",
                "Serve hot over cooked rice.",
                "Enjoy your Tofu Stir-Fry with Cashew Nuts!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Thai Coconut Curry Soup",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 tbsp vegetable oil",
                "2 tbsp Thai red curry paste",
                "1 can (14 oz) coconut milk",
                "2 cups vegetable broth",
                "1 block tofu, cubed",
                "1 cup mixed vegetables (mushrooms, bell peppers, bamboo shoots)",
                "1 tbsp soy sauce",
                "1 tbsp brown sugar",
                "Juice of 1 lime",
                "Fresh cilantro for garnish",
                "Cooked rice noodles for serving"
            ],
            "steps": [
                "Heat vegetable oil in a large pot over medium heat.",
                "Add Thai red curry paste and stir-fry for 1-2 minutes until fragrant.",
                "Add coconut milk and vegetable broth. Bring to a simmer.",
                "Add tofu cubes and mixed vegetables. Simmer for 10-15 minutes until vegetables are tender and tofu is heated through.",
                "Stir in soy sauce, brown sugar, and lime juice.",
                "Serve hot over cooked rice noodles, garnished with fresh cilantro.",
                "Enjoy your Thai Coconut Curry Soup!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Tofu Scramble",
            "cuisine": "Asian",
            "meal": "Breakfast",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 block firm tofu, crumbled",
                "1/2 cup mixed vegetables (bell peppers, spinach, mushrooms)",
                "2 tbsp soy sauce",
                "1 tbsp nutritional yeast",
                "1/2 tsp turmeric powder",
                "1/2 tsp garlic powder",
                "Salt and pepper to taste",
                "1 tbsp vegetable oil",
                "Fresh cilantro for garnish",
                "Whole grain toast or rice for serving"
            ],
            "steps": [
                "Heat vegetable oil in a large skillet over medium heat.",
                "Add crumbled tofu and sauté for 3-4 minutes until lightly browned.",
                "Add mixed vegetables and continue to cook for another 3-4 minutes until vegetables are tender.",
                "Stir in soy sauce, nutritional yeast, turmeric powder, garlic powder, salt, and pepper.",
                "Cook for additional 2-3 minutes until flavors are well combined and tofu is heated through.",
                "Garnish with fresh cilantro.",
                "Serve hot with whole grain toast or rice.",
                "Enjoy your Tofu Scramble!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetarian Congee",
            "cuisine": "Asian",
            "meal": "Breakfast",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 cup rice, rinsed",
                "6 cups vegetable broth",
                "1 block firm tofu, cubed",
                "1/2 cup mixed mushrooms, sliced",
                "1/4 cup green onions, chopped",
                "1 tbsp soy sauce",
                "1 tbsp sesame oil",
                "1 tbsp ginger, minced",
                "Salt and white pepper to taste",
                "Boiled egg (optional)",
                "Fresh cilantro for garnish"
            ],
            "steps": [
                "In a large pot, bring vegetable broth and rice to a boil. Reduce heat to low and simmer, stirring occasionally, for 40-45 minutes until rice is very soft and creamy.",
                "Add tofu cubes, mushrooms, green onions, soy sauce, sesame oil, and ginger. Cook for another 10-15 minutes until tofu and mushrooms are tender.",
                "Season with salt and white pepper.",
                "Serve hot, garnished with boiled egg (if using) and fresh cilantro.",
                "Enjoy your Vegetarian Congee!"
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Asian Inspired Tofu Omelette",
            "cuisine": "Asian",
            "meal": "Breakfast",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 block firm tofu, drained and mashed",
                "1/2 cup mixed vegetables (bell peppers, spinach, onions)",
                "2 tbsp soy sauce",
                "1 tbsp nutritional yeast",
                "1/2 tsp garlic powder",
                "1/2 tsp onion powder",
                "Salt and pepper to taste",
                "1 tbsp vegetable oil",
                "Fresh herbs (parsley or cilantro) for garnish"
            ],
            "steps": [
                "In a bowl, combine mashed tofu, mixed vegetables, soy sauce, nutritional yeast, garlic powder, onion powder, salt, and pepper.",
                "Heat vegetable oil in a non-stick skillet over medium heat.",
                "Pour tofu mixture into the skillet and spread evenly to form an omelette.",
                "Cook for 4-5 minutes until the bottom is golden brown and firm.",
                "Carefully flip the omelette and cook for another 3-4 minutes until cooked through.",
                "Garnish with fresh herbs.",
                "Serve hot.",
                "Enjoy your Asian Inspired Tofu Omelette!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetarian Congee with Mushrooms",
            "cuisine": "Asian",
            "meal": "Breakfast",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 cup rice, rinsed",
                "6 cups vegetable broth",
                "1 block firm tofu, cubed",
                "1 cup mixed mushrooms, sliced",
                "1/4 cup green onions, chopped",
                "1 tbsp soy sauce",
                "1 tbsp sesame oil",
                "1 tbsp ginger, minced",
                "Salt and white pepper to taste",
                "Boiled egg (optional)",
                "Fresh cilantro for garnish"
            ],
            "steps": [
                "In a large pot, bring vegetable broth and rice to a boil. Reduce heat to low and simmer, stirring occasionally, for 40-45 minutes until rice is very soft and creamy.",
                "Add tofu cubes, mushrooms, green onions, soy sauce, sesame oil, and ginger. Cook for another 10-15 minutes until tofu and mushrooms are tender.",
                "Season with salt and white pepper.",
                "Serve hot, garnished with boiled egg (if using) and fresh cilantro.",
                "Enjoy your Vegetarian Congee with Mushrooms!"
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Asian Inspired Tofu Omelette",
            "cuisine": "Asian",
            "meal": "Breakfast",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 block firm tofu, drained and mashed",
                "1/2 cup mixed vegetables (bell peppers, spinach, onions)",
                "2 tbsp soy sauce",
                "1 tbsp nutritional yeast",
                "1/2 tsp garlic powder",
                "1/2 tsp onion powder",
                "Salt and pepper to taste",
                "1 tbsp vegetable oil",
                "Fresh herbs (parsley or cilantro) for garnish"
            ],
            "steps": [
                "In a bowl, combine mashed tofu, mixed vegetables, soy sauce, nutritional yeast, garlic powder, onion powder, salt, and pepper.",
                "Heat vegetable oil in a non-stick skillet over medium heat.",
                "Pour tofu mixture into the skillet and spread evenly to form an omelette.",
                "Cook for 4-5 minutes until the bottom is golden brown and firm.",
                "Carefully flip the omelette and cook for another 3-4 minutes until cooked through.",
                "Garnish with fresh herbs.",
                "Serve hot.",
                "Enjoy your Asian Inspired Tofu Omelette!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetarian Thai Breakfast Soup",
            "cuisine": "Asian",
            "meal": "Breakfast",
            "allergens": ["Peanuts"],
            "ingredients": [
                "4 cups vegetable broth",
                "1 block firm tofu, cubed",
                "1 cup mixed vegetables (bok choy, carrots, mushrooms)",
                "1/4 cup green onions, chopped",
                "2 tbsp soy sauce",
                "1 tbsp lime juice",
                "1 tbsp fresh ginger, grated",
                "1 tbsp sesame oil",
                "1/2 tsp red pepper flakes (optional)",
                "Fresh cilantro for garnish",
                "Cooked rice noodles for serving"
            ],
            "steps": [
                "In a large pot, bring vegetable broth to a boil.",
                "Add tofu cubes, mixed vegetables, green onions, soy sauce, lime juice, ginger, sesame oil, and red pepper flakes (if using).",
                "Reduce heat to low and simmer for 10-12 minutes until tofu and vegetables are tender.",
                "Taste and adjust seasoning with soy sauce and lime juice.",
                "Serve hot over cooked rice noodles.",
                "Garnish with fresh cilantro.",
                "Enjoy your Vegetarian Thai Breakfast Soup!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Japanese Style Tofu Pancakes (Okonomiyaki)",
            "cuisine": "Asian",
            "meal": "Breakfast",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 block firm tofu, drained and mashed",
                "1/2 cup cabbage, shredded",
                "2 tbsp all-purpose flour",
                "2 tbsp soy sauce",
                "1 tbsp mirin",
                "1/2 tsp baking powder",
                "Salt and pepper to taste",
                "Vegetable oil for frying",
                "Okonomiyaki sauce",
                "Japanese mayonnaise",
                "Bonito flakes (optional)"
            ],
            "steps": [
                "In a bowl, combine mashed tofu, shredded cabbage, all-purpose flour, soy sauce, mirin, baking powder, salt, and pepper.",
                "Heat vegetable oil in a non-stick skillet over medium heat.",
                "Spoon tofu mixture into the skillet to form pancakes.",
                "Cook for 3-4 minutes on each side until golden brown and crispy.",
                "Drizzle with Okonomiyaki sauce and Japanese mayonnaise.",
                "Sprinkle with bonito flakes if desired.",
                "Serve hot.",
                "Enjoy your Japanese Style Tofu Pancakes!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vietnamese Fresh Spring Rolls",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": ["Peanuts"],
            "ingredients": [
                "Rice paper wrappers",
                "1 block firm tofu, sliced into strips",
                "Lettuce leaves",
                "Fresh herbs (mint, cilantro, Thai basil)",
                "1 cucumber, julienned",
                "1 carrot, julienned",
                "Rice vermicelli noodles, cooked and cooled",
                "Dipping sauce (hoisin sauce mixed with peanut butter substitute)",
                "Water for soaking rice paper wrappers"
            ],
            "steps": [
                "Prepare all ingredients and arrange them in separate bowls for easy assembly.",
                "Dip one rice paper wrapper into water to soften for about 10-15 seconds.",
                "Lay wrapper flat on a clean surface and add lettuce leaves, herbs, tofu strips, cucumber, carrot, and rice vermicelli noodles in the center.",
                "Fold the sides of the wrapper over the filling and roll tightly.",
                "Repeat with remaining ingredients.",
                "Serve fresh spring rolls with dipping sauce.",
                "Enjoy your Vietnamese Fresh Spring Rolls!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Japanese Soba Noodle Salad",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": ["Peanuts"],
            "ingredients": [
                "100g soba noodles, cooked and cooled",
                "1 block firm tofu, cubed and baked",
                "1 cucumber, thinly sliced",
                "1/2 cup edamame, shelled",
                "1/4 cup green onions, chopped",
                "2 tbsp soy sauce",
                "1 tbsp rice vinegar",
                "1 tbsp sesame oil",
                "1 tbsp sesame seeds",
                "1 tsp ginger, grated",
                "1 tsp honey",
                "Fresh cilantro for garnish"
            ],
            "steps": [
                "In a large bowl, combine soba noodles, baked tofu cubes, cucumber slices, edamame, and green onions.",
                "In a small bowl, whisk together soy sauce, rice vinegar, sesame oil, sesame seeds, ginger, and honey.",
                "Pour dressing over the noodle mixture and toss gently to combine.",
                "Garnish with fresh cilantro.",
                "Serve chilled or at room temperature.",
                "Enjoy your Japanese Soba Noodle Salad!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Korean Bibimbap",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 cup cooked white rice",
                "1 block firm tofu, sliced and pan-fried",
                "1/2 cup spinach, blanched and squeezed dry",
                "1/2 cup carrots, julienned and sautéed",
                "1/2 cup zucchini, julienned and sautéed",
                "1/2 cup bean sprouts, blanched",
                "1/4 cup kimchi",
                "1 egg, fried (optional)",
                "Toasted sesame seeds for garnish",
                "Gochujang sauce (Korean chili paste) to taste"
            ],
            "steps": [
                "Divide cooked rice among serving bowls.",
                "Arrange tofu slices, spinach, carrots, zucchini, bean sprouts, and kimchi on top of the rice in separate sections.",
                "Top with a fried egg if desired.",
                "Sprinkle with toasted sesame seeds.",
                "Serve hot with gochujang sauce on the side.",
                "Mix everything together before eating.",
                "Enjoy your Korean Bibimbap!"
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Thai Peanut-Free Pad Thai",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": ["Peanuts"],
            "ingredients": [
                "200g rice noodles, cooked and drained",
                "1 block firm tofu, cubed and pan-fried",
                "1 cup bean sprouts",
                "1/2 cup carrots, julienned",
                "1/2 cup green onions, chopped",
                "2 cloves garlic, minced",
                "2 tbsp soy sauce",
                "1 tbsp tamarind paste",
                "1 tbsp brown sugar",
                "1 tbsp lime juice",
                "1/2 tsp chili flakes (optional)",
                "1 tbsp vegetable oil",
                "Fresh cilantro and lime wedges for garnish"
            ],
            "steps": [
                "In a large skillet or wok, heat vegetable oil over medium-high heat.",
                "Add minced garlic and cook for 1 minute until fragrant.",
                "Add tofu cubes, bean sprouts, carrots, and green onions. Stir fry for 2-3 minutes.",
                "In a small bowl, whisk together soy sauce, tamarind paste, brown sugar, lime juice, and chili flakes (if using).",
                "Add cooked rice noodles and sauce to the skillet. Toss everything together until well combined and heated through.",
                "Serve hot, garnished with fresh cilantro and lime wedges.",
                "Enjoy your Thai Peanut-Free Pad Thai!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Chinese Style Vegetarian Dumplings (Jiaozi)",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 pack dumpling wrappers",
                "1 block firm tofu, drained and mashed",
                "1/2 cup napa cabbage, finely chopped",
                "1/4 cup carrots, grated",
                "2 green onions, finely chopped",
                "2 tbsp soy sauce",
                "1 tbsp sesame oil",
                "1 tbsp ginger, minced",
                "1 clove garlic, minced",
                "Water for sealing dumplings",
                "Dipping sauce (soy sauce mixed with rice vinegar and sesame oil)"
            ],
            "steps": [
                "In a large bowl, combine mashed tofu, napa cabbage, carrots, green onions, soy sauce, sesame oil, ginger, and garlic.",
                "Place a spoonful of filling in the center of each dumpling wrapper.",
                "Dip your finger in water and moisten the edges of the wrapper.",
                "Fold the wrapper in half over the filling to form a half-moon shape. Press edges together to seal tightly.",
                "Repeat with remaining wrappers and filling.",
                "Bring a large pot of water to a boil. Cook dumplings in batches for 5-6 minutes until they float to the surface and are cooked through.",
                "Serve hot with dipping sauce.",
                "Enjoy your Chinese Style Vegetarian Dumplings!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetarian Thai Green Curry",
            "cuisine": "Asian",
            "meal": "Dinner",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 cup mixed vegetables (bell peppers, zucchini, carrots)",
                "1 block firm tofu, cubed",
                "1 cup coconut milk",
                "2 tbsp Thai green curry paste",
                "1 tbsp soy sauce",
                "1 tbsp brown sugar",
                "1 tbsp vegetable oil",
                "Fresh basil leaves for garnish",
                "Cooked rice for serving"
            ],
            "steps": [
                "In a large skillet or wok, heat vegetable oil over medium heat.",
                "Add Thai green curry paste and stir fry for 1-2 minutes until fragrant.",
                "Add mixed vegetables and tofu cubes. Stir fry for 3-4 minutes until vegetables are slightly tender.",
                "Pour in coconut milk, soy sauce, and brown sugar. Stir well to combine.",
                "Simmer for 5-7 minutes until vegetables are cooked through and sauce thickens.",
                "Serve hot over cooked rice, garnished with fresh basil leaves.",
                "Enjoy your Vegetarian Thai Green Curry!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Japanese Vegetable Tempura",
            "cuisine": "Asian",
            "meal": "Dinner",
            "allergens": ["Peanuts"],
            "ingredients": [
                "Assorted vegetables (sweet potato, bell peppers, eggplant, broccoli)",
                "1 cup tempura flour (or all-purpose flour)",
                "Ice-cold water",
                "Vegetable oil for frying",
                "Tempura dipping sauce (soy sauce, mirin, dashi)",
                "Lemon wedges for garnish"
            ],
            "steps": [
                "Prepare vegetables by slicing them into thin pieces.",
                "Heat vegetable oil in a deep frying pan or wok.",
                "In a bowl, mix tempura flour with ice-cold water until just combined (batter should be lumpy).",
                "Dip vegetables into the batter and carefully place them into the hot oil.",
                "Fry until golden and crispy, turning occasionally. Drain on paper towels.",
                "Serve hot with tempura dipping sauce and lemon wedges.",
                "Enjoy your Japanese Vegetable Tempura!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Chinese Mapo Tofu",
            "cuisine": "Asian",
            "meal": "Dinner",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 block soft tofu, cubed",
                "1/2 cup minced meat substitute (optional)",
                "1/2 cup frozen peas",
                "2 tbsp chili bean paste (doubanjiang)",
                "2 tbsp soy sauce",
                "1 tbsp vegetable oil",
                "1 tsp Sichuan peppercorns",
                "2 green onions, chopped",
                "1 clove garlic, minced",
                "1 tsp ginger, minced",
                "Cooked rice for serving"
            ],
            "steps": [
                "Heat vegetable oil in a large skillet or wok over medium heat.",
                "Add Sichuan peppercorns and toast for 1 minute until fragrant.",
                "Add minced garlic, ginger, and green onions. Stir fry for another minute.",
                "If using, add minced meat substitute and cook until browned.",
                "Stir in chili bean paste and soy sauce. Mix well.",
                "Add cubed tofu and frozen peas. Gently stir to coat tofu with sauce.",
                "Simmer for 5-7 minutes until heated through and flavors meld.",
                "Serve hot over cooked rice.",
                "Enjoy your Chinese Mapo Tofu!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Thai Pineapple Fried Rice",
            "cuisine": "Asian",
            "meal": "Dinner",
            "allergens": ["Peanuts"],
            "ingredients": [
                "2 cups cooked jasmine rice, chilled",
                "1 cup pineapple chunks",
                "1/2 cup mixed vegetables (bell peppers, peas, carrots)",
                "1/2 cup cashew nuts",
                "2 tbsp soy sauce",
                "1 tbsp curry powder",
                "1 tbsp vegetable oil",
                "1/4 cup green onions, chopped",
                "Lime wedges for garnish"
            ],
            "steps": [
                "Heat vegetable oil in a large skillet or wok over medium heat.",
                "Add curry powder and stir fry for 1 minute until fragrant.",
                "Add mixed vegetables and pineapple chunks. Stir fry for 3-4 minutes until vegetables are tender.",
                "Add chilled jasmine rice, soy sauce, and cashew nuts. Stir fry for another 3-4 minutes until rice is heated through.",
                "Stir in chopped green onions.",
                "Serve hot, garnished with lime wedges.",
                "Enjoy your Thai Pineapple Fried Rice!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Indian Chana Masala",
            "cuisine": "Asian",
            "meal": "Dinner",
            "allergens": ["Peanuts"],
            "ingredients": [
                "2 cups cooked chickpeas",
                "1 onion, finely chopped",
                "2 tomatoes, chopped",
                "1 green chili, minced (optional)",
                "1 tbsp ginger-garlic paste",
                "1 tsp cumin seeds",
                "1 tsp turmeric powder",
                "1 tsp garam masala",
                "1/2 tsp chili powder",
                "1/2 cup coconut milk",
                "1 tbsp vegetable oil",
                "Fresh cilantro for garnish",
                "Cooked rice or naan for serving"
            ],
            "steps": [
                "Heat vegetable oil in a large skillet or pot over medium heat.",
                "Add cumin seeds and toast for 1 minute until fragrant.",
                "Add chopped onions and sauté until golden brown.",
                "Stir in ginger-garlic paste, green chili (if using), turmeric powder, garam masala, and chili powder. Cook for 2 minutes.",
                "Add chopped tomatoes and cook until soft and oil separates from the masala.",
                "Add cooked chickpeas and coconut milk. Stir well to combine.",
                "Simmer for 10-12 minutes until flavors meld and sauce thickens.",
                "Garnish with fresh cilantro.",
                "Serve hot with rice or naan.",
                "Enjoy your Indian Chana Masala!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Mango Sticky Rice",
            "cuisine": "Asian",
            "meal": "Dessert",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 cup glutinous rice (sticky rice)",
                "1 cup coconut milk",
                "1/2 cup sugar",
                "1/2 tsp salt",
                "2 ripe mangoes, sliced",
                "Toasted sesame seeds for garnish"
            ],
            "steps": [
                "Rinse sticky rice until water runs clear. Soak in water for 1 hour.",
                "Drain rice and steam for 20-25 minutes until tender.",
                "In a saucepan, heat coconut milk, sugar, and salt until sugar dissolves.",
                "Fluff steamed rice and pour coconut milk mixture over it. Mix well and let it sit for 10 minutes.",
                "Serve sticky rice with sliced mangoes.",
                "Garnish with toasted sesame seeds.",
                "Enjoy your Mango Sticky Rice!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Japanese Matcha Ice Cream",
            "cuisine": "Asian",
            "meal": "Dessert",
            "allergens": ["Peanuts"],
            "ingredients": [
                "2 cups heavy cream",
                "1 cup whole milk",
                "3/4 cup sugar",
                "4 egg yolks",
                "2 tbsp matcha green tea powder",
                "1 tsp vanilla extract"
            ],
            "steps": [
                "In a saucepan, heat heavy cream and whole milk until just simmering.",
                "In a separate bowl, whisk together sugar and egg yolks until pale and creamy.",
                "Gradually whisk hot cream mixture into the egg mixture.",
                "Return the mixture to the saucepan and cook over low heat, stirring constantly, until it thickens enough to coat the back of a spoon.",
                "Remove from heat and stir in matcha powder and vanilla extract until well combined.",
                "Strain mixture through a fine sieve and chill for several hours or overnight.",
                "Churn in an ice cream maker according to manufacturer's instructions.",
                "Transfer to a container and freeze until firm.",
                "Enjoy your Japanese Matcha Ice Cream!"
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Thai Coconut Pancakes (Khanom Ba-Bin)",
            "cuisine": "Asian",
            "meal": "Dessert",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 cup rice flour",
                "1/2 cup coconut milk",
                "1/2 cup water",
                "1/2 cup palm sugar",
                "1/4 cup shredded coconut",
                "1/4 tsp salt",
                "Banana leaves or parchment paper"
            ],
            "steps": [
                "In a bowl, mix rice flour, coconut milk, water, palm sugar, shredded coconut, and salt until smooth.",
                "Heat a non-stick pan over medium heat and lightly grease with oil.",
                "Pour a thin layer of batter onto the pan and swirl to coat evenly.",
                "Cook until the edges start to lift and the bottom is golden brown.",
                "Fold the pancake in half and cook for another minute until cooked through.",
                "Remove from heat and repeat with remaining batter.",
                "Serve warm or at room temperature.",
                "Enjoy your Thai Coconut Pancakes!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Indian Gulab Jamun",
            "cuisine": "Asian",
            "meal": "Dessert",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 cup milk powder",
                "1/4 cup all-purpose flour",
                "1/4 tsp baking powder",
                "2 tbsp ghee (clarified butter)",
                "1/4 cup milk",
                "1/4 cup water",
                "1 cup sugar",
                "1 cup water",
                "1/2 tsp cardamom powder",
                "Saffron strands for garnish"
            ],
            "steps": [
                "In a bowl, combine milk powder, all-purpose flour, and baking powder.",
                "Add ghee and mix until crumbly.",
                "Gradually add milk and water to form a soft dough.",
                "Divide dough into small balls and roll them smooth.",
                "Heat oil in a deep pan and fry dough balls until golden brown.",
                "In a separate saucepan, combine sugar, water, cardamom powder, and saffron.",
                "Simmer until syrup thickens slightly.",
                "Soak fried balls in warm syrup for at least 1 hour.",
                "Serve warm or chilled, garnished with saffron strands.",
                "Enjoy your Indian Gulab Jamun!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Filipino Turon (Banana Spring Rolls)",
            "cuisine": "Asian",
            "meal": "Dessert",
            "allergens": ["Peanuts"],
            "ingredients": [
                "6 ripe saba bananas, peeled and halved lengthwise",
                "12 spring roll wrappers",
                "1 cup brown sugar",
                "1/2 cup jackfruit strips (optional)",
                "Vegetable oil for frying"
            ],
            "steps": [
                "Lay a spring roll wrapper flat on a clean surface.",
                "Place a banana half on the wrapper and sprinkle with brown sugar.",
                "Add jackfruit strips (if using).",
                "Fold sides of the wrapper over the filling and roll tightly into a cylinder, sealing the edge with water.",
                "Heat vegetable oil in a pan over medium heat.",
                "Fry turon until golden brown and crispy on all sides.",
                "Drain on paper towels.",
                "Serve warm with a sprinkle of brown sugar.",
                "Enjoy your Filipino Turon!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Classic Chocolate Chip Cookies",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 cup unsalted butter, softened",
                "1 cup granulated sugar",
                "1 cup packed brown sugar",
                "2 large eggs",
                "1 tsp vanilla extract",
                "3 cups all-purpose flour",
                "1 tsp baking soda",
                "1/2 tsp salt",
                "2 cups semisweet chocolate chips"
            ],
            "steps": [
                "Preheat oven to 350°F (175°C).",
                "In a large bowl, cream together butter, granulated sugar, and brown sugar until smooth.",
                "Beat in eggs one at a time, then stir in vanilla.",
                "Combine flour, baking soda, and salt; gradually stir into the creamed mixture.",
                "Fold in chocolate chips.",
                "Drop by rounded spoonfuls onto ungreased cookie sheets.",
                "Bake for 10 to 12 minutes until edges are golden brown.",
                "Allow cookies to cool on baking sheet for 5 minutes before transferring to a wire rack to cool completely.",
                "Enjoy your Classic Chocolate Chip Cookies!"
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Tiramisu",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Peanuts"],
            "ingredients": [
                "6 egg yolks",
                "3/4 cup granulated sugar",
                "1 cup mascarpone cheese",
                "1 1/2 cups heavy cream",
                "1 cup strong brewed coffee, cooled",
                "2 tbsp coffee liqueur (optional)",
                "24 ladyfinger cookies",
                "Unsweetened cocoa powder for dusting"
            ],
            "steps": [
                "In a heatproof bowl, whisk together egg yolks and sugar until thick and pale.",
                "Set the bowl over a pan of simmering water, making sure the water doesn't touch the bottom of the bowl.",
                "Whisk constantly until mixture reaches 160°F (70°C).",
                "Remove from heat and beat mascarpone into the egg mixture until smooth.",
                "In a separate bowl, whip heavy cream until stiff peaks form.",
                "Gently fold whipped cream into mascarpone mixture.",
                "Combine coffee and coffee liqueur in a shallow dish.",
                "Quickly dip each ladyfinger into coffee mixture and arrange in a single layer in a serving dish.",
                "Spread half of the mascarpone mixture over the ladyfingers.",
                "Repeat with another layer of dipped ladyfingers and mascarpone mixture.",
                "Cover and refrigerate for at least 4 hours or overnight.",
                "Dust with cocoa powder before serving.",
                "Enjoy your Tiramisu!"
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Lemon Tart",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 1/4 cups all-purpose flour",
                "1/2 cup unsalted butter, cold and diced",
                "1/4 cup granulated sugar",
                "Pinch of salt",
                "4 large eggs",
                "3/4 cup granulated sugar",
                "1/2 cup fresh lemon juice",
                "1 tbsp lemon zest",
                "1/4 cup heavy cream"
            ],
            "steps": [
                "Preheat oven to 350°F (175°C).",
                "In a food processor, pulse together flour, butter, sugar, and salt until mixture resembles coarse crumbs.",
                "Press mixture into the bottom and up the sides of a 9-inch tart pan with removable bottom.",
                "Bake crust for 15-20 minutes until golden brown.",
                "In a bowl, whisk together eggs, sugar, lemon juice, lemon zest, and heavy cream until smooth.",
                "Pour filling into warm crust.",
                "Reduce oven temperature to 325°F (165°C) and bake for 20-25 minutes until filling is set.",
                "Cool completely on a wire rack.",
                "Refrigerate for at least 2 hours before serving.",
                "Enjoy your Lemon Tart!"
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Raspberry Cheesecake Bars",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 1/2 cups graham cracker crumbs",
                "1/4 cup granulated sugar",
                "1/2 cup unsalted butter, melted",
                "16 oz cream cheese, softened",
                "1/2 cup granulated sugar",
                "2 large eggs",
                "1 tsp vanilla extract",
                "1 cup fresh raspberries",
                "Powdered sugar for dusting"
            ],
            "steps": [
                "Preheat oven to 350°F (175°C).",
                "Line a 9x9-inch baking pan with parchment paper, leaving an overhang on the sides.",
                "In a bowl, combine graham cracker crumbs, sugar, and melted butter until mixture resembles wet sand.",
                "Press mixture evenly into the bottom of the prepared pan.",
                "In another bowl, beat cream cheese and sugar until smooth and creamy.",
                "Beat in eggs, one at a time, until combined.",
                "Stir in vanilla extract.",
                "Pour cream cheese mixture over crust and spread evenly.",
                "Drop raspberry preserves by spoonfuls onto cream cheese mixture and swirl gently with a knife.",
                "Bake for 30-35 minutes until edges are set and center is slightly jiggly.",
                "Cool completely in pan on a wire rack.",
                "Refrigerate for at least 2 hours before cutting into bars.",
                "Dust with powdered sugar before serving.",
                "Enjoy your Raspberry Cheesecake Bars!"
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Apple Crisp",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Peanuts"],
            "ingredients": [
                "6 cups sliced apples",
                "1 tbsp lemon juice",
                "1/2 cup granulated sugar",
                "1/2 tsp ground cinnamon",
                "1/4 tsp ground nutmeg",
                "1/2 cup old-fashioned oats",
                "1/3 cup all-purpose flour",
                "1/3 cup packed brown sugar",
                "1/4 cup cold unsalted butter, diced"
            ],
            "steps": [
                "Preheat oven to 350°F (175°C).",
                "In a large bowl, toss sliced apples with lemon juice, granulated sugar, cinnamon, and nutmeg.",
                "Spread apple mixture evenly into a greased 9x13-inch baking dish.",
                "In a separate bowl, combine oats, flour, brown sugar, and butter until crumbly.",
                "Sprinkle oat mixture evenly over apples.",
                "Bake for 40-45 minutes until apples are tender and topping is golden brown.",
                "Cool slightly before serving.",
                "Enjoy your Apple Crisp!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vanilla Panna Cotta with Berry Compote",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Peanuts"],
            "ingredients": [
                "2 cups heavy cream",
                "1/2 cup granulated sugar",
                "1 tsp vanilla extract",
                "2 tsp powdered gelatin",
                "3 tbsp cold water",
                "2 cups mixed berries (such as strawberries, blueberries, raspberries)",
                "1/4 cup granulated sugar"
            ],
            "steps": [
                "In a saucepan, combine heavy cream and sugar. Bring to a simmer over medium heat, stirring occasionally.",
                "Remove from heat and stir in vanilla extract.",
                "In a small bowl, sprinkle gelatin over cold water. Let stand for 5 minutes to soften.",
                "Add softened gelatin to warm cream mixture and stir until completely dissolved.",
                "Pour mixture into serving glasses or molds. Refrigerate for at least 4 hours or until set.",
                "In a saucepan, combine mixed berries and sugar. Cook over medium heat until berries release their juices and mixture thickens slightly.",
                "Remove from heat and let cool to room temperature.",
                "Top chilled panna cotta with berry compote before serving.",
                "Enjoy your Vanilla Panna Cotta with Berry Compote!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetable Lasagna",
            "cuisine": "Western",
            "meal": "Dinner",
            "allergens": ["Peanuts"],
            "ingredients": [
                "9 lasagna noodles, cooked al dente",
                "2 cups ricotta cheese",
                "1 cup grated Parmesan cheese",
                "2 cups shredded mozzarella cheese",
                "1 large egg",
                "2 cups marinara sauce",
                "1 cup chopped spinach",
                "1 cup sliced mushrooms",
                "1 cup diced zucchini",
                "1 cup diced bell peppers",
                "1/2 cup diced onions",
                "2 cloves garlic, minced",
                "1 tbsp olive oil",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Preheat oven to 375°F (190°C).",
                "In a large skillet, heat olive oil over medium heat. Saute onions and garlic until softened.",
                "Add mushrooms, zucchini, and bell peppers. Cook until vegetables are tender. Season with salt and pepper.",
                "In a bowl, combine ricotta cheese, Parmesan cheese, mozzarella cheese, and egg. Mix well.",
                "Spread a thin layer of marinara sauce on the bottom of a 9x13-inch baking dish.",
                "Arrange 3 lasagna noodles on top of the sauce. Spread half of the ricotta mixture over the noodles.",
                "Top with half of the vegetable mixture. Repeat layers, ending with marinara sauce and shredded mozzarella cheese.",
                "Cover with foil and bake for 30 minutes. Remove foil and bake for an additional 15 minutes until bubbly and golden.",
                "Let stand for 10 minutes before slicing and serving.",
                "Enjoy your Vegetable Lasagna!"
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Spinach and Mushroom Risotto",
            "cuisine": "Western",
            "meal": "Dinner",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 1/2 cups Arborio rice",
                "4 cups vegetable broth, heated",
                "1 cup white wine",
                "1 cup grated Parmesan cheese",
                "1 cup chopped spinach",
                "1 cup sliced mushrooms",
                "1/2 cup diced onions",
                "2 cloves garlic, minced",
                "2 tbsp olive oil",
                "Salt and pepper to taste"
            ],
            "steps": [
                "In a large skillet or Dutch oven, heat olive oil over medium heat. Saute onions and garlic until softened.",
                "Add mushrooms and cook until tender.",
                "Stir in Arborio rice and cook for 1-2 minutes until lightly toasted.",
                "Pour in white wine and cook until wine is absorbed, stirring constantly.",
                "Gradually add hot vegetable broth, 1 cup at a time, stirring frequently until liquid is absorbed before adding more.",
                "Continue cooking and stirring until rice is creamy and tender, about 20 minutes.",
                "Stir in chopped spinach and Parmesan cheese until spinach is wilted and cheese is melted.",
                "Season with salt and pepper to taste.",
                "Serve immediately.",
                "Enjoy your Spinach and Mushroom Risotto!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Stuffed Bell Peppers",
            "cuisine": "Western",
            "meal": "Dinner",
            "allergens": ["Peanuts"],
            "ingredients": [
                "6 large bell peppers, tops removed and seeded",
                "1 cup quinoa, cooked",
                "1 can (15 oz) black beans, rinsed and drained",
                "1 cup corn kernels",
                "1 cup diced tomatoes",
                "1/2 cup shredded cheddar cheese",
                "1/4 cup chopped fresh cilantro",
                "1 tsp ground cumin",
                "1 tsp chili powder",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Preheat oven to 375°F (190°C).",
                "In a large bowl, combine cooked quinoa, black beans, corn, tomatoes, cheddar cheese, cilantro, cumin, and chili powder.",
                "Season with salt and pepper to taste.",
                "Stuff each bell pepper with quinoa mixture and place upright in a baking dish.",
                "Cover with foil and bake for 30 minutes.",
                "Remove foil and bake for an additional 10-15 minutes until peppers are tender and filling is heated through.",
                "Serve hot.",
                "Enjoy your Stuffed Bell Peppers!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Mushroom and Spinach Quesadillas",
            "cuisine": "Western",
            "meal": "Dinner",
            "allergens": ["Peanuts"],
            "ingredients": [
                "4 large flour tortillas",
                "2 cups shredded Monterey Jack cheese",
                "1 cup sliced mushrooms",
                "2 cups fresh spinach",
                "1/2 cup diced onions",
                "2 cloves garlic, minced",
                "2 tbsp olive oil",
                "Salt and pepper to taste"
            ],
            "steps": [
                "In a large skillet, heat olive oil over medium heat. Saute onions and garlic until softened.",
                "Add mushrooms and cook until tender.",
                "Add spinach and cook until wilted. Season with salt and pepper.",
                "Remove from heat and set aside.",
                "In another skillet, heat a tortilla over medium heat. Sprinkle with shredded cheese.",
                "Top with mushroom and spinach mixture and another tortilla.",
                "Cook until tortilla is golden brown and cheese is melted, flipping once.",
                "Repeat with remaining tortillas and filling.",
                "Cut quesadillas into wedges and serve hot.",
                "Enjoy your Mushroom and Spinach Quesadillas!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Caprese Stuffed Portobello Mushrooms",
            "cuisine": "Western",
            "meal": "Dinner",
            "allergens": ["Peanuts"],
            "ingredients": [
                "4 large portobello mushrooms, stems removed",
                "1 cup cherry tomatoes, halved",
                "1 cup fresh mozzarella balls, halved",
                "1/4 cup chopped fresh basil",
                "2 cloves garlic, minced",
                "2 tbsp balsamic vinegar",
                "2 tbsp olive oil",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Preheat oven to 400°F (200°C).",
                "In a bowl, combine cherry tomatoes, mozzarella balls, basil, garlic, balsamic vinegar, olive oil, salt, and pepper.",
                "Scoop out gills from portobello mushrooms and brush with olive oil.",
                "Stuff mushrooms with tomato and mozzarella mixture.",
                "Place stuffed mushrooms on a baking sheet and bake for 15-20 minutes until mushrooms are tender and cheese is melted.",
                "Serve hot.",
                "Enjoy your Caprese Stuffed Portobello Mushrooms!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetarian Shepherd's Pie",
            "cuisine": "Western",
            "meal": "Dinner",
            "allergens": ["Peanuts"],
            "ingredients": [
                "4 large potatoes, peeled and cubed",
                "1/4 cup milk",
                "2 tbsp butter",
                "Salt and pepper to taste",
                "2 tbsp olive oil",
                "1 cup diced onions",
                "2 cloves garlic, minced",
                "2 cups mixed vegetables (carrots, peas, corn)",
                "1 can (15 oz) lentils, rinsed and drained",
                "1 cup vegetable broth",
                "2 tbsp tomato paste",
                "1 tsp dried thyme",
                "1 tsp dried rosemary",
                "1/2 cup shredded cheddar cheese"
            ],
            "steps": [
                "Preheat oven to 400°F (200°C).",
                "In a large pot, cover potatoes with water and bring to a boil. Cook until tender, about 15 minutes. Drain.",
                "Mash potatoes with milk, butter, salt, and pepper until smooth. Set aside.",
                "In a large skillet, heat olive oil over medium heat. Saute onions and garlic until softened.",
                "Add mixed vegetables and cook until tender.",
                "Stir in lentils, vegetable broth, tomato paste, thyme, and rosemary. Simmer for 10 minutes until mixture thickens.",
                "Pour lentil mixture into a baking dish. Spread mashed potatoes over the top.",
                "Sprinkle with shredded cheddar cheese.",
                "Bake for 25-30 minutes until heated through and cheese is melted.",
                "Let stand for 10 minutes before serving.",
                "Enjoy your Vegetarian Shepherd's Pie!"
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Caprese Sandwich",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": ["Peanuts"],
            "ingredients": [
                "4 slices whole grain bread",
                "1 large tomato, sliced",
                "1 ball fresh mozzarella cheese, sliced",
                "1/2 cup fresh basil leaves",
                "2 tbsp balsamic glaze",
                "Salt and pepper to taste",
                "1 tbsp olive oil"
            ],
            "steps": [
                "Brush one side of each bread slice with olive oil.",
                "Layer tomato slices, mozzarella slices, and basil leaves on two bread slices.",
                "Drizzle with balsamic glaze and season with salt and pepper.",
                "Top with remaining bread slices, oil side out.",
                "Heat a non-stick skillet over medium heat.",
                "Grill sandwiches until golden brown and cheese is melted, about 3-4 minutes per side.",
                "Slice in half and serve warm."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Veggie Wrap with Hummus",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 large whole wheat tortilla",
                "1/4 cup hummus",
                "1/2 cup mixed salad greens",
                "1/2 cup thinly sliced cucumber",
                "1/2 cup shredded carrots",
                "1/4 cup sliced red bell pepper",
                "1/4 cup crumbled feta cheese",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Spread hummus evenly over the tortilla.",
                "Layer salad greens, cucumber, carrots, bell pepper, and feta cheese on top of the hummus.",
                "Season with salt and pepper.",
                "Roll up the tortilla tightly, folding in the sides as you go.",
                "Slice in half diagonally and serve."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Mediterranean Quinoa Salad",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 cup quinoa, cooked and cooled",
                "1/2 cup cherry tomatoes, halved",
                "1/2 cup cucumber, diced",
                "1/4 cup Kalamata olives, pitted and sliced",
                "1/4 cup red onion, thinly sliced",
                "1/4 cup crumbled feta cheese",
                "2 tbsp fresh parsley, chopped",
                "2 tbsp olive oil",
                "1 tbsp lemon juice",
                "Salt and pepper to taste"
            ],
            "steps": [
                "In a large bowl, combine quinoa, cherry tomatoes, cucumber, olives, red onion, feta cheese, and parsley.",
                "Drizzle with olive oil and lemon juice.",
                "Season with salt and pepper, toss gently to combine.",
                "Chill in the refrigerator for 30 minutes before serving."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Veggie Omelette",
            "cuisine": "Western",
            "meal": "Breakfast",
            "allergens": ["Peanuts"],
            "ingredients": [
                "3 eggs",
                "1/4 cup diced bell peppers",
                "1/4 cup diced tomatoes",
                "1/4 cup chopped spinach",
                "1/4 cup shredded cheddar cheese",
                "Salt and pepper to taste",
                "1 tbsp butter or olive oil"
            ],
            "steps": [
                "In a bowl, beat eggs until well combined.",
                "Stir in diced bell peppers, tomatoes, spinach, and shredded cheddar cheese.",
                "Season with salt and pepper.",
                "Heat butter or olive oil in a non-stick skillet over medium heat.",
                "Pour egg mixture into the skillet and cook until edges are set, about 2-3 minutes.",
                "Gently lift edges with a spatula and tilt the skillet to let uncooked egg flow underneath.",
                "Cook until the omelette is set but still slightly moist on top.",
                "Fold omelette in half and slide onto a plate.",
                "Serve hot."
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Greek Yogurt Parfait",
            "cuisine": "Western",
            "meal": "Breakfast",
            "allergens": ["Peanuts"],
            "ingredients": [
                "1 cup Greek yogurt",
                "1/2 cup granola",
                "1/2 cup mixed berries (strawberries, blueberries, raspberries)",
                "1 tbsp honey or maple syrup",
                "1/4 cup sliced almonds (optional, omit for nut allergy)"
            ],
            "steps": [
                "In a glass or bowl, layer Greek yogurt, granola, and mixed berries.",
                "Drizzle with honey or maple syrup.",
                "Top with sliced almonds if using.",
                "Repeat layers if desired.",
                "Serve immediately."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Avocado Toast",
            "cuisine": "Western",
            "meal": "Breakfast",
            "allergens": ["Peanuts"],
            "ingredients": [
                "2 slices whole grain bread, toasted",
                "1 ripe avocado, mashed",
                "1 tbsp lemon juice",
                "Salt and pepper to taste",
                "Red pepper flakes (optional)",
                "Cherry tomatoes, sliced (optional)"
            ],
            "steps": [
                "Spread mashed avocado evenly over toasted bread slices.",
                "Drizzle with lemon juice and season with salt, pepper, and red pepper flakes if using.",
                "Top with sliced cherry tomatoes if desired.",
                "Serve immediately."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Classic French Toast",
            "cuisine": "Western",
            "meal": "Breakfast",
            "allergens": ["Soy"],
            "ingredients": [
                "4 slices of bread (thickly sliced preferred)",
                "2 eggs",
                "1/2 cup milk",
                "1/2 tsp vanilla extract",
                "1/4 tsp ground cinnamon",
                "Butter or oil for frying",
                "Maple syrup and fresh berries for serving"
            ],
            "steps": [
                "In a shallow bowl, whisk together eggs, milk, vanilla extract, and ground cinnamon.",
                "Heat a non-stick skillet or griddle over medium heat.",
                "Dip each slice of bread into the egg mixture, coating both sides evenly.",
                "Cook bread slices on the skillet until golden brown on both sides, about 2-3 minutes per side.",
                "Serve hot with butter, maple syrup, and fresh berries."
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Veggie Breakfast Burrito",
            "cuisine": "Western",
            "meal": "Breakfast",
            "allergens": ["Soy"],
            "ingredients": [
                "4 large flour tortillas",
                "4 eggs, scrambled",
                "1/2 cup black beans, drained and rinsed",
                "1/2 cup diced bell peppers",
                "1/4 cup diced onions",
                "1/2 cup shredded cheddar cheese",
                "Salt and pepper to taste",
                "Salsa and sour cream for serving"
            ],
            "steps": [
                "Heat a non-stick skillet over medium heat.",
                "Add diced onions and bell peppers, sauté until softened, about 3-4 minutes.",
                "Add scrambled eggs to the skillet, cook until eggs are set.",
                "Warm tortillas in a separate skillet or microwave.",
                "Divide scrambled eggs, black beans, and shredded cheddar cheese among tortillas.",
                "Fold tortillas to enclose filling, forming burritos.",
                "Serve with salsa and sour cream on the side."
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Blueberry Muffins",
            "cuisine": "Western",
            "meal": "Breakfast",
            "allergens": ["Soy"],
            "ingredients": [
                "1 3/4 cups all-purpose flour",
                "1/2 cup granulated sugar",
                "1 tbsp baking powder",
                "1/4 tsp salt",
                "1/2 cup milk",
                "1/2 cup unsalted butter, melted",
                "2 large eggs",
                "1 tsp vanilla extract",
                "1 cup fresh or frozen blueberries",
                "Turbinado sugar for sprinkling (optional)"
            ],
            "steps": [
                "Preheat oven to 400°F (200°C). Line a muffin tin with paper liners or grease well.",
                "In a large bowl, whisk together flour, sugar, baking powder, and salt.",
                "In another bowl, whisk together milk, melted butter, eggs, and vanilla extract.",
                "Pour wet ingredients into dry ingredients, stir until just combined.",
                "Gently fold in blueberries.",
                "Divide batter evenly among muffin cups, filling each about 3/4 full.",
                "Sprinkle turbinado sugar over the tops of muffins if desired.",
                "Bake for 18-20 minutes or until a toothpick inserted into the center comes out clean.",
                "Cool in the pan for 5 minutes, then transfer muffins to a wire rack to cool completely."
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Breakfast Hash",
            "cuisine": "Western",
            "meal": "Breakfast",
            "allergens": ["Soy"],
            "ingredients": [
                "2 large potatoes, peeled and diced",
                "1 onion, diced",
                "1 red bell pepper, diced",
                "1 cup diced mushrooms",
                "1 cup cooked black beans",
                "2 tbsp olive oil",
                "1 tsp smoked paprika",
                "Salt and pepper to taste",
                "Fresh parsley or cilantro for garnish"
            ],
            "steps": [
                "Heat olive oil in a large skillet over medium heat.",
                "Add diced potatoes and cook until golden and tender, stirring occasionally, about 10-12 minutes.",
                "Add diced onion, bell pepper, and mushrooms to the skillet, cook until softened, about 5-6 minutes.",
                "Stir in cooked black beans and smoked paprika, season with salt and pepper.",
                "Cook for another 2-3 minutes until heated through.",
                "Garnish with fresh parsley or cilantro before serving."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Caprese Salad with Balsamic Glaze",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": ["Soy"],
            "ingredients": [
                "2 large tomatoes, sliced",
                "1 ball fresh mozzarella cheese, sliced",
                "Fresh basil leaves",
                "Salt and pepper to taste",
                "Extra virgin olive oil",
                "Balsamic glaze"
            ],
            "steps": [
                "Arrange tomato and mozzarella slices on a serving platter.",
                "Tuck fresh basil leaves between tomato and mozzarella slices.",
                "Season with salt and pepper, drizzle with olive oil and balsamic glaze.",
                "Serve immediately."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Veggie Wrap with Hummus",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": ["Soy"],
            "ingredients": [
                "1 large whole wheat tortilla",
                "1/4 cup hummus",
                "1/2 cup mixed salad greens",
                "1/4 cup shredded carrots",
                "1/4 cup sliced cucumber",
                "1/4 cup sliced bell peppers",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Spread hummus evenly over the tortilla.",
                "Layer salad greens, shredded carrots, sliced cucumber, and bell peppers on top.",
                "Season with salt and pepper.",
                "Roll up tightly, slice in half, and serve."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Quinoa Stuffed Bell Peppers",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": ["Soy"],
            "ingredients": [
                "4 large bell peppers, tops cut off and seeds removed",
                "1 cup quinoa, rinsed",
                "2 cups vegetable broth",
                "1 can (15 oz) black beans, drained and rinsed",
                "1 cup corn kernels",
                "1 cup diced tomatoes",
                "1/2 cup shredded cheddar cheese",
                "1 tsp cumin",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Preheat oven to 375°F (190°C).",
                "In a saucepan, bring vegetable broth to a boil, add quinoa, cover, and simmer for 15-20 minutes until quinoa is cooked and liquid is absorbed.",
                "In a large bowl, combine cooked quinoa, black beans, corn kernels, diced tomatoes, shredded cheddar cheese, cumin, salt, and pepper.",
                "Stuff each bell pepper with quinoa mixture, place in a baking dish.",
                "Cover with foil and bake for 30-35 minutes until peppers are tender.",
                "Remove foil, sprinkle with additional cheese if desired, and bake for another 5 minutes until cheese is melted.",
                "Serve hot."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Tomato Basil Soup with Grilled Cheese",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": ["Soy"],
            "ingredients": [
                "2 tbsp olive oil",
                "1 onion, diced",
                "2 cloves garlic, minced",
                "4 cups vegetable broth",
                "2 cans (14 oz each) diced tomatoes",
                "1/2 cup fresh basil leaves, chopped",
                "Salt and pepper to taste",
                "8 slices bread",
                "8 slices cheddar cheese",
                "Butter for spreading"
            ],
            "steps": [
                "In a large pot, heat olive oil over medium heat.",
                "Add diced onion and garlic, sauté until softened, about 5 minutes.",
                "Add vegetable broth, diced tomatoes (with juices), and chopped basil.",
                "Season with salt and pepper, bring to a boil, then reduce heat and simmer for 20-25 minutes.",
                "Meanwhile, preheat a skillet over medium heat.",
                "Spread butter on one side of each bread slice.",
                "Place buttered side down in the skillet, top with cheddar cheese slices, and another bread slice (buttered side up).",
                "Cook until golden brown and cheese is melted, flip and cook the other side until golden brown.",
                "Serve grilled cheese sandwiches with tomato basil soup."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Avocado Toast with Poached Egg",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": ["Soy"],
            "ingredients": [
                "2 slices whole grain bread, toasted",
                "1 ripe avocado, mashed",
                "2 large eggs, poached",
                "Salt and pepper to taste",
                "Red pepper flakes (optional)",
                "Fresh cilantro or parsley for garnish"
            ],
            "steps": [
                "Spread mashed avocado evenly over toasted bread slices.",
                "Top each toast with a poached egg.",
                "Season with salt, pepper, and red pepper flakes if using.",
                "Garnish with fresh cilantro or parsley.",
                "Serve immediately."
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Mediterranean Couscous Salad",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": ["Soy"],
            "ingredients": [
                "1 cup couscous",
                "1 1/4 cups vegetable broth",
                "1/4 cup extra virgin olive oil",
                "2 tbsp lemon juice",
                "1 clove garlic, minced",
                "1/2 cup cherry tomatoes, halved",
                "1/2 cup cucumber, diced",
                "1/4 cup Kalamata olives, pitted and sliced",
                "1/4 cup crumbled feta cheese",
                "2 tbsp chopped fresh parsley",
                "Salt and pepper to taste"
            ],
            "steps": [
                "In a saucepan, bring vegetable broth to a boil.",
                "Stir in couscous, cover, and remove from heat. Let stand for 5 minutes, then fluff with a fork.",
                "In a large bowl, whisk together olive oil, lemon juice, minced garlic, salt, and pepper.",
                "Add cooked couscous, cherry tomatoes, cucumber, Kalamata olives, crumbled feta cheese, and chopped parsley.",
                "Toss gently to combine.",
                "Serve chilled or at room temperature."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Stuffed Portobello Mushrooms",
            "cuisine": "Western",
            "meal": "Dinner",
            "allergens": ["Soy"],
            "ingredients": [
                "4 large portobello mushrooms",
                "1 cup cooked quinoa",
                "1 cup spinach, chopped",
                "1/2 cup sun-dried tomatoes, chopped",
                "1/2 cup crumbled goat cheese (or vegan cheese substitute)",
                "2 tbsp balsamic vinegar",
                "2 tbsp olive oil",
                "2 cloves garlic, minced",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Preheat oven to 375°F (190°C).",
                "Remove stems from mushrooms and gently scrape out gills using a spoon.",
                "In a bowl, mix cooked quinoa, chopped spinach, sun-dried tomatoes, goat cheese, balsamic vinegar, olive oil, garlic, salt, and pepper.",
                "Divide the quinoa mixture evenly among the mushrooms, filling each cap.",
                "Place stuffed mushrooms on a baking sheet lined with parchment paper.",
                "Bake for 20-25 minutes until mushrooms are tender and filling is heated through.",
                "Serve hot, optionally garnished with fresh parsley."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Quinoa-Stuffed Bell Peppers",
            "cuisine": "Western",
            "meal": "Dinner",
            "allergens": ["Soy"],
            "ingredients": [
                "4 large bell peppers, any color",
                "1 cup quinoa, cooked",
                "1 can (15 oz) black beans, drained and rinsed",
                "1 cup corn kernels",
                "1 cup diced tomatoes",
                "1 tsp cumin",
                "1 tsp chili powder",
                "Salt and pepper to taste",
                "1 cup shredded cheddar cheese (optional, omit for vegan)"
            ],
            "steps": [
                "Preheat oven to 375°F (190°C).",
                "Cut the tops off the bell peppers and remove seeds.",
                "In a large bowl, mix quinoa, black beans, corn, tomatoes, cumin, chili powder, salt, and pepper.",
                "Stuff the peppers with the quinoa mixture and place them in a baking dish.",
                "If using cheese, sprinkle it on top of each stuffed pepper.",
                "Cover with foil and bake for 30 minutes. Remove foil and bake for an additional 10 minutes until peppers are tender and cheese is melted.",
                "Serve hot."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetarian Chili",
            "cuisine": "Western",
            "meal": "Dinner",
            "allergens": ["Soy"],
            "ingredients": [
                "1 tbsp olive oil",
                "1 onion, chopped",
                "3 cloves garlic, minced",
                "1 bell pepper, chopped",
                "1 zucchini, diced",
                "1 cup corn kernels",
                "2 cans (15 oz each) black beans, drained and rinsed",
                "1 can (28 oz) diced tomatoes",
                "1 cup vegetable broth",
                "2 tbsp chili powder",
                "1 tsp cumin",
                "Salt and pepper to taste",
                "Chopped cilantro and lime wedges for serving"
            ],
            "steps": [
                "In a large pot, heat olive oil over medium heat.",
                "Add onion, garlic, bell pepper, and zucchini. Sauté until vegetables are softened.",
                "Stir in corn, black beans, diced tomatoes (with juices), vegetable broth, chili powder, cumin, salt, and pepper.",
                "Bring to a boil, then reduce heat and simmer for 20-25 minutes, stirring occasionally.",
                "Adjust seasoning if needed.",
                "Serve hot, garnished with chopped cilantro and lime wedges."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Caprese Pasta",
            "cuisine": "Western",
            "meal": "Dinner",
            "allergens": ["Soy"],
            "ingredients": [
                "12 oz pasta (penne or spaghetti)",
                "2 cups cherry tomatoes, halved",
                "8 oz fresh mozzarella balls (bocconcini), halved",
                "1/2 cup fresh basil leaves, torn",
                "3 tbsp balsamic vinegar",
                "3 tbsp olive oil",
                "2 cloves garlic, minced",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Cook pasta according to package instructions. Drain and set aside.",
                "In a large bowl, combine cherry tomatoes, mozzarella balls, and torn basil leaves.",
                "In a small bowl, whisk together balsamic vinegar, olive oil, minced garlic, salt, and pepper.",
                "Add cooked pasta to the tomato mixture. Pour the dressing over and toss gently to combine.",
                "Serve immediately, optionally garnished with additional basil leaves."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Classic Apple Crisp",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Soy"],
            "ingredients": [
                "6 cups apples, peeled, cored, and sliced",
                "1 tbsp lemon juice",
                "1/2 cup granulated sugar",
                "1 tsp ground cinnamon",
                "1/4 tsp ground nutmeg",
                "1 cup rolled oats",
                "1/2 cup all-purpose flour",
                "1/2 cup brown sugar",
                "1/2 cup butter, cold and diced",
                "Vanilla ice cream or whipped cream for serving (optional)"
            ],
            "steps": [
                "Preheat oven to 350°F (175°C).",
                "In a large bowl, toss apples with lemon juice, granulated sugar, cinnamon, and nutmeg.",
                "Spread apple mixture evenly in a greased baking dish.",
                "In another bowl, combine rolled oats, flour, brown sugar, and cold diced butter. Mix until crumbly.",
                "Sprinkle oat mixture over apples in the baking dish.",
                "Bake for 40-45 minutes until topping is golden brown and apples are tender.",
                "Serve warm, optionally topped with vanilla ice cream or whipped cream."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Chocolate Chip Cookies",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Soy"],
            "ingredients": [
                "1 cup butter, softened",
                "3/4 cup granulated sugar",
                "3/4 cup brown sugar, packed",
                "2 tsp vanilla extract",
                "2 eggs",
                "2 1/4 cups all-purpose flour",
                "1 tsp baking soda",
                "1/2 tsp salt",
                "2 cups chocolate chips"
            ],
            "steps": [
                "Preheat oven to 375°F (190°C).",
                "In a large bowl, cream together butter, granulated sugar, brown sugar, and vanilla extract until light and fluffy.",
                "Beat in eggs one at a time.",
                "Combine flour, baking soda, and salt; gradually add to creamed mixture and mix well.",
                "Stir in chocolate chips.",
                "Drop by rounded tablespoonfuls onto ungreased baking sheets.",
                "Bake for 9-11 minutes until edges are golden brown.",
                "Cool on baking sheets for 2 minutes before transferring to wire racks to cool completely."
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Vanilla Panna Cotta",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Soy"],
            "ingredients": [
                "1 cup heavy cream",
                "1 cup milk",
                "1/4 cup granulated sugar",
                "1 tsp vanilla extract",
                "2 tsp gelatin powder",
                "2 tbsp cold water",
                "Fresh berries for garnish"
            ],
            "steps": [
                "In a small bowl, sprinkle gelatin over cold water and let stand for 5 minutes to soften.",
                "In a saucepan, combine heavy cream, milk, sugar, and vanilla extract. Heat over medium heat until sugar dissolves and mixture is hot but not boiling.",
                "Remove from heat. Stir in softened gelatin until completely dissolved.",
                "Pour mixture into serving glasses or ramekins.",
                "Chill in the refrigerator for at least 4 hours or until set.",
                "Serve chilled, garnished with fresh berries."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Strawberry Shortcake",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Soy"],
            "ingredients": [
                "For the shortcakes:",
                "- 2 cups all-purpose flour",
                "- 1/4 cup granulated sugar",
                "- 1 tbsp baking powder",
                "- 1/2 tsp salt",
                "- 1/2 cup cold butter, cubed",
                "- 3/4 cup milk",
                "For the strawberries:",
                "- 4 cups fresh strawberries, sliced",
                "- 1/4 cup granulated sugar",
                "Whipped cream for serving"
            ],
            "steps": [
                "Preheat oven to 425°F (220°C).",
                "In a large bowl, combine flour, sugar, baking powder, and salt.",
                "Cut in cold butter until mixture resembles coarse crumbs.",
                "Stir in milk until dough forms a ball.",
                "Turn dough out onto a lightly floured surface. Knead gently 10 times.",
                "Roll or pat dough to 3/4-inch thickness. Cut with a floured 2 1/2-inch biscuit cutter.",
                "Place biscuits 2 inches apart on an ungreased baking sheet.",
                "Bake for 10-12 minutes until golden brown.",
                "Meanwhile, in a bowl, combine sliced strawberries and sugar. Let stand until juices are released.",
                "To serve, split warm shortcakes horizontally. Fill with strawberries and whipped cream. Replace tops and garnish with more strawberries."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Chocolate Mousse",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Shellfish"],
            "ingredients": [
                "6 oz semi-sweet chocolate, chopped",
                "1/4 cup unsalted butter",
                "3 eggs, separated",
                "1/4 cup granulated sugar",
                "1/2 tsp vanilla extract",
                "1/2 cup heavy cream",
                "Chocolate shavings or cocoa powder for garnish"
            ],
            "steps": [
                "Melt chocolate and butter in a heatproof bowl over simmering water, stirring until smooth. Remove from heat and let cool slightly.",
                "In a large bowl, beat egg yolks with granulated sugar until pale and thick.",
                "Stir in melted chocolate mixture and vanilla extract.",
                "In another bowl, whip heavy cream until stiff peaks form.",
                "Gently fold whipped cream into chocolate mixture.",
                "In a separate bowl, beat egg whites until stiff peaks form. Fold into chocolate mixture until no streaks remain.",
                "Spoon mousse into serving glasses or bowls. Chill for at least 2 hours.",
                "Before serving, garnish with chocolate shavings or dust with cocoa powder."
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Peach Cobbler",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Shellfish"],
            "ingredients": [
                "For the filling:",
                "- 6 cups sliced peaches (fresh or canned)",
                "- 1/2 cup granulated sugar",
                "- 2 tbsp cornstarch",
                "- 1 tsp vanilla extract",
                "- 1/4 tsp ground cinnamon",
                "For the topping:",
                "- 1 cup all-purpose flour",
                "- 1/4 cup granulated sugar",
                "- 1 1/2 tsp baking powder",
                "- 1/4 tsp salt",
                "- 1/2 cup unsalted butter, cold and diced",
                "- 1/4 cup boiling water"
            ],
            "steps": [
                "Preheat oven to 400°F (200°C).",
                "In a large bowl, toss sliced peaches with granulated sugar, cornstarch, vanilla extract, and ground cinnamon.",
                "Spread peach mixture evenly in a greased 9x13-inch baking dish.",
                "In another bowl, combine flour, granulated sugar, baking powder, and salt.",
                "Cut in cold diced butter until mixture resembles coarse crumbs.",
                "Stir in boiling water until mixture is just combined.",
                "Drop spoonfuls of dough over the peaches.",
                "Bake for 25-30 minutes until topping is golden brown and peaches are bubbly.",
                "Serve warm, optionally with vanilla ice cream."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vanilla Cupcakes",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Shellfish"],
            "ingredients": [
                "1 1/2 cups all-purpose flour",
                "1 1/2 tsp baking powder",
                "1/4 tsp salt",
                "1/2 cup unsalted butter, softened",
                "3/4 cup granulated sugar",
                "2 eggs",
                "1 tsp vanilla extract",
                "1/2 cup milk",
                "Frosting of your choice (optional)"
            ],
            "steps": [
                "Preheat oven to 350°F (175°C). Line a muffin tin with paper liners.",
                "In a bowl, whisk together flour, baking powder, and salt.",
                "In another bowl, cream together butter and granulated sugar until light and fluffy.",
                "Beat in eggs one at a time, then stir in vanilla extract.",
                "Gradually add dry ingredients to wet ingredients, alternating with milk, mixing until just combined.",
                "Divide batter evenly among muffin cups, filling each about 2/3 full.",
                "Bake for 18-20 minutes until a toothpick inserted into the center comes out clean.",
                "Cool in pan for 5 minutes, then transfer to a wire rack to cool completely.",
                "Once cooled, frost cupcakes if desired."
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Vegan Chocolate Cake",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Milk"],
            "ingredients": [
                "1 1/2 cups all-purpose flour",
                "1 cup granulated sugar",
                "1/4 cup cocoa powder",
                "1 tsp baking soda",
                "1/2 tsp salt",
                "1 cup brewed coffee, cooled",
                "1/3 cup vegetable oil",
                "1 tbsp white vinegar",
                "1 tsp vanilla extract"
            ],
            "steps": [
                "Preheat oven to 350°F (175°C). Grease and flour a 9x9-inch baking pan.",
                "In a large bowl, whisk together flour, sugar, cocoa powder, baking soda, and salt.",
                "Add cooled coffee, vegetable oil, vinegar, and vanilla extract. Mix until smooth and well combined.",
                "Pour batter into prepared pan.",
                "Bake for 30-35 minutes until a toothpick inserted into the center comes out clean.",
                "Cool completely on a wire rack before serving."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Fruit Salad with Honey-Lime Dressing",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Milk"],
            "ingredients": [
                "2 cups mixed fresh fruit (such as berries, grapes, melon)",
                "1 tbsp honey",
                "1 tbsp lime juice",
                "Fresh mint leaves for garnish"
            ],
            "steps": [
                "In a bowl, combine mixed fresh fruit.",
                "In a small bowl, whisk together honey and lime juice.",
                "Drizzle honey-lime dressing over fruit and toss gently to coat.",
                "Chill salad in the refrigerator for at least 30 minutes before serving.",
                "Garnish with fresh mint leaves before serving."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Coconut Macaroons",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Milk"],
            "ingredients": [
                "3 cups shredded coconut",
                "3/4 cup granulated sugar",
                "1/3 cup all-purpose flour",
                "1/4 tsp salt",
                "3 egg whites",
                "1 tsp vanilla extract"
            ],
            "steps": [
                "Preheat oven to 325°F (160°C). Line a baking sheet with parchment paper.",
                "In a bowl, combine shredded coconut, granulated sugar, flour, and salt.",
                "In another bowl, whisk egg whites until foamy.",
                "Stir in vanilla extract.",
                "Add egg white mixture to coconut mixture and mix until well combined.",
                "Drop spoonfuls of mixture onto prepared baking sheet.",
                "Bake for 20-25 minutes until edges are golden brown.",
                "Let cool on baking sheet for 5 minutes, then transfer to a wire rack to cool completely."
            ],
            "vegetarian": True,
            "eggs": True
        },
        {
            "name": "Pumpkin Pie",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Milk"],
            "ingredients": [
                "1 1/4 cups pumpkin puree",
                "1/2 cup brown sugar",
                "1 tsp ground cinnamon",
                "1/2 tsp ground ginger",
                "1/4 tsp ground nutmeg",
                "1/4 tsp salt",
                "1 cup coconut cream",
                "2 tbsp cornstarch",
                "1 9-inch pie crust (store-bought or homemade)"
            ],
            "steps": [
                "Preheat oven to 425°F (220°C). Place pie crust in a 9-inch pie dish and crimp edges as desired.",
                "In a bowl, whisk together pumpkin puree, brown sugar, cinnamon, ginger, nutmeg, and salt.",
                "In another bowl, whisk together coconut cream and cornstarch until smooth.",
                "Add coconut cream mixture to pumpkin mixture and whisk until well combined.",
                "Pour filling into pie crust.",
                "Bake for 15 minutes, then reduce oven temperature to 350°F (175°C).",
                "Continue baking for 40-45 minutes until filling is set and crust is golden brown.",
                "Cool completely on a wire rack before serving."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Mixed Berry Sorbet",
            "cuisine": "Western",
            "meal": "Dessert",
            "allergens": ["Milk"],
            "ingredients": [
                "4 cups mixed berries (such as strawberries, raspberries, blueberries)",
                "1/2 cup granulated sugar",
                "1/4 cup water",
                "1 tbsp lemon juice"
            ],
            "steps": [
                "In a saucepan, combine mixed berries, granulated sugar, and water.",
                "Bring to a boil, then reduce heat and simmer for 5-7 minutes until berries are soft.",
                "Remove from heat and let cool slightly.",
                "Puree berry mixture in a blender or food processor until smooth.",
                "Stir in lemon juice.",
                "Pour mixture through a fine mesh sieve to remove seeds, if desired.",
                "Chill mixture in the refrigerator for at least 2 hours.",
                "Transfer chilled mixture to an ice cream maker and churn according to manufacturer's instructions.",
                "Serve immediately as soft serve or transfer to a container and freeze for 2-3 hours for a firmer sorbet."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Thai Coconut Tapioca Pudding (Sago)",
            "cuisine": "Asian",
            "meal": "Dessert",
            "allergens": ["Milk"],
            "ingredients": [
                "1/2 cup small tapioca pearls (sago)",
                "4 cups coconut milk",
                "1/2 cup granulated sugar",
                "1/4 tsp salt",
                "Fresh fruits (such as mango, lychee) for topping"
            ],
            "steps": [
                "Soak tapioca pearls in water for 30 minutes, then drain.",
                "In a saucepan, bring coconut milk, sugar, and salt to a gentle boil.",
                "Add soaked tapioca pearls and simmer over low heat, stirring frequently, for 20-25 minutes until pearls are translucent and mixture thickens.",
                "Remove from heat and let cool slightly.",
                "Transfer to serving bowls and chill in the refrigerator until cold.",
                "Top with fresh fruits before serving."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Indian Mango Lassi Popsicles",
            "cuisine": "Asian",
            "meal": "Dessert",
            "allergens": ["Milk"],
            "ingredients": [
                "2 cups ripe mango chunks",
                "1 cup coconut milk yogurt",
                "1/4 cup granulated sugar or honey",
                "1/2 cup coconut milk",
                "1/2 tsp ground cardamom",
                "Sliced almonds for garnish (optional)"
            ],
            "steps": [
                "In a blender, combine mango chunks, coconut milk yogurt, sugar or honey, coconut milk, and ground cardamom.",
                "Blend until smooth and creamy.",
                "Pour mixture into popsicle molds.",
                "Insert popsicle sticks and freeze for at least 4 hours or until solid.",
                "To unmold, briefly run molds under warm water.",
                "Garnish with sliced almonds before serving."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetable Pad Thai",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": ["Shellfish"],
            "ingredients": [
                "8 oz rice noodles",
                "1/4 cup tamarind paste",
                "1/4 cup soy sauce",
                "2 tbsp brown sugar",
                "2 tbsp vegetable oil",
                "2 cloves garlic, minced",
                "1 block tofu, diced",
                "1 cup bean sprouts",
                "1 carrot, julienned",
                "1 bell pepper, sliced",
                "2 green onions, chopped",
                "1/4 cup peanuts, chopped",
                "Lime wedges for serving"
            ],
            "steps": [
                "Cook rice noodles according to package instructions, drain, and set aside.",
                "In a small bowl, whisk together tamarind paste, soy sauce, and brown sugar.",
                "In a large skillet or wok, heat vegetable oil over medium-high heat.",
                "Add minced garlic and diced tofu, stir-fry until tofu is golden brown.",
                "Add bean sprouts, julienned carrot, sliced bell pepper, and chopped green onions. Stir-fry for 3-4 minutes until vegetables are tender-crisp.",
                "Add cooked rice noodles and tamarind-soy sauce mixture to the skillet, toss to combine and heat through.",
                "Serve hot, garnished with chopped peanuts and lime wedges."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetarian Sushi Rolls",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": ["Shellfish"],
            "ingredients": [
                "3 nori seaweed sheets",
                "1 cup sushi rice, cooked",
                "1/2 cucumber, julienned",
                "1/2 avocado, sliced",
                "1/2 carrot, julienned",
                "1/2 bell pepper, sliced",
                "Pickled ginger and wasabi for serving"
            ],
            "steps": [
                "Place a nori seaweed sheet on a bamboo sushi mat, shiny side down.",
                "Spread cooked sushi rice evenly over the nori sheet, leaving a 1-inch border at the top.",
                "Arrange cucumber, avocado, carrot, and bell pepper strips in a line across the center of the rice.",
                "Using the bamboo mat, roll the sushi tightly from the bottom, applying gentle pressure.",
                "Moisten the top border of the nori sheet with water to seal the roll.",
                "Slice the sushi roll into bite-sized pieces using a sharp knife.",
                "Serve with pickled ginger and wasabi."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetarian Pho",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": ["Shellfish"],
            "ingredients": [
                "8 cups vegetable broth",
                "4 oz rice noodles",
                "1 block tofu, sliced",
                "1 onion, thinly sliced",
                "2 cloves garlic, minced",
                "1-inch piece ginger, sliced",
                "2 tbsp soy sauce",
                "1 tbsp hoisin sauce",
                "1 star anise",
                "1 cinnamon stick",
                "1 cup bean sprouts",
                "Fresh basil and lime wedges for serving"
            ],
            "steps": [
                "In a large pot, bring vegetable broth to a boil.",
                "Add rice noodles, tofu slices, sliced onion, minced garlic, ginger slices, soy sauce, hoisin sauce, star anise, and cinnamon stick.",
                "Reduce heat and simmer for 15-20 minutes until noodles are tender and flavors are infused.",
                "Remove star anise and cinnamon stick before serving.",
                "Divide pho into bowls, garnish with bean sprouts, fresh basil, and lime wedges.",
                "Serve hot."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetarian Summer Rolls with Peanut Sauce",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": ["Shellfish"],
            "ingredients": [
                "8 rice paper wrappers",
                "2 oz rice vermicelli noodles, cooked and cooled",
                "1/2 cucumber, julienned",
                "1 carrot, julienned",
                "1/2 bell pepper, thinly sliced",
                "1/2 cup fresh mint leaves",
                "1/2 cup fresh cilantro leaves",
                "1/2 cup lettuce leaves",
                "Peanut sauce for dipping"
            ],
            "steps": [
                "Fill a shallow dish with warm water.",
                "Dip one rice paper wrapper into the water for a few seconds until softened.",
                "Lay wrapper flat on a clean surface.",
                "Arrange rice vermicelli noodles, julienned cucumber, carrot, bell pepper, mint leaves, cilantro leaves, and lettuce leaves in the center of the wrapper.",
                "Fold sides of the wrapper over the filling, then roll tightly.",
                "Repeat with remaining ingredients.",
                "Serve vegetarian summer rolls with peanut sauce for dipping."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetarian Thai Papaya Salad (Som Tum)",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": [],
            "ingredients": [
                "1 small green papaya, peeled and julienned",
                "1 carrot, peeled and julienned",
                "1/2 cup cherry tomatoes, halved",
                "2 tbsp roasted peanuts, chopped",
                "2 cloves garlic, minced",
                "2 Thai bird's eye chilies, minced (optional)",
                "2 tbsp soy sauce",
                "1 tbsp palm sugar or brown sugar",
                "2 tbsp lime juice",
                "1 tbsp fish sauce substitute or soy sauce",
                "Fresh cilantro leaves for garnish"
            ],
            "steps": [
                "In a large mortar and pestle, pound garlic and Thai chilies together.",
                "Add palm sugar, soy sauce, lime juice, and fish sauce substitute. Mix well.",
                "Add julienned green papaya and carrot. Gently pound to soften the vegetables and absorb flavors.",
                "Add cherry tomatoes and chopped roasted peanuts. Toss gently to combine.",
                "Transfer to a serving plate, garnish with fresh cilantro leaves.",
                "Serve immediately."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Vegetarian Japanese Ramen",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": [],
            "ingredients": [
                "4 cups vegetable broth",
                "2 servings ramen noodles",
                "1 block tofu, sliced and pan-fried",
                "1 cup mixed mushrooms (shiitake, oyster), sliced",
                "1 cup baby bok choy, chopped",
                "2 tbsp soy sauce",
                "1 tbsp miso paste",
                "1 tsp sesame oil",
                "Green onions and sesame seeds for garnish"
            ],
            "steps": [
                "In a large pot, bring vegetable broth to a boil.",
                "Add ramen noodles and cook according to package instructions.",
                "Add sliced tofu, mixed mushrooms, and chopped baby bok choy.",
                "In a small bowl, mix soy sauce, miso paste, and sesame oil. Stir into the broth.",
                "Simmer for 5-7 minutes until vegetables are tender.",
                "Serve hot, garnished with green onions and sesame seeds."
            ],
            "vegetarian": True,
            "eggs": False
        },
        {
            "name": "Thai Basil Chicken",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": [],
            "ingredients": [
                "1 lb boneless chicken thighs, chopped",
                "2 tbsp soy sauce",
                "1 tbsp oyster sauce",
                "1 tbsp fish sauce",
                "1 tbsp brown sugar",
                "2 tbsp vegetable oil",
                "4 cloves garlic, minced",
                "1 onion, sliced",
                "1 bell pepper, sliced",
                "1 cup fresh Thai basil leaves",
                "Cooked rice for serving"
            ],
            "steps": [
                "In a bowl, mix soy sauce, oyster sauce, fish sauce, and brown sugar.",
                "Heat vegetable oil in a large skillet or wok over medium-high heat.",
                "Add minced garlic and chopped chicken thighs, stir-fry until chicken is cooked through.",
                "Add sliced onion and bell pepper, stir-fry for another 3-4 minutes until vegetables are tender-crisp.",
                "Stir in fresh Thai basil leaves and the soy sauce mixture. Toss everything together until basil wilts.",
                "Serve hot over cooked rice."
            ],
            "vegetarian": False,
            "eggs": False
        },
        {
            "name": "Pork Ramen",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": [],
            "ingredients": [
                "4 cups pork or chicken broth",
                "2 servings ramen noodles",
                "1/2 lb pork belly or pork loin, thinly sliced",
                "2 soft-boiled eggs, halved",
                "1 cup mixed mushrooms (shiitake, enoki)",
                "1 cup baby bok choy, chopped",
                "2 tbsp soy sauce",
                "1 tbsp miso paste",
                "1 tsp sesame oil",
                "Green onions and nori sheets for garnish"
            ],
            "steps": [
                "In a large pot, bring pork or chicken broth to a boil.",
                "Add ramen noodles and cook according to package instructions.",
                "In a separate skillet, cook thinly sliced pork belly until browned and cooked through.",
                "Add mixed mushrooms and chopped baby bok choy to the boiling broth.",
                "In a small bowl, mix soy sauce, miso paste, and sesame oil. Stir into the broth.",
                "Simmer for 5-7 minutes until vegetables are tender and flavors are infused.",
                "Serve hot, topped with sliced pork, soft-boiled eggs, green onions, and nori sheets."
            ],
            "vegetarian": False,
            "eggs": True
        },
        {
            "name": "Beef Bulgogi Bowl",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": [],
            "ingredients": [
                "1 lb beef sirloin or flank steak, thinly sliced",
                "1/2 cup soy sauce",
                "3 tbsp brown sugar",
                "2 tbsp sesame oil",
                "3 cloves garlic, minced",
                "1 inch ginger, grated",
                "1 onion, thinly sliced",
                "2 green onions, chopped",
                "2 cups cooked rice",
                "Sesame seeds for garnish"
            ],
            "steps": [
                "In a bowl, mix soy sauce, brown sugar, sesame oil, minced garlic, and grated ginger.",
                "Marinate thinly sliced beef in the mixture for 30 minutes.",
                "Heat a large skillet or grill pan over medium-high heat.",
                "Add marinated beef slices and thinly sliced onion. Stir-fry or grill until beef is cooked and caramelized.",
                "Serve hot over cooked rice, garnished with chopped green onions and sesame seeds."
            ],
            "vegetarian": False,
            "eggs": False
        },
        {
            "name": "Shrimp Pad Thai",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": [],
            "ingredients": [
                "8 oz rice noodles",
                "1/2 lb shrimp, peeled and deveined",
                "1/4 cup soy sauce",
                "2 tbsp fish sauce",
                "2 tbsp tamarind paste",
                "2 tbsp brown sugar",
                "2 tbsp vegetable oil",
                "2 cloves garlic, minced",
                "2 eggs, beaten",
                "1 cup bean sprouts",
                "1/2 cup chopped peanuts",
                "Lime wedges for serving"
            ],
            "steps": [
                "Cook rice noodles according to package instructions, drain, and set aside.",
                "In a small bowl, mix soy sauce, fish sauce, tamarind paste, and brown sugar.",
                "Heat vegetable oil in a large skillet or wok over medium-high heat.",
                "Add minced garlic and shrimp, stir-fry until shrimp turns pink and cooked.",
                "Push shrimp to one side of the skillet, pour beaten eggs into the other side. Scramble eggs until cooked.",
                "Add cooked rice noodles, soy sauce mixture, bean sprouts, and chopped peanuts to the skillet. Toss everything together.",
                "Serve hot, garnished with lime wedges."
            ],
            "vegetarian": False,
            "eggs": True
        },
        {
            "name": "Chicken Teriyaki Stir-Fry",
            "cuisine": "Asian",
            "meal": "Lunch",
            "allergens": [],
            "ingredients": [
                "1 lb boneless chicken breast, sliced",
                "1/4 cup soy sauce",
                "2 tbsp honey",
                "1 tbsp rice vinegar",
                "1 tbsp sesame oil",
                "2 cloves garlic, minced",
                "1 inch ginger, minced",
                "1 onion, sliced",
                "1 bell pepper, sliced",
                "1 cup broccoli florets",
                "2 cups cooked rice",
                "Salt and pepper to taste",
                "Green onions for garnish"
            ],
            "steps": [
                "In a bowl, mix soy sauce, honey, rice vinegar, sesame oil, minced garlic, and minced ginger.",
                "Marinate sliced chicken breast in the mixture for 20 minutes.",
                "Heat a large skillet or wok over medium-high heat.",
                "Add marinated chicken slices and stir-fry until cooked through.",
                "Add sliced onion, bell pepper, and broccoli florets. Stir-fry for another 3-4 minutes until vegetables are tender-crisp.",
                "Season with salt and pepper.",
                "Serve hot over cooked rice, garnished with green onions."
            ],
            "vegetarian": False,
            "eggs": False
        },
        {
            "name": "Classic Club Sandwich",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": [],
            "ingredients": [
                "3 slices of bread (toasted)",
                "3 slices cooked bacon",
                "2 slices cooked turkey breast",
                "1 leaf lettuce",
                "2 slices tomato",
                "Mayonnaise",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Spread mayonnaise on one side of each toasted bread slice.",
                "Layer one slice of bread with lettuce, tomato slices, and one slice of turkey.",
                "Place another slice of toasted bread on top, mayo side down.",
                "Layer with bacon slices and the remaining turkey.",
                "Top with the third slice of toasted bread, mayo side down.",
                "Cut the sandwich into halves or quarters. Secure with toothpicks if necessary.",
                "Serve immediately."
            ],
            "vegetarian": False,
            "eggs": False
        },
        {
            "name": "Classic Club Sandwich",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": [],
            "ingredients": [
                "3 slices of bread (toasted)",
                "3 slices cooked bacon",
                "2 slices cooked turkey breast",
                "1 leaf lettuce",
                "2 slices tomato",
                "Mayonnaise",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Spread mayonnaise on one side of each toasted bread slice.",
                "Layer one slice of bread with lettuce, tomato slices, and one slice of turkey.",
                "Place another slice of toasted bread on top, mayo side down.",
                "Layer with bacon slices and the remaining turkey.",
                "Top with the third slice of toasted bread, mayo side down.",
                "Cut the sandwich into halves or quarters. Secure with toothpicks if necessary.",
                "Serve immediately."
            ],
            "vegetarian": False,
            "eggs": False
        },
        {
            "name": "Beef Burger with Caramelized Onions",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": [],
            "ingredients": [
                "1/2 lb ground beef",
                "1 burger bun (toasted)",
                "1/2 onion, thinly sliced",
                "1 tbsp butter",
                "1 slice cheddar cheese",
                "Lettuce leaves",
                "Tomato slices",
                "Ketchup and mustard",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Form ground beef into a patty, season with salt and pepper.",
                "Heat butter in a skillet over medium heat.",
                "Add thinly sliced onions and cook until caramelized, about 15 minutes.",
                "Grill or pan-fry the beef patty until cooked to desired doneness.",
                "Top with cheddar cheese slice to melt.",
                "Assemble burger with toasted bun, lettuce leaves, tomato slices, caramelized onions, ketchup, and mustard.",
                "Serve hot."
            ],
            "vegetarian": False,
            "eggs": False
        },
        {
            "name": "Beef Burger with Caramelized Onions",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": [],
            "ingredients": [
                "1/2 lb ground beef",
                "1 burger bun (toasted)",
                "1/2 onion, thinly sliced",
                "1 tbsp butter",
                "1 slice cheddar cheese",
                "Lettuce leaves",
                "Tomato slices",
                "Ketchup and mustard",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Form ground beef into a patty, season with salt and pepper.",
                "Heat butter in a skillet over medium heat.",
                "Add thinly sliced onions and cook until caramelized, about 15 minutes.",
                "Grill or pan-fry the beef patty until cooked to desired doneness.",
                "Top with cheddar cheese slice to melt.",
                "Assemble burger with toasted bun, lettuce leaves, tomato slices, caramelized onions, ketchup, and mustard.",
                "Serve hot."
            ],
            "vegetarian": False,
            "eggs": False
        },
        {
            "name": "Chicken Caesar Salad",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": ["Dairy"],
            "ingredients": [
                "2 cups Romaine lettuce, chopped",
                "1 boneless chicken breast, grilled and sliced",
                "1/4 cup Caesar dressing",
                "1/4 cup croutons",
                "2 tbsp grated Parmesan cheese",
                "Salt and pepper to taste"
            ],
            "steps": [
                "In a large bowl, toss chopped Romaine lettuce with Caesar dressing.",
                "Add grilled and sliced chicken breast.",
                "Sprinkle with croutons and grated Parmesan cheese.",
                "Season with salt and pepper.",
                "Toss gently to combine.",
                "Serve immediately."
            ],
            "vegetarian": False,
            "eggs": False
        },
        {
            "name": "Pasta Carbonara",
            "cuisine": "Western",
            "meal": "Lunch",
            "allergens": ["Dairy", "Eggs"],
            "ingredients": [
                "8 oz spaghetti",
                "4 slices bacon, diced",
                "2 cloves garlic, minced",
                "2 eggs",
                "1/2 cup grated Parmesan cheese",
                "Salt and pepper to taste",
                "Chopped parsley for garnish"
            ],
            "steps": [
                "Cook spaghetti according to package instructions, drain and set aside.",
                "In a skillet, cook diced bacon until crispy. Add minced garlic and sauté until fragrant.",
                "In a bowl, whisk together eggs and grated Parmesan cheese.",
                "Add cooked spaghetti to the skillet with bacon and garlic. Toss to combine.",
                "Remove from heat and quickly stir in egg mixture, tossing continuously to coat the pasta.",
                "Season with salt and pepper. Garnish with chopped parsley.",
                "Serve immediately."
            ],
            "vegetarian": False,
            "eggs": True
        }

    ]

    return recipes
