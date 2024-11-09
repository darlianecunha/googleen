import streamlit as st
from scholarly import scholarly
import time

def search_research_areas_google_scholar(researcher_name):
    try:
        # Search for the researcher's profile by name
        search_query = scholarly.search_author(researcher_name)
        author = next(search_query)  # Get the first result

        # Load the full profile of the author
        author = scholarly.fill(author)

        # Collect research areas
        research_areas = author.get("interests", [])
        
        return research_areas if research_areas else ["No research areas found."]
    except StopIteration:
        return ["Profile not found on Google Scholar."]
    except Exception as e:
        return [f"Error retrieving research areas: {e}"]

# Streamlit Interface
st.markdown("<h1 style='color: navy;'>Exploring Research Interests of Scholars on Google Scholar</h1>", unsafe_allow_html=True)

# Input for multiple researcher names separated by commas
researcher_names = st.text_input("Enter the names of scholars on Google Scholar, separated by commas:")

if st.button("Search"):
    if researcher_names:
        with st.spinner("Searching..."):
            # Split the list of names and remove extra spaces
            names_list = [name.strip() for name in researcher_names.split(",")]
            for name in names_list:
                st.subheader(f"Research areas for: {name}")
                research_areas = search_research_areas_google_scholar(name)
                for area in research_areas:
                    st.write(f"- {area}")
                # Add a 2-second interval between searches
                time.sleep(2)
    else:
        st.warning("Please enter at least one scholar's name.")

# Add signature at the end in navy blue
st.markdown("<p style='color: navy;'>Tool developed by: Darliane Cunha</p>", unsafe_allow_html=True)


