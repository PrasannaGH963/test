import streamlit as st

# Set the background image using HTML and CSS
background_image = "your_image_url.jpg"  # Replace with the URL or local path of your image

# Define custom CSS with the background image
# custom_css = f"""
#     <style>
#         body {{
#             background-image: url('{background_image}');
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#         }}
#     </style>
# """
st.button("button")
# Apply the custom CSS using st.markdown
# st.markdown(custom_css, unsafe_allow_html=True)

# Rest of your Streamlit app code
st.title("My Streamlit App")
st.write("Welcome to my app!")
