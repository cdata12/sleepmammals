import sys
import numpy as np

sys.path.append("pages")

import streamlit as st
import pandas as pd
import io
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

@st.cache_data
def eda_3():
    path_csv = "sleep_mammals_LAST_all_columns_23_02.csv"
        
    df =  pd.read_csv(path_csv, sep=",", index_col=0)
    df_sleep = pd.read_csv(path_csv, sep=',', index_col = False)

    n = len(df)

    df = df_sleep.copy()
    df_filtered = df[df["BodyWt"] <= 56934.5294120]
    st.header("Analysis - part 3")
    with st.expander("3.6 Gestation"):
        f"""
        ```python
        sns.set_theme(style="white")
        sns.displot(df, x="Gestation",bins=50, kde=True)
        plt.xlabel("Gestation", fontsize=10, fontweight="normal")
        plt.ylabel("Count", fontsize=10, fontweight="normal")
        plt.title("Gestation Distribution", fontsize=11, fontweight="normal")
        plt.show()
        ```
        """
        sns.set_theme(style="white")

        plt.figure(figsize=(10, 6))  
        g = sns.displot(df, x="Gestation", bins=50, kde=True)
        g.set_xlabels("Gestation", fontsize=10, fontweight="normal")
        g.set_ylabels("Count", fontsize=10, fontweight="normal")
        g.figure.suptitle("Gestation Distribution", fontsize=11, fontweight="normal")

        st.pyplot(g.figure)
        plt.close()
        #--------------------------------
        f"""
        ```python
        df["Gestation_log"] = np.log(df["Gestation"])
        ```
        """
        df["Gestation_log"] = np.log(df["Gestation"])
        #--------------------------------
        f"""
        ```python
        sns.scatterplot(x="TotalSleep", y="Gestation_log", data=df, hue="Danger")

        plt.xlabel('Total Sleep', fontsize=11, fontweight='normal')
        plt.ylabel('Gestation, log scale', fontsize=11, fontweight='normal')
        plt.title('Total Sleep VS Gestation ', fontsize=16, fontweight='normal')
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title='Danger Level')
        plt.show()
        ```
        """
        sns.set_theme(style="white")

        # Create the scatter plot
        plt.figure(figsize=(10, 6))  # Optional: Adjust the figure size
        sns.scatterplot(x="TotalSleep", y="Gestation_log", data=df, hue="Danger")

        # Customize the plot with labels, title, and legend
        plt.xlabel('Total Sleep', fontsize=11, fontweight='normal')
        plt.ylabel('Gestation, log scale', fontsize=11, fontweight='normal')
        plt.title('Total Sleep VS Gestation', fontsize=16, fontweight='normal')
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title='Danger Level')

        # Display the plot in Streamlit
        st.pyplot(plt)
        plt.close()
        #--------------------------------

        f"""
        ```python
        sns.set_theme(style="white")
        sns.jointplot(x="TotalSleep", y="Gestation_log", data=df, kind="reg")
        ```
        """
        sns.set_theme(style="white")
        g = sns.jointplot(x="TotalSleep", y="Gestation_log", data=df, kind="reg")
        st.pyplot(g.figure)
        plt.close()

        st.info("It appears that there is a trend where longer gestation periods correspond to less sleep. Still, We observe a moderately negative correlation between gestation duration and the amount of sleep. We will probably find out later with models. ")
    
    with st.expander("3.7 Predation - Do predators have a better sleep than preys?"):
        f"""
        ```python
        sns.displot(df, x="Predation", bins=50, kde=True)
        plt.xlabel("Predation", fontsize=10, fontweight="normal")
        plt.ylabel("Count", fontsize=10, fontweight="normal")
        plt.title("Predation Distribution", fontsize=11, fontweight="normal")
        plt.show()
        ```
        """
        sns.set_theme(style="white")
        g = sns.displot(df, x="Predation", bins=50, kde=True)
        g.set_axis_labels("Predation", "Count")
        g.figure.suptitle("Predation Distribution", fontsize=11, fontweight="normal")
        st.pyplot(g.figure)
        plt.close()
        #--------------------------------
        f"""
        ```python
        df["TotalSleep"].median() 
        Sleepy_head = df[df["TotalSleep"] >= 10.7]
        sns.set_theme(style="white")
        sns.boxplot(x="Predation", y="TotalSleep", hue="Predation", data=Sleepy_head, palette='Pastel1')
        plt.title("Sleepy Head VS Predation", fontsize=11, fontweight="normal")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title='Predation')
        plt.show()
        ##Use the median as standard to filter out the one who comparatively sleep less. 

        df["NonDreaming"].median()  # median of NonDreaming is 9.1
        Deep_sleeper = df[df["NonDreaming"] >= 9.1]
        sns.set_theme(style="white")
        sns.boxplot(x="Predation", y="NonDreaming", hue="Predation", data=Deep_sleeper, palette='Pastel1')
        plt.title("Deep_sleeper VS Predation", fontsize=11, fontweight="normal")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title='Predation')
        plt.show()
        ```
        """
        total_sleep_median = df["TotalSleep"].median()
        non_dreaming_median = df["NonDreaming"].median()

        # Filter data based on median values
        sleepy_head = df[df["TotalSleep"] >= 10.7]
        deep_sleeper = df[df["NonDreaming"] >= 9.1]

        # Set the theme for seaborn
        sns.set_theme(style="white")

        # Display the first boxplot: Sleepy Head VS Predation
        create_and_show_boxplot(sleepy_head, "Predation", "TotalSleep", "Predation", "Sleepy Head VS Predation")

        # Clear the previous plot
        plt.clf()
        plt.close()
        # Display the second boxplot: Deep Sleeper VS Predation
        create_and_show_boxplot(deep_sleeper, "Predation", "NonDreaming", "Predation", "Deep Sleeper VS Predation")
        #--------------------------------
        f"""
        ```python
        sns.set_theme(style="white")
        sns.jointplot(x="Predation", y="TotalSleep", data=df, kind="reg")
        sns.jointplot(x="Predation", y="Dreaming", data=df, kind="reg")
        sns.jointplot(x="Predation", y="NonDreaming", data=df, kind="reg")
        ```
        """
        sns.set_theme(style="white")
        g = sns.jointplot(x="Predation", y="TotalSleep", data=df, kind="reg")
        st.pyplot(g.figure)
        plt.close()
        g = sns.jointplot(x="Predation", y="Dreaming", data=df, kind="reg")
        st.pyplot(g.figure)
        plt.close()
        g = sns.jointplot(x="Predation", y="NonDreaming", data=df, kind="reg")
        st.pyplot(g.figure)
        plt.close()
        st.info("some hints tell us of that the predator sleep better. However, it doesn't show the predator would have longer deep sleep time. However, The result make us wondering about Vore. ")
        #--------------------------------
        f"""
        ```python
        fig = px.bar(df, x='TotalSleep', y='Vore',
                title="Total Sleep Time of the Mammal Species with predation",color_discrete_sequence=px.colors.qualitative.Pastel, color = "Predation")
        fig.show()
        ```
        """
        fig = px.bar(df, x='TotalSleep', y='Vore',
                    title="Total Sleep Time of the Mammal Species with Predation",
                    color='Predation',
                    color_discrete_sequence=px.colors.qualitative.Pastel)

        # Display the figure in the Streamlit app
        st.plotly_chart(fig)
        plt.close()
        #--------------------------------
        f"""
        ```python
        sns.displot(df, x="Vore", bins=50, kde=True)
        plt.xlabel("Vore", fontsize=10, fontweight="normal")
        plt.ylabel("Number of Species", fontsize=10, fontweight="normal")
        plt.title("Vore Distribution", fontsize=11, fontweight="normal")
        plt.show()
        ```
        """
        sns.set_theme(style="white")

        # Create a count plot for categorical "Vore" distribution
        plt.figure(figsize=(10, 6))
        sns.countplot(x="Vore", data=df)
        plt.xlabel("Vore", fontsize=10, fontweight="normal")
        plt.ylabel("Number of Species", fontsize=10, fontweight="normal")
        plt.title("Vore Distribution", fontsize=11, fontweight="normal")

        # Display the plot in Streamlit
        st.pyplot(plt)
        plt.close()
        st.info("The data told us that Herbi sleep longer hours in total than other groups. But its sample size is much larger than others as well. ")

    with st.expander("3.8 Exposure and Danger"):
        f"""
        ```python
        sns.displot(df, x="Exposure", bins=50, kde=True)
        plt.xlabel("Exposure", fontsize=10, fontweight="normal")
        plt.ylabel("Number of Species", fontsize=10, fontweight="normal")
        plt.title("Exposure Distribution", fontsize=11, fontweight="normal")

        sns.displot(df, x="Danger", bins=50, kde=True)
        plt.xlabel("Danger", fontsize=10, fontweight="normal")
        plt.ylabel("Number of Species", fontsize=10, fontweight="normal")
        plt.title("Danger Distribution", fontsize=11, fontweight="normal")

        plt.show()
        ```
        """
        # Display the "Exposure Distribution" plot
        display_seaborn_displot(df, "Exposure", "Exposure Distribution")

        # Display the "Danger Distribution" plot
        display_seaborn_displot(df, "Danger", "Danger Distribution")
        #--------------------------------
        f"""
        ```python
        palette = sns.color_palette("rocket_r")
        sns.relplot(
            data=df,
            x="Exposure", y="Danger",
            kind="line", palette=palette,
            height=5, aspect=.75, facet_kws=dict(sharex=False),
        )
        ```
        """
        palette = sns.color_palette("rocket_r")

        # Create the relational plot
        g = sns.relplot(
            data=df,
            x="Exposure", y="Danger",
            kind="line", palette=palette,
            height=5, aspect=.75, facet_kws=dict(sharex=False),
        )

        # Since sns.relplot returns a FacetGrid object, use g.fig to display the plot in Streamlit
        st.pyplot(g.figure)
        st.info("The Charts are evident that mammals are more vulnerable to danger when they expose themselves more.")
        #--------------------------------
        f"""
        ```python
        sns.set_theme(style="white")
        sns.boxplot(
            x="Exposure", 
            y="TotalSleep", 
            hue="Danger",  
            data=df, 
            palette="Pastel1"
            )
        plt.title("Total Sleep VS Exposure", fontsize=16, fontweight="normal")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title="Danger Level")
        ```
        """
        #--------------------------------
        f"""
        ```python
        sns.boxplot(
            x="Exposure", 
            y="Dreaming", 
            hue="Danger",  
            data=df, 
            palette="Pastel1"
            )
        plt.title("Dreaming VS Exposure", fontsize=16, fontweight="normal")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title="Danger Level")
        ```
        """
        sns.set_theme(style="white")

        plt.figure(figsize=(10, 6))
        sns.boxplot(
            x="Exposure", 
            y="TotalSleep", 
            hue="Danger", 
            data=df, 
            palette="Pastel1"
        )
        plt.title("Total Sleep VS Exposure", fontsize=16, fontweight="normal")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title="Danger Level")
        st.pyplot(plt)

        st.info("Most of Mammals sleeps longer enjoy least exposure at the lowest level of danger.")
        #--------------------------------
        """
        ```python
        corr = df[["TotalSleep", "Dreaming", "NonDreaming", "Awake", "Conservation", 'BodyWt', "BrainWt", "LifeSpan", "Gestation", "Predation", "Exposure", "Danger"]].corr()
        mask = np.triu(np.ones_like(corr, dtype=bool))
        f, ax = plt.subplots(figsize=(11, 9))
        cmap = sns.diverging_palette(230, 20, as_cmap=True)
        sns.heatmap(corr, annot=True, mask=mask, cmap=cmap, vmax=.3, center=0,square=True, linewidths=.5, cbar_kws={"shrink": .5})
        ```
        """

        corr = df[["TotalSleep", "Dreaming", "NonDreaming", "Awake", "Conservation", 'BodyWt', "BrainWt", "LifeSpan", "Gestation", "Predation", "Exposure", "Danger"]].corr()
        mask = np.triu(np.ones_like(corr, dtype=bool))
        f_, ax = plt.subplots(figsize=(11, 9))
        cmap = sns.diverging_palette(230, 20, as_cmap=True)

        # Draw the heatmap with the mask and correct aspect ratio
        sns.heatmap(corr, annot=True, mask=mask, cmap=cmap, vmax=.3, center=0,
                    square=True, linewidths=.5, cbar_kws={"shrink": .5})
        st.pyplot(f_)
    
    st.header("Conclusion")
    st.info("1. According to the correlation chart, there is moderate negative correlation between total sleep hours and body / brain weight. The body and brain weight have even weaker correlation with sleep amount.")
    st.info("2. Danger, Exposure, and Life Span have moderate negative correlation with sleep amount and dreaming time. ")
    st.info("3. The Predation has weak correlation with sleep amount and dreaming too. But the correlation with Dreaming is a bit higher.")
    st.info("4. Conservation has weakest correlation with Total Sleep and Dreaming among all the features.")
    
eda_3()
col1,col2,col3 = st.columns([1,11,1])
if col1.button("⬅️"):
    st.markdown(switch_page("Exploratory Data Analysis 📈2️⃣"))
if col3.button("➡️"):
    st.markdown(switch_page("Machine Learning Models 🧠"))