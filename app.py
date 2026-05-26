import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("🌍 Country Statistics Dashboard")

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

# Sidebar filter
st.sidebar.header("Filters")

continent = st.sidebar.selectbox("Select Continent", df['continent'].unique())
df = df[df['continent'] == continent]

country = st.sidebar.selectbox("Select Country", df['country'].unique())

filtered = df[df['country'] == country]

# Show data
st.subheader("📄 Data")
st.write(filtered)

# -------------------------------
# 📈 Line Chart (Life Expectancy)
# -------------------------------
st.subheader("📈 Life Expectancy Over Time")

st.line_chart(filtered.set_index('year')['lifeExp'])

# -------------------------------
# 📊 Bar Chart (Top GDP Countries)
# -------------------------------
st.subheader("💰 Top 10 GDP per Capita Countries")

latest_year = df['year'].max()
latest_data = df[df['year'] == latest_year]

top_countries = latest_data.sort_values(by='gdpPercap', ascending=False).head(10)

st.bar_chart(top_countries.set_index('country')['gdpPercap'])

# -------------------------------
# 🌍 Scatter Plot (GDP vs LifeExp)
# -------------------------------
st.subheader("🌍 GDP vs Life Expectancy")

fig, ax = plt.subplots()

ax.scatter(df['gdpPercap'], df['lifeExp'])

ax.set_xlabel("GDP per Capita")
ax.set_ylabel("Life Expectancy")
ax.set_title("GDP vs Life Expectancy")

st.pyplot(fig)