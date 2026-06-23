import streamlit as strl

# 1. Page Configuration
strl.set_page_config(
    page_title="Sayrayan",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Inject Custom CSS for Google-like Styling
strl.markdown(
    """
    <style>
    /* Hide default Streamlit headers, menus, and footers */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Center the main container content vertically */
    .block-container {
        padding-top: 5rem;
        max-width: 700px;
    }

    /* Style the main Logo */
    .logo-text {
        font-family: 'Product Sans', Arial, sans-serif;
        font-size: 80px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        letter-spacing: -2px;
    }

    /* Style individual letters for a search engine vibe */
    .letter-s1 { color: #4285F4; } /* Blue */
    .letter-a1 { color: #EA4335; } /* Red */
    .letter-y1 { color: #FBBC05; } /* Yellow */
    .letter-r { color: #4285F4; }  /* Blue */
    .letter-a2 { color: #34A853; } /* Green */
    .letter-y2 { color: #EA4335; } /* Red */
    .letter-a3 { color: #FBBC05; } /* Yellow */
    .letter-n { color: #34A853; }  /* Green */

    /* Footer styles */
    .search-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f2f2f2;
        color: #70757a;
        text-align: left;
        padding: 15px;
        font-size: 14px;
        border-top: 1px solid #e4e4e4;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

