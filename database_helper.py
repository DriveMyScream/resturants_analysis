import mysql.connector

class DataBaseHelper:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host = '127.0.0.1',
                                                      user = 'root',
                                                      password = 'admin',
                                                      database = 'restaurants_orders')
            self.mycursor = self.connection.cursor()
            print("Connection Establish")
        except:
            print("Connection Error")
    
    def get_sales(self, date):
        query = """
        SELECT r.RestaurantName, SUM(o.`Order Amount`) as `total_sales`
        FROM restaurants r
        INNER JOIN orders_df o
        ON r.RestaurantID = o.`RestaurantID`
        WHERE DATE(`Order Date`) = '{date}'
        GROUP BY r.RestaurantName
        ORDER BY total_sales DESC
        """.format(date=date)

        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        hotel_name = []
        sales_amount = []
        for item in data:
            hotel_name.append(item[0])
            sales_amount.append(float(item[1]))
            
        return hotel_name, sales_amount
    
    def get_sales_per_time_slots(self, date):
        query = """
        SELECT SUM(`Order Amount`) AS 'sale_amount',
               CASE 
                   WHEN TIME(`Order Date`) BETWEEN '09:00:00' AND '12:00:00' THEN 'Morning'
                   WHEN TIME(`Order Date`) BETWEEN '12:00:00' AND '15:00:00' THEN 'Afternoon'
                   WHEN TIME(`Order Date`) BETWEEN '15:00:00' AND '18:00:00' THEN 'Late afternoon'
                   WHEN TIME(`Order Date`) BETWEEN '18:00:00' AND '21:00:00' THEN 'Night'
                   ELSE 'Late night'
               END AS timeslots
        FROM orders_df WHERE DATE(`Order Date`) = '{date}'
        GROUP BY timeslots
        ORDER BY sale_amount DESC;
        """.format(date=date)
        
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        sales = []
        time_slots = []
        for item in data:
            sales.append(float(item[0]))
            time_slots.append(item[1])
        
        return time_slots, sales 
    
    def get_order_sold_count(self, date):
        query = """
        SELECT r.RestaurantName, SUM(o.`Quantity of Items`) AS 'orders_sold'
        FROM orders_df o
        INNER JOIN restaurants r ON o.RestaurantID = r.RestaurantID
        WHERE DATE(`Order Date`) = '{date}'
        GROUP BY r.RestaurantName 
        ORDER BY orders_sold DESC;
        """.format(date=date)

        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        hotel_name = []
        total_orders = []
        for item in data:
            hotel_name.append(item[0])
            total_orders.append(float(item[1]))
            
        return hotel_name, total_orders 
        
    def get_payment(self, date):
        query = """
        SELECT `Payment Mode`, SUM(`Order Amount`) AS 'sale' FROM orders_df
        WHERE DATE(`Order Date`) = '{date}'
        GROUP BY `Payment Mode`
        ORDER BY sale DESC
        """.format(date=date)

        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        payment_type = []
        amount = []
        for item in data:
            payment_type.append(item[0])
            amount.append(float(item[1]))
            
        return payment_type, amount
    
    def get_resturant_ratings(self, date):
        query = """
        SELECT r.RestaurantName, AVG(o.`Customer Rating-Food`) as 'rating' FROM orders_df o
        JOIN restaurants r
        ON o.RestaurantID = r.RestaurantID
        WHERE DATE(`Order Date`) = '{date}'
        GROUP BY r.RestaurantName
        ORDER BY rating DESC
        """.format(date=date)

        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        resturant_name = []
        resturant_rating = []
        for item in data:
            resturant_name.append(item[0])
            resturant_rating.append(float(item[1]))
        
        return resturant_name, resturant_rating 
    
    def get_cusine_sold(self, date):
        query = """
        SELECT r.Cuisine, SUM(o.`Quantity of Items`) AS 'sales' FROM orders_df o
        INNER JOIN restaurants r
        ON o.RestaurantID = r.RestaurantID
        WHERE DATE(`Order Date`) = '{date}'
        GROUP BY r.Cuisine
        ORDER BY sales DESC;
        """.format(date=date)

        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        cuisine = []
        solds = []
        for item in data:
            cuisine.append(item[0])
            solds.append(float(item[1]))
        
        return cuisine, solds 