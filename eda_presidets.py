import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

st.set_page_config(
    page_title="US Presidents Heights",
    page_icon="📊", layout='wide'
)
st.title("US Presidents Heights")

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/amankharwal/US-presidents-heights/master/president_heights.csv')
st.dataframe(df)



heights = np.array(df['height(cm)'])
st.bar_chart(heights)
st.write("heights = np.array(df['height(cm)'])")
st.write(heights)

# Height analysis
st.subheader("Height Analysis")
st.write("Average Height: ", heights.mean().__round__(2))
st.write("Tallest President: ", heights.max(), df.loc[df['height(cm)'].idxmax()]['name'])
st.write("Shortest President: ", heights.min(), df.loc[df['height(cm)'].idxmin()]['name'])
st.write("Height Standard Deviation: ", heights.std())
st.write("Height Variance: ", heights.var())

plt.figure(figsize=(6, 3))
plt.hist(heights)
plt.title("Distribution of US Presidents' Heights")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
st.pyplot(plt)