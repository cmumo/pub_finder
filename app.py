import streamlit as st
import pandas as pd


# Step 1: Load the dataset

df = pd.read_csv('openpubs_cleaned.csv')

# Step 2: Create the web application
def main():
    st.title("Hello, trying to find a pub nearby?")


    # Page 1: Home Page
    st.subheader("If you are trying to find a nearby pub but Google Maps is not working, dont worry we got you covered.")
    st.subheader("Dataset Information:")
    st.write("Number of pubs around:", len(df))
    st.balloons()
    
    st.subheader("Click on the Pub Locations button to see and find for pubs around. Enjoy.")

if __name__ == "__main__":
    main()
