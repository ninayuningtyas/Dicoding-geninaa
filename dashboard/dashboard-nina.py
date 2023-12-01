import pandas as pd
import matplotlib.pyplot as plt
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

# chart 1
st.header("Hari Favorit Para Penyewa Sepeda")
bar_chart1 = alt.Chart(df).mark_bar().encode(
    alt.X('weekday',title="Hari"),
    alt.Y('cnt',title="Jumlah"),
    alt.Color('year')
)

st.altair_chart(bar_chart1)

# chart 2
st.header("Musim Favorit Para Penyewa Sepeda")
bar_chart2 = alt.Chart(df).mark_bar().encode(
    alt.X('season',title="Musim"),
    alt.Y('cnt',title="Jumlah"),
    alt.Color('year')
)

st.altair_chart(bar_chart2)

# chart 3
st.header("Tren Total Penyewa Sepeda (2011)")
line_chart11 = alt.Chart(df11).mark_line().encode(
    alt.X('month',title="Bulan", timeUnit='month'),
    alt.Y('cnt',title="Jumlah",aggregate='sum')
)

st.altair_chart(line_chart11)

# chart 3.1
st.header("Tren Total Penyewa Sepeda (2012)")
line_chart12 = alt.Chart(df12).mark_line().encode(
    alt.X('month',title="Bulan", timeUnit='month'),
    alt.Y('cnt',title="Jumlah",aggregate='sum')
)

st.altair_chart(line_chart12)

# chart 4
st.header("Jumlah Penyewa Berdasarkan Status Per Tahun (2011)")

nama_bulan = {
    1 : "Jan", 2 : "Feb", 3 : "Mar", 4 : "Apr",
    5 : "Mei", 6 : "Jun", 7 : "Jul", 8 : "Ags",
    9 : "Sept", 10 : "Okt", 11 : "Nov", 12 : "Des"
}


x = df11['month']
y = df11['casual']
y2 = df11['registered']

fig, ax = plt.subplots(figsize=(16, 5))
plt.plot(x, y, label="Casual", marker="o")
plt.plot(x, y2, label="Registered", marker="o")

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
plt.plot(x, y, label="Casual", marker="o")
plt.plot(x, y2, label="Registered", marker="o")

# custom xlabel 
ax.set_xticks(x)
ax.set_xticklabels([nama_bulan[month] for month in x])

plt.title("Perbandingan Jumlah Penyewa Sepeda Berdasarkan Status Penyewa Pada Tahun 2012",fontsize=20)
plt.xlabel("Bulan",fontsize=14)
plt.ylabel("Total Penyewa",fontsize=14)
plt.legend(loc="right")
plt.show()
st.pyplot(fig)
