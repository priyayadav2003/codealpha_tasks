import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#styling...
sns.set(style="whitegrid")

#creating sample dataset...
data={
    "Date":pd.date_range(start ="2025-01-01",periods=100),
    "Products":["Refrigerator","Phone","Watch","Headphones","Laptop"]*20,
    "Categories":["Electronics","Electronics","Accessories","Accessories","Electronics"]*20,
    "Regions":["East","West","North","South","Central"]*20,
    "Sales":[30000,40000,10000,25000,50000]*20
     }
df=pd.DataFrame(data)

#extracting months...
df["Month"] = df["Date"].dt.month

# creating dashboard..
plt.figure(figsize=(14,10))

#Total Sales by Categories..
plt.subplot(2,2,1)
Category_Sales =df.groupby("Categories")["Sales"].sum().reset_index()
sns.barplot(x="Categories",y="Sales",data=Category_Sales)
plt.title("Total Sales by Categories")


#Monthly sales trend...
plt.subplot(2,2,2)
monthly_sales =df.groupby("Month")["Sales"].sum().reset_index()
sns.lineplot(x="Month",y="Sales",
data=monthly_sales,marker="o")
plt.title("monthly sales trends")



#Top 5 products are..
plt.subplot(2,2,3)
ProductSales=df.groupby("Products")["Sales"].sum().reset_index()
ProductSales=ProductSales.sort_values(by="Sales",ascending=False)
sns.barplot(x="Products",y="Sales",data=ProductSales)
plt.title("Top 5 products by sales")
plt.xticks(rotation=45)


# sales by region ...
plt.subplot(2,2,4)
regional_sales=df.groupby("Regions")["Sales"].sum()
plt.pie(regional_sales,labels=regional_sales.index,autopct='%1.1f%%')
plt.title("sales distrubution by region")



plt.tight_layout()
plt.show()
print("Data Visualization Complete Successfully")



