# imports
import streamlit as st
import pandas as pd

def write():
    """Used to write the page in the app.py file"""
    st.title('Data Description')

    # Description of Data Fields
    st.markdown("""
    Most of the data fields are straightforward, but here are some key features to highlight:
    - **Store, Date, Sales, Customers, Open, State Holiday, School Holiday, Store Type, Assortment, Competition, and Promotion.**
    - The **Store Type, Assortment, Competition,** and **Promotion** features are store-specific.
    - The **Sales, Customers, Open, State Holiday,** and **School Holiday** features vary across stores and over time.
    """)

    # Load CSVs with custom NA values and error handling
    na_values = ['', ' ', 'nan', 'Nan', 'NaN', 'na', '<Na>']
    try:
        train = pd.read_csv('src/data/train.csv', na_values=na_values)
        store = pd.read_csv('src/data/store.csv', na_values=na_values)
        
        # Merge train and store data on 'Store' column
        full_train = pd.merge(left=train, right=store, how='inner', on='Store')
        full_train = full_train.set_index('Store')
        
        # Display Data Samples
        st.write('---')
        st.subheader('Sample Stores Data')
        st.dataframe(store.head(20))  # Interactive display

        st.write('---')
        st.subheader('Sample Historical Data (Sales and Customers)')
        st.dataframe(train.sample(20))  # Interactive display

        st.write('---')
        st.subheader('Sample Training Data with Input Features')
        st.dataframe(full_train.sample(20))  # Interactive display
        
    except FileNotFoundError as e:
        st.error(f"Error loading data: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
