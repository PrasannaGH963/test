import streamlit as st

# Set the background image using HTML and CSS
background_image = "your_image_url.jpg"  # Replace with the URL or local path of your image

# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.markdown("""
<div style="position:fixed;bottom:0;left:0;right:0;padding:10px;background-color:rgba(0,0,0,0.5);text-align:center;color:rgba(255,255,255,0.5);font-size:12px;">
Hosted with Streamlit
</div>
""", unsafe_allow_html=True)



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
