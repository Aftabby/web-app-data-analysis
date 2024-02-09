import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
                        # -- streamlit.io  -- is an open source python library that makes it easy to create and share custom webapps for machine learning and data science
                            # TO instal use -- pip install stramlit -- 


# ==============  Deploying WebApp locally for EDA (Exploratory Data Analysis) using streamlit  ====


#Title and subheader
st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")



#Upload Dataset
upload = st.file_uploader("Upload Your Dataset (In CSV Format)")
print(type(upload))

if upload is not None:
    df1 = pd.read_csv(upload)



#Show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(df1.head())
        if st.button("Tail"):
            st.write(df1.tail())



#Check DataType of Each Column
if upload is not None:
    if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(df1.dtypes)



#Find Shape of Our Dataset (Num of rows and columns)
if upload is not None:
    data_shape = st.radio("What Dimension Do You Want to Check?", ("Rows", "Columns"))

    if data_shape == "Rows":
        st.text("Number of Rows")
        st.write(df1.shape[0])
    elif data_shape == "Columns":
        st.text("Number of Columns")
        st.write(df1.shape[1])



#Find Null Values in the Dataset
if upload is not None:
    check_null = df1.isnull().values.any()      # -- any() -- method works on numpy array, if any value is True it will return True otherwise False, we converted the dataframe_object to numpy arrays by using -- .values -- attribute
    if check_null:
        st.text("N.B: There is Null values in the dataset.")
        if st.checkbox("Show the Null Values in the graph"):
            fig, ax = plt.subplots(figsize=(10, 5))            # - plt.subplots() - is a function in matplotlib that creates a new figure and set of subplots (axes). This function returns a figure object and a single axis or an array of axes, depending on the parameters you pass in.The figure is like a canvas that holds the plots, while the axes are the actual plots. You can think of the figure as a window, and the axes as individual plots within that window.By using plt.subplots(), you can create multiple plots in the same figure, arrange them in a grid, and control their individual properties.
            sns.heatmap(df1.isnull(), ax=ax)            #The - ax - argument in Seaborn functions is used to specify the matplotlib axes where the plot will be drawn. When you create a plot, you can specify the ax argument to tell Seaborn where to draw the plot.
            plt.tight_layout()                          #Stops cropping when you change the figure size
            st.pyplot(fig)                             #When you create a plot using matplotlib/seaborn, you can use streamlit.pyplot() to display that plot in your Streamlit app. It's similar to calling plt.show() in a traditional Python script, but instead of opening a new window with the plot, it embeds the plot in the Streamlit app's user interface.
                                                            #The -- fig -- argument typically refers to a Figure object in matplotlib            
    else:
        st.success("N.B: There is no null values in the dataset.")




#Find Duplicate Values in the dataset
if upload is not None:
    test = df1.duplicated().any()
    if test:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup = st.selectbox("Do You Want to Remove Duplicate Values?", ("Select One", "Yes", "No"))
        
        if dup == "Yes":
            df1 = df1.drop_duplicates()
            st.success("Duplicate Values are Removed")
        
        if dup == "No":
            st.text("Okay!")



#Get Overall Statistics
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(df1.describe(include="all"))



#About Section
if st.button("About App"):
    st.text("Built by Aftab Uddin")


#Bye
if st.checkbox("Bye"):
    st.success("Visit: www.Aftabby.com")