import streamlit as st
import os
import spacy 

from gensim.summarization.summarizer import summarize
from nltk_summarization import nltk_elaborate, nltk_executive, nltk_inshorts
from spacy_summarization import spacy_elaborate, spacy_executive, spacy_inshorts
from sumy_summarization import sumy_elaborate, sumy_executive, sumy_inshorts

from url_summarization import get_text
from reading_time import readingTime

from doc_upload import read_docx
from doc_upload import read_pdf

def app():
    #INPUT DATA OPTIONS
    st.markdown("""<style>
            .big-font4 {
            font-size:25px !important;
            }
            </style>"""
            , unsafe_allow_html=True)
    st.markdown('<p class="big-font4"><b>Select the Data Type:</b></p>', unsafe_allow_html=True)
    data_option = st.selectbox(' ',['Text', 'URL', 'Upload File'])
    st.markdown("""<style>
            .big-font3 {
            font-size:40px !important;
            }
            </style>"""
            , unsafe_allow_html=True)
    if data_option == 'Text':
        st.markdown('<p class="big-font3"><b>Text Summarization</b></p>', unsafe_allow_html=True)
        message = st.text_area('Enter text')
    elif data_option == 'URL':
        st.markdown('<p class="big-font3"><b>Web Page Summarization</b></p>', unsafe_allow_html=True)
        try:
            url = st.text_input('Enter the URL')
            message = get_text(url)
        except:
            pass
    elif data_option == 'Upload File':
        st.markdown('<p class="big-font3"><b>Document Summarization</b></p>', unsafe_allow_html=True)
        docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])
        if docx_file is not None:
            file_details = {"Filename":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
            if docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                message = read_docx(docx_file) 
            elif docx_file.type == "application/octet-stream":
                message = read_docx(docx_file) 
            elif docx_file.type == "application/pdf":
                st.markdown('<p class="big-font3"><b>PDF Summarization</b></p>', unsafe_allow_html=True)
                try:
                    message = read_pdf(docx_file)
                except:
                    pass
    
    #DEFAULT SUMMARIZE
    if st.checkbox('Default Summarizer'):
        st.text("Using Gensim Summarizer ..")
        summary_result = summarize(message, ratio = 0.1)

        #READING TIME
        reading_time = readingTime(summary_result)
        st.write('Human Reading Time:',reading_time,'mins')
        st.write("")

        #FINAL SUMMARY 
        st.write(summary_result)


    if st.checkbox('Custom Summarizer'):
        #SUMMARIZATION TYPE DROP MENU 
        summary_options = st.selectbox('Summarizer Type', ['Spacy', 'NLTK', 'Sumy'])
        if summary_options == 'Spacy':
            #TYPE OF SUMMARIES DROP MENU
            type_summary = st.selectbox('Kind',['InShorts','Executive','Elaborate'])

            
            if st.button('Summarize'):    
                if type_summary == 'InShorts':
                    st.text("Using Spacy Summarizer ..")
                    summary_result = spacy_inshorts(message)
                elif type_summary == 'Executive':
                    st.text("Using Spacy Summarizer ..")
                    summary_result = spacy_executive(message)
                elif type_summary == 'Elaborate':
                    st.text("Using Spacy Summarizer ..")
                    summary_result = spacy_elaborate(message)  

                #READING TIME 
                reading_time = readingTime(summary_result)
                st.write('Human Reading Time:',reading_time,'mins')
                st.write("")

                #FINAL SUMMARY 
                st.write(summary_result)



        elif summary_options == 'NLTK':
            #TYPE OF SUMMARIES
            type_summary = st.selectbox('Kind',['InShorts','Executive','Elaborate'])

            if st.button('Summarize'):
                if type_summary == 'InShorts':
                    st.text("Using NLTK Summarizer ..")
                    summary_result = nltk_inshorts(message)
                elif type_summary == 'Executive':
                    st.text("Using NLTK Summarizer ..")
                    summary_result = nltk_executive(message)
                elif type_summary == 'Elaborate':
                    st.text("Using NLTK Summarizer ..")
                    summary_result = nltk_elaborate(message)

                #READING TIME
                reading_time = readingTime(summary_result)
                st.write('Human Reading Time:',reading_time,'mins')
                st.write("")

                #FINAL SUMMARY 
                st.write(summary_result)
    


        elif summary_options == 'Sumy':
            #TYPES OF SUMMARIES
            type_summary = st.selectbox('Kind',['Elaborate','Executive','Inshorts'])
            
            if st.button('Summarize'):
                if type_summary == 'InShorts':
                    st.text("Using Sumy Summarizer ..")
                    summary_result = sumy_inshorts(message)
                elif type_summary == 'Executive':
                    st.text("Using Sumy Summarizer ..")
                    summary_result = sumy_executive(message)
                elif type_summary == 'Elaborate':
                    st.text("Using Sumy Summarizer ..")
                    summary_result = sumy_elaborate(message)

                #READING TIME
                reading_time = readingTime(summary_result)
                st.write('Human Reading Time:',reading_time,'mins')
                st.write("")

                #FINAL SUMMARY
                st.write(summary_result)