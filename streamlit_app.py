import streamlit as st

from recipes import get_recipes


st.set_page_config(page_title="Recipe Recommendation", page_icon="🍲", layout="wide")

st.title("🍲 Recipe Recommendation")
st.write("Explore recipes by diet, cuisine, and meal preference.")
st.warning(
    "Allergen tags come from the source recipe data and may be incomplete or incorrect. "
    "Do not rely on this app to determine whether a recipe is safe for an allergy. "
    "Check every ingredient and confirm preparation details with the cook or manufacturer."
)

recipes = get_recipes()
allergen_options = ["Peanuts", "Shellfish", "Soy", "Eggs"]

with st.sidebar:
    st.header("Your preferences")
    allergies = st.multiselect(
        "Allergies to avoid",
        allergen_options,
        help="Recipes tagged with any selected allergen will be excluded.",
    )
    diet = st.radio("Diet", ["Vegetarian", "Non-vegetarian"], horizontal=False)
    eats_eggs = True
    if diet == "Vegetarian":
        eats_eggs = st.radio("Do you eat eggs?", ["Yes", "No"], horizontal=True) == "Yes"

    cuisines = sorted({recipe["cuisine"] for recipe in recipes})
    meals = sorted({recipe["meal"] for recipe in recipes})
    cuisine = st.selectbox("Cuisine", cuisines)
    meal = st.selectbox("Meal", meals)

matches = []
for recipe in recipes:
    if recipe["cuisine"] != cuisine or recipe["meal"] != meal:
        continue
    if any(allergen in recipe["allergens"] for allergen in allergies):
        continue
    if diet == "Vegetarian" and not recipe.get("vegetarian", False):
        continue
    if diet == "Vegetarian" and not eats_eggs and recipe.get("eggs", False):
        continue
    matches.append(recipe)

st.subheader(f"{len(matches)} recipe{'s' if len(matches) != 1 else ''} found")
if not matches:
    st.info("No recipes match these choices. Try changing your filters.")
else:
    for recipe in matches:
        with st.container(border=True):
            st.subheader(recipe["name"])
            st.caption(f"{recipe['cuisine']} · {recipe['meal']}")
            if recipe["allergens"]:
                st.write("**Tagged allergens:** " + ", ".join(recipe["allergens"]))
            else:
                st.write("**Tagged allergens:** None")
            left, right = st.columns(2)
            with left:
                st.markdown("**Ingredients**")
                for ingredient in recipe["ingredients"]:
                    st.markdown(f"- {ingredient}")
            with right:
                st.markdown("**Method**")
                for step_number, step in enumerate(recipe["steps"], start=1):
                    st.markdown(f"{step_number}. {step}")

