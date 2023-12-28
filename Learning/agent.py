from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.chat_models import ChatOpenAI
import pandas as pd
import time
from langchain.llms import Tongyi
import os

# openai
os.environ["OPENAI_API_KEY"] = "sk-LIzY4hrTG0r2HXux3308CcBeC0Ab4f1eA60c6cD7736aB122"
os.environ["OPENAI_API_BASE"] = "https://openkey.cloud/v1"

# os.environ["DASHSCOPE_API_KEY"] = "sk-24402a9f1f2b4a9dbb4a9a36b28fd772"
# llm_tongyi = Tongyi(temperature=0)
# print(llm_tongyi)
db = SQLDatabase.from_uri("mysql+mysqlconnector://root:123456@10.166.41.205:5193/LangChain_sql_2")
llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
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




# def run_agent(question):
#     # 这是一个包装函数，用于处理agent_executor.run的异常
#     # 并在失败时进行重试
#     max_retries = 3
#     for attempt in range(max_retries):
#         try:
#             return agent_executor.run(question)
#         except Exception as e:
#             print(f"Error: {e}, retrying... ({attempt + 1}/{max_retries})")
#             time.sleep(1)  # 休眠1秒再重试
#     return "Error: Unable to get answer after retries."
#
#
# # 检查上次的进度
# try:
#     with open('progress2.txt', 'r') as progress_file:
#         last_index = int(progress_file.read().strip())
# except Exception:
#     last_index = -1  # 如果没有进度文件或读取失败，则从头开始
#
# with open('output2.txt', 'a') as file:  # 使用追加模式
#     for index, question in enumerate(column_data, start=0):
#         if index <= last_index:
#             continue  # 跳过已处理的问题
#
#         answer = run_agent(question)
#
#         # 打印并写入答案
#         print(f"Question {index}: {question}")
#         print(f"Answer: {answer}\n")
#         file.write(f"Question {index}: {question}\n")
#         file.write(f"Answer: {answer}\n\n")
#
#         # 更新进度
#         with open('progress2.txt', 'w') as progress_file:
#             progress_file.write(str(index))
