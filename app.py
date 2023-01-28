import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import csv



gss_data = pd.read_csv("gss2016.csv")

#title the webapp
st.title("The General Social Survey Data Analytics Web App")

#insight into the survey with a youtube video
st.write(f'<iframe width ="560",height="315" src="https://www.youtube.com/embed/hyirTanipAc" title = "Youtube video player" frameborder="0" allow="acclerometer; autoplay;clipboard-write;encrypeted-media; gyroscope; picture-in-picture" allowfullscreen> </iframe>', unsafe_allow_html=True,)

st.write("")
st.write("")
st.write("")
st.write("")

st.header('GSS 2016 Dataset')
st.write("")
st.dataframe(gss_data)
st.write("")
st.write("")

gss_data_filtered = gss_data[['sex','race','age','degree','wrkstat','income','happy']]

st.write("")
st.write("")
st.write("")
st.header("GSS 2016 Dataset Filtered on Sex, Race, Age, Degree, Work, Status, Income and Happiness")
st.dataframe(gss_data_filtered)


#create a column to show count
#dict to show values
columns = {'sex','race','age','degree','wrkstat','income','happy'}

st.write("")
st.write("")
st.write("")
st.header("GSS 2016 Dataset Aggregated by Count")

#create a dropdown based off above selection
pick_columns = st.selectbox("Count by column: ",list(columns))


gss_data_filtered['Count'] = 0
gss_data_filtered_count = gss_data_filtered.groupby(pick_columns).count()
gss_data_filtered_count = gss_data_filtered_count[['Count']]


#create new percentage column
gss_data_filtered_count['Percentages'] = (gss_data_filtered_count.Count/gss_data_filtered_count.Count.sum())*100 

st.dataframe(gss_data_filtered_count)

st.write("")
st.write("")
st.write("")
st.header("GSS 2016 Dataset Correlation between columns")

#create a multi select tool

multi_select_column=st.multiselect("Multi-select columns for correlation",list(columns),default=['sex'])
multi_select_gss_data_filtered = gss_data_filtered[multi_select_column]

st.dataframe(multi_select_gss_data_filtered)

st.write("")
st.write("")
st.write("")
st.header("GSS 2016 Dataset Correlation between columns multi-select")

#combining everything

multi_select_column2 = st.multiselect("Multi-select columns grouped by: ", list(columns),default =['sex'])


multi_select_groupby = gss_data_filtered[multi_select_column2].groupby(multi_select_column2).size().reset_index(name='Count')

multi_select_groupby['Percentages'] = (multi_select_groupby.Count/multi_select_groupby.Count.sum())*100


st.dataframe(multi_select_groupby)
st.write("")
st.write("")
st.write("")
st.header("GSS 2016 Dataset Aggregated by Count Pie Chart")

pick_columns_visualized = st.selectbox("Visualize by Column", list(columns))
gss_data_filtered_count_visual = gss_data_filtered.groupby(pick_columns_visualized).count()


#creating a pie chart
gss_data_filtered_count_visual['x-axis'] = gss_data_filtered_count_visual.index
fig = go.Figure(data=[go.Pie(labels=gss_data_filtered_count_visual['x-axis'],values= gss_data_filtered_count_visual['Count'])])


st.plotly_chart(fig)




