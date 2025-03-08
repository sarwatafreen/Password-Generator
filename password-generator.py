import streamlit as st
import random
import string
def generate_password(length,use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
     characters += string.punctuation # add special characters (!,@,#,$,%,^,&,*,)
                        
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit App
st.title("🔑 Password Generator")

# Password Length
length = st.slider("Length of password", min_value=6, max_value=32, value=12)

# Options to include digits and special characters
use_digits = st.checkbox("Include Digits (0-9)")
use_special = st.checkbox("Include Special Characters (!@#$%^&*)")

# Generate Password Button
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"🔐 **Generated Password:** 💖`{password}`")
    st.write("---")
    st.write("⚠️ **Copy the password and store it in a safe place!**")





#   st.title("🔑Password Generator")
                    
#   length = st.slider("Length of password", min_value=6, max_value=32, value=12)
                    
#   use_digits = st.checkbox("Include Digits")
                    
#   use_special = st.checkbox("Include Special Characters")
                    
#     if st.button("Generate Password"):
#         password = generate_password(length, use_digits, use_special)
#         st.write(f"Generated Password: `{password}`")
                    
#         st.write("-------------------------------------")
                    
#         st.write("Copy the password and store it in a safe place")



             