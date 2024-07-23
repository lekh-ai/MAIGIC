# MAIGIC: My AI Generates Insights and Charts 🚀
MAIGIC is a `Retrieval Augmented Generation(RAG)` based AI-powered tool designed to generate insightful analyses and visualizations from user's submitted CSV file. The project uses `Langchain LLM` and  `llama-3-70b-instruct` to interpret datasets and create meaningful charts that help users understand underlying patterns and trends.

[![Deploy in Hugging Face](https://img.shields.io/badge/Deploy-Hugging%20Face-ffd500?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/spaces/lekhsisodiya/Magic)

For deploying in local server(flask version) pull the entire repository and run app.py.
 - LLM API creds would be made available on request

## Features ✨
- **Data Insights**: Takes user input data as a CSV file and requested query returns responses from a `llama-3-70b-instruct` hosted on IBM cloud using `IBM WatsonX` framework.
- **Chart Generation**: Internally utilises python's seaborm(matplotlib) and creates visualizations on the submitted data such as bar charts, line graphs, and more, creativity beyond limits.
- **User Interface**: Provides a visually appelaing & easy-to-use web interface for interaction.
- **Pandas dataframe agent**: Utilizes Pandas dataframe agent models to predict and analyze data.


## Technologies Used 🛠️

![RAG](https://img.shields.io/badge/RAG-28a745?style=for-the-badge&logo=ai)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![LLMs](https://img.shields.io/badge/LLMs-llama3_70b-67232A?style=for-the-badge&logo=alpaca&logoColor=white)
![IBM Watson](https://img.shields.io/badge/IBM_Watson-1F70C1?style=for-the-badge&logo=ibm&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-3498DB?style=for-the-badge&logo=langchain&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD500?style=for-the-badge&logo=huggingface&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## Deployments 🌐

There are two deployments of this project across two Python frameworks:

### Flask Version
- Runs on a local server
- Supports robust designs and functionality using HTML, CSS, and JS
- Clone the repository:
```git clone https://github.com/lekh-ai/RAG.git```

### Streamlit Version
- Deployed on Hugging Face
- [Streamlit Deployment Link](https://huggingface.co/spaces/lekhsisodiya/Magic)

Both versions have different UI and frontend configurations. Unlike Streamlit/Gradio, Flask supports HTML, CSS, and JS for more robust designs and functionality.

## UI Appearance 🖼️

### Flask Version (localhost)
![Flask Version](https://github.com/lekh-ai/MAIGIC/blob/main/MAGIC%20Spark.png)

### Streamlit Version (Hugging Face)
![Streamlit Version](https://github.com/lekh-ai/MAIGIC/blob/main/MAGIC%20Streamlit.png)

## Example Test Run Case 🧪

`the app uses a demo test studentdat.csv file for testing and generate queries and charts from it`

**Query Used**: "Make a histogram for column Fjob"

### API Response 
![Sample result](https://github.com/lekh-ai/MAIGIC/blob/main/static/test.png)


### Future Development 🚀
Ticketing System: Facilitate recording and tracking of issues and grant the LLM access to this data to generate insights.
Roles and Permissions: Allot admin and user roles so only admins can create insights from the ticketing database using credentials.

Contact 📬
For more information or to get in touch, please email lekhsiosdiya@gmail.com
Phone number : 9179041912
