import streamlit as st
from PIL import Image

st.balloons()
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st.image(Image.open("logo.png"))
    # col4, col5, col6 = st.columns((0.1, 4, 0.1))
    # with col5:
st.image(Image.open("MMiKG.png"))

col7, col8 = st.columns((2, 2))
with col7:
    header = 'How to Collect Data?'
    st.title(header)

    st.markdown("Mass of intermediate materials, including "
                "neurotransmitters, BDNF, SCFA etc., made"
                " huge contributions to the interaction between "
                "microbiota and mental diseases, regulating "
                "and manipulating an abundance of essential"
                " biological functional pathways and processes,"
                " which is a second to none element in the discovery"
                " of gut-brain axis. In this research, we defined three"
                " relevant labels to elucidate Microbiota-Gut-Brain-axis:"
                " Microbiota, Intermediate and Diseases, as the"
                " basic logical schema to construct the knowledge graph."
                " Searching through plentiful bibliographic retrieval"
                " databases, covering Pubmed, Springer, Google Scholar etc."
                " , we carefully selected 907 literatures related to gut-brain"
                " axis and mental diseases, using the keywords: gut-brain axis,"
                " mental diseases, depression,  schizophrenia, anxiety, autism,"
                " bipolar disorders.")

    st.success('First step', icon='✅')

with col8:
    header = 'How to Extract Information?'
    st.title(header)

    st.markdown("As artificial intelligence progressed rapidly,"
                " text mining and semantic data extraction"
                " technology has become more and more widespread"
                " and popular in relative domain, so as to"
                " knowledge graph, namely Natural Language"
                " Processing (NLP). There’s growing evidence"
                " that NLP algorithms are highly effective in"
                " relation extraction and named entity recognition"
                " task, which are important procedures during the"
                " process of knowledge graph construction. Consequently,"
                " we apply NLP text extraction algorithms in knowledge"
                " graph construction, too, with thousands of triples"
                " recognized and extracted, which are manually corrected"
                " later to fit our needs and logical schema. Ultimately,"
                " with human reading literature, too, we summarize 1257"
                " triples by both NLP extraction and manual reading to"
                " construct our knowledge graph. ")

    st.success('Second step', icon='✅')

col9, col10, col11 = st.columns((1, 4, 1))
with col10:
    image = Image.open('flow-chart.png')
    st.image(image, caption='**Flow chart**')

col12, col13 = st.columns((2, 2))
with col12:
    header = 'How to Visualize?'
    st.title(header)

    st.markdown("We visualized the data by GraphXR,"
                " which fully supports standard data"
                " analysis workflows for data filtering "
                "and further analysis, and users could"
                " elegantly create dimensionless and "
                "insightful data visualizations through"
                " its 3D data geometry layout. In this way,"
                " we can use the graph algorithms of both software"
                " to analyze each entity node of microbiota,"
                " intermediates and diseases as well as the relational"
                " edges representing “Promote”, “Inhibit” and “Associated”."
                " In GraphXR, we apply relational depth algorithm from"
                " GraphXR centrality calculations to calculate the"
                " connectivity of each node and to reflect the importance"
                " of that node in terms of the size of the node."
                " Similarly, for repeated relational edges, we display"
                " different relational line thinness based on the"
                " importance of the edge layout. ")

    st.success('Third step', icon='✅')

with col13:
    header = 'How to Mine?'
    st.title(header)

    st.markdown("Moreover, we also utilize Neo4j Graph Data Science"
                " module to analyze and probe more deeply"
                " into our knowledge graph.  Neo4j Graph Data"
                " Science module contains mass of graph algorithms"
                " and machine learning pipelines, including similarity"
                " calculation and linkage prediction, which provides"
                " a superb choice to discover more about graph data."
                " We implement similarity calculation and linkage"
                " prediction algorithms available in Neo4j and"
                " figure out some intriguing results on the status"
                " of microbiome which are available on the webserver.")

    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.success('Fourth step', icon='✅')
