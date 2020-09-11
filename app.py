"""Main module for the streamlit app"""
import streamlit as st

import awesome_streamlit as ast
import pages.Intro
#import pages.Dataset
import pages.SIER
import pages.MongoDataset

ast.core.services.other.set_logging_format()

PAGES = {
    "Home": pages.Intro,
    #"Just test with CSV": pages.Dataset,
    "SIER model ": pages.SIER,
    "MongoDB test": pages.MongoDataset
}

def main():

    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

if __name__ == "__main__":
    main()