import matplotlib.pyplot as plt
import pandas as pd

from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watsonx_ai import APIClient

from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

def initialize_model():
    # Create a dictionary to store credential information
    credentials = {
        "url": "https://jp-tok.ml.cloud.ibm.com",
        "apikey" : "UQ2jF4FyhBND5S7Xc5ImfQOCRsikRFFJ6AtQe-80StGp"
    }

    project_id = "da4c5444-528c-4452-b677-71ed875add4c"
    space_id = None
    verify = False

    # Indicate the model we would like to initialize. In this case, Llama 3 70B.
    model_id = 'meta-llama/llama-3-70b-instruct'

    # Initialize some watsonx.ai model parameters
    params = {
        GenParams.MAX_NEW_TOKENS: 512,  # The maximum number of tokens that the model can generate in a single run.
        GenParams.TEMPERATURE: 0,  # A parameter that controls the randomness of the token generation.
    }

    # Launch a watsonx.ai model
    model = Model(
        model_id=model_id,
        credentials=credentials,
        params=params,
        project_id=project_id,
        space_id=space_id,
        verify=verify
    )

    # Integrate the watsonx.ai model with the langchain framework
    llm = WatsonxLLM(model=model)
    return llm

def create_agent(llm, df,allow_dangerous_code=True):
    return create_pandas_dataframe_agent(llm, df, verbose=False, return_intermediate_steps=True,allow_dangerous_code=True)

def data_mining_assistant(agent, query):
    response = agent.invoke(query)
    return response
