import streamlit as st
import pandas as pd
import altair as alt
from datetime import date

# 页面配置
st.set_page_config(page_title="复杂美观的 Streamlit 示例", layout="wide")

# 侧边栏导航
st.sidebar.title("导航")
navigation = st.sidebar.radio("选择页面", ["首页", "数据分析", "交互图表"])

# 示例数据
@st.cache_data  # 使用缓存加快重复加载速度
def load_data():
    data_url = ("https://raw.githubusercontent.com/streamlit/example-data/master/data/cars.csv")
    data = pd.read_csv(data_url)
    return data

data = load_data()

# 首页
if navigation == "首页":
    st.title("欢迎来到 Streamlit 示例应用!")
    st.write("这是一个展示 Streamlit 功能的示例应用，包括数据可视化、交互组件等。")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=300)

# 数据分析页面
elif navigation == "数据分析":
    st.title("汽车数据分析")
    st.write("这里我们对汽车数据进行基本分析。")

    # 数据筛选
    manufacturer = st.selectbox("选择制造商", data['manufacturer'].unique())
    filtered_data = data[data['manufacturer'] == manufacturer]

    # 数据展示
    st.dataframe(filtered_data.head(10))

    # 统计信息
    st.subheader(f"{manufacturer} 的统计信息")
    st.write(filtered_data.describe())

# 交互图表页面
elif navigation == "交互图表":
    st.title("交互式图表")
    st.write("使用 Altair 创建的交互式图表。")

    # 数据筛选
    year_slider = st.slider("选择年份范围", 1990, 2015, (1990, 2015))
    filtered_data_year = data[(data['year'] >= year_slider[0]) & (data['year'] <= year_slider[1])]

    # 图表绘制
    chart = (
        alt.Chart(filtered_data_year)
        .mark_circle(size=60)
        .encode(
            x="Horsepower",
            y="Miles_per_Gallon",
            color="Origin",
            tooltip=["Name", "Horsepower", "Miles_per_Gallon", "Origin"],
        )
        .interactive()
    )
    st.altair_chart(chart, use_container_width=True)

# 页面底部信息
st.sidebar.text("由 Streamlit 提供技术支持")
st.sidebar.markdown("[了解更多关于 Streamlit](https://streamlit.io/)")
