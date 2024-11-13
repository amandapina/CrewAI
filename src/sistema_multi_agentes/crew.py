from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import os
from dotenv import load_dotenv, find_dotenv

# Se você não tiver o SerperDevTool, substitua por uma ferramenta disponível.
# Se o SerperDevTool for necessário, certifique-se de que está importado corretamente.
from crewai_tools import SerperDevTool  # Certifique-se de que o 'SerperDevTool' existe!

def load_env():
    _ = load_dotenv(find_dotenv())

def get_gemini_api_key():
    load_env()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    return gemini_api_key

LLModel = LLM(
    model="gemini/gemini-1.5-pro", 
    temperature=0.5,
    api_key=get_gemini_api_key(),
)

@CrewBase
class SistemaMultiAgentesCrew():
    """SistemaMultiAgentes crew"""

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool()],  # Aqui deve ser definida a ferramenta correta
            verbose=True,
            llm=LLModel
        )

    @agent
    def fact_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['fact_checker'],
            tools=[SerperDevTool()],  # Usando SerperDevTool
            verbose=True,
            llm=LLModel
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            tools=[SerperDevTool()],  # Usando SerperDevTool se for necessário
            verbose=True,
            llm=LLModel
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            verbose=True
        )

    @task
    def fact_checking_task(self) -> Task:
        return Task(
            config=self.tasks_config['fact_checking_task'],
            verbose=True
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='results/report.md',
            verbose=True
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SistemaMultiAgentes crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,  # Pode usar Process.hierarchical se preferir
            verbose=True,
        )
