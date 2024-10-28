# SistemaMultiAgentes Crew

Bem vindo ao projeto SistemaMultiAgente base sobre uso de sistemas multi agentes baseados em LLM com a ferramenta crewAI.

### Instalando

`git clone`


### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/sistema_multi_agentes/config/agents.yaml` to define your agents
- Modify `src/sistema_multi_agentes/config/tasks.yaml` to define your tasks
- Modify `src/sistema_multi_agentes/crew.py` to add your own logic, tools and specific args
- Modify `src/sistema_multi_agentes/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the sistema_multi_agentes Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The sistema_multi_agentes Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
