import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib

from upsetplot import generate_counts, UpSet, from_memberships,plot
from matplotlib import pyplot as plt
from io import BytesIO
import base64

matplotlib.use("Agg")



st.balloons()
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st.image(Image.open("logo.png"))
# col4, col5, col6 = st.columns((0.1, 4, 0.1))
    # with col5:
st.image(Image.open("Case shows.png"))



header = 'Visualization'
st.title(header)
Back="Theoretically, visualization of a" \
     " knowledge graph is to display the" \
     " data and information in the knowledge" \
     " graph in a visual way so that users" \
     " can understand the content and relationships" \
     " in the knowledge graph in a more intuitive" \
     " and easy-to-understand manner. In addition," \
     " visualization facilitates the exploration and" \
     " discovery of hidden information and new correlations" \
     " in the knowledge graph to uncover new knowledge." \
     " We also provide an interactive approach to" \
     " support decision-making and planning so that users" \
     " can freely explore and control the data and information" \
     " in the knowledge graph to meet their needs better." \
     " The following figure illustrates the visualization of our knowledge" \
     " graph. Gut microbiota, intermediates, and mental diseases" \
     " are labeled with different icons. We also define a "'connectivity'" for" \
     " each entity to show its importance in the knowledge graph," \
     " which is displayed visually in node size. The relationship" \
     " between entities is identified as “Promote”, “Associated”," \
     " and “Inhibit” and shown as directed lines in green, blue, and red," \
     " respectively. Similarly, for the repeated triples in the extracted" \
     " data, we propose using the directed lines’ width to reflect the frequency" \
     " of recurrence of the relationships. In short, larger nodes and" \
     " thicker directed line segments are information of greater" \
     " research significance in the knowledge graph."
st.markdown(Back)


col7, col8, col9 = st.columns((1, 4, 1))
with col8:
    st.image(Image.open("Visual.png"))

st.markdown("## Entity Relevance Display")

with st.expander("Note:"):
    st.markdown("""
    - This image shows the association between different diseases, quantified by the number of gut microbes that string the diseases together.
    - Specifically, we want to explore the degree of association between autism and schizophrenia, which can be shown by the number of microorganisms that are associated with the two diseases.
    - You can select the disease you are interested in from the box below.
    """)

entity = st.multiselect(
    'Please select the disease you wish to compare!',
    ['Autism', "Parkinson's Disease", 'Depression', 'Schizophrenia','Major Depressive Disorder','Others','Anxiety',"Alzheimer's Disease",
     "Chronic fatigue syndrome","Rem sleep behavior disorder","Bipolar Disorders","Attention deficit hyperactive disorder","Post-Traumatic Stress Disorder",
     "Stress Syndrome"])
@st.cache
def return_data():
    import pandas as pd
    df = pd.read_csv("output.csv")
    return df

data = return_data()
data_by_dis = from_memberships(data.Disease.str.split(','), data=data)

# 在Streamlit应用程序中显示UpSet plot
# upset = UpSet(data_by_dis,show_counts=True,sort_by='cardinality',min_subset_size=2)
upset = UpSet(data_by_dis, show_counts=True, sort_by='cardinality', min_subset_size=2)
upset.style_subsets(present=entity,
                    facecolor="red",)
upset.plot()
col10,col11,col12 = st.columns((1,3,1))
with col11:
    st.pyplot(plt.gcf())

st.title("Mining Knowledge")
st.markdown("To explore the possible connections"
            " between gut microbiota, intermediates,"
            " and mental diseases in the knowledge graph,"
            " we save the knowledge of GraphXR in the Neo4j"
            " database and further explore the existing"
            " knowledge through Neo4j's graph data algorithm"
            " to optimize the treatment options for mental"
            " diseases. For researchers who do not have a"
            " programming background or knowledge of MMiKG,"
            " we propose to build a user-friendly knowledge"
            " graph platform with Neo4j. Therefore, we have"
            " designed mining pathways to facilitate user learning"
            " and practice for the four needs. The Cypher"
            " mining approach based on the Neo4j graph algorithm"
            " is used as a template that users can adapt to their needs.")

option = st.selectbox(
    'Which task would you like to mine?',
    ('Task 1', 'Task 2', 'Task 3'))
result = st.checkbox('Show results or not')

if option=="Task 1" :
    st.markdown("## Mining Homologous Disease")
    st.markdown("Homologous mental diseases have similar"
                " etiology and symptoms, so their treatment"
                " needs to consider various factors such"
                " as the type of disorder, severity of symptoms,"
                " individual patient differences and family"
                " genetic background, and individualized treatment"
                " plans to achieve the best treatment results."
                " At the same time, the treatment process requires"
                " continuous follow-up and management to avoid"
                " adverse effects and relapse. However, co-treatment"
                " of homozygous mental diseases can improve treatment"
                " outcomes, reduce treatment burden, facilitate condition"
                " management and reduce social costs. In this context,"
                " we are interested in how to identify different"
                " disorders caused by similar gut microorganisms"
                " within the existing knowledge of the gut-brain"
                " axis and thus by studying their causative mechanisms"
                " for more efficient treatment. We assume that a person"
                " suffers from depression as well as anxiety disorders."
                " We want to explore whether the causative factors of anxiety"
                " disorders can be considered while treating depression,"
                " thus providing a synergistic treatment effect. ")
    code = '''CALL gds.graph.project(
           'myGraph1',
           ['Diseases', 'Intermediate','Microbiota'],
           {Associated: {properties: {}},
           Inhibit: {properties: {}},
           Promote: {properties: {}}
    });
MATCH (p1:Microbiota)-[:Promote]->(q1:Diseases{name:'Depression'})                        
WITH q1, collect(id(p1)) AS p1ID                                                             
MATCH (p2:Microbiota)-[:Promote]->(q2:Diseases)                                                   
WITH q1, p1ID, q2, collect(id(p2)) AS p2ID       
RETURN q1.name AS from, q2.name AS to, gds. similarity.jaccard(p1ID, p2ID) AS similarity
MATCH(p3:Microbiota)-[:Promote]->(q3:Diseases{name:'Depression'})                               
WITH q3, collect(id(p3)) AS p3ID                                                            
MATCH (p4:Microbiota)-[:Promote]->(q4:Diseases)                                                   
WITH q3, p3ID, q4, collect(id(p4)) AS p4ID       
RETURN q3.name AS from, q4.name AS to, gds.similarity.overlap(p3ID, p4ID) AS similarity
'''
    st.code(code, language='cypher')
    if result:
        st.markdown("## Result show")
        st.markdown("The results show six disorders,"
                    " including Anxiety, Autism, Parkinson's"
                    " Disease (ADHD), Schizophrenia, Alzheimer's Disease,"
                    " and Attention Deficit Hyperactive Disorder."
                    " We defined by Neo4j graph algorithm the Homologous Index(HI)"
                    " to indicate the degree of similarity of diseases"
                    " affected by different microbiota. In addition,"
                    " we calculated the HI with Jaccard and Overlap indexes,"
                    " respectively. The mining results are shown in"
                    " following figure, which shows Depression as the source"
                    " and the rest of the diseases in descending order of HI."
                    " In short, diseases closer to Depression have greater research"
                    " value for synergistic treatment. However, ADHD and Alzheimer's"
                    " Disease are almost not homologous in nature. In conclusion,"
                    " the knowledge graph can uncover potentially synergistic treatable diseases. ")
        col10, col11, col12 = st.columns((1, 4, 1))
        with col11:
            image = Image.open('CASE1.png')
            st.image(image, caption='**Mining Task1**')


if option=="Task 2" :
    st.markdown("## Mining Co-pathway Microbiota")
    st.markdown("Currently, the treatment of mental diseases is"
                " mainly carried out using medication and"
                " psychotherapy. However, the effectiveness"
                " of these treatments is limited and there are"
                " many adverse effects. By tapping into gut microbiota"
                " with common pathways, new ideas can be provided"
                " for treating mental diseases. For example, by"
                " modulating the structure of the gut microbial"
                " community, the neurotransmitter metabolism and"
                " immune function of the host can be improved,"
                " thereby reducing the symptoms and risk of mental"
                " diseases. In addition, studying these microbiota"
                " may also provide insights into the development of"
                " novel antimicrobial drugs. With the increasing"
                " antibiotic abuse and resistance, the search for"
                " new antimicrobial drugs has become imperative."
                " Understanding the interactions and common pathways"
                " between microorganisms can help us discover new"
                " targets and directions for drug development. Our"
                " case of interest is a depressed patient carrying"
                " two bacteria, Ruminococcus gnavus and L. plantarum,"
                " yet we do not know the mechanism of L. plantarum.")
    code = '''CALL gds.graph.project(
            'myGraph1',
            ['Diseases', 'Intermediate','Microbiota'],
            {Associated: {properties: {}},
            Inhibit: {properties: {}},
            Promote: {properties: {}}
});
MATCH(p1:Microbiota{name:'Ruminococcus gnavus'})-[:Promote]->(q1:Intermediate)
WITH p1,collect(id(q1)) AS p1ID
MATCH(p2:Microbiota)-[:Promote]->(q2:Intermediate)
WITH p1, p1ID,p2,collect(id(q2)) AS p2ID
RETURN p1.name AS from, p2.name AS to, gds.similarity.overlap(p1ID, p2ID) AS similarity
MATCH(p3:Microbiota{name:'Ruminococcus gnavus'})-[:Promote]->(q3:Intermediate)
WITH p3,collect(id(q3)) AS p3ID
MATCH (p4:Microbiota)-[:Promote]->(q4:Intermediate)
WITH p3, p3ID,p4,collect(id(q4)) AS p4ID
RETURN p3.name AS from, p4.name AS to, gds.similarity.jaccard(p3ID, p4ID) AS similarity
'''
    st.code(code, language='cypher')
    if result:
        st.markdown("## Result show")
        st.markdown("Thus, knowledge graph can open up new areas"
                    " of drug development by analyzing a given microbiota's"
                    " pathogenic mechanisms and pathways. Specifically,"
                    " we still defined Co-pathway Index in two ways,"
                    " which aims to quantify the similarity of pathogenic"
                    " pathways of different microbiota. Finally, the"
                    " following table shows the results listing the Co-pathway"
                    " relationships of Ruminococcus gnavus with the rest"
                    " of the microbiota. In summary, we were unable to"
                    " explore the pathogenic mechanism of L. plantarum"
                    " due to the higher correlation of Ruminococcus gnavus"
                    " with B. longum and L. helveticus.")
        col13, col14, col15 = st.columns((1, 4, 1))
        with col14:
            data=pd.read_csv("CASE2.csv")
            st.table(data)


if option=="Task 3" :
    st.markdown("## Topological Linkage Prediction of Potential Interaction Machanism")
    st.markdown("Our target in building knowledge graph is to explore"
                " deeper, underlying relationships among nodes"
                " that didn’t exist in our original graph data."
                " We briefly call it “Linkage Prediction”. Link"
                " prediction involves guessing which unknown connections"
                " between existing nodes in the graph are more likely"
                " to be convincing and experimentally feasible now or"
                " in the future. That is to say, it was so meritorious"
                " that it was possible to instruct biological and clinical"
                " experiments, which enhanced the practical utility of our"
                " knowledge graph. After a full-workflow of Linkage prediction,"
                " we surprisingly discovered the potential interactions"
                " among Microbiota, Intermediate and Diseases, revealing"
                " brand-new thinking to research on Gut-brain axis and mental diseases.")
    code = '''MATCH (Inter1) MATCH (inter2) WHERE Inter1<> inter2
RETURN  Inter1.name as Inter1_name,
                    inter2.name as inter2_name,  
                    gds.alpha.linkprediction.adamicAdar(inter1, inter2, {
                    relationshipQuery: "Associated",
                    direction: "BOTH"
                     }) as score
//If interested in the predicting results about the relation of “Promote” and “Inhibit”, then just replace the parameter ‘relationshipQuery’ value to “Promote” and “Inhibit”.
'''
    st.code(code, language='cypher')
    if result:
        st.markdown("## Result show")
        st.markdown("We surprisingly found out that Ruminococcus gnavus"
                    " was predicted to be associated with both Schizophrenia"
                    " and Parkinson's Disease, denoting that this genre of"
                    " gut microbiota could be a critical adjusting element"
                    " in mental diseases mechanism, influencing multiple types"
                    " of mental diseases. Meanwhile, GABA and Lactate, occurred"
                    " as a pair, were demonstrated to impact and promote Schizophrenia"
                    " and Major Depressive Disorder, indicating that GABA"
                    " and Lactate was possible to generated by the same type"
                    " of microbiota, and participated in the other reactions"
                    " together, too. Similarly, it could be elucidated that"
                    " Butyrate was also a key metabolite manipulating the"
                    " mechanism of both Anxiety, Bipolar Disorders and Depression,"
                    " so as to Cortisol and Kynurenine, strongly correlated to mental diseases. ")
        col16, col17, col18 = st.columns((1, 4, 1))
        with col17:
            image = Image.open('CASE3.png')
            st.image(image, caption='**Mining Task3**')


