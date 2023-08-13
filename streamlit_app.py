import streamlit as st 
from PIL import Image 

st.set_page_config(page_title = 'Analytics Data Challenge' , page_icon = ':brain:')
st.title('Analytics Data Challenge :brain: ')

brand_analysis_file = '/Analysis/brand_related_data_analysis.ipynb'
campaign_analysis_file = '/Analysis/campaign_related_data_analysis.ipynb'
image_file = 'Data Viz/powerbi_dashboard_png.png'

st.header("Purpose ")
st.write("The main purpose of this exercise is to look at raw data provided in an excel file, analyze the data and come up with a visualization along with patterns in the data. The data is a record of Brands that have signed up on OpenSponsorship during a particular period of time along with some brands’ demographic and behavioral attributes. Some of those brands upgraded to a paid subscription (planLevel > 0) but most didn’t. As the data analyst at OpenSponsorship, you need to explore the dataset, analyze the underlying trends, and come up with some possible factors that lead to the customer success (subscription!) AND also the possible factors that prevent them from upgrading to a paid subscription. ")


st.header("I did some analysis based on the challenge 👨‍💻 ")
st.write("You can downloads the files using below links !")
st.download_button(label = "Download brand analysis" ,file_name= 'Brand_analysis.ipynb' , data= brand_analysis_file)
st.download_button(label = "Download campaign analysis" , file_name = 'Campaign_analysis.ipynb' , data = campaign_analysis_file)


st.header("Here is the PowerbI Dashboard PNG 📶 ")

IMAGE_FILE = Image.open(image_file)

st.image(image = IMAGE_FILE , caption = "PowerBI Dashboard")