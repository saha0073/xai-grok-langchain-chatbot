from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.runnables.history import RunnableWithMessageHistory
from tools import Tools  
from chat_history import chat_history_manager
from langchain_xai import ChatXAI

class Agent:
    def __init__(self, prompt_text, agent_type, Temperature, llm_model):
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", prompt_text),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        self.llm = ChatXAI(model_name=llm_model, temperature=Temperature, streaming=False)

        self.tools = Tools.setup_tools() 
        print(agent_type, " : ", self.tools )

        self.agent = create_openai_tools_agent(
            self.llm.with_config({"tags": ["agent_llm"]}), self.tools, self.prompt
        )

    def get_agent_executor(self):
        return AgentExecutor(agent=self.agent, tools=self.tools, verbose=True)

    def get_agent_with_history(self):
        return RunnableWithMessageHistory(
            self.get_agent_executor(),
            chat_history_manager.get_history_by_session_id,
            input_messages_key="input",
            history_messages_key="chat_history",
        )