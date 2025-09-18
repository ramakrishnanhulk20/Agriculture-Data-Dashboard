# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


agri = pd.read_csv(r"C:\Users\levih\Downloads\ICRISAT-District Level Data - ICRISAT-District Level Data.csv")
agri

# %%
agri.info()
agri.isnull().sum()

# %%
top_rice_production = agri.groupby("State Name")["RICE PRODUCTION (1000 tons)"].sum().sort_values(ascending= False).head(7).reset_index()
top_rice_production

# %%
# Top 7 Rice Production States in 1000 tons

fig, ax = plt.subplots(figsize = (10,6))

sns.set(style="darkgrid")
sns.barplot( data = top_rice_production, x = "State Name", y = "RICE PRODUCTION (1000 tons)", hue= "State Name")

plt.title("Top 7 Rice Production States in 1000 tons")
plt.tight_layout()
plt.show()

# %%
top_wheat_production = agri.groupby("State Name")["WHEAT PRODUCTION (1000 tons)"].sum().sort_values(ascending= False).head(5).reset_index()
top_wheat_production

# %%
# Top 5 Wheat Production States in 1000 tons

fig, ax = plt.subplots(figsize = (10,6))

sns.set(style="darkgrid")
sns.barplot(data= top_wheat_production, x = "State Name", y = "WHEAT PRODUCTION (1000 tons)", hue= "State Name")


plt.tight_layout()
plt.title("Top 5 Wheat Production States in 1000 tons")
plt.show()

# %%
# Top 5 wheat production states in 1000 tons using pie chart(%)

value = top_wheat_production["WHEAT PRODUCTION (1000 tons)"]
label = top_wheat_production["State Name"]

fig, ax = plt.subplots(figsize = (10,10))

plt.pie( value, labels= label, colors= sns.color_palette('pastel'), autopct="%0.0f%%")
plt.title("Top 5 wheat production states in 1000 tons")
plt.show()

# %%
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
agri

# %%
top_oil_production = agri.groupby("State Name")["OILSEEDS PRODUCTION (1000 tons)"].sum().sort_values(ascending= False).head(5).reset_index()

top_sunflower_production = agri.groupby("State Name")["SUNFLOWER PRODUCTION (1000 tons)"].sum().sort_values(ascending= False).head(7).reset_index()

top_sugarcane_production = agri[agri["Year"] > 1967].groupby("State Name")["SUGARCANE PRODUCTION (1000 tons)"].sum().reset_index().sort_values(by="SUGARCANE PRODUCTION (1000 tons)" ,ascending= False)

rice_vs_whaet_production = agri[agri["Year"] > 1967].groupby("State Name")[["RICE PRODUCTION (1000 tons)", "WHEAT PRODUCTION (1000 tons)"]].sum().reset_index().sort_values(by=["RICE PRODUCTION (1000 tons)" , "WHEAT PRODUCTION (1000 tons)"],ascending=[False, False])

westbengal_dist_rice_production = agri[agri["State Name"] =="West Bengal"].groupby("Dist Name")["RICE PRODUCTION (1000 tons)"].sum().reset_index().sort_values(by="RICE PRODUCTION (1000 tons)" ,ascending= False)

top_UP_wheatpro_yearwise = agri[agri["State Name"] == "Uttar Pradesh"].groupby("Year")["WHEAT PRODUCTION (1000 tons)"].sum().sort_values(ascending=False).reset_index().head(10)

millet_production = agri[agri["Year"] > 1967].groupby("State Name")["PEARL MILLET PRODUCTION (1000 tons)"].sum().sort_values(ascending=False).reset_index()

kharif_vs_rabi_production = agri.groupby("State Name")[["KHARIF SORGHUM PRODUCTION (1000 tons)", "RABI SORGHUM PRODUCTION (1000 tons)"]].sum().sort_values(by="RABI SORGHUM PRODUCTION (1000 tons)", ascending=False)

top_groundnut_production = agri.groupby("State Name")["GROUNDNUT PRODUCTION (1000 tons)"].sum().sort_values(ascending=False).reset_index().head(7)

top_soyabean_prodandyield = agri.groupby("State Name")[["SOYABEAN PRODUCTION (1000 tons)", "SOYABEAN YIELD (Kg per ha)"]].sum().sort_values(by="SOYABEAN YIELD (Kg per ha)", ascending=False).head(5)

major_oil_production = agri.groupby("State Name")["OILSEEDS PRODUCTION (1000 tons)"].sum().sort_values(ascending=False).reset_index()

area_vs_production = agri[["State Name", "RICE AREA (1000 ha)", "RICE PRODUCTION (1000 tons)", "WHEAT AREA (1000 ha)", "WHEAT PRODUCTION (1000 tons)", "MAIZE AREA (1000 ha)", "MAIZE PRODUCTION (1000 tons)"]]

rice_vs_wheat_yield = agri.groupby("State Name")[["RICE YIELD (Kg per ha)", "WHEAT YIELD (Kg per ha)"]].sum().sort_values(by= ["RICE YIELD (Kg per ha)" ,"WHEAT YIELD (Kg per ha)"], ascending=[False, False])



# %%
#Top 5 oil production by states

fig, ax = plt.subplots(figsize= (10,6))

sns.set_style(style="darkgrid")
sns.barplot(data=top_oil_production, x= "State Name", y="OILSEEDS PRODUCTION (1000 tons)", hue= "State Name")

plt.title("Top 5 states by oil production")
plt.show()


# %%
# Top 7 SUNFLOWER PRODUCTION  State


fig, ax = plt.subplots(figsize= (10,6))

sns.barplot(data=top_sunflower_production, x="State Name", y="SUNFLOWER PRODUCTION (1000 tons)", hue= "State Name")
sns.set_style(style="darkgrid")

plt.title("Top 7 sunflowet production by state")
plt.show()

# %%
# India's SUGARCANE PRODUCTION From Last 50 Years(Line_plot)

top_sugarcane_production

fig, ax = plt.subplots(figsize= (23,6))

sns.barplot(data=top_sugarcane_production, x="State Name", y="SUGARCANE PRODUCTION (1000 tons)", hue="State Name")
sns.set_style("whitegrid")

plt.title("Last 50 years top sugarcane production")
plt.tight_layout()
plt.show()

# %%
# Rice Production Vs Wheat Production (Last 50y)

rice_vs_whaet_production
fig, ax = plt.subplots(figsize= (23,6))

melted_data = pd.melt(rice_vs_whaet_production, id_vars="State Name", value_vars=["RICE PRODUCTION (1000 tons)", "WHEAT PRODUCTION (1000 tons)"], var_name="Crop", value_name="Production")

sns.barplot(data=melted_data, x="State Name", y="Production", hue="Crop")

plt.title("Rice Vs Wheat production in the last 50 years")
plt.tight_layout()
plt.show()

# %%
# Rice Production By West Bengal Districts

westbengal_dist_rice_production

fig, ax = plt.subplots(figsize= (23,6))

sns.barplot(data=westbengal_dist_rice_production, x="Dist Name", y="RICE PRODUCTION (1000 tons)", hue="Dist Name")
sns.set_style("darkgrid")

plt.title("westbengal district wise rice production")
plt.show()

# %%
# Top 10 Wheat Production Years From UP

top_UP_wheatpro_yearwise

fig, ax = plt.subplots(figsize=(10,6))

sns.barplot(data=top_UP_wheatpro_yearwise, x="Year", y="WHEAT PRODUCTION (1000 tons)", color="green")
sns.set_style("darkgrid")

plt.title("Uttar Pradesh Top 10 Year Wheat Production")
plt.show()

# %%
# Millet Production (Last 50y)

millet_production

fig, ax = plt.subplots(figsize=(10,6))

sns.barplot(data=millet_production, x="PEARL MILLET PRODUCTION (1000 tons)", y="State Name", hue="State Name")
sns.set_style("darkgrid")

plt.title("Millet Production by State Wise in the Last 50 Years")
plt.show()

# %%
# Sorghum Production (Kharif and Rabi) by Region


kharif_vs_rabi_production.reset_index(inplace=True)

melted_data1 = pd.melt(kharif_vs_rabi_production, id_vars="State Name", value_vars=["KHARIF SORGHUM PRODUCTION (1000 tons)", "RABI SORGHUM PRODUCTION (1000 tons)"], var_name="Crop", value_name="Production")

fig,ax = plt.subplots(figsize=(25,6))

sns.barplot(melted_data1, x="State Name", y="Production", hue="Crop")
sns.set_style("darkgrid")

plt.title("Sorghum(Kharif & Rabi) Production By Region")
plt.show()


# %%
# Top 7 States for Groundnut Production

top_groundnut_production

values = top_groundnut_production["GROUNDNUT PRODUCTION (1000 tons)"]
label = top_groundnut_production["State Name"]

plt.figure(figsize=(20,10))
plt.pie(values, labels= label, autopct="%0.0f%%", startangle=10)
plt.axis("equal")
plt.title("Top 7 Groundnut Production")
plt.show()

# %%
# Soybean Production by Top 5 States and Yield Efficiency

top_soyabean_prodandyield.reset_index(inplace=True)

melted_data2 = pd.melt(top_soyabean_prodandyield, id_vars="State Name", value_vars=["SOYABEAN PRODUCTION (1000 tons)", "SOYABEAN YIELD (Kg per ha)"], var_name="Crop", value_name="Production")

fig, ax = plt.subplots(figsize= (10,6))

sns.barplot(melted_data2, x="State Name", y="Production", hue="Crop")
sns.set_style("darkgrid")

plt.title("Production Vs Yield Of Soybean by Top 5 States")
plt.show()

# %%
# Oilseed Production in Major States

major_oil_production

fig,ax = plt.subplots(1,2, figsize= (20,6))

sns.lineplot(data=major_oil_production, x="OILSEEDS PRODUCTION (1000 tons)", y="State Name", ax=ax[0])
ax[0].set_title("Major Oil Production States In India")

sns.barplot(data=major_oil_production, x="OILSEEDS PRODUCTION (1000 tons)", y="State Name", ax=ax[1])
ax[1].set_title("Major Oil Production States In India")

plt.show()

# %%
# Impact of Area Cultivated on Production (Rice, Wheat, Maize)

area_vs_production

fig,ax = plt.subplots(1,3, figsize=(18,6))

sns.set_style("darkgrid")

sns.regplot(data=area_vs_production, x="RICE AREA (1000 ha)", y="RICE PRODUCTION (1000 tons)", ax=ax[0], color="green", line_kws={'color':'black'})
ax[0].set_title("Area vs Production Trend Of Rice")

sns.regplot(data=area_vs_production, x="WHEAT AREA (1000 ha)", y="WHEAT PRODUCTION (1000 tons)", ax=ax[1], color="red", line_kws={'color':'black'})
ax[1].set_title("Area vs Production Trend Of Wheat")

sns.regplot(data=area_vs_production, x="MAIZE AREA (1000 ha)", y="MAIZE PRODUCTION (1000 tons)", ax=ax[2], color="orange", line_kws={'color':'black'})
ax[2].set_title("Area vs Production Trend Of Maize")

plt.tight_layout()
plt.show()

# %%
# Connecting with MySQL 

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:4122@localhost:3306/agri_data")

with engine.connect() as conn:
    print("successfull!")

# %%
# Importing the data into database

agri.to_sql("agriculture_data", con= engine, if_exists= "replace", index=False)

# %%



