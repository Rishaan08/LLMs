import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

#Function to get response from Llama2 model
def get_llama_response(input_text,no_words,blog_style,tone,blog_type):
    llm = OllamaLLM(model='llama2', temperature=0.01)
    template = ChatPromptTemplate.from_template("""Write a blog for {blog_style} for a topic 
                                                {input_text} within {no_words} words, tone should 
                                                be {tone} and it should be {blog_type}.""")

    prompt = template.format(
    blog_style=blog_style,
    input_text=input_text,
    no_words=no_words,
    tone=tone,
    blog_type=blog_type
    )
    response = llm.invoke(prompt)
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs",
                    page_icon='🪶',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("AI Writes 🪶")

input_text = st.text_input("Enter the blog topic")

#Creating more columns for additional fields
col1, col2, col3, col4 = st.columns([5,5,5,5])

with col1:
    no_words = st.text_input("Number of words")

with col2:
    blog_style = st.selectbox("Audience", ('Researchers','DataScientist','Students','Buisness Professionals'),index=0)

with col3:
    tone = st.selectbox("Tone", ('Professional','Casual','Technical','Persuasive'),index=0)

with col4:
    blog_type = st.selectbox("Type", ('Tutorial','Opinion','Guide','Case Study'),index=0)

submit = st.button("Generate")

#Final Response
if submit:
    response = get_llama_response(input_text,no_words,blog_style,tone,blog_type)
    st.write(response)
