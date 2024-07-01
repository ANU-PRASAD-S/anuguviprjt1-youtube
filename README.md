Youtube Data Harvesting and Warehousing with Streamlit and Plotly.express
This Streamlit application allows you to extract, transform, and visualize data from YouTube channels using the Youtube Data API, Plotly.express, and other libraries.

Key Functionalities:
Extract Data: Enter a YouTube channel ID to retrieve channel details, video information, and comments (up to a limit).
Transform Data: Migrate extracted data from MongoDB to a MySQL database for further analysis.
Visualize Data: Query the MySQL database and generate interactive visualizations with Plotly.express for insights like:
Top viewed videos and their channels
Channels with the most videos
Average video duration per channel
Video comments and corresponding video titles
Running the App:
Prerequisites:

Python 3.x
Streamlit (install using pip install streamlit)
plotly (install using pip install plotly)
pymongo (install using pip install pymongo)
mysql-connector-python (install using pip install mysql-connector-python)
Google Cloud API Key (refer to https://developers.google.com/youtube/v3 for instructions on creating an API key)
Configuration:

Update the following details in Hello.py:
MongoDB connection string (client = pymongo.MongoClient("..."))
MySQL connection details (mydb = sql.connect(...))
Google Cloud API Key (api_key = "...")
Place your YouTube channel logo image at the path specified in st.set_page_config(...) (optional).
Run the script:

Bash
streamlit run Hello.py
