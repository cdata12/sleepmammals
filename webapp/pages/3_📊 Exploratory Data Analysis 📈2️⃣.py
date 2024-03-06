import sys
sys.path.append("pages")

import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
from matplotlib import pyplot as plt
from streamlit_extras.switch_page_button import switch_page

#hidden or visible
st.markdown("""
    <style>
    #MainMenu {visibility: visible;}
    footer {visibility: visible;} 
    </style>
    """, unsafe_allow_html=True)

# Function to display a Seaborn jointplot in Streamlit
def display_jointplot(x, y, data, kind="reg"):
        # Create a jointplot
        g = sns.jointplot(x=x, y=y, data=data, kind=kind)
        plt.tight_layout() 
        st.pyplot(g.figure)
        plt.close() 

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

@st.cache_data
def eda_2():
    path_csv = "sleep_mammals_LAST_all_columns_23_02.csv"
        
    df =  pd.read_csv(path_csv, sep=",", index_col=0)
    df_sleep = pd.read_csv(path_csv, sep=',', index_col = False)

    n = len(df)

    df = df_sleep.copy()
    df_filtered = df[df["BodyWt"] <= 56934.5294120]
    st.header("Analysis - part 2")
    with st.expander("3.3 Brain Weight"):
        f"""
        ```python
        sns.set_theme(style="white")
        sns.displot(df, x="BrainWt", bins=50, kde=True)
        plt.xlabel("Brain Weight (G)", fontsize=10, fontweight="normal")
        plt.ylabel("Count", fontsize=10, fontweight="normal")
        plt.title("Brain Weight Distribution", fontsize=11, fontweight="normal")
        plt.show()
        ```
        """

        # Create the plot
        plt.figure(figsize=(10, 6))  # Adjust figure size as needed
        sns.histplot(df, x="BrainWt", bins=50, kde=True)
        plt.xlabel("Brain Weight (G)", fontsize=10, fontweight="normal")
        plt.ylabel("Count", fontsize=10, fontweight="normal")
        plt.title("Brain Weight Distribution", fontsize=11, fontweight="normal")

        # Display the plot in the Streamlit app
        st.pyplot(plt)
        plt.close()
        ################################

        f"""
        ```python
        sns.set_theme(style="whitegrid")
        sns.scatterplot(x="TotalSleep", y="BrainWt", data=df, hue="Vore")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title="Vore")
        plt.show()

        sns.scatterplot(x="Dreaming", y="BrainWt", data=df, hue="Vore")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title="Vore")
        plt.show()
        ```
        """

        sns.set_theme(style="whitegrid")

        # Plot 1: TotalSleep vs. BrainWt
        plt.figure(figsize=(10, 6))  # Adjust figure size as needed
        sns.scatterplot(x="TotalSleep", y="BrainWt", data=df, hue="Vore")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title="Vore")
        st.pyplot(plt)  # Display the first plot in Streamlit
        plt.close()

        # Plot 2: Dreaming vs. BrainWt
        plt.figure(figsize=(10, 6))  # Create a new figure for the second plot
        sns.scatterplot(x="Dreaming", y="BrainWt", data=df, hue="Vore")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title="Vore")
        st.pyplot(plt)  # Display the second plot in Streamlit
        plt.close()
        ################################
        f"""
        ```python
        sns.set_theme(style="whitegrid")
        sns.jointplot(x="TotalSleep", y="BrainWt", data=df, kind="reg")
        sns.jointplot(x="Dreaming",   y="BrainWt", data=df, kind="reg")
        ```
        """

        sns.set_theme(style="whitegrid")

        # Display the first jointplot
        display_jointplot(x="TotalSleep", y="BrainWt", data=df, kind="reg")

        # Display the second jointplot
        display_jointplot(x="Dreaming", y="BrainWt", data=df, kind="reg")

        st.info("From the charts above, it is evident that individuals with larger brains do not necessarily enjoy better sleep patterns or have longer dream time.")
        ################################

    with st.expander("3.4 Life Span"):
        f"""
        ```python
        sns.set_theme(style="white")
        sns.displot(df, x="LifeSpan", bins=100, kde=True)
        plt.xlabel("LifeSpan", fontsize=10, fontweight="normal")
        plt.ylabel("Count", fontsize=10, fontweight="normal")
        plt.title("Life Span Distribution", fontsize=16, fontweight="normal")
        plt.show()
        ```
        """
        sns.set_theme(style="white")

        # Create the plot with histplot for compatibility with plt methods
        plt.figure(figsize=(10, 6))
        sns.histplot(df, x="LifeSpan", bins=100, kde=True)
        plt.xlabel("LifeSpan", fontsize=10, fontweight="normal")
        plt.ylabel("Count", fontsize=10, fontweight="normal")
        plt.title("Life Span Distribution", fontsize=16, fontweight="normal")

        # Display the plot in Streamlit
        st.pyplot(plt)
        plt.close()
        ################################

        f"""
        ```python
        fig = px.histogram(df, "LifeSpan", color="Species", nbins=20, 
                        color_discrete_sequence=px.colors.sequential.Sunset,
                        title="Distribution of Life Span"
                        )
        fig.show()
        ```
        """
        # Create the Plotly histogram
        fig = px.histogram(df, x="LifeSpan", color="Species", nbins=20, 
                        color_discrete_sequence=px.colors.sequential.Sunset,
                        title="Distribution of Life Span")

        # Display the figure in the Streamlit app
        st.plotly_chart(fig)

        st.info("It is not doubt that human has longest life span in this data set. most of them lives less than 20k days.")

        ################################
        f"""
        ```python

        ## interactive on Vore hue
        fig = px.scatter(df, x="TotalSleep", y="LifeSpan", color="Vore")
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
        fig.show()


        fig = px.scatter(df, x="Dreaming", y="LifeSpan", color="Vore")
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
        fig.show()
        ```
        """
        
        # Create scatter plots
        fig1 = create_custom_scatter(df, "TotalSleep", "LifeSpan", "Vore")
        fig2 = create_custom_scatter(df, "Dreaming", "LifeSpan", "Vore")

        # Display the scatter plots in the Streamlit app
        st.plotly_chart(fig1)
        st.plotly_chart(fig2)
        st.info("It suggests that sleeping does not necessarily highly affect lifespans in mammals. Moreover, the Asian Elephant, which only sleeps around 2.5 hours, lives longer than most mammals in our dataset. Interestingly, dreaming less in some cases probably lead a longer life span. Then, We guess that the living environment likely plays a crucial role. Let us delve deeper into its significance.")
        ################################
        f"""
        ```python
        sns.set_theme(style="white")
        sns.jointplot(x="TotalSleep", y="LifeSpan", data=df, kind="reg")
        sns.jointplot(x="Dreaming", y="LifeSpan", data=df, kind="reg")
        ```
        """
        display_jointplot(x="TotalSleep", y="LifeSpan", data=df, kind="reg")

        display_jointplot(x="Dreaming", y="LifeSpan", data=df, kind="reg")

        st.info("It suggests that sleeping does not necessarily highly affect lifespans in mammals. Moreover, the Asian Elephant, which only sleeps around 2.5 hours, lives longer than most mammals in our dataset. Interestingly, dreaming less in some cases probably lead a longer life span. Then, We guess that the living environment likely plays a crucial role. Let us delve deeper into its significance.")

    with st.expander("3.5 Conservation"):
        f"""
        ```python
        sns.set_theme(style="white")
        sns.displot(df, x="Conservation", hue="Conservation",bins=50, kde=True)
        plt.xlabel("Conservation", fontsize=10, fontweight="normal")
        plt.ylabel("Count", fontsize=10, fontweight="normal")
        plt.title("Conservation Distribution", fontsize=11, fontweight="normal")
        plt.show()
        ```
        """
        sns.set_theme(style="white")

        # Create the plot
        g = sns.displot(df, x="Conservation", hue="Conservation", bins=50, kde=True)

        # Adjustments and titles using matplotlib due to sns.displot returning a FacetGrid
        g.set_xlabels("Conservation", fontsize=10, fontweight="normal")
        g.set_ylabels("Count", fontsize=10, fontweight="normal")
        g.figure.suptitle("Conservation Distribution", fontsize=11, fontweight="normal")

        # Show the plot in Streamlit
        st.pyplot(g.figure)
        plt.close()

        st.info("We Mannually set the importance of conservation to build our models. Following is our rules to encode them.")
        st.info("'dd' : 0 # data deficient")
        st.info("'domesticated' : 1 # domisticated")
        st.info("'lc' : 2 # least concern ")
        st.info("'nt' : 3 # near threatened")
        st.info("cd' : 4 # lr/cd lower risk : conservation dependent")
        st.info("'vu' : 5 # vulnerable ")
        st.info("'en' : 6 # endangered")
        st.info("'cr' : 7 # critically Endangered ")

        ################################
        f"""
        ```python
        sns.scatterplot(x="TotalSleep", y="Conservation", data=df,hue="Conservation")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title='Conservation Level')
        plt.show()

        sns.scatterplot(x="Dreaming", y="Conservation", data=df, hue="Conservation")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title='Conservation Level')
        plt.show()

        ```
        """
        sns.set_theme(style="whitegrid")

        plt.figure(figsize=(10, 6))
        sns.scatterplot(x="TotalSleep", y="Conservation", data=df, hue="Conservation")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title='Conservation Level')
        st.pyplot(plt)  
        plt.close()

        plt.figure(figsize=(10, 6))  # Create a new figure for the second plot
        sns.scatterplot(x="Dreaming", y="Conservation", data=df, hue="Conservation")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title='Conservation Level')
        st.pyplot(plt) 
        plt.close()
        
    #with st.expander("-                - part 2"):
        f"""
        ```python
        fig = px.pie(
            df, values="TotalSleep", 
            names="Conservation", 
            title="TotalSleep VS Conservation",
            color_discrete_sequence=px.colors.qualitative.Pastel1 

            )
        fig.show()
        fig = px.pie(
            df, values="Dreaming", 
            names="Conservation", 
            title="Dreaming VS Conservation",
            color_discrete_sequence=px.colors.qualitative.Pastel1 

            )
        fig.show()
        ```
        """
        fig_total_sleep = px.pie(
            df, values="TotalSleep",
            names="Conservation",
            title="TotalSleep VS Conservation",
            color_discrete_sequence=px.colors.qualitative.Pastel1
        )

        st.plotly_chart(fig_total_sleep)
        plt.close()
        # Create the second pie chart for Dreaming VS Conservation
        fig_dreaming = px.pie(
            df, values="Dreaming",
            names="Conservation",
            title="Dreaming VS Conservation",
            color_discrete_sequence=px.colors.qualitative.Pastel1
        )
        
        st.plotly_chart(fig_dreaming)
        plt.close()
        st.info("From the chart, \"2 - least concern\" have large ratio to get more sleep. But We can't be sure on thia as the sample size of 2 is much bigger than others. ")
        ################################
        f"""
        ```python
        sns.set_theme(style="white")
        sns.jointplot(x="TotalSleep", y="Conservation", data=df, kind="reg")
        sns.jointplot(x="Dreaming", y="Conservation", data=df, kind="reg")

        ```
        """
        display_jointplot(x="TotalSleep", y="Conservation", data=df, kind="reg")
    
        display_jointplot(x="Dreaming", y="Conservation", data=df, kind="reg")

        st.info("According to the regression, it is not evident that the conservation influence the sleep hours. Probably because of the data is imbalanced. We do have much larger sample on LC. ")
        ################################
   
eda_2()
col1, col2, col3 = st.columns([1,11,1])
if col1.button("⬅️"):
    st.markdown(switch_page("Exploratory Data Analysis 📈1️⃣"))
if col3.button("➡️"):
    st.markdown(switch_page("Exploratory Data Analysis 📈3️⃣"))
