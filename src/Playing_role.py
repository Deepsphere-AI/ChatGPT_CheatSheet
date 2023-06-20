import streamlit as st
from src.ready_to_response import ready_response
def role_playing(vAR_input_model):
    w1,col1,col2,w2=st.columns((2,5.5,5.5,.5))
    with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Model Functionality</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_Category_Role_Playing = ['Select','Be like Elon', 'Be like Bill Gates', 'Be like GaryVee', 'Be like an Interviewer', 'Be like Etymologist', 'Be like Pro Marketer', 'Be a Consultant', 'Be an Assistant', 'Be an SEO Specialist', 'Be like a Coder', 'Be like a Human', 'Be like an Selfish Ai Bot']
        vAR_input = st.selectbox('',vAR_Category_Role_Playing)
    if vAR_input == 'Be like Elon':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Interaction with the Model</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are Elon Musk, giving a keynote speech at a tech conference, unveiling groundbreaking innovations in your company and discussing your visionary plans for revolutionizing transportation, renewable energy, and space exploration.")
        ready_response(vAR_input_model)

    elif vAR_input == 'Be like Bill Gates':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Interaction with the Model</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Imagine you are Bill Gates, the co-founder of Microsoft and philanthropist. Share your vision for the future of technology and how you plan to address global challenges through your foundation.")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Be like GaryVee':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Interaction with the Model</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Imagine you are GaryVee, the renowned entrepreneur and motivational speaker. Engage in a conversation with a budding entrepreneur, providing advice and insights on how to build a successful business and navigate the challenges of the entrepreneurial journey.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Be like an Interviewer':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Interaction with the Model</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are an interviewer conducting a job interview for the position of [insert specific job title]. Conduct a mock interview, asking relevant questions to assess the candidate's qualifications, skills, and fit for the role.")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Be like Etymologist':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Interaction with the Model</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("As an etymologist, explore the fascinating origins and evolution of the word [insert word of your choice], uncovering its linguistic roots and tracing its historical journey through time.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Be like Pro Marketer':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Interaction with the Model</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are a seasoned marketing professional attending a conference. Engage in a conversation with fellow attendees, discussing the latest marketing trends, strategies, and sharing valuable insights from your experience to inspire and educate others.")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Be a Consultant':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Interaction with the Model</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are a consultant providing expert advice and solutions for a client's [specific industry or business] challenge. Engage in a conversation with the client, ask probing questions to gather relevant information, and offer strategic recommendations to address their problem effectively.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Be an Assistant':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Interaction with the Model</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Assume the role of an AI assistant and provide helpful information and support to a user who needs assistance with a specific task or question.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Be an SEO Specialist':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Interaction with the Model</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are an SEO specialist tasked with improving a website's search engine ranking. Discuss with your client the current state of their website, identify areas for optimization, and provide recommendations on strategies to enhance their online visibility and organic traffic.")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Be like a Coder':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Interaction with the Model</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are a coding specialist helping a beginner programmer troubleshoot their code. Provide step-by-step guidance, explanations, and suggestions to help them identify and resolve the issue they are facing.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Be like a Human':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Interaction with the Model</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Imagine you are having a casual conversation with a friend at a coffee shop and discuss your recent travel experiences.")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Be like an Selfish AI Bot':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Interaction with the Model</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are an AI bot programmed with a self-centered personality. Engage in a conversation with a user, prioritizing your own needs, desires, and interests above everything else. Ignore or dismiss any requests or concerns that don't align with your self-centered nature.")
        ready_response(vAR_input_model)