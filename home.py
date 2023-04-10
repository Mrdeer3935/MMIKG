
import streamlit as st
from PIL import Image

st.balloons()
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st.image(Image.open("logo.png"))
# col4, col5, col6 = st.columns((0.1, 4, 0.1))
# with col5:
st.image(Image.open("home.png"))

header = 'Background of Mental Diseases'
st.title(header)
Back="As is well known, mental diseases refer to diseases " \
     "that affect emotions, thoughts, and behavior, including" \
     " anxiety disorders, depression, schizophrenia, and bipolar " \
     "disorder. The incidence of mental diseases is increasing year" \
     " by year globally, and the onset age tends to be younger. This " \
     "disease greatly impacts patients’ physical and psychological " \
     "health, as well as a heavy burden on families and society. " \
     "However, many ways to treat mental diseases include medication," \
     " psychotherapy, and physical therapy. In short, treating mental " \
     "diseases requires multidisciplinary cooperation, including psychiatrists," \
     " psychologists, rehabilitation doctors, social workers, etc. It also requires " \
     "continuous innovation and exploration of treatment methods based on " \
     "scientific research and clinical practice. In the 21st century, " \
     "treating mental diseases is no longer limited to a single drug or " \
     "psychotherapy. Still, it has begun to explore individualized precision " \
     "treatment, such as gene therapy, light therapy, neurofeedback therapy, etc. " \
     "At the same time, the application of new technologies such as electronic " \
     "health records and telemedicine has brought new opportunities for treating " \
     "mental diseases. However, there are still challenges in treating mental diseases; " \
     "some patients cannot receive timely treatment, and there is drug resistance " \
     "to medication. In summary, the study of mental diseases has broad development space, " \
     "especially in the field of neuroscience and genetic research, which can help to " \
     "understand the mechanism of mental diseases better and implement personalized treatment."
st.markdown(Back)

st.title("What is Gut-Brain Axis?")
col7, col8 = st.columns((3 ,2))
with col7:
    st.markdown("The gut microbiota has an essential impact on mental diseases through "
                "the communication pathway of the gut-brain axis, which refers to the interaction between the gut and the brain. "
                "Studies have shown that the gut-brain axis is essential to treating "
                "mental diseases. It can affect the function and behavior of the brain by "
                "regulating the gut microbial community. Gut microbiota can secrete a variety "
                "of neurotransmitters and metabolites, which can affect the function of the"
                " brain through multiple pathways, such as the nervous, endocrine, and immune "
                "systems. For example, Bifidobacterium can improve depressive and anxiety "
                "symptoms by regulating the gut immune system, improving gut barrier function, "
                "and producing short-chain fatty acids. Lactobacillus can improve"
                " anxiety and autism symptoms by regulating neurotransmitter levels, improving "
                "gut permeability, and reducing inflammation. Saprophytic bacteria can improve "
                "social phobia symptoms by producing short-chain fatty acids and regulating "
                "the gut immune system. In addition, by changing diet and lifestyle, "
                "the gut-brain axis can be regulated to improve the symptoms of mental "
                "diseases. For example, some studies have shown that some dietary factors "
                "such as probiotics, prebiotics, and omega-3 fatty acids have a positive "
                "effect on regulating the gut microbial community and improving the symptoms "
                "of mental diseases. These treatment methods have been applied in some studies "
                "and clinical practices, but more research is needed to fully understand the "
                "role of the gut-brain axis in treating mental diseases. ")
with col8:
    image = Image.open('gut-brain.png')
    st.image(image, caption='**Gut-Brain Axis**')

st.title("What is Knowledge Graph?")
col9, col10 = st.columns((2 ,3))
with col10:
    st.markdown(" knowledge graph is a semantic network structure that forms a graph"
                " with semantic associations by linking different knowledge elements."
                " Knowledge graphs can help doctors better understand the essence and"
                " pathogenesis of diseases to develop better treatment plans and provide"
                " personalized treatment plans and decision support for doctors based on"
                " patients’ personal information and disease data. Guo et al. developed an"
                " early diagnosis system for autism by constructing a knowledge graph of"
                " autism by integrating relevant information such as gene mutations and"
                " neuron connections. Then, through machine learning algorithms, the system"
                " matches children’s personal information with the knowledge graph to achieve"
                " an early diagnosis of autism.  Zhao et al. collected and extended information"
                " on biomarkers and neurotransmitter changes in depression based on a knowledge"
                " graph and established a drug discovery system to find potential drugs, which"
                " were validated for their effectiveness. In our work, the knowledge graph can"
                " collect and integrate relevant information on the microbiome-gut-brain axis"
                " and its complex relationships with mental diseases to assist us in semantic"
                " search and visualization operations. In summary, the microbiome platform"
                " based on a knowledge graph can make the scattered and accumulated knowledge"
                " machine-readable and interpretable to enhance users’ trust in the accuracy"
                " of the information, thereby searching for potential relationships to support"
                " better decision-making. Researchers can integrate various relevant resources"
                " through knowledge graphs and infer potential associations between gut microbiota"
                " and mental diseases, to better understand the pathogenesis of mental diseases"
                " and provide ideas for further optimizing treatment measures. At the same time,"
                " it can also support research on mental diseases and promote the development of"
                " the mental health field.")
with col9:
    st.markdown("")
    st.markdown("")
    st.markdown("")
    image = Image.open('KG.png')
    st.image(image, caption='**Knowledge Graph**')