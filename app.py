import plotly.express as px
from database_helper import DataBaseHelper
import streamlit as st

st.title("Restaurant Insights Hub")
date = st.date_input("Select a date")
database = DataBaseHelper()

restaurant_fig = None
time_slots_fig = None
orders_fig = None
payment_method_fig = None
rating_fig = None
cusine_fig = None

if st.button("Restaurant-wise sales chart"):
    hotel_name, sales_amount = database.get_sales(date)

    custom_colors = ['#1F77B4']
    restaurant_fig = px.bar(x=hotel_name, y=sales_amount, title='Restaurant-wise sales',
                            labels={'x': 'Restaurant Names', 'y': 'Sales Amount'},
                            color_discrete_sequence=custom_colors, text_auto='.2s')

if st.button("Sales by time slots chart"):
    time_slots, sales = database.get_sales_per_time_slots(date)

    custom_colors = ['#FF5733']
    time_slots_fig = px.bar(x=time_slots, y=sales, title='Sales by time slots',
                            labels={'x': 'Time Slots', 'y': 'Sales Amount'},
                            color_discrete_sequence=custom_colors, text_auto='.2s')

if st.button("Total orders sales by restaurants chart"):
    hotel_name, total_orders = database.get_order_sold_count(date)

    orders_fig = px.pie(values=total_orders, names=hotel_name, title='Total orders sale by restaurants')

if st.button("Types of payment methods used chart"):
    payment_type, amount = database.get_payment(date)

    payment_method_fig = px.pie(values=amount, names=payment_type, title='Types of payment methods used')
    
if st.button("Rating of different resturants chart"):
    resturant_name, resturant_rating  = database.get_resturant_ratings(date)
    custom_colors = ['#1F77B4']
    rating_fig = px.bar(x=resturant_name, y=resturant_rating, title="Today's Rating of different resturants",
                        labels={'x': 'Resturant Name', 'y': 'Resturant Rating'},
                        color_discrete_sequence=custom_colors, text_auto='.2s')
    
if st.button("Most selling cusine chart"):
    cuisine, count = database.get_cusine_sold(date)
    custom_colors = ['#FF5733']
    cusine_fig = px.bar(x=cuisine, y=count, title="Today's Most Selling Cusine",
                labels={'x': 'cuisine Name', 'y': 'Sale Count'},
                color_discrete_sequence=custom_colors, text_auto='.2s')
    
if restaurant_fig is not None:
    st.plotly_chart(restaurant_fig, use_container_width=True)

if time_slots_fig is not None:
    st.plotly_chart(time_slots_fig, use_container_width=True)

if orders_fig is not None:
    st.plotly_chart(orders_fig, use_container_width=True)

if payment_method_fig is not None:
    st.plotly_chart(payment_method_fig, use_container_width=True)

if rating_fig is not None:
    st.plotly_chart(rating_fig, use_container_width=True)

if cusine_fig is not None:
    st.plotly_chart(cusine_fig, use_container_width=True)