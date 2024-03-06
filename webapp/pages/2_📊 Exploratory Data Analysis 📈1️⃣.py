import sys
import numpy as np

sys.path.append("pages")

import streamlit as st
import io
import pandas as pd
import plotly.express as px
import seaborn as sns
from matplotlib import pyplot as plt
from streamlit_extras.switch_page_button import switch_page

# streamlit page setup
# sidebar : collapsed, auto or expanded
st.set_page_config(
    page_title="Welcome to Sleep Mammals",
    page_icon="🦍",
    layout="centered",
    initial_sidebar_state="expanded"
)

#hidden or visible
st.markdown("""
    <style>
    #MainMenu {visibility: visible;}
    footer {visibility: visible;} 
    </style>
    """, unsafe_allow_html=True)

# Function to create and customize scatter plot
def create_custom_scatter(df, x, y, color):
    fig = px.scatter(df, x=x, y=y, color=color)
    fig.update_layout(plot_bgcolor="white")
    fig.update_xaxes(
        mirror=True,
        ticks="outside",
        showline=True,
        linecolor="black",
        gridcolor="lightgrey",
    )
    fig.update_yaxes(
        mirror=True,
        ticks="outside",
        showline=True,
        linecolor="black",
        gridcolor="lightgrey",
    )
    return fig

# Function to create and display a boxplot

def create_and_show_boxplot(data, x, y, hue, title):
    plt.figure(figsize=(10, 6))  # Adjust figure size as needed
    sns.boxplot(x=x, y=y, hue=hue, data=data, palette='Pastel1')
    plt.title(title, fontsize=11, fontweight="normal")
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title=hue)
    st.pyplot(plt)
    plt.close()


def display_seaborn_displot(data, x, title):
    g = sns.displot(data, x=x, bins=50, kde=True)
    g.set_xlabels(x, fontsize=10, fontweight="normal")
    g.set_ylabels("Number of Species", fontsize=10, fontweight="normal")
    plt.title(title, fontsize=11, fontweight="normal")
    st.pyplot(plt)  # Display the plot in Streamlit
    plt.clf()  # Clear the current figure to avoid overlap in subsequent calls
    plt.close()
    
@st.cache_data(experimental_allow_widgets=True)
def eda():
    path_csv = "sleep_mammals_LAST_all_columns_23_02.csv"
        
    df =  pd.read_csv(path_csv, sep=",", index_col=0)
    df_sleep = pd.read_csv(path_csv, sep=',', index_col = False)

    n = len(df)

    st.markdown("""Sleeping is a common activity for all the mammals. But there are huge discrepancies in the characteristics of their sleep. For example, some mammals sleep 10% of their day, others sleep 80% of their day. Many questions can be asked:
    - Does a large mammal have a better sleep than a small mammal?
    - Do predators have a better sleep than preys?
    - Who has the longer dreams?
    """)
    st.subheader("Data")

    f"""
    [![](https://img.shields.io/badge/download-csv-brightgreen)](https://github.com/cdouadi/sleepmammals/blob/3ef60fa40e52a271eaadc8e82d9ac993b48fcc3b/sleep_mammals.csv)


    Dataset created on 2024. A total of {n} raws.

    """

    with st.expander("1- Libraries"):
        f"""
        ```python
        import pandas as pd
        import numpy as np 
        import pandas as pd 
        import scipy as sc
        import warnings
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        import seaborn as sns
        from matplotlib import pyplot as plt
        import plotly.express as px
        ```
        """

    with st.expander("2- Load Dataset & Examine the general Info"):
        """
        ```python
        path = "{path_csv}"
        df = pd.read_csv(path, sep=",", index_col=0)
        ```
        """
        #--------------------------------
        f"""
        ```python
        df.head()
        ```
        """

        st.dataframe(df)
        #--------------------------------
        df = df_sleep.copy()
        #--------------------------------
        f"""
        ```python
        df.info()
        ```
        """

        buffer = io.StringIO()
        df.info(buf=buffer)
        info = buffer.getvalue()
        st.text(info)
 
    st.subheader("Analysis")
    with st.expander("3- Initiate Analysis"):
        f"""
        ```python
        df.describe()
        ```
        """
        st.dataframe(df.describe())

    with st.expander("3.1 Distribution of Sleep & Dreaming"):
        f"""
        ```python
        fig = px.histogram(df, "TotalSleep",color="Species", nbins=20, 
                            color_discrete_sequence=px.colors.sequential.Sunset,
                            title="Distribution of Sleep"
                            )
        fig.show()
        ```
        """
        # Create the Plotly figure
        fig = px.histogram(df, "TotalSleep", color="Species", nbins=20, 
                        color_discrete_sequence=px.colors.sequential.Sunset,
                        title="Distribution of Sleep")

        # Display the figure in the Streamlit app
        st.plotly_chart(fig)
        plt.close()
        #--------------------------------

        f"""
        ```python
        fig = px.histogram(df, "Dreaming",color="Species", nbins=20, 
                        color_discrete_sequence=px.colors.sequential.Sunset,
                        title="Distribution of Dreaming"
                        )
        fig.show()
        ```
        """

        fig = px.histogram(df, "Dreaming",color="Species", nbins=20, 
                        color_discrete_sequence=px.colors.sequential.Sunset,
                        title="Distribution of Dreaming"
                        )
        st.plotly_chart(fig)
        plt.close()
        #--------------------------------
        f"""
        ```python
        fig = px.histogram(df, "NonDreaming",color="Species", nbins=20, 
                        color_discrete_sequence=px.colors.sequential.Sunset,
                        title="Distribution of Deep Sleep"
                        )
        fig.show()
        ```
        """
        fig = px.histogram(df, "NonDreaming",color="Species", nbins=20, 
                        color_discrete_sequence=px.colors.sequential.Sunset,
                        title="Distribution of Deep Sleep"
                        )
        st.plotly_chart(fig)
        plt.close()
        #--------------------------------
        f"""
        ```python
        fig = px.scatter_3d(df, x='TotalSleep', y='Dreaming', z='NonDreaming', 
                            color="Species", size_max=20, opacity=0.7,
                            color_discrete_sequence=px.colors.sequential.Sunset,)


        fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        fig.show()
        ```
        """
        fig = px.scatter_3d(df, x='TotalSleep', y='Dreaming', z='NonDreaming', 
                            color="Species", size_max=20, opacity=0.7,
                            color_discrete_sequence=px.colors.sequential.Sunset)

        # Update the layout to minimize margins
        fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

        # Display the figure in the Streamlit app
        st.plotly_chart(fig)
        plt.close()

        st.info("These plots reveals that there are 5 mammal species capable of sleeping for over 19 hours. And 4 species dream a lot longer than others. They are Water Opossum(6.6 hours), Thick-tail Opposum(6.6 hours), Giant Armadillo(6.1) and North American Opossum(5.6 hours). For None Dreaming, Velvet's deep sleeping hours reach 17.9, the longest one.")
        #--------------------------------
    
    with st.expander("3.2 Body Weight Visualization - Let's find out who is the giant!"):
        f"""
        ```python
        sns.set_theme(style="white")
        sns.displot(df, x="BodyWt", bins=50, kde=True)
        plt.xlabel("Body Weight (G)", fontsize=10, fontweight="normal")
        plt.ylabel("Count", fontsize=10, fontweight="normal")
        plt.title('Body Weight Distribution', fontsize=11, fontweight="normal")
        plt.show()
        ```
        """

        sns.set_theme(style="white")
        plt.figure(figsize=(10, 6))  # Optional: Adjust the figure size as needed
        sns.displot(df, x="BodyWt", bins=50, kde=True)
        plt.xlabel("Body Weight (G)", fontsize=10, fontweight="normal")
        plt.ylabel("Count", fontsize=10, fontweight="normal")
        plt.title('Body Weight Distribution', fontsize=11, fontweight="normal")
        st.pyplot(plt)
        plt.close()
        st.info("Most of species in this dataset seemed to be small size Mammals. However, according to the max value of body weight, we do have giants in them. So, Who are they?")
        #--------------------------------
        f"""
        ```python
        fig = px.histogram(df, "BodyWt", color="Species", nbins=20, 
                        color_discrete_sequence=px.colors.qualitative.Light24,
                        title="Distribution of Body Weight"
                        )
        fig.show()
        ```
        """
        fig = px.histogram(df, "BodyWt", color="Species", nbins=20, 
                        color_discrete_sequence=px.colors.qualitative.Light24,
                        title="Distribution of Body Weight"
                        )
        st.plotly_chart(fig)
        st.info("We found two elephants are actually the giants who. The giants appear insomniac compared to humans. Nevertheless, the sleep patterns of mammals with medium-sized bodies remain uncertain. Thus, do larger animals sleep less than smaller ones, or is it the opposite ? Let's explore and discover !")
        #--------------------------------

        st.dataframe(df[df["BodyWt"] <= 2000000].describe())

        f"""
        ```python
        fig = px.scatter(df[df["BodyWt"] <= 2000000], x="TotalSleep", y="BodyWt", size="BodyWt", color="Vore", 
                        hover_name="Family", log_x=True, size_max=80, 
                        color_discrete_sequence=px.colors.qualitative.Pastel,
                        title="Distribution of Sleep"
                        )
        fig.show()
        ```
        """
        fig = px.scatter(df[df["BodyWt"] <= 2000000], x="TotalSleep", y="BodyWt", size="BodyWt", color="Vore", 
                        hover_name="Family", log_x=True, size_max=80, 
                        color_discrete_sequence=px.colors.qualitative.Pastel,
                        title="Distribution of Sleep"
                        )
        st.plotly_chart(fig)

        #--------------------------------
        f"""
        ```python
        fig = px.scatter(df[df["BodyWt"] <= 56934.5294120], x="TotalSleep", y="BodyWt", size="BodyWt", color="Vore", 
                        hover_name="Family", log_x=True, size_max=80, 
                        color_discrete_sequence=px.colors.qualitative.Pastel,
                        title="Distribution of Sleep"
                        )
        fig.show()
        #<= 2000000 is the 50 percentille to exclude the two elephants who are extremely heavy and 56934.5294120 is the mean of body weight in the group of mammals without presence of the two Giants."

        ```
        """
        fig = px.scatter(df[df["BodyWt"] <= 56934.5294120], x="TotalSleep", y="BodyWt", size="BodyWt", color="Vore", 
                        hover_name="Family", log_x=True, size_max=80, 
                        color_discrete_sequence=px.colors.qualitative.Pastel,
                        title="Distribution of Sleep"
                        )
        st.plotly_chart(fig)

        st.info("From the plot, We exclude the giants. It appears that a large mammal does not necessarily sleep better than a small one and so on dreaming cases.")
        #--------------------------------
        f"""
        ```python
        sns.set_theme(style="white")
        sns.regplot(x="TotalSleep", y="BodyWt", data=df[df["BodyWt"] <= 56934.5294120])
        ##56934.5294120 is the mean of body weight in the group of mammals without presence of the two Giants.
        ```
        """
        # Filter the DataFrame based on your criteria
        df_filtered = df[df["BodyWt"] <= 56934.5294120]

        # Setting the theme for seaborn
        sns.set_theme(style="white")

        # Create a Seaborn regression plot
        plt.figure(figsize=(10, 6))  # Optional: Adjust the figure size as needed
        sns.regplot(x="TotalSleep", y="BodyWt", data=df_filtered)
        # Display the figure in the Streamlit app
        st.pyplot(plt)
        plt.close()
        

eda()

col1, col2, col3 = st.columns([1,11,1])

if col1.button("⬅️"):
    st.markdown(switch_page("project 💤"))
if col3.button("➡️"):
    st.markdown(switch_page("Exploratory Data Analysis 📈2️⃣"))
