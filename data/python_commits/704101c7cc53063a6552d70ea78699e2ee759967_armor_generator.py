import streamlit as st

# App Title
st.title("Custom Armor Generator")
st.subheader("Design your own armor and create AI prompts for it.")

# Sidebar for Armor Customization
st.sidebar.header("Customize Your Armor")

# Under Armor Options
under_armor = st.sidebar.selectbox(
    "Under Armor (Base Layer)", 
    ["None", "Simple Tunic", "Quilted Gambeson", "Richly Embroidered Gambeson", "Chainmail Hauberk"]
)

# Over Armor Options
over_armor = st.sidebar.multiselect(
    "Over Armor (Accessories)", 
    ["None", "Hooded Cloak", "Flowing Cape", "Heraldic Surcoat", "Fur-Lined Mantle"]
)

# Armor Material
armor_material = st.sidebar.selectbox(
    "Armor Material", 
    ["Steel", "Bronze", "Gold", "Blackened Iron"]
)

# Engraving Style
engraving_style = st.sidebar.selectbox(
    "Engraving Style", 
    ["None", "Floral", "Runes", "Geometric"]
)

# Color Customization
st.sidebar.header("Color Customizations")
base_layer_color = st.sidebar.color_picker("Base Layer Color (Tunic/Gambeson)", "#B87333")
armor_accent_color = st.sidebar.color_picker("Armor Accent Color", "#FFD700")
cloak_color = st.sidebar.color_picker("Cloak or Cape Color", "#5B84B1")

# Generate Prompt
st.header("Generated AI Prompt")

prompt = f"A warrior clad in {armor_material.lower()} armor. "
if under_armor != "None":
    prompt += f"Underneath, they wear a {under_armor.lower()} dyed {base_layer_color}. "
if over_armor and "None" not in over_armor:
    prompt += f"Over the armor, they wear {', '.join(over_armor).lower()}, dyed {cloak_color}. "
prompt += f"The armor features {engraving_style.lower()} engravings and accents of {armor_accent_color}."

st.write(prompt)

# Color Preview
st.header("Color Preview")
st.write("Base Layer Color:")
st.color_picker("Preview Base Layer", base_layer_color, key="preview_base")
st.write("Armor Accent Color:")
st.color_picker("Preview Armor Accents", armor_accent_color, key="preview_accent")
if "None" not in over_armor:
    st.write("Cloak or Cape Color:")
    st.color_picker("Preview Cloak", cloak_color, key="preview_cloak")

# Next Steps Placeholder
st.header("Next Steps")
st.write("In the next phase, we will integrate AI image generation to visualize your armor.")