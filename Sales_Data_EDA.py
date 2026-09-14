import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\DATA ANALYSIS\Sales Data_Dashboard.xlsx", sheet_name="Sheet18")
print(df.columns)

print(df.info())

# 1.SEGMENT WISE SALES (BAR CHART)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print(df.groupby(["Segment"])["Sales"].sum())
print(df.groupby(["Segment"],as_index=False)["Sales"].sum().sort_values(by="Sales",ascending=False))

x=df['Segment']
y=df['Sales']
plt.bar(x,y,color="Green",width=0.4)
plt.title("Sales by Segment")
plt.xlabel("Segment")
plt.ylabel("Sales")
plt.show()


# 2.SALES HISTOGRAM>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
y=df['Sales']
plt.hist(y,color="Green")
plt.title("sales data-HIST")
plt.show()


# 1.1.SEGMENT WISE SALES (PIE CHART)
segment_grp=df.groupby(["Segment"])["Sales"].sum()
segment_grp.plot(
    kind="pie",
    autopct="%1.2f%%",
    startangle=90,
    cmap="Set2",
)
plt.title("SEGMENT WISE SALES")
plt.show()


# 3.SEGMENT WISE PROFIT>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print(df.groupby(["Segment"])["Profit"].sum())
profit_grp=df.groupby(["Segment"])["Profit"].sum()

profit_grp.plot(
    kind="bar",
    color="#4B007E",width=0.5,
    title="Profit by Segment"
)
plt.ylabel("Profit")
plt.xlabel("Segment")
plt.title("Segment Wise Profit")
plt.axhline(0, color="Red", linestyle="-", linewidth=1.5)
plt.grid(axis="y", linestyle="--", alpha=0.5, color="#FA0000", zorder=0)
plt.show()



print(df.columns)
#SALES BY YEAR/QUARTER/MONTH>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#plot1
x=df['Year']
y=df['Sales']
plt.subplot(1,3,1)
plt.bar(x,y,color="Green",width=0.4)
plt.title("Sales by Year")
plt.xlabel("Year")
plt.ylabel("Sales")

#plot2
x=df['Quarter']
y=df['Sales']
plt.subplot(1,3,2)
plt.bar(x,y,color="Red",width=0.4)
plt.title("Sales by Quarter")
plt.xlabel("Quarter")
plt.ylabel("Sales")

#plot3
x=df['Month']
y=df['Sales']
plt.subplot(1,3,3)
plt.bar(x,y,color="Red",width=0.4)
plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.suptitle("YEAR / QUARTER / MONTH wise sales")
plt.show()


#SEGMENT WISE MANUFACTURING PRICE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
mf_group=df.groupby(["Segment"])["Manufacturing Price"].sum()
print(mf_group)
mf_group.plot(        
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    colormap="Set2",
    ylabel="",
    explode=[0,0,0.1,0,0],
    shadow=True
    )
plt.legend(title="Segment",bbox_to_anchor=(1.0,0.5),loc="upper left")
plt.title('Segment wise Manufacturing Price')
plt.show()

#RELATION BETWEEN SALES AND PROFIT>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
df[["Sales","Profit"]].corr()

x=df["Sales"]
y=df["Profit"]
plt.scatter(x,y)
plt.title("Sales and Profit Co-Relation")
plt.show()

#COUNTRY WISE SALES>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
x=df['Country']
y=df['Sales']
plt.bar(x,y,color="Green",width=0.5)
plt.title("Sales by Country")
plt.xlabel("Country")
plt.ylabel("Sales")
plt.show()


#MONTH-WISE PROFIT ANALYSIS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
x=df['Month']
y=df['Profit']
plt.bar(x, y,color="Green",width=0.4)
plt.axhline(0, color="black", linestyle="-", linewidth=1.5)
plt.title("Month-Wise Profit Analysis",
    fontsize=16,
    fontweight="bold",
    pad=20,
    color="#222222")
plt.grid(axis="y", linestyle="--", alpha=0.5, color="#CCCCCC", zorder=0)
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()


#HIGHEST SELLING PRODUCT ANALYSIS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
x=df['Product_Name']
y=df['Units Sold']
plt.bar(x, y,color="#CD810F",width=0.4)
plt.axhline(0, color="black", linestyle="-", linewidth=1.5)
plt.title("Highest Selling Product analysis",
    fontsize=16,
    fontweight="bold",
    pad=20,
    color="#222222")
plt.grid(axis="y", linestyle="--", alpha=0.5, color="#CD810F", zorder=0)
plt.xlabel("Product_Name")
plt.ylabel("'Units Sold'")
plt.show()


