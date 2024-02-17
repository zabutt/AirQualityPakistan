import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Clean Air For Pakistan')

# Add an expandable section with multiple subsections
with st.expander('More Information'):
    # Add an "About" subsection
    st.markdown('### About The Project')
    st.write('This project is an interactive visualization of air quality data for cities in Pakistan. The goal of this project is to provide an accessible and informative way for people to explore air quality data and learn more about public policies.')

    # Add a subsection on air quality in India
    st.markdown('### Air Quality in India')
    st.write('Air quality in Pakistan is a vital issue due to its severe health impacts, including respiratory diseases and increased healthcare costs, economic productivity losses, and environmental degradation. Also, India\'s commitment to global agreements and the interconnectedness of air pollution and climate change underline the urgency of improving air quality.\n\nUrbanization, industrialization, and regulatory needs demand attention. Enhancing air quality ensures better quality of life, sustains long-term development, and fosters a healthier population. Despite progress, sustained efforts are crucial to mitigate the broad spectrum of issues stemming from poor air quality.')

    # Add a subsection on the source code
    st.markdown('### Clean Air for Pakistan')
    st.write('By providing accessible air quality information, we aim to enhance awareness and create a way for people to collaborate effectively. This approach fosters informed actions, empowering individuals to collectively contribute to improving air quality and aligns with the website\'s focus on enhancing public engagement for cleaner air.')

    # Add a subsection on the source code
    st.markdown('### Source Code')
    st.write('The source code for this project is written in Python and uses the Streamlit and Plotly libraries to create a web-based user-friendly interface. The code is available on GitHub: https://github.com/hsheikh7/Streamlit_Projects.')

    # Add a subsection on the source code
    st.markdown('### Data')
    st.write('The data originates from "Air Quality Data in India (2015 - 2020)" available at: https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india?select=city_day.csv')

# Load the air quality dataset
