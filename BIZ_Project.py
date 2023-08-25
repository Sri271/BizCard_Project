BIZ_Project

import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import easyocr
import sqlite3
from PIL import Image
import cv2
import os
import matplotlib.pyplot as plt
import re

# Setting Page Configuration
icon = Image.open("C:/Users/BALAVIGNESH S S/OneDrive/Desktop/PROJECT 3/icon.png")
st.set_page_config(page_title="BizCardX: Extracting Business Card Data with OCR | By BALAVIGNESH S S",
                   page_icon= icon,
                   layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items={'About': """# This OCR app is created by *BALAVIGNESH S S*!"""})
st.markdown("<h1 style='text-align: center; color: blue;'>BizCardX: Extracting Business Card Data with OCR</h1>",
            unsafe_allow_html=True)