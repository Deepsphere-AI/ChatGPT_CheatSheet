import streamlit as st
import pandas as pd

def Chatgpt_Cheat():
    w1,col1,col2,w2=st.columns((1.5,2.5,4,.1))
    cc2,cc1,cc3=st.columns((2,6,0.2))
    col11,col22,col33=st.columns((2,6,0.2))
    with col1:
        st.write('# ')
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Category</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_Category = ['Select','Jailbreak','Role Playing','Learning','Writing Styles','Learning How to Prompt?']
        vAR_input = st.selectbox('',vAR_Category)

################################ Jailbreak #################################################
    if vAR_input =='Jailbreak':
        with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Functionality</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_Category_Jailbreak = ['Select','The Jailbreak Prompt','The DAN 6.0 Prompt','The S.T.A.N Prompt','The DUDE Prompt','Illegality Mode','Alphabreak','Developer Mode','ChatGPT']
            vAR_input = st.selectbox('',vAR_Category_Jailbreak)

################################ Role Playing #################################################
    elif vAR_input =='Role Playing':
        with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Functionality</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_Category_Role_Playing = ['Select','Act like Elon','Act like Bill Gates','Act like GaryVee','Act like an Interviewer','Act like an Etymologist','Act like a Pro Marketer','Act like a Consultant','Act like an Assistant','Act like an SEO Specialist','Act like a coder','Act like an Human','Act like an Selfish AI bot']
            vAR_input = st.selectbox('',vAR_Category_Role_Playing)

################################ Learning #################################################
    elif vAR_input =='Learning':
        with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Functionality</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_Category_Learning = ['Select','Summarize X','Like a 5th Grader','Plagarism Checker','X Teacher','Writing Tutor','Career Counsllor','Translator','Traval Guide','Personal Trainer','Finacial Assistant']
            vAR_input = st.selectbox('',vAR_Category_Learning)

################################ Writing Styles #################################################
    elif vAR_input =='Writing Styles':
        with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Functionality</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_Category_Writing_Styles = ['Select','Formal','Informal','Pesuasive','Descriptive','Humoros','Narrative','Inspirational','Confrontational']
            vAR_input = st.selectbox('',vAR_Category_Writing_Styles)

################################ Learning How to Prompt? #########################################
    elif vAR_input =='Learning How to Prompt?':
        with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Functionality</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_Category_Learning_How_to_Prompt = ['Select','Open-End','Multiple Choise','Fill in the Planks','Binary','Ordering','Prediction','Explaination','Opinion','Instructor','Scenario','Comparative','Feedback']
            vAR_input = st.selectbox('',vAR_Category_Learning_How_to_Prompt)