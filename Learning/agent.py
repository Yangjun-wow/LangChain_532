from mysql_agent import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.chat_models import ChatOpenAI
import pandas as pd
import time
from langchain.llms import Tongyi
from prompt_c import (
    SQL_FUNCTIONS_SUFFIX,
    SQL_PREFIX,
    SQL_SUFFIX,
)
import os

# openai
os.environ["OPENAI_API_KEY"] = "sk-LIzY4hrTG0r2HXux3308CcBeC0Ab4f1eA60c6cD7736aB122"
os.environ["OPENAI_API_BASE"] = "https://openkey.cloud/v1"

# os.environ["DASHSCOPE_API_KEY"] = "sk-24402a9f1f2b4a9dbb4a9a36b28fd772"
# llm_tongyi = Tongyi(temperature=0)
# print(llm_tongyi)
db = SQLDatabase.from_uri("mysql+mysqlconnector://root:123456@10.166.41.205:5193/LangChain_sql_2")
llm = OpenAI(temperature=0)
print(llm)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

# 读取CSV文件
csv_data = pd.read_csv('QA.csv', header=None)
# 提取特定的列
column_data = csv_data[0]  # 替换 'column_name' 为你要提取的列名
# print(column_data)
answer = agent_executor.run("神经外科诊室在什么地方？")
