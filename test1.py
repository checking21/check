import streamlit as st
import requests

st.title("📥 Custom Data Downloader")

# Input for custom URL (with default value)
url = st.text_input("Enter the download URL:", value="http://172.16.3.229/XID_OTRS2/11.php")

# Validate URL before downloading
if url:
    if st.button("Download Data"):
        try:
            response = requests.get(url)
            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "text/plain")
            file_extension = content_type.split("/")[-1] if "/" in content_type else "txt"
            file_name = f"downloaded_file.{file_extension}"

            st.success("✅ File downloaded successfully. Ready to save.")

            st.download_button(
                label="💾 Save File",
                data=response.content,
                file_name=file_name,
                mime=content_type
            )

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error: {e}")
else:
    st.warning("⚠️ Please enter a valid URL to download the file.")
