import streamlit as st
from googleapiclient.discovery import build
st.header("Search for Disease Treatment Videos on YouTube")

 
try:
    disease_to_search = st.session_state["disease"]            
    if disease_to_search:
# Initialize the YouTube Data API client
            youtube = build('youtube', 'v3', developerKey=st.secrets["YOUTUBE_API_KEY"])

# Perform the YouTube search
            search_response = youtube.search().list(
            q=f"{disease_to_search} treatment",
            part="id,snippet",
            type="video",
            maxResults=5  # You can adjust the number of results here
            ).execute()

            # Display the search results as clickable links
            st.write(f"Search results for '{disease_to_search} treatment' on YouTube:")
            for search_result in search_response.get("items", []):
                video_id = search_result["id"]["videoId"]
                video_title = search_result["snippet"]["title"]
                st.markdown(f"- [{video_title}](https://www.youtube.com/watch?v={video_id})")

            # Display video search results with thumbnails
            st.header("YouTube Video Search Results")

            for search_result in search_response.get("items", []):
                video_title = search_result["snippet"]["title"]
                video_description = search_result["snippet"]["description"]
                video_id = search_result["id"]["videoId"]
                video_thumbnail_url = search_result["snippet"]["thumbnails"]["medium"]["url"]  # Use "medium" format

                # Create a hyperlink around the thumbnail image
                video_link = f"[![{video_title}]({video_thumbnail_url})](https://www.youtube.com/watch?v={video_id})"
                st.markdown(video_link, unsafe_allow_html=True)
                st.write(f"Title: {video_title}")
                st.write(f"Description: {video_description}")
                st.write(f"Video ID: {video_id}")
except KeyError:
    st.warning("Please upload disease image to search for treatment videos on YouTube.")