import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import altair as alt

# set judul dashboard
st.set_page_config(page_title="Bike Rental Dashboard",
                   layout= "centered")

# import data
df = pd.read_csv('day.csv')
df['dteday'] = pd.to_datetime(df['dteday']) # convert dtypes kolom 'dteday' menjadi datetime
df['year'] = df.dteday.dt.year # ekstrak tahun dan simpan ke kolom baru "year"
df['month'] = df.dteday.dt.month # ekstrak bulan dan simpan ke kolom baru "month"

st.title("Bike Rental Dashboard")

st.dataframe(df)

# split data berdasarkan tahun
df11 = df[df['year'] == 2011]
df12 = df[df['year'] == 2012]

# dict untuk mengganti nama bulan
nama_bulan = {
    1 : "Jan", 2 : "Feb", 3 : "Mar", 4 : "Apr",
    5 : "Mei", 6 : "Jun", 7 : "Jul", 8 : "Ags",
    9 : "Sept", 10 : "Okt", 11 : "Nov", 12 : "Des"
}

# chart 1
st.header("Hari Favorit Para Penyewa Sepeda")
fig, ax = plt.subplots(figsize=(12, 8))

sns.barplot(x="weekday", y="cnt", hue="year", data=df, ci=None)

plt.title("Perbandingan Jumlah Penyewa Sepeda Per Tahun Berdasarkan Hari", fontsize=20)
plt.xlabel("Hari",fontsize =12)
plt.ylabel("Jumlah",fontsize =12)
st.pyplot(fig)

# chart 2
st.header("Musim Favorit Para Penyewa Sepeda")
fig, ax = plt.subplots(figsize=(12, 8))

sns.barplot(x="season", y="cnt", hue="year", data=df, ci=None)

plt.title("Perbandingan Jumlah Penyewa Sepeda Per Musim",fontsize = 20)
plt.xlabel("Musim (Season)",fontsize =12)
plt.ylabel("Jumlah",fontsize =12)
st.pyplot(fig)

# chart 3
st.header("Tren Total Penyewa Sepeda (2011)")
x = df11['month']
y = df11['cnt']

fig, ax = plt.subplots(figsize=(16, 5))
plt.plot(x, y)

# custom xlabel 
ax.set_xticks(x)
ax.set_xticklabels([nama_bulan[month] for month in x])

plt.title("Jumlah Penyewa Sepeda Pada Tahun 2011",fontsize = 16)
plt.xlabel("Bulan",fontsize = 12)
plt.ylabel("Total Penyewa",fontsize = 12)
st.pyplot(fig)

# chart 3.1
st.header("Tren Total Penyewa Sepeda (2012)")
x = df12['month']
y = df12['cnt']

fig, ax = plt.subplots(figsize=(16, 5))
plt.plot(x, y)

# custom xlabel 
ax.set_xticks(x)
ax.set_xticklabels([nama_bulan[month] for month in x])

plt.title("Jumlah Penyewa Sepeda Pada Tahun 2012",fontsize = 16)
plt.xlabel("Bulan",fontsize = 12)
plt.ylabel("Total Penyewa",fontsize = 12)
st.pyplot(fig)

# chart 4
st.header("Jumlah Penyewa Berdasarkan Status Per Tahun (2011)")

x = df11['month']
y = df11['casual']
y2 = df11['registered']

fig, ax = plt.subplots(figsize=(16, 5))
plt.plot(x, y, label="Casual")
plt.plot(x, y2, label="Registered")

# custom xlabel 
ax.set_xticks(x)
ax.set_xticklabels([nama_bulan[month] for month in x])

plt.title("Perbandingan Jumlah Penyewa Sepeda Berdasarkan Status Penyewa Pada Tahun 2011",fontsize=20)
plt.xlabel("Bulan",fontsize=14)
plt.ylabel("Total Penyewa",fontsize=14)
plt.legend(loc="right")
st.pyplot(fig)

# chart 4.1
st.header("Jumlah Penyewa Berdasarkan Status Per Tahun (2012)")
#plot
x = df12['month']
y = df12['casual']
y2 = df12['registered']

fig, ax = plt.subplots(figsize=(16, 5))
plt.plot(x, y, label="Casual")
plt.plot(x, y2, label="Registered")

# custom xlabel 
ax.set_xticks(x)
ax.set_xticklabels([nama_bulan[month] for month in x])

plt.title("Perbandingan Jumlah Penyewa Sepeda Berdasarkan Status Penyewa Pada Tahun 2012",fontsize=20)
plt.xlabel("Bulan",fontsize=14)
plt.ylabel("Total Penyewa",fontsize=14)
plt.legend(loc="right")
plt.show()
st.pyplot(fig)