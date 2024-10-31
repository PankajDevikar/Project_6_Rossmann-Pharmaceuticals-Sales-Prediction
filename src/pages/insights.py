import streamlit as st
import awesome_streamlit as ast

def write():
    """Used to write the page in the app.py file"""
    st.title('Insights from the Historical Data')
    
    st.write('---')
    st.markdown('## StoreType vs Sales and Customers')
    st.image("./src/images/a.png", caption="StoreType vs Sales and Customers")
    st.write('The most selling and crowded store type is b.')

    st.write('---')
    st.markdown('## Assortment vs Sales and Customers')
    st.image("./src/images/b.png", caption="Assortment vs Sales and Customers")
    st.write('The most selling and crowded assortment is b.')

    st.write('---')
    st.markdown('## Open vs DayOfWeek')
    st.image("./src/images/c.png", caption="Open vs DayOfWeek")
    st.write('Most of the stores are closed on Sundays but almost every store is open on Saturday.')

    st.write('---')
    st.markdown('## CompetitionDistance vs Sales')
    st.image("./src/images/d.png", caption="Competition Distance vs Sales")
    st.markdown("""
            Stores with the smallest competition distance have the highest sales. This indicates that the
            stores are located in city centers or near hospitals. Although having large distances between
            competitors is ideally considered good for sales, stores located in city centers will still achieve
            more sales regardless of competitors' distance due to higher customer density in these areas.
        """)

    st.write('---')
    st.markdown('## Correlation Analysis')
    st.image("./src/images/e.png", caption="Correlation Analysis")
    st.write('Sales is highly correlated to customers.')

    st.write('---')
    st.markdown('## Monthly Sales per StoreType and Promo')
    st.image("./src/images/f.png", caption="Monthly Sales per StoreType and Promo")

    st.write('---')
    st.markdown('## Monthly Sales per Assortment and Promo')
    st.image("./src/images/g.png", caption="Monthly Sales per Assortment and Promo")
    st.markdown("""
            For all stores, promotions lead to increases in Sales and Customers. However, promotions have 
            less impact on store type B and assortment B compared to other types and assortments. 
            Therefore, promotions should be targeted more toward other store types and assortments.
        """)

    st.write('---')
    st.markdown('## Sales of Stores Open per DayOfWeek and StoreType')
    st.image("./src/images/h.png", caption="Sales of Stores Open per DayOfWeek and StoreType")
    st.write('Store type B is the most frequently open store type on all weekdays, with its highest sales on Sundays.')

    st.write('---')
    st.markdown('## Sales of Stores Open per DayOfWeek and Assortment')
    st.image("./src/images/i.png", caption="Sales of Stores Open per DayOfWeek and Assortment")
    st.write('Assortments A and B are the most frequently open on all weekdays, with their highest sales on Sundays.')

    st.write('---')
    st.markdown('## Sales Before, During, and After Christmas')
    st.image("./src/images/j.png", caption="Sales Before, During, and After Christmas")
    st.markdown("""
            Sales increase during the Christmas season, especially in the week leading up to Christmas. 
            This is possibly due to customers buying beauty products or common medicines for precaution 
            during holiday celebrations.
        """)
