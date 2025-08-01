import streamlit as st
import hashlib

st.title("⚖️ YUDHISHTHIRA - File Hasher")

file1 = st.file_uploader("Upload Original File", key="file1")
file2 = st.file_uploader("Upload Copied File", key="file2")

def get_hash(data):
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()

if file1 and file2:
    hash1 = get_hash(file1.read())
    hash2 = get_hash(file2.read())
    st.write("Original SHA256:", hash1)
    st.write("Copied SHA256:", hash2)
    if hash1 == hash2:
        st.success("Integrity Verified")
    else:
        st.error("Hash Mismatch Detected")