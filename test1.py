import streamlit as st
import requests

st.title("Download Data from Internal Server")

download_url = "http://172.16.3.229/XID_OTRS2/11.php"

# Add a download button
if st.button("Download Data"):
    try:
        response = requests.get(download_url)
        response.raise_for_status()

        # Try to guess the content type
        content_type = response.headers.get("Content-Type", "text/plain")
        file_extension = content_type.split("/")[-1] if "/" in content_type else "txt"
        file_name = f"downloaded_file.{file_extension}"

        # Offer file as a download
        st.download_button(
            label="Click here to save the file",
            data=response.content,
            file_name=file_name,
            mime=content_type
        )

    except requests.exceptions.RequestException as e:
        st.error(f"Failed to download the file: {e}")
