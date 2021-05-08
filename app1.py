import streamlit as st
def app():
    st.markdown("""<style>
    .big-font2 {
    font-size:60px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font2"><b>Welcome to CrunchIt! :))</b></p>', unsafe_allow_html=True)

    st.markdown("""<style>
    .big-font4 {
    font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font4"; style = "color: #F63366"><b>A Text Summarization Web App using Natural Language Processing</b></p>', unsafe_allow_html=True)

    st.markdown("""<style>
    .big-font3 {
    font-size:35px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font3"><b>&#10004 <u>Works where you do</u></b></p>', unsafe_allow_html=True)

    st.markdown("""<style>
    .big-font5 {
    font-size:25px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    col1, mid, col2 = st.beta_columns([1,500,200])
    with col1:
        st.image('text_sum.png', width=500)
    with col2:
        st.markdown('<p class="big-font5"; style = "color: #F63366"><b><br><br>Long Text? Summarize It</br></br></b></p>', unsafe_allow_html=True)

    st.markdown("""<style>
    .big-font5 {
    font-size:25px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    col1, mid, col2 = st.beta_columns([130,20,500])
    with col2:
        st.image('url_sum.png', width=500)
    with col1:
        st.markdown('<p class="big-font5"; style = "color: #F63366"><b><br>Read the Webpage 2x Faster</b></p>', unsafe_allow_html=True)

    st.markdown("""<style>
    .big-font5 {
    font-size:25px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    col1, mid, col2 = st.beta_columns([1,500,200])
    with col1:
        st.image('doc_sum.png', width=500)
    with col2:
        st.markdown('<p class="big-font5"; style = "color: #F63366"><b><br><br><br>Speed Read a Document</b></p>', unsafe_allow_html=True)

    st.markdown("""<style>
    .big-font5 {
    font-size:25px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    col1, mid, col2 = st.beta_columns([140,30,500])
    with col2:
        st.image('pdf_sum.png', width=500)
    with col1:
        st.markdown('<p class="big-font5"; style = "color: #F63366"><b><br><br>Parse<br> Data<br> Faster</b></p>', unsafe_allow_html=True)

    st.markdown('<p class="big-font3"><b>&#10004 <u>How to CrunchIt?</u></b></p>', unsafe_allow_html=True)
    
    st.markdown('<p class="big-font5"; style = "color: #F63366"><b>When in Hurry, use the Default Summary...</b></p>', unsafe_allow_html=True)
    
    st.image('default_sum.png', width = 700)

    st.markdown('<p class="big-font5"; style = "color: #F63366"><b>Or Personalize your Summary</b></p>', unsafe_allow_html=True)


    col1, mid, col2 = st.beta_columns([1,500,200])
    with col1:
        st.image('summ_type.png', width=500)
    with col2:
        st.info('Click the custom button. Choose any type of summarizer from the list available. And for the next step select the kind of summary you want from the options mentioned below.')

    col1, mid, col2 = st.beta_columns([170,30,500])
    with col2:
        st.image('summ_kind.png', width=500)
    with col1:
        st.info('Kinds of Summary: Inshorts (3 lines), Executive (7 lines) and Elaborate (15 lines). Once done selecting just hit the summarize button!')

