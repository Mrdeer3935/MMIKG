import streamlit as st
import streamlit_book as stb
from pathlib import Path
from PIL import Image

# Set multipage
path = Path(__file__).parent.absolute()

# Supervised Learning
st.set_page_config(layout="wide",page_title="MMiKG", page_icon="/logo.png") #
stb.set_book_config(menu_title="",
                    menu_icon="list",
                    options=[
                            "Home",
                            "MMiKG",
                            "Case Shows",
                            "User Ports",
                            ],
                    paths=[
                        path / "home.py",
                        path / "MMiKG.py",
                        path / "Case shows.py",
                        path / "User Port.py"
                          ],
                    icons=[
                          "dice-1-fill",
                          "dice-1-fill",
                          "dice-1-fill",
                          "dice-1-fill"
                          ],
                    save_answers=False,
                    )


with st.sidebar:
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")





    st.sidebar.title("Contact us")
    st.sidebar.info(
        """
        Copyright © 2023 by Yang Fenglong
        (yangfenglong110 ANTI_SPAM_@126.com)
        """
    )



