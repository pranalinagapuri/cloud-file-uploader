
import streamlit as st
import boto3
import os

st.title("📁 Cloud File Uploader")

uploaded_file = st.file_uploader("Choose a file to upload")

if uploaded_file is not None:
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )
    bucket_name = "your-s3-bucket-name"
    s3.upload_fileobj(uploaded_file, bucket_name, uploaded_file.name)
    st.success(f"{uploaded_file.name} uploaded successfully to S3!")
