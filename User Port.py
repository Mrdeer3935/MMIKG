import streamlit as st
from PIL import Image
from streamlit_player import st_player

st.balloons()
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st.image(Image.open("logo.png"))
# col4, col5, col6 = st.columns((0.1, 4, 0.1))
    # with col5:
st.image(Image.open("User Port.png"))

st.markdown("# What is the MMiKG?")
st.write("""
Integrate the existing knowledge of the gut-brain axis and present it in the form
 of a knowledge graph, which is called MMiKG. In this research, our team collected 
 critical knowledge by reading a large amount of literature and mined the GraphXR 
 platform and Neo4j database for visualization and implicit information, respectively.
            For full details
            [read the paper](https://www.sciencedirect.com/science/article/pii/S0016703721005007)!
            """)
with st.expander("Note:"):
    st.markdown(
        """
    - Particularly,MMiKG is a novel knowledge graph constructed by Fujian Medical University, providing visualization of MGB-axis-related relations and deeper data mining of similarity validation and linkage predictions.
    - Whereas, there is still mass of information not contained in MMiKG and the predicting results are not 100% accurate, which only provide a referring evidence for biological and clinical experiment. 
    - Welcome interested users to provide constructive suggestions for MMiKG.
    """
    )

st.markdown("# Let's explore the MMiKG!")
st.markdown("""
            Model, analyze and visualize data with unprecedented speed, power and flexibility. GraphXR is a browser-based visual analytics platform for solving ever-changing scenarios and unforeseen problems.

KineViz is an enterprise graphical analysis tool capable of rendering huge graphs (>100,000 elements) in two or three dimensions.KineViz supports loading data from CSV, JSON or Neo4j using Cypher. The KineViz User Guide provides detailed descriptions of all KineViz features：
1. Perform time series, geospatial, and social network analysis.
2. Perform statistical analysis on large and complex datasets.
3. Visualize over 100,000 nodes in a variety of 3D and 2D layouts.
4. Collaborate, export, and report data in a variety of formats.
            """)

st.markdown("## How to use GraphXR?")
st.markdown("""
            The instructions are as follows.
            """)

st_player("https://youtu.be/PG83PbP6exc?list=PLXpADR-eMJRJilQczveaotpgtXSHHb3A3")

st.markdown("## Usage Portal")
st.markdown("##### You can [click me](https://graphxr.kineviz.com/share/642a27d43bb85f15085ce4a2/Gut-Brain_final/642a32c83bb85f15085d1a10) to enter the MMiKG.")
st.markdown("##### If you want to mine deeper knowledge, you can do as follows.")
col7, col8, col9 = st.columns((1, 4, 1))
with col8:
    st.image(Image.open("Port.png"))