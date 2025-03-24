# Create Your Own Manager Agent - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Create Your Own Manager Agent

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/how-to/custom-manager-agent\#setting-a-specific-agent-as-manager-in-crewai)  Setting a Specific Agent as Manager in CrewAI

CrewAI allows users to set a specific agent as the manager of the crew, providing more control over the management and coordination of tasks.
This feature enables the customization of the managerial role to better fit your project’s requirements.

## [​](https://docs.crewai.com/how-to/custom-manager-agent\#using-the-manager-agent-attribute)  Using the `manager_agent` Attribute

### [​](https://docs.crewai.com/how-to/custom-manager-agent\#custom-manager-agent)  Custom Manager Agent

The `manager_agent` attribute allows you to define a custom agent to manage the crew. This agent will oversee the entire process, ensuring that tasks are completed efficiently and to the highest standard.

### [​](https://docs.crewai.com/how-to/custom-manager-agent\#example)  Example

Code

Copy

```python
import os
from crewai import Agent, Task, Crew, Process

# Define your agents
researcher = Agent(
    role="Researcher",
    goal="Conduct thorough research and analysis on AI and AI agents",
    backstory="You're an expert researcher, specialized in technology, software engineering, AI, and startups. You work as a freelancer and are currently researching for a new client.",
    allow_delegation=False,
)

writer = Agent(
    role="Senior Writer",
    goal="Create compelling content about AI and AI agents",
    backstory="You're a senior writer, specialized in technology, software engineering, AI, and startups. You work as a freelancer and are currently writing content for a new client.",
    allow_delegation=False,
)

# Define your task
task = Task(
    description="Generate a list of 5 interesting ideas for an article, then write one captivating paragraph for each idea that showcases the potential of a full article on this topic. Return the list of ideas with their paragraphs and your notes.",
    expected_output="5 bullet points, each with a paragraph and accompanying notes.",
)

# Define the manager agent
manager = Agent(
    role="Project Manager",
    goal="Efficiently manage the crew and ensure high-quality task completion",
    backstory="You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
    allow_delegation=True,
)

# Instantiate your crew with a custom manager
crew = Crew(
    agents=[researcher, writer],
    tasks=[task],
    manager_agent=manager,
    process=Process.hierarchical,
)

# Start the crew's work
result = crew.kickoff()

```

## [​](https://docs.crewai.com/how-to/custom-manager-agent\#benefits-of-a-custom-manager-agent)  Benefits of a Custom Manager Agent

- **Enhanced Control**: Tailor the management approach to fit the specific needs of your project.
- **Improved Coordination**: Ensure efficient task coordination and management by an experienced agent.
- **Customizable Management**: Define managerial roles and responsibilities that align with your project’s goals.

## [​](https://docs.crewai.com/how-to/custom-manager-agent\#setting-a-manager-llm)  Setting a Manager LLM

If you’re using the hierarchical process and don’t want to set a custom manager agent, you can specify the language model for the manager:

Code

Copy

```python
from crewai import LLM

manager_llm = LLM(model="gpt-4o")

crew = Crew(
    agents=[researcher, writer],
    tasks=[task],
    process=Process.hierarchical,
    manager_llm=manager_llm
)

```

Either `manager_agent` or `manager_llm` must be set when using the hierarchical process.

Was this page helpful?

YesNo

[Hierarchical Process](https://docs.crewai.com/how-to/hierarchical-process) [Connect to any LLM](https://docs.crewai.com/how-to/llm-connections)

On this page

- [Setting a Specific Agent as Manager in CrewAI](https://docs.crewai.com/how-to/custom-manager-agent#setting-a-specific-agent-as-manager-in-crewai)
- [Using the manager\_agent Attribute](https://docs.crewai.com/how-to/custom-manager-agent#using-the-manager-agent-attribute)
- [Custom Manager Agent](https://docs.crewai.com/how-to/custom-manager-agent#custom-manager-agent)
- [Example](https://docs.crewai.com/how-to/custom-manager-agent#example)
- [Benefits of a Custom Manager Agent](https://docs.crewai.com/how-to/custom-manager-agent#benefits-of-a-custom-manager-agent)
- [Setting a Manager LLM](https://docs.crewai.com/how-to/custom-manager-agent#setting-a-manager-llm)

# EXA Search Web Loader - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

EXA Search Web Loader

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/exasearchtool\#exasearchtool)  `EXASearchTool`

## [​](https://docs.crewai.com/tools/exasearchtool\#description)  Description

The EXASearchTool is designed to perform a semantic search for a specified query from a text’s content across the internet.
It utilizes the [exa.ai](https://exa.ai/) API to fetch and display the most relevant search results based on the query provided by the user.

## [​](https://docs.crewai.com/tools/exasearchtool\#installation)  Installation

To incorporate this tool into your project, follow the installation instructions below:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/exasearchtool\#example)  Example

The following example demonstrates how to initialize the tool and execute a search with a given query:

Code

Copy

```python
from crewai_tools import EXASearchTool

# Initialize the tool for internet searching capabilities
tool = EXASearchTool()

```

## [​](https://docs.crewai.com/tools/exasearchtool\#steps-to-get-started)  Steps to Get Started

To effectively use the EXASearchTool, follow these steps:

1

Package Installation

Confirm that the `crewai[tools]` package is installed in your Python environment.

2

API Key Acquisition

Acquire a [exa.ai](https://exa.ai/) API key by registering for a free account at [exa.ai](https://exa.ai/).

3

Environment Configuration

Store your obtained API key in an environment variable named `EXA_API_KEY` to facilitate its use by the tool.

## [​](https://docs.crewai.com/tools/exasearchtool\#conclusion)  Conclusion

By integrating the `EXASearchTool` into Python projects, users gain the ability to conduct real-time, relevant searches across the internet directly from their applications.
By adhering to the setup and usage guidelines provided, incorporating this tool into projects is streamlined and straightforward.

Was this page helpful?

YesNo

[DOCX RAG Search](https://docs.crewai.com/tools/docxsearchtool) [File Read](https://docs.crewai.com/tools/filereadtool)

On this page

- [EXASearchTool](https://docs.crewai.com/tools/exasearchtool#exasearchtool)
- [Description](https://docs.crewai.com/tools/exasearchtool#description)
- [Installation](https://docs.crewai.com/tools/exasearchtool#installation)
- [Example](https://docs.crewai.com/tools/exasearchtool#example)
- [Steps to Get Started](https://docs.crewai.com/tools/exasearchtool#steps-to-get-started)
- [Conclusion](https://docs.crewai.com/tools/exasearchtool#conclusion)

# Hierarchical Process - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Hierarchical Process

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/how-to/hierarchical-process\#introduction)  Introduction

The hierarchical process in CrewAI introduces a structured approach to task management, simulating traditional organizational hierarchies for efficient task delegation and execution.
This systematic workflow enhances project outcomes by ensuring tasks are handled with optimal efficiency and accuracy.

The hierarchical process is designed to leverage advanced models like GPT-4, optimizing token usage while handling complex tasks with greater efficiency.

## [​](https://docs.crewai.com/how-to/hierarchical-process\#hierarchical-process-overview)  Hierarchical Process Overview

By default, tasks in CrewAI are managed through a sequential process. However, adopting a hierarchical approach allows for a clear hierarchy in task management,
where a ‘manager’ agent coordinates the workflow, delegates tasks, and validates outcomes for streamlined and effective execution. This manager agent can now be either
automatically created by CrewAI or explicitly set by the user.

### [​](https://docs.crewai.com/how-to/hierarchical-process\#key-features)  Key Features

- **Task Delegation**: A manager agent allocates tasks among crew members based on their roles and capabilities.
- **Result Validation**: The manager evaluates outcomes to ensure they meet the required standards.
- **Efficient Workflow**: Emulates corporate structures, providing an organized approach to task management.
- **System Prompt Handling**: Optionally specify whether the system should use predefined prompts.
- **Stop Words Control**: Optionally specify whether stop words should be used, supporting various models including the o1 models.
- **Context Window Respect**: Prioritize important context by enabling respect of the context window, which is now the default behavior.
- **Delegation Control**: Delegation is now disabled by default to give users explicit control.
- **Max Requests Per Minute**: Configurable option to set the maximum number of requests per minute.
- **Max Iterations**: Limit the maximum number of iterations for obtaining a final answer.

## [​](https://docs.crewai.com/how-to/hierarchical-process\#implementing-the-hierarchical-process)  Implementing the Hierarchical Process

To utilize the hierarchical process, it’s essential to explicitly set the process attribute to `Process.hierarchical`, as the default behavior is `Process.sequential`.
Define a crew with a designated manager and establish a clear chain of command.

Assign tools at the agent level to facilitate task delegation and execution by the designated agents under the manager’s guidance.
Tools can also be specified at the task level for precise control over tool availability during task execution.

Configuring the `manager_llm` parameter is crucial for the hierarchical process.
The system requires a manager LLM to be set up for proper function, ensuring tailored decision-making.

Code

Copy

```python
from langchain_openai import ChatOpenAI
from crewai import Crew, Process, Agent

# Agents are defined with attributes for backstory, cache, and verbose mode
researcher = Agent(
    role='Researcher',
    goal='Conduct in-depth analysis',
    backstory='Experienced data analyst with a knack for uncovering hidden trends.',
    cache=True,
    verbose=False,
    # tools=[]  # This can be optionally specified; defaults to an empty list
    use_system_prompt=True,  # Enable or disable system prompts for this agent
    max_rpm=30,  # Limit on the number of requests per minute
    max_iter=5  # Maximum number of iterations for a final answer
)
writer = Agent(
    role='Writer',
    goal='Create engaging content',
    backstory='Creative writer passionate about storytelling in technical domains.',
    cache=True,
    verbose=False,
    # tools=[]  # Optionally specify tools; defaults to an empty list
    use_system_prompt=True,  # Enable or disable system prompts for this agent
    max_rpm=30,  # Limit on the number of requests per minute
    max_iter=5  # Maximum number of iterations for a final answer
)

# Establishing the crew with a hierarchical process and additional configurations
project_crew = Crew(
    tasks=[...],  # Tasks to be delegated and executed under the manager's supervision
    agents=[researcher, writer],
    manager_llm=ChatOpenAI(temperature=0, model="gpt-4"),  # Mandatory if manager_agent is not set
    process=Process.hierarchical,  # Specifies the hierarchical management approach
    respect_context_window=True,  # Enable respect of the context window for tasks
    memory=True,  # Enable memory usage for enhanced task execution
    manager_agent=None,  # Optional: explicitly set a specific agent as manager instead of the manager_llm
    planning=True,  # Enable planning feature for pre-execution strategy
)

```

### [​](https://docs.crewai.com/how-to/hierarchical-process\#workflow-in-action)  Workflow in Action

1. **Task Assignment**: The manager assigns tasks strategically, considering each agent’s capabilities and available tools.
2. **Execution and Review**: Agents complete their tasks with the option for asynchronous execution and callback functions for streamlined workflows.
3. **Sequential Task Progression**: Despite being a hierarchical process, tasks follow a logical order for smooth progression, facilitated by the manager’s oversight.

## [​](https://docs.crewai.com/how-to/hierarchical-process\#conclusion)  Conclusion

Adopting the hierarchical process in CrewAI, with the correct configurations and understanding of the system’s capabilities, facilitates an organized and efficient approach to project management.
Utilize the advanced features and customizations to tailor the workflow to your specific needs, ensuring optimal task execution and project success.

Was this page helpful?

YesNo

[Sequential Processes](https://docs.crewai.com/how-to/sequential-process) [Create Your Own Manager Agent](https://docs.crewai.com/how-to/custom-manager-agent)

On this page

- [Introduction](https://docs.crewai.com/how-to/hierarchical-process#introduction)
- [Hierarchical Process Overview](https://docs.crewai.com/how-to/hierarchical-process#hierarchical-process-overview)
- [Key Features](https://docs.crewai.com/how-to/hierarchical-process#key-features)
- [Implementing the Hierarchical Process](https://docs.crewai.com/how-to/hierarchical-process#implementing-the-hierarchical-process)
- [Workflow in Action](https://docs.crewai.com/how-to/hierarchical-process#workflow-in-action)
- [Conclusion](https://docs.crewai.com/how-to/hierarchical-process#conclusion)

# Installation - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Get Started

Installation

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

**Python Version Requirements**

CrewAI requires `Python >=3.10 and <3.13`. Here’s how to check your version:

Copy

```bash
python3 --version

```

If you need to update Python, visit [python.org/downloads](https://python.org/downloads)

# [​](https://docs.crewai.com/installation\#setting-up-your-environment)  Setting Up Your Environment

Before installing CrewAI, it’s recommended to set up a virtual environment. This helps isolate your project dependencies and avoid conflicts.

1

Create a Virtual Environment

Choose your preferred method to create a virtual environment:

**Using venv (Python’s built-in tool):**

Terminal

Copy

```shell
python3 -m venv .venv

```

**Using conda:**

Terminal

Copy

```shell
conda create -n crewai-env python=3.12

```

2

Activate the Virtual Environment

Activate your virtual environment based on your platform:

**On macOS/Linux (venv):**

Terminal

Copy

```shell
source .venv/bin/activate

```

**On Windows (venv):**

Terminal

Copy

```shell
.venv\Scripts\activate

```

**Using conda (all platforms):**

Terminal

Copy

```shell
conda activate crewai-env

```

# [​](https://docs.crewai.com/installation\#installing-crewai)  Installing CrewAI

Now let’s get you set up! 🚀

1

Install CrewAI

Install CrewAI with all recommended tools using either method:

Terminal

Copy

```shell
pip install 'crewai[tools]'

```

or

Terminal

Copy

```shell
pip install crewai crewai-tools

```

Both methods install the core package and additional tools needed for most use cases.

2

Upgrade CrewAI (Existing Installations Only)

If you have an older version of CrewAI installed, you can upgrade it:

Terminal

Copy

```shell
pip install --upgrade crewai crewai-tools

```

If you see a Poetry-related warning, you’ll need to migrate to our new dependency manager:

Terminal

Copy

```shell
crewai update

```

This will update your project to use [UV](https://github.com/astral-sh/uv), our new faster dependency manager.

Skip this step if you’re doing a fresh installation.

3

Verify Installation

Check your installed versions:

Terminal

Copy

```shell
pip freeze | grep crewai

```

You should see something like:

Output

Copy

```markdown
crewai==X.X.X
crewai-tools==X.X.X

```

Installation successful! You’re ready to create your first crew.

# [​](https://docs.crewai.com/installation\#creating-a-new-project)  Creating a New Project

We recommend using the YAML Template scaffolding for a structured approach to defining agents and tasks.

1

Generate Project Structure

Run the CrewAI CLI command:

Terminal

Copy

```shell
crewai create crew <project_name>

```

This creates a new project with the following structure:

Copy

```
my_project/
├── .gitignore
├── pyproject.toml
├── README.md
├── .env
└── src/
    └── my_project/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── tools/
        │   ├── custom_tool.py
        │   └── __init__.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml

```

2

Install Additional Tools

You can install additional tools using UV:

Terminal

Copy

```shell
uv add <tool-name>

```

UV is our preferred package manager as it’s significantly faster than pip and provides better dependency resolution.

3

Customize Your Project

Your project will contain these essential files:

| File | Purpose |
| --- | --- |
| `agents.yaml` | Define your AI agents and their roles |
| `tasks.yaml` | Set up agent tasks and workflows |
| `.env` | Store API keys and environment variables |
| `main.py` | Project entry point and execution flow |
| `crew.py` | Crew orchestration and coordination |
| `tools/` | Directory for custom agent tools |

Start by editing `agents.yaml` and `tasks.yaml` to define your crew’s behavior.
Keep sensitive information like API keys in `.env`.

## [​](https://docs.crewai.com/installation\#next-steps)  Next Steps

[**Build Your First Agent** \\
\\
Follow our quickstart guide to create your first CrewAI agent and get hands-on experience.](https://docs.crewai.com/quickstart) [**Join the Community** \\
\\
Connect with other developers, get help, and share your CrewAI experiences.](https://community.crewai.com/)

Was this page helpful?

YesNo

[Introduction](https://docs.crewai.com/introduction) [Quickstart](https://docs.crewai.com/quickstart)

On this page

- [Setting Up Your Environment](https://docs.crewai.com/installation#setting-up-your-environment)
- [Installing CrewAI](https://docs.crewai.com/installation#installing-crewai)
- [Creating a New Project](https://docs.crewai.com/installation#creating-a-new-project)
- [Next Steps](https://docs.crewai.com/installation#next-steps)

# Flows - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Flows

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/flows\#introduction)  Introduction

CrewAI Flows is a powerful feature designed to streamline the creation and management of AI workflows. Flows allow developers to combine and coordinate coding tasks and Crews efficiently, providing a robust framework for building sophisticated AI automations.

Flows allow you to create structured, event-driven workflows. They provide a seamless way to connect multiple tasks, manage state, and control the flow of execution in your AI applications. With Flows, you can easily design and implement multi-step processes that leverage the full potential of CrewAI’s capabilities.

1. **Simplified Workflow Creation**: Easily chain together multiple Crews and tasks to create complex AI workflows.

2. **State Management**: Flows make it super easy to manage and share state between different tasks in your workflow.

3. **Event-Driven Architecture**: Built on an event-driven model, allowing for dynamic and responsive workflows.

4. **Flexible Control Flow**: Implement conditional logic, loops, and branching within your workflows.


## [​](https://docs.crewai.com/concepts/flows\#getting-started)  Getting Started

Let’s create a simple Flow where you will use OpenAI to generate a random city in one task and then use that city to generate a fun fact in another task.

Code

Copy

```python

from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv
from litellm import completion

class ExampleFlow(Flow):
    model = "gpt-4o-mini"

    @start()
    def generate_city(self):
        print("Starting flow")
        # Each flow state automatically gets a unique ID
        print(f"Flow State ID: {self.state['id']}")

        response = completion(
            model=self.model,
            messages=[\
                {\
                    "role": "user",\
                    "content": "Return the name of a random city in the world.",\
                },\
            ],
        )

        random_city = response["choices"][0]["message"]["content"]
        # Store the city in our state
        self.state["city"] = random_city
        print(f"Random City: {random_city}")

        return random_city

    @listen(generate_city)
    def generate_fun_fact(self, random_city):
        response = completion(
            model=self.model,
            messages=[\
                {\
                    "role": "user",\
                    "content": f"Tell me a fun fact about {random_city}",\
                },\
            ],
        )

        fun_fact = response["choices"][0]["message"]["content"]
        # Store the fun fact in our state
        self.state["fun_fact"] = fun_fact
        return fun_fact

flow = ExampleFlow()
result = flow.kickoff()

print(f"Generated fun fact: {result}")

```

In the above example, we have created a simple Flow that generates a random city using OpenAI and then generates a fun fact about that city. The Flow consists of two tasks: `generate_city` and `generate_fun_fact`. The `generate_city` task is the starting point of the Flow, and the `generate_fun_fact` task listens for the output of the `generate_city` task.

Each Flow instance automatically receives a unique identifier (UUID) in its state, which helps track and manage flow executions. The state can also store additional data (like the generated city and fun fact) that persists throughout the flow’s execution.

When you run the Flow, it will:

1. Generate a unique ID for the flow state
2. Generate a random city and store it in the state
3. Generate a fun fact about that city and store it in the state
4. Print the results to the console

The state’s unique ID and stored data can be useful for tracking flow executions and maintaining context between tasks.

**Note:** Ensure you have set up your `.env` file to store your `OPENAI_API_KEY`. This key is necessary for authenticating requests to the OpenAI API.

### [​](https://docs.crewai.com/concepts/flows\#%40start)  @start()

The `@start()` decorator is used to mark a method as the starting point of a Flow. When a Flow is started, all the methods decorated with `@start()` are executed in parallel. You can have multiple start methods in a Flow, and they will all be executed when the Flow is started.

### [​](https://docs.crewai.com/concepts/flows\#%40listen)  @listen()

The `@listen()` decorator is used to mark a method as a listener for the output of another task in the Flow. The method decorated with `@listen()` will be executed when the specified task emits an output. The method can access the output of the task it is listening to as an argument.

#### [​](https://docs.crewai.com/concepts/flows\#usage)  Usage

The `@listen()` decorator can be used in several ways:

1. **Listening to a Method by Name**: You can pass the name of the method you want to listen to as a string. When that method completes, the listener method will be triggered.





Code







Copy













```python
@listen("generate_city")
def generate_fun_fact(self, random_city):
       # Implementation

```

2. **Listening to a Method Directly**: You can pass the method itself. When that method completes, the listener method will be triggered.





Code







Copy













```python
@listen(generate_city)
def generate_fun_fact(self, random_city):
       # Implementation

```


### [​](https://docs.crewai.com/concepts/flows\#flow-output)  Flow Output

Accessing and handling the output of a Flow is essential for integrating your AI workflows into larger applications or systems. CrewAI Flows provide straightforward mechanisms to retrieve the final output, access intermediate results, and manage the overall state of your Flow.

#### [​](https://docs.crewai.com/concepts/flows\#retrieving-the-final-output)  Retrieving the Final Output

When you run a Flow, the final output is determined by the last method that completes. The `kickoff()` method returns the output of this final method.

Here’s how you can access the final output:

Code

Output

Copy

```python
from crewai.flow.flow import Flow, listen, start

class OutputExampleFlow(Flow):
    @start()
    def first_method(self):
        return "Output from first_method"

    @listen(first_method)
    def second_method(self, first_output):
        return f"Second method received: {first_output}"

flow = OutputExampleFlow()
final_output = flow.kickoff()

print("---- Final Output ----")
print(final_output)

```

In this example, the `second_method` is the last method to complete, so its output will be the final output of the Flow.
The `kickoff()` method will return the final output, which is then printed to the console.

#### [​](https://docs.crewai.com/concepts/flows\#accessing-and-updating-state)  Accessing and Updating State

In addition to retrieving the final output, you can also access and update the state within your Flow. The state can be used to store and share data between different methods in the Flow. After the Flow has run, you can access the state to retrieve any information that was added or updated during the execution.

Here’s an example of how to update and access the state:

Code

Output

Copy

```python
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

class ExampleState(BaseModel):
    counter: int = 0
    message: str = ""

class StateExampleFlow(Flow[ExampleState]):

    @start()
    def first_method(self):
        self.state.message = "Hello from first_method"
        self.state.counter += 1

    @listen(first_method)
    def second_method(self):
        self.state.message += " - updated by second_method"
        self.state.counter += 1
        return self.state.message

flow = StateExampleFlow()
final_output = flow.kickoff()
print(f"Final Output: {final_output}")
print("Final State:")
print(flow.state)

```

In this example, the state is updated by both `first_method` and `second_method`.
After the Flow has run, you can access the final state to see the updates made by these methods.

By ensuring that the final method’s output is returned and providing access to the state, CrewAI Flows make it easy to integrate the results of your AI workflows into larger applications or systems,
while also maintaining and accessing the state throughout the Flow’s execution.

## [​](https://docs.crewai.com/concepts/flows\#flow-state-management)  Flow State Management

Managing state effectively is crucial for building reliable and maintainable AI workflows. CrewAI Flows provides robust mechanisms for both unstructured and structured state management,
allowing developers to choose the approach that best fits their application’s needs.

### [​](https://docs.crewai.com/concepts/flows\#unstructured-state-management)  Unstructured State Management

In unstructured state management, all state is stored in the `state` attribute of the `Flow` class.
This approach offers flexibility, enabling developers to add or modify state attributes on the fly without defining a strict schema.
Even with unstructured states, CrewAI Flows automatically generates and maintains a unique identifier (UUID) for each state instance.

Code

Copy

```python
from crewai.flow.flow import Flow, listen, start

class UnstructuredExampleFlow(Flow):

    @start()
    def first_method(self):
        # The state automatically includes an 'id' field
        print(f"State ID: {self.state['id']}")
        self.state['counter'] = 0
        self.state['message'] = "Hello from structured flow"

    @listen(first_method)
    def second_method(self):
        self.state['counter'] += 1
        self.state['message'] += " - updated"

    @listen(second_method)
    def third_method(self):
        self.state['counter'] += 1
        self.state['message'] += " - updated again"

        print(f"State after third_method: {self.state}")

flow = UnstructuredExampleFlow()
flow.kickoff()

```

**Note:** The `id` field is automatically generated and preserved throughout the flow’s execution. You don’t need to manage or set it manually, and it will be maintained even when updating the state with new data.

**Key Points:**

- **Flexibility:** You can dynamically add attributes to `self.state` without predefined constraints.
- **Simplicity:** Ideal for straightforward workflows where state structure is minimal or varies significantly.

### [​](https://docs.crewai.com/concepts/flows\#structured-state-management)  Structured State Management

Structured state management leverages predefined schemas to ensure consistency and type safety across the workflow.
By using models like Pydantic’s `BaseModel`, developers can define the exact shape of the state, enabling better validation and auto-completion in development environments.

Each state in CrewAI Flows automatically receives a unique identifier (UUID) to help track and manage state instances. This ID is automatically generated and managed by the Flow system.

Code

Copy

```python
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

class ExampleState(BaseModel):
    # Note: 'id' field is automatically added to all states
    counter: int = 0
    message: str = ""

class StructuredExampleFlow(Flow[ExampleState]):

    @start()
    def first_method(self):
        # Access the auto-generated ID if needed
        print(f"State ID: {self.state.id}")
        self.state.message = "Hello from structured flow"

    @listen(first_method)
    def second_method(self):
        self.state.counter += 1
        self.state.message += " - updated"

    @listen(second_method)
    def third_method(self):
        self.state.counter += 1
        self.state.message += " - updated again"

        print(f"State after third_method: {self.state}")

flow = StructuredExampleFlow()
flow.kickoff()

```

**Key Points:**

- **Defined Schema:** `ExampleState` clearly outlines the state structure, enhancing code readability and maintainability.
- **Type Safety:** Leveraging Pydantic ensures that state attributes adhere to the specified types, reducing runtime errors.
- **Auto-Completion:** IDEs can provide better auto-completion and error checking based on the defined state model.

### [​](https://docs.crewai.com/concepts/flows\#choosing-between-unstructured-and-structured-state-management)  Choosing Between Unstructured and Structured State Management

- **Use Unstructured State Management when:**
  - The workflow’s state is simple or highly dynamic.
  - Flexibility is prioritized over strict state definitions.
  - Rapid prototyping is required without the overhead of defining schemas.
- **Use Structured State Management when:**
  - The workflow requires a well-defined and consistent state structure.
  - Type safety and validation are important for your application’s reliability.
  - You want to leverage IDE features like auto-completion and type checking for better developer experience.

By providing both unstructured and structured state management options, CrewAI Flows empowers developers to build AI workflows that are both flexible and robust, catering to a wide range of application requirements.

## [​](https://docs.crewai.com/concepts/flows\#flow-persistence)  Flow Persistence

The @persist decorator enables automatic state persistence in CrewAI Flows, allowing you to maintain flow state across restarts or different workflow executions. This decorator can be applied at either the class level or method level, providing flexibility in how you manage state persistence.

### [​](https://docs.crewai.com/concepts/flows\#class-level-persistence)  Class-Level Persistence

When applied at the class level, the @persist decorator automatically persists all flow method states:

Copy

```python
@persist  # Using SQLiteFlowPersistence by default
class MyFlow(Flow[MyState]):
    @start()
    def initialize_flow(self):
        # This method will automatically have its state persisted
        self.state.counter = 1
        print("Initialized flow. State ID:", self.state.id)

    @listen(initialize_flow)
    def next_step(self):
        # The state (including self.state.id) is automatically reloaded
        self.state.counter += 1
        print("Flow state is persisted. Counter:", self.state.counter)

```

### [​](https://docs.crewai.com/concepts/flows\#method-level-persistence)  Method-Level Persistence

For more granular control, you can apply @persist to specific methods:

Copy

```python
class AnotherFlow(Flow[dict]):
    @persist  # Persists only this method's state
    @start()
    def begin(self):
        if "runs" not in self.state:
            self.state["runs"] = 0
        self.state["runs"] += 1
        print("Method-level persisted runs:", self.state["runs"])

```

### [​](https://docs.crewai.com/concepts/flows\#how-it-works)  How It Works

1. **Unique State Identification**
   - Each flow state automatically receives a unique UUID
   - The ID is preserved across state updates and method calls
   - Supports both structured (Pydantic BaseModel) and unstructured (dictionary) states
2. **Default SQLite Backend**
   - SQLiteFlowPersistence is the default storage backend
   - States are automatically saved to a local SQLite database
   - Robust error handling ensures clear messages if database operations fail
3. **Error Handling**
   - Comprehensive error messages for database operations
   - Automatic state validation during save and load
   - Clear feedback when persistence operations encounter issues

### [​](https://docs.crewai.com/concepts/flows\#important-considerations)  Important Considerations

- **State Types**: Both structured (Pydantic BaseModel) and unstructured (dictionary) states are supported
- **Automatic ID**: The `id` field is automatically added if not present
- **State Recovery**: Failed or restarted flows can automatically reload their previous state
- **Custom Implementation**: You can provide your own FlowPersistence implementation for specialized storage needs

### [​](https://docs.crewai.com/concepts/flows\#technical-advantages)  Technical Advantages

1. **Precise Control Through Low-Level Access**
   - Direct access to persistence operations for advanced use cases
   - Fine-grained control via method-level persistence decorators
   - Built-in state inspection and debugging capabilities
   - Full visibility into state changes and persistence operations
2. **Enhanced Reliability**
   - Automatic state recovery after system failures or restarts
   - Transaction-based state updates for data integrity
   - Comprehensive error handling with clear error messages
   - Robust validation during state save and load operations
3. **Extensible Architecture**
   - Customizable persistence backend through FlowPersistence interface
   - Support for specialized storage solutions beyond SQLite
   - Compatible with both structured (Pydantic) and unstructured (dict) states
   - Seamless integration with existing CrewAI flow patterns

The persistence system’s architecture emphasizes technical precision and customization options, allowing developers to maintain full control over state management while benefiting from built-in reliability features.

## [​](https://docs.crewai.com/concepts/flows\#flow-control)  Flow Control

### [​](https://docs.crewai.com/concepts/flows\#conditional-logic%3A-or)  Conditional Logic: `or`

The `or_` function in Flows allows you to listen to multiple methods and trigger the listener method when any of the specified methods emit an output.

Code

Output

Copy

```python
from crewai.flow.flow import Flow, listen, or_, start

class OrExampleFlow(Flow):

    @start()
    def start_method(self):
        return "Hello from the start method"

    @listen(start_method)
    def second_method(self):
        return "Hello from the second method"

    @listen(or_(start_method, second_method))
    def logger(self, result):
        print(f"Logger: {result}")

flow = OrExampleFlow()
flow.kickoff()

```

When you run this Flow, the `logger` method will be triggered by the output of either the `start_method` or the `second_method`.
The `or_` function is used to listen to multiple methods and trigger the listener method when any of the specified methods emit an output.

### [​](https://docs.crewai.com/concepts/flows\#conditional-logic%3A-and)  Conditional Logic: `and`

The `and_` function in Flows allows you to listen to multiple methods and trigger the listener method only when all the specified methods emit an output.

Code

Output

Copy

```python
from crewai.flow.flow import Flow, and_, listen, start

class AndExampleFlow(Flow):

    @start()
    def start_method(self):
        self.state["greeting"] = "Hello from the start method"

    @listen(start_method)
    def second_method(self):
        self.state["joke"] = "What do computers eat? Microchips."

    @listen(and_(start_method, second_method))
    def logger(self):
        print("---- Logger ----")
        print(self.state)

flow = AndExampleFlow()
flow.kickoff()

```

When you run this Flow, the `logger` method will be triggered only when both the `start_method` and the `second_method` emit an output.
The `and_` function is used to listen to multiple methods and trigger the listener method only when all the specified methods emit an output.

### [​](https://docs.crewai.com/concepts/flows\#router)  Router

The `@router()` decorator in Flows allows you to define conditional routing logic based on the output of a method.
You can specify different routes based on the output of the method, allowing you to control the flow of execution dynamically.

Code

Output

Copy

```python
import random
from crewai.flow.flow import Flow, listen, router, start
from pydantic import BaseModel

class ExampleState(BaseModel):
    success_flag: bool = False

class RouterFlow(Flow[ExampleState]):

    @start()
    def start_method(self):
        print("Starting the structured flow")
        random_boolean = random.choice([True, False])
        self.state.success_flag = random_boolean

    @router(start_method)
    def second_method(self):
        if self.state.success_flag:
            return "success"
        else:
            return "failed"

    @listen("success")
    def third_method(self):
        print("Third method running")

    @listen("failed")
    def fourth_method(self):
        print("Fourth method running")

flow = RouterFlow()
flow.kickoff()

```

In the above example, the `start_method` generates a random boolean value and sets it in the state.
The `second_method` uses the `@router()` decorator to define conditional routing logic based on the value of the boolean.
If the boolean is `True`, the method returns `"success"`, and if it is `False`, the method returns `"failed"`.
The `third_method` and `fourth_method` listen to the output of the `second_method` and execute based on the returned value.

When you run this Flow, the output will change based on the random boolean value generated by the `start_method`.

## [​](https://docs.crewai.com/concepts/flows\#adding-crews-to-flows)  Adding Crews to Flows

Creating a flow with multiple crews in CrewAI is straightforward.

You can generate a new CrewAI project that includes all the scaffolding needed to create a flow with multiple crews by running the following command:

Copy

```bash
crewai create flow name_of_flow

```

This command will generate a new CrewAI project with the necessary folder structure. The generated project includes a prebuilt crew called `poem_crew` that is already working. You can use this crew as a template by copying, pasting, and editing it to create other crews.

### [​](https://docs.crewai.com/concepts/flows\#folder-structure)  Folder Structure

After running the `crewai create flow name_of_flow` command, you will see a folder structure similar to the following:

| Directory/File | Description |
| --- | --- |
| `name_of_flow/` | Root directory for the flow. |
| ├── `crews/` | Contains directories for specific crews. |
| │ └── `poem_crew/` | Directory for the “poem\_crew” with its configurations and scripts. |
| │ ├── `config/` | Configuration files directory for the “poem\_crew”. |
| │ │ ├── `agents.yaml` | YAML file defining the agents for “poem\_crew”. |
| │ │ └── `tasks.yaml` | YAML file defining the tasks for “poem\_crew”. |
| │ ├── `poem_crew.py` | Script for “poem\_crew” functionality. |
| ├── `tools/` | Directory for additional tools used in the flow. |
| │ └── `custom_tool.py` | Custom tool implementation. |
| ├── `main.py` | Main script for running the flow. |
| ├── `README.md` | Project description and instructions. |
| ├── `pyproject.toml` | Configuration file for project dependencies and settings. |
| └── `.gitignore` | Specifies files and directories to ignore in version control. |

### [​](https://docs.crewai.com/concepts/flows\#building-your-crews)  Building Your Crews

In the `crews` folder, you can define multiple crews. Each crew will have its own folder containing configuration files and the crew definition file. For example, the `poem_crew` folder contains:

- `config/agents.yaml`: Defines the agents for the crew.
- `config/tasks.yaml`: Defines the tasks for the crew.
- `poem_crew.py`: Contains the crew definition, including agents, tasks, and the crew itself.

You can copy, paste, and edit the `poem_crew` to create other crews.

### [​](https://docs.crewai.com/concepts/flows\#connecting-crews-in-main-py)  Connecting Crews in `main.py`

The `main.py` file is where you create your flow and connect the crews together. You can define your flow by using the `Flow` class and the decorators `@start` and `@listen` to specify the flow of execution.

Here’s an example of how you can connect the `poem_crew` in the `main.py` file:

Code

Copy

```python
#!/usr/bin/env python
from random import randint

from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from .crews.poem_crew.poem_crew import PoemCrew

class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""

class PoemFlow(Flow[PoemState]):

    @start()
    def generate_sentence_count(self):
        print("Generating sentence count")
        self.state.sentence_count = randint(1, 5)

    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem")
        result = PoemCrew().crew().kickoff(inputs={"sentence_count": self.state.sentence_count})

        print("Poem generated", result.raw)
        self.state.poem = result.raw

    @listen(generate_poem)
    def save_poem(self):
        print("Saving poem")
        with open("poem.txt", "w") as f:
            f.write(self.state.poem)

def kickoff():
    poem_flow = PoemFlow()
    poem_flow.kickoff()

def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()

if __name__ == "__main__":
    kickoff()

```

In this example, the `PoemFlow` class defines a flow that generates a sentence count, uses the `PoemCrew` to generate a poem, and then saves the poem to a file. The flow is kicked off by calling the `kickoff()` method.

### [​](https://docs.crewai.com/concepts/flows\#running-the-flow)  Running the Flow

(Optional) Before running the flow, you can install the dependencies by running:

Copy

```bash
crewai install

```

Once all of the dependencies are installed, you need to activate the virtual environment by running:

Copy

```bash
source .venv/bin/activate

```

After activating the virtual environment, you can run the flow by executing one of the following commands:

Copy

```bash
crewai flow kickoff

```

or

Copy

```bash
uv run kickoff

```

The flow will execute, and you should see the output in the console.

## [​](https://docs.crewai.com/concepts/flows\#plot-flows)  Plot Flows

Visualizing your AI workflows can provide valuable insights into the structure and execution paths of your flows. CrewAI offers a powerful visualization tool that allows you to generate interactive plots of your flows, making it easier to understand and optimize your AI workflows.

### [​](https://docs.crewai.com/concepts/flows\#what-are-plots%3F)  What are Plots?

Plots in CrewAI are graphical representations of your AI workflows. They display the various tasks, their connections, and the flow of data between them. This visualization helps in understanding the sequence of operations, identifying bottlenecks, and ensuring that the workflow logic aligns with your expectations.

### [​](https://docs.crewai.com/concepts/flows\#how-to-generate-a-plot)  How to Generate a Plot

CrewAI provides two convenient methods to generate plots of your flows:

#### [​](https://docs.crewai.com/concepts/flows\#option-1%3A-using-the-plot-method)  Option 1: Using the `plot()` Method

If you are working directly with a flow instance, you can generate a plot by calling the `plot()` method on your flow object. This method will create an HTML file containing the interactive plot of your flow.

Code

Copy

```python
# Assuming you have a flow instance
flow.plot("my_flow_plot")

```

This will generate a file named `my_flow_plot.html` in your current directory. You can open this file in a web browser to view the interactive plot.

#### [​](https://docs.crewai.com/concepts/flows\#option-2%3A-using-the-command-line)  Option 2: Using the Command Line

If you are working within a structured CrewAI project, you can generate a plot using the command line. This is particularly useful for larger projects where you want to visualize the entire flow setup.

Copy

```bash
crewai flow plot

```

This command will generate an HTML file with the plot of your flow, similar to the `plot()` method. The file will be saved in your project directory, and you can open it in a web browser to explore the flow.

### [​](https://docs.crewai.com/concepts/flows\#understanding-the-plot)  Understanding the Plot

The generated plot will display nodes representing the tasks in your flow, with directed edges indicating the flow of execution. The plot is interactive, allowing you to zoom in and out, and hover over nodes to see additional details.

By visualizing your flows, you can gain a clearer understanding of the workflow’s structure, making it easier to debug, optimize, and communicate your AI processes to others.

### [​](https://docs.crewai.com/concepts/flows\#conclusion)  Conclusion

Plotting your flows is a powerful feature of CrewAI that enhances your ability to design and manage complex AI workflows. Whether you choose to use the `plot()` method or the command line, generating plots will provide you with a visual representation of your workflows, aiding in both development and presentation.

## [​](https://docs.crewai.com/concepts/flows\#next-steps)  Next Steps

If you’re interested in exploring additional examples of flows, we have a variety of recommendations in our examples repository. Here are four specific flow examples, each showcasing unique use cases to help you match your current problem type to a specific example:

1. **Email Auto Responder Flow**: This example demonstrates an infinite loop where a background job continually runs to automate email responses. It’s a great use case for tasks that need to be performed repeatedly without manual intervention. [View Example](https://github.com/crewAIInc/crewAI-examples/tree/main/email_auto_responder_flow)

2. **Lead Score Flow**: This flow showcases adding human-in-the-loop feedback and handling different conditional branches using the router. It’s an excellent example of how to incorporate dynamic decision-making and human oversight into your workflows. [View Example](https://github.com/crewAIInc/crewAI-examples/tree/main/lead-score-flow)

3. **Write a Book Flow**: This example excels at chaining multiple crews together, where the output of one crew is used by another. Specifically, one crew outlines an entire book, and another crew generates chapters based on the outline. Eventually, everything is connected to produce a complete book. This flow is perfect for complex, multi-step processes that require coordination between different tasks. [View Example](https://github.com/crewAIInc/crewAI-examples/tree/main/write_a_book_with_flows)

4. **Meeting Assistant Flow**: This flow demonstrates how to broadcast one event to trigger multiple follow-up actions. For instance, after a meeting is completed, the flow can update a Trello board, send a Slack message, and save the results. It’s a great example of handling multiple outcomes from a single event, making it ideal for comprehensive task management and notification systems. [View Example](https://github.com/crewAIInc/crewAI-examples/tree/main/meeting_assistant_flow)


By exploring these examples, you can gain insights into how to leverage CrewAI Flows for various use cases, from automating repetitive tasks to managing complex, multi-step processes with dynamic decision-making and human feedback.

Also, check out our YouTube video on how to use flows in CrewAI below!

CrewAI Flows \| Sales Pipeline Flow Demo - YouTube

CrewAI

3.58K subscribers

[CrewAI Flows \| Sales Pipeline Flow Demo](https://www.youtube.com/watch?v=MTb5my6VOT8)

CrewAI

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

Full screen is unavailable. [Learn More](https://support.google.com/youtube/answer/6276924)

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

More videos

## More videos

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=MTb5my6VOT8&embeds_referring_euri=https%3A%2F%2Fdocs.crewai.com%2F)

0:00

0:00 / 6:17•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=MTb5my6VOT8 "Watch on YouTube")

Was this page helpful?

YesNo

[Crews](https://docs.crewai.com/concepts/crews) [Knowledge](https://docs.crewai.com/concepts/knowledge)

On this page

- [Introduction](https://docs.crewai.com/concepts/flows#introduction)
- [Getting Started](https://docs.crewai.com/concepts/flows#getting-started)
- [@start()](https://docs.crewai.com/concepts/flows#%40start)
- [@listen()](https://docs.crewai.com/concepts/flows#%40listen)
- [Usage](https://docs.crewai.com/concepts/flows#usage)
- [Flow Output](https://docs.crewai.com/concepts/flows#flow-output)
- [Retrieving the Final Output](https://docs.crewai.com/concepts/flows#retrieving-the-final-output)
- [Accessing and Updating State](https://docs.crewai.com/concepts/flows#accessing-and-updating-state)
- [Flow State Management](https://docs.crewai.com/concepts/flows#flow-state-management)
- [Unstructured State Management](https://docs.crewai.com/concepts/flows#unstructured-state-management)
- [Structured State Management](https://docs.crewai.com/concepts/flows#structured-state-management)
- [Choosing Between Unstructured and Structured State Management](https://docs.crewai.com/concepts/flows#choosing-between-unstructured-and-structured-state-management)
- [Flow Persistence](https://docs.crewai.com/concepts/flows#flow-persistence)
- [Class-Level Persistence](https://docs.crewai.com/concepts/flows#class-level-persistence)
- [Method-Level Persistence](https://docs.crewai.com/concepts/flows#method-level-persistence)
- [How It Works](https://docs.crewai.com/concepts/flows#how-it-works)
- [Important Considerations](https://docs.crewai.com/concepts/flows#important-considerations)
- [Technical Advantages](https://docs.crewai.com/concepts/flows#technical-advantages)
- [Flow Control](https://docs.crewai.com/concepts/flows#flow-control)
- [Conditional Logic: or](https://docs.crewai.com/concepts/flows#conditional-logic%3A-or)
- [Conditional Logic: and](https://docs.crewai.com/concepts/flows#conditional-logic%3A-and)
- [Router](https://docs.crewai.com/concepts/flows#router)
- [Adding Crews to Flows](https://docs.crewai.com/concepts/flows#adding-crews-to-flows)
- [Folder Structure](https://docs.crewai.com/concepts/flows#folder-structure)
- [Building Your Crews](https://docs.crewai.com/concepts/flows#building-your-crews)
- [Connecting Crews in main.py](https://docs.crewai.com/concepts/flows#connecting-crews-in-main-py)
- [Running the Flow](https://docs.crewai.com/concepts/flows#running-the-flow)
- [Plot Flows](https://docs.crewai.com/concepts/flows#plot-flows)
- [What are Plots?](https://docs.crewai.com/concepts/flows#what-are-plots%3F)
- [How to Generate a Plot](https://docs.crewai.com/concepts/flows#how-to-generate-a-plot)
- [Option 1: Using the plot() Method](https://docs.crewai.com/concepts/flows#option-1%3A-using-the-plot-method)
- [Option 2: Using the Command Line](https://docs.crewai.com/concepts/flows#option-2%3A-using-the-command-line)
- [Understanding the Plot](https://docs.crewai.com/concepts/flows#understanding-the-plot)
- [Conclusion](https://docs.crewai.com/concepts/flows#conclusion)
- [Next Steps](https://docs.crewai.com/concepts/flows#next-steps)

# File Write - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

File Write

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/filewritetool\#filewritertool)  `FileWriterTool`

## [​](https://docs.crewai.com/tools/filewritetool\#description)  Description

The `FileWriterTool` is a component of the crewai\_tools package, designed to simplify the process of writing content to files with cross-platform compatibility (Windows, Linux, macOS).
It is particularly useful in scenarios such as generating reports, saving logs, creating configuration files, and more.
This tool handles path differences across operating systems, supports UTF-8 encoding, and automatically creates directories if they don’t exist, making it easier to organize your output reliably across different platforms.

## [​](https://docs.crewai.com/tools/filewritetool\#installation)  Installation

Install the crewai\_tools package to use the `FileWriterTool` in your projects:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/filewritetool\#example)  Example

To get started with the `FileWriterTool`:

Code

Copy

```python
from crewai_tools import FileWriterTool

# Initialize the tool
file_writer_tool = FileWriterTool()

# Write content to a file in a specified directory
result = file_writer_tool._run('example.txt', 'This is a test content.', 'test_directory')
print(result)

```

## [​](https://docs.crewai.com/tools/filewritetool\#arguments)  Arguments

- `filename`: The name of the file you want to create or overwrite.
- `content`: The content to write into the file.
- `directory` (optional): The path to the directory where the file will be created. Defaults to the current directory ( `.`). If the directory does not exist, it will be created.

## [​](https://docs.crewai.com/tools/filewritetool\#conclusion)  Conclusion

By integrating the `FileWriterTool` into your crews, the agents can reliably write content to files across different operating systems.
This tool is essential for tasks that require saving output data, creating structured file systems, and handling cross-platform file operations.
It’s particularly recommended for Windows users who may encounter file writing issues with standard Python file operations.

By adhering to the setup and usage guidelines provided, incorporating this tool into projects is straightforward and ensures consistent file writing behavior across all platforms.

Was this page helpful?

YesNo

[File Read](https://docs.crewai.com/tools/filereadtool) [Firecrawl Crawl Website](https://docs.crewai.com/tools/firecrawlcrawlwebsitetool)

On this page

- [FileWriterTool](https://docs.crewai.com/tools/filewritetool#filewritertool)
- [Description](https://docs.crewai.com/tools/filewritetool#description)
- [Installation](https://docs.crewai.com/tools/filewritetool#installation)
- [Example](https://docs.crewai.com/tools/filewritetool#example)
- [Arguments](https://docs.crewai.com/tools/filewritetool#arguments)
- [Conclusion](https://docs.crewai.com/tools/filewritetool#conclusion)

# MySQL RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

MySQL RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/mysqltool\#mysqlsearchtool)  `MySQLSearchTool`

## [​](https://docs.crewai.com/tools/mysqltool\#description)  Description

This tool is designed to facilitate semantic searches within MySQL database tables. Leveraging the RAG (Retrieve and Generate) technology,
the MySQLSearchTool provides users with an efficient means of querying database table content, specifically tailored for MySQL databases.
It simplifies the process of finding relevant data through semantic search queries, making it an invaluable resource for users needing
to perform advanced queries on extensive datasets within a MySQL database.

## [​](https://docs.crewai.com/tools/mysqltool\#installation)  Installation

To install the `crewai_tools` package and utilize the MySQLSearchTool, execute the following command in your terminal:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/mysqltool\#example)  Example

Below is an example showcasing how to use the MySQLSearchTool to conduct a semantic search on a table within a MySQL database:

Code

Copy

```python
from crewai_tools import MySQLSearchTool

# Initialize the tool with the database URI and the target table name
tool = MySQLSearchTool(
    db_uri='mysql://user:password@localhost:3306/mydatabase',
    table_name='employees'
)

```

## [​](https://docs.crewai.com/tools/mysqltool\#arguments)  Arguments

The MySQLSearchTool requires the following arguments for its operation:

- `db_uri`: A string representing the URI of the MySQL database to be queried. This argument is mandatory and must include the necessary authentication details and the location of the database.
- `table_name`: A string specifying the name of the table within the database on which the semantic search will be performed. This argument is mandatory.

## [​](https://docs.crewai.com/tools/mysqltool\#custom-model-and-embeddings)  Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

Code

Copy

```python
tool = MySQLSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[MDX RAG Search](https://docs.crewai.com/tools/mdxsearchtool) [NL2SQL Tool](https://docs.crewai.com/tools/nl2sqltool)

On this page

- [MySQLSearchTool](https://docs.crewai.com/tools/mysqltool#mysqlsearchtool)
- [Description](https://docs.crewai.com/tools/mysqltool#description)
- [Installation](https://docs.crewai.com/tools/mysqltool#installation)
- [Example](https://docs.crewai.com/tools/mysqltool#example)
- [Arguments](https://docs.crewai.com/tools/mysqltool#arguments)
- [Custom model and embeddings](https://docs.crewai.com/tools/mysqltool#custom-model-and-embeddings)

# Google Serper Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Google Serper Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/serperdevtool\#serperdevtool)  `SerperDevTool`

We are still working on improving tools, so there might be unexpected behavior or changes in the future.

## [​](https://docs.crewai.com/tools/serperdevtool\#description)  Description

This tool is designed to perform a semantic search for a specified query from a text’s content across the internet. It utilizes the [serper.dev](https://serper.dev/) API
to fetch and display the most relevant search results based on the query provided by the user.

## [​](https://docs.crewai.com/tools/serperdevtool\#installation)  Installation

To incorporate this tool into your project, follow the installation instructions below:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/serperdevtool\#example)  Example

The following example demonstrates how to initialize the tool and execute a search with a given query:

Code

Copy

```python
from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()

```

## [​](https://docs.crewai.com/tools/serperdevtool\#steps-to-get-started)  Steps to Get Started

To effectively use the `SerperDevTool`, follow these steps:

1. **Package Installation**: Confirm that the `crewai[tools]` package is installed in your Python environment.
2. **API Key Acquisition**: Acquire a `serper.dev` API key by registering for a free account at `serper.dev`.
3. **Environment Configuration**: Store your obtained API key in an environment variable named `SERPER_API_KEY` to facilitate its use by the tool.

## [​](https://docs.crewai.com/tools/serperdevtool\#parameters)  Parameters

The `SerperDevTool` comes with several parameters that will be passed to the API :

- **search\_url**: The URL endpoint for the search API. (Default is `https://google.serper.dev/search`)

- **country**: Optional. Specify the country for the search results.

- **location**: Optional. Specify the location for the search results.

- **locale**: Optional. Specify the locale for the search results.

- **n\_results**: Number of search results to return. Default is `10`.


The values for `country`, `location`, `locale` and `search_url` can be found on the [Serper Playground](https://serper.dev/playground).

## [​](https://docs.crewai.com/tools/serperdevtool\#example-with-parameters)  Example with Parameters

Here is an example demonstrating how to use the tool with additional parameters:

Code

Copy

```python
from crewai_tools import SerperDevTool

tool = SerperDevTool(
    search_url="https://google.serper.dev/scholar",
    n_results=2,
)

print(tool.run(search_query="ChatGPT"))

# Using Tool: Search the internet

# Search results: Title: Role of chat gpt in public health
# Link: https://link.springer.com/article/10.1007/s10439-023-03172-7
# Snippet: … ChatGPT in public health. In this overview, we will examine the potential uses of ChatGPT in
# ---
# Title: Potential use of chat gpt in global warming
# Link: https://link.springer.com/article/10.1007/s10439-023-03171-8
# Snippet: … as ChatGPT, have the potential to play a critical role in advancing our understanding of climate
# ---

```

Code

Copy

```python
from crewai_tools import SerperDevTool

tool = SerperDevTool(
    country="fr",
    locale="fr",
    location="Paris, Paris, Ile-de-France, France",
    n_results=2,
)

print(tool.run(search_query="Jeux Olympiques"))

# Using Tool: Search the internet

# Search results: Title: Jeux Olympiques de Paris 2024 - Actualités, calendriers, résultats
# Link: https://olympics.com/fr/paris-2024
# Snippet: Quels sont les sports présents aux Jeux Olympiques de Paris 2024 ? · Athlétisme · Aviron · Badminton · Basketball · Basketball 3x3 · Boxe · Breaking · Canoë ...
# ---
# Title: Billetterie Officielle de Paris 2024 - Jeux Olympiques et Paralympiques
# Link: https://tickets.paris2024.org/
# Snippet: Achetez vos billets exclusivement sur le site officiel de la billetterie de Paris 2024 pour participer au plus grand événement sportif au monde.
# ---

```

## [​](https://docs.crewai.com/tools/serperdevtool\#conclusion)  Conclusion

By integrating the `SerperDevTool` into Python projects, users gain the ability to conduct real-time, relevant searches across the internet directly from their applications.
The updated parameters allow for more customized and localized search results. By adhering to the setup and usage guidelines provided, incorporating this tool into projects is streamlined and straightforward.

Was this page helpful?

YesNo

[Github Search](https://docs.crewai.com/tools/githubsearchtool) [JSON RAG Search](https://docs.crewai.com/tools/jsonsearchtool)

On this page

- [SerperDevTool](https://docs.crewai.com/tools/serperdevtool#serperdevtool)
- [Description](https://docs.crewai.com/tools/serperdevtool#description)
- [Installation](https://docs.crewai.com/tools/serperdevtool#installation)
- [Example](https://docs.crewai.com/tools/serperdevtool#example)
- [Steps to Get Started](https://docs.crewai.com/tools/serperdevtool#steps-to-get-started)
- [Parameters](https://docs.crewai.com/tools/serperdevtool#parameters)
- [Example with Parameters](https://docs.crewai.com/tools/serperdevtool#example-with-parameters)
- [Conclusion](https://docs.crewai.com/tools/serperdevtool#conclusion)

# Collaboration - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Collaboration

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/collaboration\#collaboration-fundamentals)  Collaboration Fundamentals

Collaboration in CrewAI is fundamental, enabling agents to combine their skills, share information, and assist each other in task execution, embodying a truly cooperative ecosystem.

- **Information Sharing**: Ensures all agents are well-informed and can contribute effectively by sharing data and findings.
- **Task Assistance**: Allows agents to seek help from peers with the required expertise for specific tasks.
- **Resource Allocation**: Optimizes task execution through the efficient distribution and sharing of resources among agents.

## [​](https://docs.crewai.com/concepts/collaboration\#enhanced-attributes-for-improved-collaboration)  Enhanced Attributes for Improved Collaboration

The `Crew` class has been enriched with several attributes to support advanced functionalities:

| Feature | Description |
| --- | --- |
| **Language Model Management** ( `manager_llm`, `function_calling_llm`) | Manages language models for executing tasks and tools. `manager_llm` is required for hierarchical processes, while `function_calling_llm` is optional with a default value for streamlined interactions. |
| **Custom Manager Agent** ( `manager_agent`) | Specifies a custom agent as the manager, replacing the default CrewAI manager. |
| **Process Flow** ( `process`) | Defines execution logic (e.g., sequential, hierarchical) for task distribution. |
| **Verbose Logging** ( `verbose`) | Provides detailed logging for monitoring and debugging. Accepts integer and boolean values to control verbosity level. |
| **Rate Limiting** ( `max_rpm`) | Limits requests per minute to optimize resource usage. Setting guidelines depend on task complexity and load. |
| **Internationalization / Customization** ( `language`, `prompt_file`) | Supports prompt customization for global usability. [Example of file](https://github.com/joaomdmoura/crewAI/blob/main/src/crewai/translations/en.json) |
| **Execution and Output Handling** ( `full_output`) | Controls output granularity, distinguishing between full and final outputs. |
| **Callback and Telemetry** ( `step_callback`, `task_callback`) | Enables step-wise and task-level execution monitoring and telemetry for performance analytics. |
| **Crew Sharing** ( `share_crew`) | Allows sharing crew data with CrewAI for model improvement. Privacy implications and benefits should be considered. |
| **Usage Metrics** ( `usage_metrics`) | Logs all LLM usage metrics during task execution for performance insights. |
| **Memory Usage** ( `memory`) | Enables memory for storing execution history, aiding in agent learning and task efficiency. |
| **Embedder Configuration** ( `embedder`) | Configures the embedder for language understanding and generation, with support for provider customization. |
| **Cache Management** ( `cache`) | Specifies whether to cache tool execution results, enhancing performance. |
| **Output Logging** ( `output_log_file`) | Defines the file path for logging crew execution output. |
| **Planning Mode** ( `planning`) | Enables action planning before task execution. Set `planning=True` to activate. |
| **Replay Feature** ( `replay`) | Provides CLI for listing tasks from the last run and replaying from specific tasks, aiding in task management and troubleshooting. |

## [​](https://docs.crewai.com/concepts/collaboration\#delegation-dividing-to-conquer)  Delegation (Dividing to Conquer)

Delegation enhances functionality by allowing agents to intelligently assign tasks or seek help, thereby amplifying the crew’s overall capability.

## [​](https://docs.crewai.com/concepts/collaboration\#implementing-collaboration-and-delegation)  Implementing Collaboration and Delegation

Setting up a crew involves defining the roles and capabilities of each agent. CrewAI seamlessly manages their interactions, ensuring efficient collaboration and delegation, with enhanced customization and monitoring features to adapt to various operational needs.

## [​](https://docs.crewai.com/concepts/collaboration\#example-scenario)  Example Scenario

Consider a crew with a researcher agent tasked with data gathering and a writer agent responsible for compiling reports. The integration of advanced language model management and process flow attributes allows for more sophisticated interactions, such as the writer delegating complex research tasks to the researcher or querying specific information, thereby facilitating a seamless workflow.

## [​](https://docs.crewai.com/concepts/collaboration\#conclusion)  Conclusion

The integration of advanced attributes and functionalities into the CrewAI framework significantly enriches the agent collaboration ecosystem. These enhancements not only simplify interactions but also offer unprecedented flexibility and control, paving the way for sophisticated AI-driven solutions capable of tackling complex tasks through intelligent collaboration and delegation.

Was this page helpful?

YesNo

[Processes](https://docs.crewai.com/concepts/processes) [Training](https://docs.crewai.com/concepts/training)

On this page

- [Collaboration Fundamentals](https://docs.crewai.com/concepts/collaboration#collaboration-fundamentals)
- [Enhanced Attributes for Improved Collaboration](https://docs.crewai.com/concepts/collaboration#enhanced-attributes-for-improved-collaboration)
- [Delegation (Dividing to Conquer)](https://docs.crewai.com/concepts/collaboration#delegation-dividing-to-conquer)
- [Implementing Collaboration and Delegation](https://docs.crewai.com/concepts/collaboration#implementing-collaboration-and-delegation)
- [Example Scenario](https://docs.crewai.com/concepts/collaboration#example-scenario)
- [Conclusion](https://docs.crewai.com/concepts/collaboration#conclusion)

# MDX RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

MDX RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/mdxsearchtool\#mdxsearchtool)  `MDXSearchTool`

The MDXSearchTool is in continuous development. Features may be added or removed, and functionality could change unpredictably as we refine the tool.

## [​](https://docs.crewai.com/tools/mdxsearchtool\#description)  Description

The MDX Search Tool is a component of the `crewai_tools` package aimed at facilitating advanced markdown language extraction. It enables users to effectively search and extract relevant information from MD files using query-based searches. This tool is invaluable for data analysis, information management, and research tasks, streamlining the process of finding specific information within large document collections.

## [​](https://docs.crewai.com/tools/mdxsearchtool\#installation)  Installation

Before using the MDX Search Tool, ensure the `crewai_tools` package is installed. If it is not, you can install it with the following command:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/mdxsearchtool\#usage-example)  Usage Example

To use the MDX Search Tool, you must first set up the necessary environment variables. Then, integrate the tool into your crewAI project to begin your market research. Below is a basic example of how to do this:

Code

Copy

```python
from crewai_tools import MDXSearchTool

# Initialize the tool to search any MDX content it learns about during execution
tool = MDXSearchTool()

# OR

# Initialize the tool with a specific MDX file path for an exclusive search within that document
tool = MDXSearchTool(mdx='path/to/your/document.mdx')

```

## [​](https://docs.crewai.com/tools/mdxsearchtool\#parameters)  Parameters

- mdx: **Optional**. Specifies the MDX file path for the search. It can be provided during initialization.

## [​](https://docs.crewai.com/tools/mdxsearchtool\#customization-of-model-and-embeddings)  Customization of Model and Embeddings

The tool defaults to using OpenAI for embeddings and summarization. For customization, utilize a configuration dictionary as shown below:

Code

Copy

```python
tool = MDXSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # Options include google, openai, anthropic, llama2, etc.
            config=dict(
                model="llama2",
                # Optional parameters can be included here.
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # Optional title for the embeddings can be added here.
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[JSON RAG Search](https://docs.crewai.com/tools/jsonsearchtool) [MySQL RAG Search](https://docs.crewai.com/tools/mysqltool)

On this page

- [MDXSearchTool](https://docs.crewai.com/tools/mdxsearchtool#mdxsearchtool)
- [Description](https://docs.crewai.com/tools/mdxsearchtool#description)
- [Installation](https://docs.crewai.com/tools/mdxsearchtool#installation)
- [Usage Example](https://docs.crewai.com/tools/mdxsearchtool#usage-example)
- [Parameters](https://docs.crewai.com/tools/mdxsearchtool#parameters)
- [Customization of Model and Embeddings](https://docs.crewai.com/tools/mdxsearchtool#customization-of-model-and-embeddings)

# Agent Monitoring with Langfuse - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Agent Monitoring with Langfuse

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/how-to/langfuse-observability\#integrate-langfuse-with-crewai)  Integrate Langfuse with CrewAI

This notebook demonstrates how to integrate **Langfuse** with **CrewAI** using OpenTelemetry via the **OpenLit** SDK. By the end of this notebook, you will be able to trace your CrewAI applications with Langfuse for improved observability and debugging.

> **What is Langfuse?** [Langfuse](https://langfuse.com/) is an open-source LLM engineering platform. It provides tracing and monitoring capabilities for LLM applications, helping developers debug, analyze, and optimize their AI systems. Langfuse integrates with various tools and frameworks via native integrations, OpenTelemetry, and APIs/SDKs.

[![Langfuse Overview Video](https://github.com/user-attachments/assets/3926b288-ff61-4b95-8aa1-45d041c70866)](https://langfuse.com/watch-demo)

## [​](https://docs.crewai.com/how-to/langfuse-observability\#get-started)  Get Started

We’ll walk through a simple example of using CrewAI and integrating it with Langfuse via OpenTelemetry using OpenLit.

### [​](https://docs.crewai.com/how-to/langfuse-observability\#step-1%3A-install-dependencies)  Step 1: Install Dependencies

Copy

```python
%pip install langfuse openlit crewai crewai_tools

```

### [​](https://docs.crewai.com/how-to/langfuse-observability\#step-2%3A-set-up-environment-variables)  Step 2: Set Up Environment Variables

Set your Langfuse API keys and configure OpenTelemetry export settings to send traces to Langfuse. Please refer to the [Langfuse OpenTelemetry Docs](https://langfuse.com/docs/opentelemetry/get-started) for more information on the Langfuse OpenTelemetry endpoint `/api/public/otel` and authentication.

Copy

```python
import os
import base64

LANGFUSE_PUBLIC_KEY="pk-lf-..."
LANGFUSE_SECRET_KEY="sk-lf-..."
LANGFUSE_AUTH=base64.b64encode(f"{LANGFUSE_PUBLIC_KEY}:{LANGFUSE_SECRET_KEY}".encode()).decode()

os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "https://cloud.langfuse.com/api/public/otel" # EU data region
# os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "https://us.cloud.langfuse.com/api/public/otel" # US data region
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"Authorization=Basic {LANGFUSE_AUTH}"

# your openai key
os.environ["OPENAI_API_KEY"] = "sk-..."

```

### [​](https://docs.crewai.com/how-to/langfuse-observability\#step-3%3A-initialize-openlit)  Step 3: Initialize OpenLit

Initialize the OpenLit OpenTelemetry instrumentation SDK to start capturing OpenTelemetry traces.

Copy

```python
import openlit

openlit.init()

```

### [​](https://docs.crewai.com/how-to/langfuse-observability\#step-4%3A-create-a-simple-crewai-application)  Step 4: Create a Simple CrewAI Application

We’ll create a simple CrewAI application where multiple agents collaborate to answer a user’s question.

Copy

```python
from crewai import Agent, Task, Crew

from crewai_tools import (
    WebsiteSearchTool
)

web_rag_tool = WebsiteSearchTool()

writer = Agent(
        role="Writer",
        goal="You make math engaging and understandable for young children through poetry",
        backstory="You're an expert in writing haikus but you know nothing of math.",
        tools=[web_rag_tool],
    )

task = Task(description=("What is {multiplication}?"),
            expected_output=("Compose a haiku that includes the answer."),
            agent=writer)

crew = Crew(
  agents=[writer],
  tasks=[task],
  share_crew=False
)

```

### [​](https://docs.crewai.com/how-to/langfuse-observability\#step-5%3A-see-traces-in-langfuse)  Step 5: See Traces in Langfuse

After running the agent, you can view the traces generated by your CrewAI application in [Langfuse](https://cloud.langfuse.com/). You should see detailed steps of the LLM interactions, which can help you debug and optimize your AI agent.

![CrewAI example trace in Langfuse](https://langfuse.com/images/cookbook/integration_crewai/crewai-example-trace.png)

_[Public example trace in Langfuse](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/e2cf380ffc8d47d28da98f136140642b?timestamp=2025-02-05T15%3A12%3A02.717Z&observation=3b32338ee6a5d9af)_

## [​](https://docs.crewai.com/how-to/langfuse-observability\#references)  References

- [Langfuse OpenTelemetry Docs](https://langfuse.com/docs/opentelemetry/get-started)

Was this page helpful?

YesNo

[Agent Monitoring with Portkey](https://docs.crewai.com/how-to/portkey-observability) [Browserbase Web Loader](https://docs.crewai.com/tools/browserbaseloadtool)

On this page

- [Integrate Langfuse with CrewAI](https://docs.crewai.com/how-to/langfuse-observability#integrate-langfuse-with-crewai)
- [Get Started](https://docs.crewai.com/how-to/langfuse-observability#get-started)
- [Step 1: Install Dependencies](https://docs.crewai.com/how-to/langfuse-observability#step-1%3A-install-dependencies)
- [Step 2: Set Up Environment Variables](https://docs.crewai.com/how-to/langfuse-observability#step-2%3A-set-up-environment-variables)
- [Step 3: Initialize OpenLit](https://docs.crewai.com/how-to/langfuse-observability#step-3%3A-initialize-openlit)
- [Step 4: Create a Simple CrewAI Application](https://docs.crewai.com/how-to/langfuse-observability#step-4%3A-create-a-simple-crewai-application)
- [Step 5: See Traces in Langfuse](https://docs.crewai.com/how-to/langfuse-observability#step-5%3A-see-traces-in-langfuse)
- [References](https://docs.crewai.com/how-to/langfuse-observability#references)

![CrewAI example trace in Langfuse](https://docs.crewai.com/how-to/langfuse-observability)

![Langfuse Overview Video](https://docs.crewai.com/how-to/langfuse-observability)

# Connect to any LLM - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Connect to any LLM

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/how-to/llm-connections\#connect-crewai-to-llms)  Connect CrewAI to LLMs

CrewAI uses LiteLLM to connect to a wide variety of Language Models (LLMs). This integration provides extensive versatility, allowing you to use models from numerous providers with a simple, unified interface.

By default, CrewAI uses the `gpt-4o-mini` model. This is determined by the `OPENAI_MODEL_NAME` environment variable, which defaults to “gpt-4o-mini” if not set.
You can easily configure your agents to use a different model or provider as described in this guide.

## [​](https://docs.crewai.com/how-to/llm-connections\#supported-providers)  Supported Providers

LiteLLM supports a wide range of providers, including but not limited to:

- OpenAI
- Anthropic
- Google (Vertex AI, Gemini)
- Azure OpenAI
- AWS (Bedrock, SageMaker)
- Cohere
- VoyageAI
- Hugging Face
- Ollama
- Mistral AI
- Replicate
- Together AI
- AI21
- Cloudflare Workers AI
- DeepInfra
- Groq
- SambaNova
- [NVIDIA NIMs](https://docs.api.nvidia.com/nim/reference/models-1)
- And many more!

For a complete and up-to-date list of supported providers, please refer to the [LiteLLM Providers documentation](https://docs.litellm.ai/docs/providers).

## [​](https://docs.crewai.com/how-to/llm-connections\#changing-the-llm)  Changing the LLM

To use a different LLM with your CrewAI agents, you have several options:

- Using a String Identifier
- Using the LLM Class

Pass the model name as a string when initializing the agent:

Code

Copy

```python
from crewai import Agent

# Using OpenAI's GPT-4
openai_agent = Agent(
    role='OpenAI Expert',
    goal='Provide insights using GPT-4',
    backstory="An AI assistant powered by OpenAI's latest model.",
    llm='gpt-4'
)

# Using Anthropic's Claude
claude_agent = Agent(
    role='Anthropic Expert',
    goal='Analyze data using Claude',
    backstory="An AI assistant leveraging Anthropic's language model.",
    llm='claude-2'
)

```

## [​](https://docs.crewai.com/how-to/llm-connections\#configuration-options)  Configuration Options

When configuring an LLM for your agent, you have access to a wide range of parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| **model** | `str` | The name of the model to use (e.g., “gpt-4”, “claude-2”) |
| **temperature** | `float` | Controls randomness in output (0.0 to 1.0) |
| **max\_tokens** | `int` | Maximum number of tokens to generate |
| **top\_p** | `float` | Controls diversity of output (0.0 to 1.0) |
| **frequency\_penalty** | `float` | Penalizes new tokens based on their frequency in the text so far |
| **presence\_penalty** | `float` | Penalizes new tokens based on their presence in the text so far |
| **stop** | `str`, `List[str]` | Sequence(s) to stop generation |
| **base\_url** | `str` | The base URL for the API endpoint |
| **api\_key** | `str` | Your API key for authentication |

For a complete list of parameters and their descriptions, refer to the LLM class documentation.

## [​](https://docs.crewai.com/how-to/llm-connections\#connecting-to-openai-compatible-llms)  Connecting to OpenAI-Compatible LLMs

You can connect to OpenAI-compatible LLMs using either environment variables or by setting specific attributes on the LLM class:

- Using Environment Variables
- Using LLM Class Attributes

Code

Copy

```python
import os

os.environ["OPENAI_API_KEY"] = "your-api-key"
os.environ["OPENAI_API_BASE"] = "https://api.your-provider.com/v1"
os.environ["OPENAI_MODEL_NAME"] = "your-model-name"

```

## [​](https://docs.crewai.com/how-to/llm-connections\#using-local-models-with-ollama)  Using Local Models with Ollama

For local models like those provided by Ollama:

1

Download and install Ollama

[Click here to download and install Ollama](https://ollama.com/download)

2

Pull the desired model

For example, run `ollama pull llama3.2` to download the model.

3

Configure your agent

Code

Copy

```python
    agent = Agent(
        role='Local AI Expert',
        goal='Process information using a local model',
        backstory="An AI assistant running on local hardware.",
        llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434")
    )

```

## [​](https://docs.crewai.com/how-to/llm-connections\#changing-the-base-api-url)  Changing the Base API URL

You can change the base API URL for any LLM provider by setting the `base_url` parameter:

Code

Copy

```python
llm = LLM(
    model="custom-model-name",
    base_url="https://api.your-provider.com/v1",
    api_key="your-api-key"
)
agent = Agent(llm=llm, ...)

```

This is particularly useful when working with OpenAI-compatible APIs or when you need to specify a different endpoint for your chosen provider.

## [​](https://docs.crewai.com/how-to/llm-connections\#conclusion)  Conclusion

By leveraging LiteLLM, CrewAI offers seamless integration with a vast array of LLMs. This flexibility allows you to choose the most suitable model for your specific needs, whether you prioritize performance, cost-efficiency, or local deployment. Remember to consult the [LiteLLM documentation](https://docs.litellm.ai/docs/) for the most up-to-date information on supported models and configuration options.

Was this page helpful?

YesNo

[Create Your Own Manager Agent](https://docs.crewai.com/how-to/custom-manager-agent) [Customize Agents](https://docs.crewai.com/how-to/customizing-agents)

On this page

- [Connect CrewAI to LLMs](https://docs.crewai.com/how-to/llm-connections#connect-crewai-to-llms)
- [Supported Providers](https://docs.crewai.com/how-to/llm-connections#supported-providers)
- [Changing the LLM](https://docs.crewai.com/how-to/llm-connections#changing-the-llm)
- [Configuration Options](https://docs.crewai.com/how-to/llm-connections#configuration-options)
- [Connecting to OpenAI-Compatible LLMs](https://docs.crewai.com/how-to/llm-connections#connecting-to-openai-compatible-llms)
- [Using Local Models with Ollama](https://docs.crewai.com/how-to/llm-connections#using-local-models-with-ollama)
- [Changing the Base API URL](https://docs.crewai.com/how-to/llm-connections#changing-the-base-api-url)
- [Conclusion](https://docs.crewai.com/how-to/llm-connections#conclusion)

# NL2SQL Tool - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

NL2SQL Tool

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/nl2sqltool\#nl2sqltool)  `NL2SQLTool`

## [​](https://docs.crewai.com/tools/nl2sqltool\#description)  Description

This tool is used to convert natural language to SQL queries. When passsed to the agent it will generate queries and then use them to interact with the database.

This enables multiple workflows like having an Agent to access the database fetch information based on the goal and then use the information to generate a response, report or any other output.
Along with that proivdes the ability for the Agent to update the database based on its goal.

**Attention**: Make sure that the Agent has access to a Read-Replica or that is okay for the Agent to run insert/update queries on the database.

## [​](https://docs.crewai.com/tools/nl2sqltool\#requirements)  Requirements

- SqlAlchemy
- Any DB compatible library (e.g. psycopg2, mysql-connector-python)

## [​](https://docs.crewai.com/tools/nl2sqltool\#installation)  Installation

Install the crewai\_tools package

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/nl2sqltool\#usage)  Usage

In order to use the NL2SQLTool, you need to pass the database URI to the tool. The URI should be in the format `dialect+driver://username:password@host:port/database`.

Code

Copy

```python
from crewai_tools import NL2SQLTool

# psycopg2 was installed to run this example with PostgreSQL
nl2sql = NL2SQLTool(db_uri="postgresql://example@localhost:5432/test_db")

@agent
def researcher(self) -> Agent:
    return Agent(
        config=self.agents_config["researcher"],
        allow_delegation=False,
        tools=[nl2sql]
    )

```

## [​](https://docs.crewai.com/tools/nl2sqltool\#example)  Example

The primary task goal was:

“Retrieve the average, maximum, and minimum monthly revenue for each city, but only include cities that have more than one user. Also, count the number of user in each city and
sort the results by the average monthly revenue in descending order”

So the Agent tried to get information from the DB, the first one is wrong so the Agent tries again and gets the correct information and passes to the next agent.

![alt text](https://github.com/crewAIInc/crewAI-tools/blob/main/crewai_tools/tools/nl2sql/images/image-2.png?raw=true)![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-3.png)

The second task goal was:

“Review the data and create a detailed report, and then create the table on the database with the fields based on the data provided.
Include information on the average, maximum, and minimum monthly revenue for each city, but only include cities that have more than one user. Also, count the number of users in each city and sort the results by the average monthly revenue in descending order.”

Now things start to get interesting, the Agent generates the SQL query to not only create the table but also insert the data into the table. And in the end the Agent still returns the final report which is exactly what was in the database.

![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-4.png)![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-5.png)

![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-9.png)![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-7.png)

This is a simple example of how the NL2SQLTool can be used to interact with the database and generate reports based on the data in the database.

The Tool provides endless possibilities on the logic of the Agent and how it can interact with the database.

Copy

```md
 DB -> Agent -> ... -> Agent -> DB

```

Was this page helpful?

YesNo

[MySQL RAG Search](https://docs.crewai.com/tools/mysqltool) [PDF RAG Search](https://docs.crewai.com/tools/pdfsearchtool)

On this page

- [NL2SQLTool](https://docs.crewai.com/tools/nl2sqltool#nl2sqltool)
- [Description](https://docs.crewai.com/tools/nl2sqltool#description)
- [Requirements](https://docs.crewai.com/tools/nl2sqltool#requirements)
- [Installation](https://docs.crewai.com/tools/nl2sqltool#installation)
- [Usage](https://docs.crewai.com/tools/nl2sqltool#usage)
- [Example](https://docs.crewai.com/tools/nl2sqltool#example)

![alt text](https://docs.crewai.com/tools/nl2sqltool)

![alt text](https://docs.crewai.com/tools/nl2sqltool)

![alt text](https://docs.crewai.com/tools/nl2sqltool)

![alt text](https://docs.crewai.com/tools/nl2sqltool)

![alt text](https://docs.crewai.com/tools/nl2sqltool)

![alt text](https://docs.crewai.com/tools/nl2sqltool)

# Create Custom Tools - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Create Custom Tools

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/how-to/create-custom-tools\#creating-and-utilizing-tools-in-crewai)  Creating and Utilizing Tools in CrewAI

This guide provides detailed instructions on creating custom tools for the CrewAI framework and how to efficiently manage and utilize these tools,
incorporating the latest functionalities such as tool delegation, error handling, and dynamic tool calling. It also highlights the importance of collaboration tools,
enabling agents to perform a wide range of actions.

### [​](https://docs.crewai.com/how-to/create-custom-tools\#subclassing-basetool)  Subclassing `BaseTool`

To create a personalized tool, inherit from `BaseTool` and define the necessary attributes, including the `args_schema` for input validation, and the `_run` method.

Code

Copy

```python
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class MyToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = "What this tool does. It's vital for effective utilization."
    args_schema: Type[BaseModel] = MyToolInput

    def _run(self, argument: str) -> str:
        # Your tool's logic here
        return "Tool's result"

```

### [​](https://docs.crewai.com/how-to/create-custom-tools\#using-the-tool-decorator)  Using the `tool` Decorator

Alternatively, you can use the tool decorator `@tool`. This approach allows you to define the tool’s attributes and functionality directly within a function,
offering a concise and efficient way to create specialized tools tailored to your needs.

Code

Copy

```python
from crewai.tools import tool

@tool("Tool Name")
def my_simple_tool(question: str) -> str:
    """Tool description for clarity."""
    # Tool logic here
    return "Tool output"

```

### [​](https://docs.crewai.com/how-to/create-custom-tools\#defining-a-cache-function-for-the-tool)  Defining a Cache Function for the Tool

To optimize tool performance with caching, define custom caching strategies using the `cache_function` attribute.

Code

Copy

```python
@tool("Tool with Caching")
def cached_tool(argument: str) -> str:
    """Tool functionality description."""
    return "Cacheable result"

def my_cache_strategy(arguments: dict, result: str) -> bool:
    # Define custom caching logic
    return True if some_condition else False

cached_tool.cache_function = my_cache_strategy

```

By adhering to these guidelines and incorporating new functionalities and collaboration tools into your tool creation and management processes,
you can leverage the full capabilities of the CrewAI framework, enhancing both the development experience and the efficiency of your AI agents.

Was this page helpful?

YesNo

[Using LlamaIndex Tools](https://docs.crewai.com/concepts/llamaindex-tools) [Sequential Processes](https://docs.crewai.com/how-to/sequential-process)

On this page

- [Creating and Utilizing Tools in CrewAI](https://docs.crewai.com/how-to/create-custom-tools#creating-and-utilizing-tools-in-crewai)
- [Subclassing BaseTool](https://docs.crewai.com/how-to/create-custom-tools#subclassing-basetool)
- [Using the tool Decorator](https://docs.crewai.com/how-to/create-custom-tools#using-the-tool-decorator)
- [Defining a Cache Function for the Tool](https://docs.crewai.com/how-to/create-custom-tools#defining-a-cache-function-for-the-tool)

# DALL-E Tool - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

DALL-E Tool

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/dalletool\#dalletool)  `DallETool`

## [​](https://docs.crewai.com/tools/dalletool\#description)  Description

This tool is used to give the Agent the ability to generate images using the DALL-E model. It is a transformer-based model that generates images from textual descriptions.
This tool allows the Agent to generate images based on the text input provided by the user.

## [​](https://docs.crewai.com/tools/dalletool\#installation)  Installation

Install the crewai\_tools package

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/dalletool\#example)  Example

Remember that when using this tool, the text must be generated by the Agent itself. The text must be a description of the image you want to generate.

Code

Copy

```python
from crewai_tools import DallETool

Agent(
    ...
    tools=[DallETool()],
)

```

If needed you can also tweak the parameters of the DALL-E model by passing them as arguments to the `DallETool` class. For example:

Code

Copy

```python
from crewai_tools import DallETool

dalle_tool = DallETool(model="dall-e-3",
                       size="1024x1024",
                       quality="standard",
                       n=1)

Agent(
    ...
    tools=[dalle_tool]
)

```

The parameters are based on the `client.images.generate` method from the OpenAI API. For more information on the parameters,
please refer to the [OpenAI API documentation](https://platform.openai.com/docs/guides/images/introduction?lang=python).

Was this page helpful?

YesNo

[CSV RAG Search](https://docs.crewai.com/tools/csvsearchtool) [Directory RAG Search](https://docs.crewai.com/tools/directorysearchtool)

On this page

- [DallETool](https://docs.crewai.com/tools/dalletool#dalletool)
- [Description](https://docs.crewai.com/tools/dalletool#description)
- [Installation](https://docs.crewai.com/tools/dalletool#installation)
- [Example](https://docs.crewai.com/tools/dalletool#example)

# TXT RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

TXT RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/txtsearchtool\#txtsearchtool)  `TXTSearchTool`

We are still working on improving tools, so there might be unexpected behavior or changes in the future.

## [​](https://docs.crewai.com/tools/txtsearchtool\#description)  Description

This tool is used to perform a RAG (Retrieval-Augmented Generation) search within the content of a text file.
It allows for semantic searching of a query within a specified text file’s content,
making it an invaluable resource for quickly extracting information or finding specific sections of text based on the query provided.

## [​](https://docs.crewai.com/tools/txtsearchtool\#installation)  Installation

To use the `TXTSearchTool`, you first need to install the `crewai_tools` package.
This can be done using pip, a package manager for Python.
Open your terminal or command prompt and enter the following command:

Copy

```shell
pip install 'crewai[tools]'

```

This command will download and install the TXTSearchTool along with any necessary dependencies.

## [​](https://docs.crewai.com/tools/txtsearchtool\#example)  Example

The following example demonstrates how to use the TXTSearchTool to search within a text file.
This example shows both the initialization of the tool with a specific text file and the subsequent search within that file’s content.

Code

Copy

```python
from crewai_tools import TXTSearchTool

# Initialize the tool to search within any text file's content
# the agent learns about during its execution
tool = TXTSearchTool()

# OR

# Initialize the tool with a specific text file,
# so the agent can search within the given text file's content
tool = TXTSearchTool(txt='path/to/text/file.txt')

```

## [​](https://docs.crewai.com/tools/txtsearchtool\#arguments)  Arguments

- `txt` (str): **Optional**. The path to the text file you want to search.
This argument is only required if the tool was not initialized with a specific text file;
otherwise, the search will be conducted within the initially provided text file.

## [​](https://docs.crewai.com/tools/txtsearchtool\#custom-model-and-embeddings)  Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization.
To customize the model, you can use a config dictionary as follows:

Code

Copy

```python
tool = TXTSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[Spider Scraper](https://docs.crewai.com/tools/spidertool) [Vision Tool](https://docs.crewai.com/tools/visiontool)

On this page

- [TXTSearchTool](https://docs.crewai.com/tools/txtsearchtool#txtsearchtool)
- [Description](https://docs.crewai.com/tools/txtsearchtool#description)
- [Installation](https://docs.crewai.com/tools/txtsearchtool#installation)
- [Example](https://docs.crewai.com/tools/txtsearchtool#example)
- [Arguments](https://docs.crewai.com/tools/txtsearchtool#arguments)
- [Custom model and embeddings](https://docs.crewai.com/tools/txtsearchtool#custom-model-and-embeddings)

# Selenium Scraper - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Selenium Scraper

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/seleniumscrapingtool\#seleniumscrapingtool)  `SeleniumScrapingTool`

This tool is currently in development. As we refine its capabilities, users may encounter unexpected behavior.
Your feedback is invaluable to us for making improvements.

## [​](https://docs.crewai.com/tools/seleniumscrapingtool\#description)  Description

The SeleniumScrapingTool is crafted for high-efficiency web scraping tasks.
It allows for precise extraction of content from web pages by using CSS selectors to target specific elements.
Its design caters to a wide range of scraping needs, offering flexibility to work with any provided website URL.

## [​](https://docs.crewai.com/tools/seleniumscrapingtool\#installation)  Installation

To get started with the SeleniumScrapingTool, install the crewai\_tools package using pip:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/seleniumscrapingtool\#usage-examples)  Usage Examples

Below are some scenarios where the SeleniumScrapingTool can be utilized:

Code

Copy

```python
from crewai_tools import SeleniumScrapingTool

# Example 1:
# Initialize the tool without any parameters to scrape
# the current page it navigates to
tool = SeleniumScrapingTool()

# Example 2:
# Scrape the entire webpage of a given URL
tool = SeleniumScrapingTool(website_url='https://example.com')

# Example 3:
# Target and scrape a specific CSS element from a webpage
tool = SeleniumScrapingTool(
    website_url='https://example.com',
    css_element='.main-content'
)

# Example 4:
# Perform scraping with additional parameters for a customized experience
tool = SeleniumScrapingTool(
    website_url='https://example.com',
    css_element='.main-content',
    cookie={'name': 'user', 'value': 'John Doe'},
    wait_time=10
)

```

## [​](https://docs.crewai.com/tools/seleniumscrapingtool\#arguments)  Arguments

The following parameters can be used to customize the SeleniumScrapingTool’s scraping process:

| Argument | Type | Description |
| --- | --- | --- |
| **website\_url** | `string` | **Mandatory**. Specifies the URL of the website from which content is to be scraped. |
| **css\_element** | `string` | **Mandatory**. The CSS selector for a specific element to target on the website, enabling focused scraping of a particular part of a webpage. |
| **cookie** | `object` | **Optional**. A dictionary containing cookie information, useful for simulating a logged-in session to access restricted content. |
| **wait\_time** | `int` | **Optional**. Specifies the delay (in seconds) before scraping, allowing the website and any dynamic content to fully load. |

Since the `SeleniumScrapingTool` is under active development, the parameters and functionality may evolve over time.
Users are encouraged to keep the tool updated and report any issues or suggestions for enhancements.

Was this page helpful?

YesNo

[Scrape Website](https://docs.crewai.com/tools/scrapewebsitetool) [Spider Scraper](https://docs.crewai.com/tools/spidertool)

On this page

- [SeleniumScrapingTool](https://docs.crewai.com/tools/seleniumscrapingtool#seleniumscrapingtool)
- [Description](https://docs.crewai.com/tools/seleniumscrapingtool#description)
- [Installation](https://docs.crewai.com/tools/seleniumscrapingtool#installation)
- [Usage Examples](https://docs.crewai.com/tools/seleniumscrapingtool#usage-examples)
- [Arguments](https://docs.crewai.com/tools/seleniumscrapingtool#arguments)

# Agent Monitoring with Langtrace - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Agent Monitoring with Langtrace

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/how-to/langtrace-observability\#langtrace-overview)  Langtrace Overview

Langtrace is an open-source, external tool that helps you set up observability and evaluations for Large Language Models (LLMs), LLM frameworks, and Vector Databases.
While not built directly into CrewAI, Langtrace can be used alongside CrewAI to gain deep visibility into the cost, latency, and performance of your CrewAI Agents.
This integration allows you to log hyperparameters, monitor performance regressions, and establish a process for continuous improvement of your Agents.

![Overview of a select series of agent session runs](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/langtrace1.png)![Overview of agent traces](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/langtrace2.png)![Overview of llm traces in details](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/langtrace3.png)

## [​](https://docs.crewai.com/how-to/langtrace-observability\#setup-instructions)  Setup Instructions

1

Sign up for Langtrace

Sign up by visiting [https://langtrace.ai/signup](https://langtrace.ai/signup).

2

Create a project

Set the project type to `CrewAI` and generate an API key.

3

Install Langtrace in your CrewAI project

Use the following command:

Copy

```bash
pip install langtrace-python-sdk

```

4

Import Langtrace

Import and initialize Langtrace at the beginning of your script, before any CrewAI imports:

Copy

```python
from langtrace_python_sdk import langtrace
langtrace.init(api_key='<LANGTRACE_API_KEY>')

# Now import CrewAI modules
from crewai import Agent, Task, Crew

```

### [​](https://docs.crewai.com/how-to/langtrace-observability\#features-and-their-application-to-crewai)  Features and Their Application to CrewAI

1. **LLM Token and Cost Tracking**
   - Monitor the token usage and associated costs for each CrewAI agent interaction.
2. **Trace Graph for Execution Steps**
   - Visualize the execution flow of your CrewAI tasks, including latency and logs.
   - Useful for identifying bottlenecks in your agent workflows.
3. **Dataset Curation with Manual Annotation**
   - Create datasets from your CrewAI task outputs for future training or evaluation.
4. **Prompt Versioning and Management**
   - Keep track of different versions of prompts used in your CrewAI agents.
   - Useful for A/B testing and optimizing agent performance.
5. **Prompt Playground with Model Comparisons**
   - Test and compare different prompts and models for your CrewAI agents before deployment.
6. **Testing and Evaluations**
   - Set up automated tests for your CrewAI agents and tasks.

Was this page helpful?

YesNo

[Agent Monitoring with AgentOps](https://docs.crewai.com/how-to/agentops-observability) [Agent Monitoring with MLflow](https://docs.crewai.com/how-to/mlflow-observability)

On this page

- [Langtrace Overview](https://docs.crewai.com/how-to/langtrace-observability#langtrace-overview)
- [Setup Instructions](https://docs.crewai.com/how-to/langtrace-observability#setup-instructions)
- [Features and Their Application to CrewAI](https://docs.crewai.com/how-to/langtrace-observability#features-and-their-application-to-crewai)

![Overview of a select series of agent session runs](https://docs.crewai.com/how-to/langtrace-observability)

![Overview of agent traces](https://docs.crewai.com/how-to/langtrace-observability)

![Overview of llm traces in details](https://docs.crewai.com/how-to/langtrace-observability)

# Conditional Tasks - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Conditional Tasks

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/how-to/conditional-tasks\#introduction)  Introduction

Conditional Tasks in crewAI allow for dynamic workflow adaptation based on the outcomes of previous tasks.
This powerful feature enables crews to make decisions and execute tasks selectively, enhancing the flexibility and efficiency of your AI-driven processes.

## [​](https://docs.crewai.com/how-to/conditional-tasks\#example-usage)  Example Usage

Code

Copy

```python
from typing import List
from pydantic import BaseModel
from crewai import Agent, Crew
from crewai.tasks.conditional_task import ConditionalTask
from crewai.tasks.task_output import TaskOutput
from crewai.task import Task
from crewai_tools import SerperDevTool

# Define a condition function for the conditional task
# If false, the task will be skipped, if true, then execute the task.
def is_data_missing(output: TaskOutput) -> bool:
    return len(output.pydantic.events) < 10  # this will skip this task

# Define the agents
data_fetcher_agent = Agent(
    role="Data Fetcher",
    goal="Fetch data online using Serper tool",
    backstory="Backstory 1",
    verbose=True,
    tools=[SerperDevTool()]
)

data_processor_agent = Agent(
    role="Data Processor",
    goal="Process fetched data",
    backstory="Backstory 2",
    verbose=True
)

summary_generator_agent = Agent(
    role="Summary Generator",
    goal="Generate summary from fetched data",
    backstory="Backstory 3",
    verbose=True
)

class EventOutput(BaseModel):
    events: List[str]

task1 = Task(
    description="Fetch data about events in San Francisco using Serper tool",
    expected_output="List of 10 things to do in SF this week",
    agent=data_fetcher_agent,
    output_pydantic=EventOutput,
)

conditional_task = ConditionalTask(
    description="""
        Check if data is missing. If we have less than 10 events,
        fetch more events using Serper tool so that
        we have a total of 10 events in SF this week..
        """,
    expected_output="List of 10 Things to do in SF this week",
    condition=is_data_missing,
    agent=data_processor_agent,
)

task3 = Task(
    description="Generate summary of events in San Francisco from fetched data",
    expected_output="A complete report on the customer and their customers and competitors, including their demographics, preferences, market positioning and audience engagement.",
    agent=summary_generator_agent,
)

# Create a crew with the tasks
crew = Crew(
    agents=[data_fetcher_agent, data_processor_agent, summary_generator_agent],
    tasks=[task1, conditional_task, task3],
    verbose=True,
    planning=True
)

# Run the crew
result = crew.kickoff()
print("results", result)

```

Was this page helpful?

YesNo

[Replay Tasks from Latest Crew Kickoff](https://docs.crewai.com/how-to/replay-tasks-from-latest-crew-kickoff) [Agent Monitoring with AgentOps](https://docs.crewai.com/how-to/agentops-observability)

On this page

- [Introduction](https://docs.crewai.com/how-to/conditional-tasks#introduction)
- [Example Usage](https://docs.crewai.com/how-to/conditional-tasks#example-usage)

# Introduction - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Get Started

Introduction

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/introduction\#what-is-crewai%3F)  What is CrewAI?

**CrewAI is a cutting-edge framework for orchestrating autonomous AI agents.**

CrewAI enables you to create AI teams where each agent has specific roles, tools, and goals, working together to accomplish complex tasks.

Think of it as assembling your dream team - each member (agent) brings unique skills and expertise, collaborating seamlessly to achieve your objectives.

## [​](https://docs.crewai.com/introduction\#how-crewai-works)  How CrewAI Works

Just like a company has departments (Sales, Engineering, Marketing) working together under leadership to achieve business goals, CrewAI helps you create an organization of AI agents with specialized roles collaborating to accomplish complex tasks.

![CrewAI Framework Overview](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crewAI-mindmap.png)

CrewAI Framework Overview

| Component | Description | Key Features |
| --- | --- | --- |
| **Crew** | The top-level organization | • Manages AI agent teams<br>• Oversees workflows<br>• Ensures collaboration<br>• Delivers outcomes |
| **AI Agents** | Specialized team members | • Have specific roles (researcher, writer)<br>• Use designated tools<br>• Can delegate tasks<br>• Make autonomous decisions |
| **Process** | Workflow management system | • Defines collaboration patterns<br>• Controls task assignments<br>• Manages interactions<br>• Ensures efficient execution |
| **Tasks** | Individual assignments | • Have clear objectives<br>• Use specific tools<br>• Feed into larger process<br>• Produce actionable results |

### [​](https://docs.crewai.com/introduction\#how-it-all-works-together)  How It All Works Together

1. The **Crew** organizes the overall operation
2. **AI Agents** work on their specialized tasks
3. The **Process** ensures smooth collaboration
4. **Tasks** get completed to achieve the goal

## [​](https://docs.crewai.com/introduction\#key-features)  Key Features

## Role-Based Agents

Create specialized agents with defined roles, expertise, and goals - from researchers to analysts to writers

## Flexible Tools

Equip agents with custom tools and APIs to interact with external services and data sources

## Intelligent Collaboration

Agents work together, sharing insights and coordinating tasks to achieve complex objectives

## Task Management

Define sequential or parallel workflows, with agents automatically handling task dependencies

## [​](https://docs.crewai.com/introduction\#why-choose-crewai%3F)  Why Choose CrewAI?

- 🧠 **Autonomous Operation**: Agents make intelligent decisions based on their roles and available tools
- 📝 **Natural Interaction**: Agents communicate and collaborate like human team members
- 🛠️ **Extensible Design**: Easy to add new tools, roles, and capabilities
- 🚀 **Production Ready**: Built for reliability and scalability in real-world applications

[**Install CrewAI** \\
\\
Get started with CrewAI in your development environment.](https://docs.crewai.com/installation) [**Quick Start** \\
\\
Follow our quickstart guide to create your first CrewAI agent and get hands-on experience.](https://docs.crewai.com/quickstart) [**Join the Community** \\
\\
Connect with other developers, get help, and share your CrewAI experiences.](https://community.crewai.com/)

Was this page helpful?

YesNo

[Installation](https://docs.crewai.com/installation)

On this page

- [What is CrewAI?](https://docs.crewai.com/introduction#what-is-crewai%3F)
- [How CrewAI Works](https://docs.crewai.com/introduction#how-crewai-works)
- [How It All Works Together](https://docs.crewai.com/introduction#how-it-all-works-together)
- [Key Features](https://docs.crewai.com/introduction#key-features)
- [Why Choose CrewAI?](https://docs.crewai.com/introduction#why-choose-crewai%3F)

![CrewAI Framework Overview](https://docs.crewai.com/introduction)

# LLMs - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

LLMs

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

CrewAI integrates with multiple LLM providers through LiteLLM, giving you the flexibility to choose the right model for your specific use case. This guide will help you understand how to configure and use different LLM providers in your CrewAI projects.

## [​](https://docs.crewai.com/concepts/llms\#what-are-llms%3F)  What are LLMs?

Large Language Models (LLMs) are the core intelligence behind CrewAI agents. They enable agents to understand context, make decisions, and generate human-like responses. Here’s what you need to know:

## LLM Basics

Large Language Models are AI systems trained on vast amounts of text data. They power the intelligence of your CrewAI agents, enabling them to understand and generate human-like text.

## Context Window

The context window determines how much text an LLM can process at once. Larger windows (e.g., 128K tokens) allow for more context but may be more expensive and slower.

## Temperature

Temperature (0.0 to 1.0) controls response randomness. Lower values (e.g., 0.2) produce more focused, deterministic outputs, while higher values (e.g., 0.8) increase creativity and variability.

## Provider Selection

Each LLM provider (e.g., OpenAI, Anthropic, Google) offers different models with varying capabilities, pricing, and features. Choose based on your needs for accuracy, speed, and cost.

## [​](https://docs.crewai.com/concepts/llms\#setting-up-your-llm)  Setting Up Your LLM

There are three ways to configure LLMs in CrewAI. Choose the method that best fits your workflow:

- 1\. Environment Variables
- 2\. YAML Configuration
- 3\. Direct Code

The simplest way to get started. Set these variables in your environment:

Copy

```bash
# Required: Your API key for authentication
OPENAI_API_KEY=<your-api-key>

# Optional: Default model selection
OPENAI_MODEL_NAME=gpt-4o-mini  # Default if not set

# Optional: Organization ID (if applicable)
OPENAI_ORGANIZATION_ID=<your-org-id>

```

Never commit API keys to version control. Use environment files (.env) or your system’s secret management.

## [​](https://docs.crewai.com/concepts/llms\#provider-configuration-examples)  Provider Configuration Examples

CrewAI supports a multitude of LLM providers, each offering unique features, authentication methods, and model capabilities.
In this section, you’ll find detailed examples that help you select, configure, and optimize the LLM that best fits your project’s needs.

OpenAI

Set the following environment variables in your `.env` file:

Code

Copy

```toml
# Required
OPENAI_API_KEY=sk-...

# Optional
OPENAI_API_BASE=<custom-base-url>
OPENAI_ORGANIZATION=<your-org-id>

```

Example usage in your CrewAI project:

Code

Copy

```python
from crewai import LLM

llm = LLM(
    model="openai/gpt-4", # call model by provider/model_name
    temperature=0.8,
    max_tokens=150,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    stop=["END"],
    seed=42
)

```

OpenAI is one of the leading providers of LLMs with a wide range of models and features.

| Model | Context Window | Best For |
| --- | --- | --- |
| GPT-4 | 8,192 tokens | High-accuracy tasks, complex reasoning |
| GPT-4 Turbo | 128,000 tokens | Long-form content, document analysis |
| GPT-4o & GPT-4o-mini | 128,000 tokens | Cost-effective large context processing |
| o3-mini | 200,000 tokens | Fast reasoning, complex reasoning |
| o1-mini | 128,000 tokens | Fast reasoning, complex reasoning |
| o1-preview | 128,000 tokens | Fast reasoning, complex reasoning |
| o1 | 200,000 tokens | Fast reasoning, complex reasoning |

Anthropic

Code

Copy

```toml
ANTHROPIC_API_KEY=sk-ant-...

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="anthropic/claude-3-sonnet-20240229-v1:0",
    temperature=0.7
)

```

Google

Set the following environment variables in your `.env` file:

Code

Copy

```toml
# Option 1: Gemini accessed with an API key.
# https://ai.google.dev/gemini-api/docs/api-key
GEMINI_API_KEY=<your-api-key>

# Option 2: Vertex AI IAM credentials for Gemini, Anthropic, and Model Garden.
# https://cloud.google.com/vertex-ai/generative-ai/docs/overview

```

Get credentials from your Google Cloud Console and save it to a JSON file with the following code:

Code

Copy

```python
import json

file_path = 'path/to/vertex_ai_service_account.json'

# Load the JSON file
with open(file_path, 'r') as file:
    vertex_credentials = json.load(file)

# Convert the credentials to a JSON string
vertex_credentials_json = json.dumps(vertex_credentials)

```

Example usage in your CrewAI project:

Code

Copy

```python
from crewai import LLM

llm = LLM(
    model="gemini/gemini-1.5-pro-latest",
    temperature=0.7,
    vertex_credentials=vertex_credentials_json
)

```

Google offers a range of powerful models optimized for different use cases:

| Model | Context Window | Best For |
| --- | --- | --- |
| gemini-2.0-flash-exp | 1M tokens | Higher quality at faster speed, multimodal model, good for most tasks |
| gemini-1.5-flash | 1M tokens | Balanced multimodal model, good for most tasks |
| gemini-1.5-flash-8B | 1M tokens | Fastest, most cost-efficient, good for high-frequency tasks |
| gemini-1.5-pro | 2M tokens | Best performing, wide variety of reasoning tasks including logical reasoning, coding, and creative collaboration |

Azure

Code

Copy

```toml
# Required
AZURE_API_KEY=<your-api-key>
AZURE_API_BASE=<your-resource-url>
AZURE_API_VERSION=<api-version>

# Optional
AZURE_AD_TOKEN=<your-azure-ad-token>
AZURE_API_TYPE=<your-azure-api-type>

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="azure/gpt-4",
    api_version="2023-05-15"
)

```

AWS Bedrock

Code

Copy

```toml
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
AWS_DEFAULT_REGION=<your-region>

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="bedrock/anthropic.claude-3-sonnet-20240229-v1:0"
)

```

Amazon SageMaker

Code

Copy

```toml
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
AWS_DEFAULT_REGION=<your-region>

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="sagemaker/<my-endpoint>"
)

```

Mistral

Set the following environment variables in your `.env` file:

Code

Copy

```toml
MISTRAL_API_KEY=<your-api-key>

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="mistral/mistral-large-latest",
    temperature=0.7
)

```

Nvidia NIM

Set the following environment variables in your `.env` file:

Code

Copy

```toml
NVIDIA_API_KEY=<your-api-key>

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="nvidia_nim/meta/llama3-70b-instruct",
    temperature=0.7
)

```

Nvidia NIM provides a comprehensive suite of models for various use cases, from general-purpose tasks to specialized applications.

| Model | Context Window | Best For |
| --- | --- | --- |
| nvidia/mistral-nemo-minitron-8b-8k-instruct | 8,192 tokens | State-of-the-art small language model delivering superior accuracy for chatbot, virtual assistants, and content generation. |
| nvidia/nemotron-4-mini-hindi-4b-instruct | 4,096 tokens | A bilingual Hindi-English SLM for on-device inference, tailored specifically for Hindi Language. |
| nvidia/llama-3.1-nemotron-70b-instruct | 128k tokens | Customized for enhanced helpfulness in responses |
| nvidia/llama3-chatqa-1.5-8b | 128k tokens | Advanced LLM to generate high-quality, context-aware responses for chatbots and search engines. |
| nvidia/llama3-chatqa-1.5-70b | 128k tokens | Advanced LLM to generate high-quality, context-aware responses for chatbots and search engines. |
| nvidia/vila | 128k tokens | Multi-modal vision-language model that understands text/img/video and creates informative responses |
| nvidia/neva-22 | 4,096 tokens | Multi-modal vision-language model that understands text/images and generates informative responses |
| nvidia/nemotron-mini-4b-instruct | 8,192 tokens | General-purpose tasks |
| nvidia/usdcode-llama3-70b-instruct | 128k tokens | State-of-the-art LLM that answers OpenUSD knowledge queries and generates USD-Python code. |
| nvidia/nemotron-4-340b-instruct | 4,096 tokens | Creates diverse synthetic data that mimics the characteristics of real-world data. |
| meta/codellama-70b | 100k tokens | LLM capable of generating code from natural language and vice versa. |
| meta/llama2-70b | 4,096 tokens | Cutting-edge large language AI model capable of generating text and code in response to prompts. |
| meta/llama3-8b-instruct | 8,192 tokens | Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation. |
| meta/llama3-70b-instruct | 8,192 tokens | Powers complex conversations with superior contextual understanding, reasoning and text generation. |
| meta/llama-3.1-8b-instruct | 128k tokens | Advanced state-of-the-art model with language understanding, superior reasoning, and text generation. |
| meta/llama-3.1-70b-instruct | 128k tokens | Powers complex conversations with superior contextual understanding, reasoning and text generation. |
| meta/llama-3.1-405b-instruct | 128k tokens | Advanced LLM for synthetic data generation, distillation, and inference for chatbots, coding, and domain-specific tasks. |
| meta/llama-3.2-1b-instruct | 128k tokens | Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation. |
| meta/llama-3.2-3b-instruct | 128k tokens | Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation. |
| meta/llama-3.2-11b-vision-instruct | 128k tokens | Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation. |
| meta/llama-3.2-90b-vision-instruct | 128k tokens | Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation. |
| google/gemma-7b | 8,192 tokens | Cutting-edge text generation model text understanding, transformation, and code generation. |
| google/gemma-2b | 8,192 tokens | Cutting-edge text generation model text understanding, transformation, and code generation. |
| google/codegemma-7b | 8,192 tokens | Cutting-edge model built on Google’s Gemma-7B specialized for code generation and code completion. |
| google/codegemma-1.1-7b | 8,192 tokens | Advanced programming model for code generation, completion, reasoning, and instruction following. |
| google/recurrentgemma-2b | 8,192 tokens | Novel recurrent architecture based language model for faster inference when generating long sequences. |
| google/gemma-2-9b-it | 8,192 tokens | Cutting-edge text generation model text understanding, transformation, and code generation. |
| google/gemma-2-27b-it | 8,192 tokens | Cutting-edge text generation model text understanding, transformation, and code generation. |
| google/gemma-2-2b-it | 8,192 tokens | Cutting-edge text generation model text understanding, transformation, and code generation. |
| google/deplot | 512 tokens | One-shot visual language understanding model that translates images of plots into tables. |
| google/paligemma | 8,192 tokens | Vision language model adept at comprehending text and visual inputs to produce informative responses. |
| mistralai/mistral-7b-instruct-v0.2 | 32k tokens | This LLM follows instructions, completes requests, and generates creative text. |
| mistralai/mixtral-8x7b-instruct-v0.1 | 8,192 tokens | An MOE LLM that follows instructions, completes requests, and generates creative text. |
| mistralai/mistral-large | 4,096 tokens | Creates diverse synthetic data that mimics the characteristics of real-world data. |
| mistralai/mixtral-8x22b-instruct-v0.1 | 8,192 tokens | Creates diverse synthetic data that mimics the characteristics of real-world data. |
| mistralai/mistral-7b-instruct-v0.3 | 32k tokens | This LLM follows instructions, completes requests, and generates creative text. |
| nv-mistralai/mistral-nemo-12b-instruct | 128k tokens | Most advanced language model for reasoning, code, multilingual tasks; runs on a single GPU. |
| mistralai/mamba-codestral-7b-v0.1 | 256k tokens | Model for writing and interacting with code across a wide range of programming languages and tasks. |
| microsoft/phi-3-mini-128k-instruct | 128K tokens | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills. |
| microsoft/phi-3-mini-4k-instruct | 4,096 tokens | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills. |
| microsoft/phi-3-small-8k-instruct | 8,192 tokens | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills. |
| microsoft/phi-3-small-128k-instruct | 128K tokens | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills. |
| microsoft/phi-3-medium-4k-instruct | 4,096 tokens | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills. |
| microsoft/phi-3-medium-128k-instruct | 128K tokens | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills. |
| microsoft/phi-3.5-mini-instruct | 128K tokens | Lightweight multilingual LLM powering AI applications in latency bound, memory/compute constrained environments |
| microsoft/phi-3.5-moe-instruct | 128K tokens | Advanced LLM based on Mixture of Experts architecure to deliver compute efficient content generation |
| microsoft/kosmos-2 | 1,024 tokens | Groundbreaking multimodal model designed to understand and reason about visual elements in images. |
| microsoft/phi-3-vision-128k-instruct | 128k tokens | Cutting-edge open multimodal model exceling in high-quality reasoning from images. |
| microsoft/phi-3.5-vision-instruct | 128k tokens | Cutting-edge open multimodal model exceling in high-quality reasoning from images. |
| databricks/dbrx-instruct | 12k tokens | A general-purpose LLM with state-of-the-art performance in language understanding, coding, and RAG. |
| snowflake/arctic | 1,024 tokens | Delivers high efficiency inference for enterprise applications focused on SQL generation and coding. |
| aisingapore/sea-lion-7b-instruct | 4,096 tokens | LLM to represent and serve the linguistic and cultural diversity of Southeast Asia |
| ibm/granite-8b-code-instruct | 4,096 tokens | Software programming LLM for code generation, completion, explanation, and multi-turn conversion. |
| ibm/granite-34b-code-instruct | 8,192 tokens | Software programming LLM for code generation, completion, explanation, and multi-turn conversion. |
| ibm/granite-3.0-8b-instruct | 4,096 tokens | Advanced Small Language Model supporting RAG, summarization, classification, code, and agentic AI |
| ibm/granite-3.0-3b-a800m-instruct | 4,096 tokens | Highly efficient Mixture of Experts model for RAG, summarization, entity extraction, and classification |
| mediatek/breeze-7b-instruct | 4,096 tokens | Creates diverse synthetic data that mimics the characteristics of real-world data. |
| upstage/solar-10.7b-instruct | 4,096 tokens | Excels in NLP tasks, particularly in instruction-following, reasoning, and mathematics. |
| writer/palmyra-med-70b-32k | 32k tokens | Leading LLM for accurate, contextually relevant responses in the medical domain. |
| writer/palmyra-med-70b | 32k tokens | Leading LLM for accurate, contextually relevant responses in the medical domain. |
| writer/palmyra-fin-70b-32k | 32k tokens | Specialized LLM for financial analysis, reporting, and data processing |
| 01-ai/yi-large | 32k tokens | Powerful model trained on English and Chinese for diverse tasks including chatbot and creative writing. |
| deepseek-ai/deepseek-coder-6.7b-instruct | 2k tokens | Powerful coding model offering advanced capabilities in code generation, completion, and infilling |
| rakuten/rakutenai-7b-instruct | 1,024 tokens | Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation. |
| rakuten/rakutenai-7b-chat | 1,024 tokens | Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation. |
| baichuan-inc/baichuan2-13b-chat | 4,096 tokens | Support Chinese and English chat, coding, math, instruction following, solving quizzes |

Groq

Set the following environment variables in your `.env` file:

Code

Copy

```toml
GROQ_API_KEY=<your-api-key>

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="groq/llama-3.2-90b-text-preview",
    temperature=0.7
)

```

| Model | Context Window | Best For |
| --- | --- | --- |
| Llama 3.1 70B/8B | 131,072 tokens | High-performance, large context tasks |
| Llama 3.2 Series | 8,192 tokens | General-purpose tasks |
| Mixtral 8x7B | 32,768 tokens | Balanced performance and context |

IBM watsonx.ai

Set the following environment variables in your `.env` file:

Code

Copy

```toml
# Required
WATSONX_URL=<your-url>
WATSONX_APIKEY=<your-apikey>
WATSONX_PROJECT_ID=<your-project-id>

# Optional
WATSONX_TOKEN=<your-token>
WATSONX_DEPLOYMENT_SPACE_ID=<your-space-id>

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="watsonx/meta-llama/llama-3-1-70b-instruct",
    base_url="https://api.watsonx.ai/v1"
)

```

Ollama (Local LLMs)

1. Install Ollama: [ollama.ai](https://ollama.ai/)
2. Run a model: `ollama run llama2`
3. Configure:

Code

Copy

```python
llm = LLM(
    model="ollama/llama3:70b",
    base_url="http://localhost:11434"
)

```

Fireworks AI

Set the following environment variables in your `.env` file:

Code

Copy

```toml
FIREWORKS_API_KEY=<your-api-key>

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="fireworks_ai/accounts/fireworks/models/llama-v3-70b-instruct",
    temperature=0.7
)

```

Perplexity AI

Set the following environment variables in your `.env` file:

Code

Copy

```toml
PERPLEXITY_API_KEY=<your-api-key>

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="llama-3.1-sonar-large-128k-online",
    base_url="https://api.perplexity.ai/"
)

```

Hugging Face

Set the following environment variables in your `.env` file:

Code

Copy

```toml
HUGGINGFACE_API_KEY=<your-api-key>

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="huggingface/meta-llama/Meta-Llama-3.1-8B-Instruct",
    base_url="your_api_endpoint"
)

```

SambaNova

Set the following environment variables in your `.env` file:

Code

Copy

```toml
SAMBANOVA_API_KEY=<your-api-key>

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="sambanova/Meta-Llama-3.1-8B-Instruct",
    temperature=0.7
)

```

| Model | Context Window | Best For |
| --- | --- | --- |
| Llama 3.1 70B/8B | Up to 131,072 tokens | High-performance, large context tasks |
| Llama 3.1 405B | 8,192 tokens | High-performance and output quality |
| Llama 3.2 Series | 8,192 tokens | General-purpose, multimodal tasks |
| Llama 3.3 70B | Up to 131,072 tokens | High-performance and output quality |
| Qwen2 familly | 8,192 tokens | High-performance and output quality |

Cerebras

Set the following environment variables in your `.env` file:

Code

Copy

```toml
# Required
CEREBRAS_API_KEY=<your-api-key>

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="cerebras/llama3.1-70b",
    temperature=0.7,
    max_tokens=8192
)

```

Cerebras features:

- Fast inference speeds
- Competitive pricing
- Good balance of speed and quality
- Support for long context windows

Open Router

Set the following environment variables in your `.env` file:

Code

Copy

```toml
OPENROUTER_API_KEY=<your-api-key>

```

Example usage in your CrewAI project:

Code

Copy

```python
llm = LLM(
    model="openrouter/deepseek/deepseek-r1",
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

```

Open Router models:

- openrouter/deepseek/deepseek-r1
- openrouter/deepseek/deepseek-chat

## [​](https://docs.crewai.com/concepts/llms\#structured-llm-calls)  Structured LLM Calls

CrewAI supports structured responses from LLM calls by allowing you to define a `response_format` using a Pydantic model. This enables the framework to automatically parse and validate the output, making it easier to integrate the response into your application without manual post-processing.

For example, you can define a Pydantic model to represent the expected response structure and pass it as the `response_format` when instantiating the LLM. The model will then be used to convert the LLM output into a structured Python object.

Code

Copy

```python
from crewai import LLM

class Dog(BaseModel):
    name: str
    age: int
    breed: str

llm = LLM(model="gpt-4o", response_format=Dog)

response = llm.call(
    "Analyze the following messages and return the name, age, and breed. "
    "Meet Kona! She is 3 years old and is a black german shepherd."
)
print(response)

# Output:
# Dog(name='Kona', age=3, breed='black german shepherd')

```

## [​](https://docs.crewai.com/concepts/llms\#advanced-features-and-optimization)  Advanced Features and Optimization

Learn how to get the most out of your LLM configuration:

Context Window Management

CrewAI includes smart context management features:

Copy

```python
from crewai import LLM

# CrewAI automatically handles:
# 1. Token counting and tracking
# 2. Content summarization when needed
# 3. Task splitting for large contexts

llm = LLM(
    model="gpt-4",
    max_tokens=4000,  # Limit response length
)

```

Best practices for context management:

1. Choose models with appropriate context windows
2. Pre-process long inputs when possible
3. Use chunking for large documents
4. Monitor token usage to optimize costs

Performance Optimization

1

Token Usage Optimization

Choose the right context window for your task:

- Small tasks (up to 4K tokens): Standard models
- Medium tasks (between 4K-32K): Enhanced models
- Large tasks (over 32K): Large context models

Copy

```python
# Configure model with appropriate settings
llm = LLM(
    model="openai/gpt-4-turbo-preview",
    temperature=0.7,    # Adjust based on task
    max_tokens=4096,    # Set based on output needs
    timeout=300        # Longer timeout for complex tasks
)

```

- Lower temperature (0.1 to 0.3) for factual responses
- Higher temperature (0.7 to 0.9) for creative tasks

2

Best Practices

1. Monitor token usage
2. Implement rate limiting
3. Use caching when possible
4. Set appropriate max\_tokens limits

Remember to regularly monitor your token usage and adjust your configuration as needed to optimize costs and performance.

## [​](https://docs.crewai.com/concepts/llms\#common-issues-and-solutions)  Common Issues and Solutions

- Authentication
- Model Names
- Context Length

Most authentication issues can be resolved by checking API key format and environment variable names.

Copy

```bash
# OpenAI
OPENAI_API_KEY=sk-...

# Anthropic
ANTHROPIC_API_KEY=sk-ant-...

```

## [​](https://docs.crewai.com/concepts/llms\#getting-help)  Getting Help

If you need assistance, these resources are available:

[**LiteLLM Documentation** \\
\\
Comprehensive documentation for LiteLLM integration and troubleshooting common issues.](https://docs.litellm.ai/docs/) [**GitHub Issues** \\
\\
Report bugs, request features, or browse existing issues for solutions.](https://github.com/joaomdmoura/crewAI/issues) [**Community Forum** \\
\\
Connect with other CrewAI users, share experiences, and get help from the community.](https://community.crewai.com/)

Best Practices for API Key Security:

- Use environment variables or secure vaults
- Never commit keys to version control
- Rotate keys regularly
- Use separate keys for development and production
- Monitor key usage for unusual patterns

Was this page helpful?

YesNo

[Knowledge](https://docs.crewai.com/concepts/knowledge) [Processes](https://docs.crewai.com/concepts/processes)

On this page

- [What are LLMs?](https://docs.crewai.com/concepts/llms#what-are-llms%3F)
- [Setting Up Your LLM](https://docs.crewai.com/concepts/llms#setting-up-your-llm)
- [Provider Configuration Examples](https://docs.crewai.com/concepts/llms#provider-configuration-examples)
- [Structured LLM Calls](https://docs.crewai.com/concepts/llms#structured-llm-calls)
- [Advanced Features and Optimization](https://docs.crewai.com/concepts/llms#advanced-features-and-optimization)
- [Common Issues and Solutions](https://docs.crewai.com/concepts/llms#common-issues-and-solutions)
- [Getting Help](https://docs.crewai.com/concepts/llms#getting-help)

# Agent Monitoring with AgentOps - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Agent Monitoring with AgentOps

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/how-to/agentops-observability\#introduction)  Introduction

Observability is a key aspect of developing and deploying conversational AI agents. It allows developers to understand how their agents are performing,
how their agents are interacting with users, and how their agents use external tools and APIs.
AgentOps is a product independent of CrewAI that provides a comprehensive observability solution for agents.

## [​](https://docs.crewai.com/how-to/agentops-observability\#agentops)  AgentOps

[AgentOps](https://agentops.ai/?=crew) provides session replays, metrics, and monitoring for agents.

At a high level, AgentOps gives you the ability to monitor cost, token usage, latency, agent failures, session-wide statistics, and more.
For more info, check out the [AgentOps Repo](https://github.com/AgentOps-AI/agentops).

### [​](https://docs.crewai.com/how-to/agentops-observability\#overview)  Overview

AgentOps provides monitoring for agents in development and production.
It provides a dashboard for tracking agent performance, session replays, and custom reporting.

Additionally, AgentOps provides session drilldowns for viewing Crew agent interactions, LLM calls, and tool usage in real-time.
This feature is useful for debugging and understanding how agents interact with users as well as other agents.

![Overview of a select series of agent session runs](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/agentops-overview.png)![Overview of session drilldowns for examining agent runs](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/agentops-session.png)![Viewing a step-by-step agent replay execution graph](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/agentops-replay.png)

### [​](https://docs.crewai.com/how-to/agentops-observability\#features)  Features

- **LLM Cost Management and Tracking**: Track spend with foundation model providers.
- **Replay Analytics**: Watch step-by-step agent execution graphs.
- **Recursive Thought Detection**: Identify when agents fall into infinite loops.
- **Custom Reporting**: Create custom analytics on agent performance.
- **Analytics Dashboard**: Monitor high-level statistics about agents in development and production.
- **Public Model Testing**: Test your agents against benchmarks and leaderboards.
- **Custom Tests**: Run your agents against domain-specific tests.
- **Time Travel Debugging**: Restart your sessions from checkpoints.
- **Compliance and Security**: Create audit logs and detect potential threats such as profanity and PII leaks.
- **Prompt Injection Detection**: Identify potential code injection and secret leaks.

### [​](https://docs.crewai.com/how-to/agentops-observability\#using-agentops)  Using AgentOps

1

Create an API Key

Create a user API key here: [Create API Key](https://app.agentops.ai/account)

2

Configure Your Environment

Add your API key to your environment variables:

Copy

```bash
AGENTOPS_API_KEY=<YOUR_AGENTOPS_API_KEY>

```

3

Install AgentOps

Install AgentOps with:

Copy

```bash
pip install 'crewai[agentops]'

```

or

Copy

```bash
pip install agentops

```

4

Initialize AgentOps

Before using `Crew` in your script, include these lines:

Copy

```python
import agentops
agentops.init()

```

This will initiate an AgentOps session as well as automatically track Crew agents. For further info on how to outfit more complex agentic systems,
check out the [AgentOps documentation](https://docs.agentops.ai/) or join the [Discord](https://discord.gg/j4f3KbeH).

### [​](https://docs.crewai.com/how-to/agentops-observability\#crew-%2B-agentops-examples)  Crew + AgentOps Examples

[**Job Posting** \\
\\
Example of a Crew agent that generates job posts.](https://github.com/joaomdmoura/crewAI-examples/tree/main/job-posting) [**Markdown Validator** \\
\\
Example of a Crew agent that validates Markdown files.](https://github.com/joaomdmoura/crewAI-examples/tree/main/markdown_validator) [**Instagram Post** \\
\\
Example of a Crew agent that generates Instagram posts.](https://github.com/joaomdmoura/crewAI-examples/tree/main/instagram_post)

### [​](https://docs.crewai.com/how-to/agentops-observability\#further-information)  Further Information

To get started, create an [AgentOps account](https://agentops.ai/?=crew).

For feature requests or bug reports, please reach out to the AgentOps team on the [AgentOps Repo](https://github.com/AgentOps-AI/agentops).

#### [​](https://docs.crewai.com/how-to/agentops-observability\#extra-links)  Extra links

[🐦 Twitter](https://twitter.com/agentopsai/)  •  [📢 Discord](https://discord.gg/JHPt4C7r)  •  [🖇️ AgentOps Dashboard](https://app.agentops.ai/?=crew)  •  [📙 Documentation](https://docs.agentops.ai/introduction)

Was this page helpful?

YesNo

[Conditional Tasks](https://docs.crewai.com/how-to/conditional-tasks) [Agent Monitoring with Langtrace](https://docs.crewai.com/how-to/langtrace-observability)

On this page

- [Introduction](https://docs.crewai.com/how-to/agentops-observability#introduction)
- [AgentOps](https://docs.crewai.com/how-to/agentops-observability#agentops)
- [Overview](https://docs.crewai.com/how-to/agentops-observability#overview)
- [Features](https://docs.crewai.com/how-to/agentops-observability#features)
- [Using AgentOps](https://docs.crewai.com/how-to/agentops-observability#using-agentops)
- [Crew + AgentOps Examples](https://docs.crewai.com/how-to/agentops-observability#crew-%2B-agentops-examples)
- [Further Information](https://docs.crewai.com/how-to/agentops-observability#further-information)
- [Extra links](https://docs.crewai.com/how-to/agentops-observability#extra-links)

![Overview of a select series of agent session runs](https://docs.crewai.com/how-to/agentops-observability)

![Overview of session drilldowns for examining agent runs](https://docs.crewai.com/how-to/agentops-observability)

![Viewing a step-by-step agent replay execution graph](https://docs.crewai.com/how-to/agentops-observability)

# Vision Tool - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Vision Tool

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/visiontool\#visiontool)  `VisionTool`

## [​](https://docs.crewai.com/tools/visiontool\#description)  Description

This tool is used to extract text from images. When passed to the agent it will extract the text from the image and then use it to generate a response, report or any other output.
The URL or the PATH of the image should be passed to the Agent.

## [​](https://docs.crewai.com/tools/visiontool\#installation)  Installation

Install the crewai\_tools package

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/visiontool\#usage)  Usage

In order to use the VisionTool, the OpenAI API key should be set in the environment variable `OPENAI_API_KEY`.

Code

Copy

```python
from crewai_tools import VisionTool

vision_tool = VisionTool()

@agent
def researcher(self) -> Agent:
    '''
    This agent uses the VisionTool to extract text from images.
    '''
    return Agent(
        config=self.agents_config["researcher"],
        allow_delegation=False,
        tools=[vision_tool]
    )

```

## [​](https://docs.crewai.com/tools/visiontool\#arguments)  Arguments

The VisionTool requires the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **image\_path\_url** | `string` | **Mandatory**. The path to the image file from which text needs to be extracted. |

Was this page helpful?

YesNo

[TXT RAG Search](https://docs.crewai.com/tools/txtsearchtool) [Website RAG Search](https://docs.crewai.com/tools/websitesearchtool)

On this page

- [VisionTool](https://docs.crewai.com/tools/visiontool#visiontool)
- [Description](https://docs.crewai.com/tools/visiontool#description)
- [Installation](https://docs.crewai.com/tools/visiontool#installation)
- [Usage](https://docs.crewai.com/tools/visiontool#usage)
- [Arguments](https://docs.crewai.com/tools/visiontool#arguments)

# Agent Monitoring with OpenLIT - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Agent Monitoring with OpenLIT

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/how-to/openlit-observability\#openlit-overview)  OpenLIT Overview

[OpenLIT](https://github.com/openlit/openlit?src=crewai-docs) is an open-source tool that makes it simple to monitor the performance of AI agents, LLMs, VectorDBs, and GPUs with just **one** line of code.

It provides OpenTelemetry-native tracing and metrics to track important parameters like cost, latency, interactions and task sequences.
This setup enables you to track hyperparameters and monitor for performance issues, helping you find ways to enhance and fine-tune your agents over time.

![Overview Agent usage including cost and tokens](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/openlit1.png)![Overview of agent otel traces and metrics](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/openlit2.png)![Overview of agent traces in details](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/openlit3.png)

OpenLIT Dashboard

### [​](https://docs.crewai.com/how-to/openlit-observability\#features)  Features

- **Analytics Dashboard**: Monitor your Agents health and performance with detailed dashboards that track metrics, costs, and user interactions.
- **OpenTelemetry-native Observability SDK**: Vendor-neutral SDKs to send traces and metrics to your existing observability tools like Grafana, DataDog and more.
- **Cost Tracking for Custom and Fine-Tuned Models**: Tailor cost estimations for specific models using custom pricing files for precise budgeting.
- **Exceptions Monitoring Dashboard**: Quickly spot and resolve issues by tracking common exceptions and errors with a monitoring dashboard.
- **Compliance and Security**: Detect potential threats such as profanity and PII leaks.
- **Prompt Injection Detection**: Identify potential code injection and secret leaks.
- **API Keys and Secrets Management**: Securely handle your LLM API keys and secrets centrally, avoiding insecure practices.
- **Prompt Management**: Manage and version Agent prompts using PromptHub for consistent and easy access across Agents.
- **Model Playground** Test and compare different models for your CrewAI agents before deployment.

## [​](https://docs.crewai.com/how-to/openlit-observability\#setup-instructions)  Setup Instructions

1

Deploy OpenLIT

1

Git Clone OpenLIT Repository

Copy

```shell
git clone git@github.com:openlit/openlit.git

```

2

Start Docker Compose

From the root directory of the [OpenLIT Repo](https://github.com/openlit/openlit), Run the below command:

Copy

```shell
docker compose up -d

```

2

Install OpenLIT SDK

Copy

```shell
pip install openlit

```

3

Initialize OpenLIT in Your Application

Add the following two lines to your application code:

- Setup using function arguments
- Setup using Environment Variables

Copy

```python
import openlit
openlit.init(otlp_endpoint="http://127.0.0.1:4318")

```

Example Usage for monitoring a CrewAI Agent:

Copy

```python
from crewai import Agent, Task, Crew, Process
import openlit

openlit.init(disable_metrics=True)
# Define your agents
researcher = Agent(
    role="Researcher",
    goal="Conduct thorough research and analysis on AI and AI agents",
    backstory="You're an expert researcher, specialized in technology, software engineering, AI, and startups. You work as a freelancer and are currently researching for a new client.",
    allow_delegation=False,
    llm='command-r'
)

# Define your task
task = Task(
    description="Generate a list of 5 interesting ideas for an article, then write one captivating paragraph for each idea that showcases the potential of a full article on this topic. Return the list of ideas with their paragraphs and your notes.",
    expected_output="5 bullet points, each with a paragraph and accompanying notes.",
)

# Define the manager agent
manager = Agent(
    role="Project Manager",
    goal="Efficiently manage the crew and ensure high-quality task completion",
    backstory="You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
    allow_delegation=True,
    llm='command-r'
)

# Instantiate your crew with a custom manager
crew = Crew(
    agents=[researcher],
    tasks=[task],
    manager_agent=manager,
    process=Process.hierarchical,
)

# Start the crew's work
result = crew.kickoff()

print(result)

```

Refer to OpenLIT [Python SDK repository](https://github.com/openlit/openlit/tree/main/sdk/python) for more advanced configurations and use cases.

4

Visualize and Analyze

With the Agent Observability data now being collected and sent to OpenLIT, the next step is to visualize and analyze this data to get insights into your Agent’s performance, behavior, and identify areas of improvement.

Just head over to OpenLIT at `127.0.0.1:3000` on your browser to start exploring. You can login using the default credentials

- **Email**: `user@openlit.io`
- **Password**: `openlituser`

![Overview Agent usage including cost and tokens](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/openlit1.png)![Overview of agent otel traces and metrics](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/openlit2.png)

OpenLIT Dashboard

Was this page helpful?

YesNo

[Agent Monitoring with MLflow](https://docs.crewai.com/how-to/mlflow-observability) [Agent Monitoring with Portkey](https://docs.crewai.com/how-to/portkey-observability)

On this page

- [OpenLIT Overview](https://docs.crewai.com/how-to/openlit-observability#openlit-overview)
- [Features](https://docs.crewai.com/how-to/openlit-observability#features)
- [Setup Instructions](https://docs.crewai.com/how-to/openlit-observability#setup-instructions)

![Overview Agent usage including cost and tokens](https://docs.crewai.com/how-to/openlit-observability)

![Overview of agent otel traces and metrics](https://docs.crewai.com/how-to/openlit-observability)

![Overview of agent traces in details](https://docs.crewai.com/how-to/openlit-observability)

![Overview Agent usage including cost and tokens](https://docs.crewai.com/how-to/openlit-observability)

![Overview of agent otel traces and metrics](https://docs.crewai.com/how-to/openlit-observability)

# Using LangChain Tools - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Using LangChain Tools

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/langchain-tools\#using-langchain-tools)  Using LangChain Tools

CrewAI seamlessly integrates with LangChain’s comprehensive [list of tools](https://python.langchain.com/docs/integrations/tools/), all of which can be used with CrewAI.

Code

Copy

```python
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai.tools import BaseTool
from pydantic import Field
from langchain_community.utilities import GoogleSerperAPIWrapper

# Set up your SERPER_API_KEY key in an .env file, eg:
# SERPER_API_KEY=<your api key>
load_dotenv()

search = GoogleSerperAPIWrapper()

class SearchTool(BaseTool):
    name: str = "Search"
    description: str = "Useful for search-based queries. Use this to find current information about markets, companies, and trends."
    search: GoogleSerperAPIWrapper = Field(default_factory=GoogleSerperAPIWrapper)

    def _run(self, query: str) -> str:
        """Execute the search query and return results"""
        try:
            return self.search.run(query)
        except Exception as e:
            return f"Error performing search: {str(e)}"

# Create Agents
researcher = Agent(
    role='Research Analyst',
    goal='Gather current market data and trends',
    backstory="""You are an expert research analyst with years of experience in
    gathering market intelligence. You're known for your ability to find
    relevant and up-to-date market information and present it in a clear,
    actionable format.""",
    tools=[SearchTool()],
    verbose=True
)

# rest of the code ...

```

## [​](https://docs.crewai.com/concepts/langchain-tools\#conclusion)  Conclusion

Tools are pivotal in extending the capabilities of CrewAI agents, enabling them to undertake a broad spectrum of tasks and collaborate effectively.
When building solutions with CrewAI, leverage both custom and existing tools to empower your agents and enhance the AI ecosystem. Consider utilizing error handling, caching mechanisms,
and the flexibility of tool arguments to optimize your agents’ performance and capabilities.

Was this page helpful?

YesNo

[Tools](https://docs.crewai.com/concepts/tools) [Using LlamaIndex Tools](https://docs.crewai.com/concepts/llamaindex-tools)

On this page

- [Using LangChain Tools](https://docs.crewai.com/concepts/langchain-tools#using-langchain-tools)
- [Conclusion](https://docs.crewai.com/concepts/langchain-tools#conclusion)

# Firecrawl Scrape Website - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Firecrawl Scrape Website

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/firecrawlscrapewebsitetool\#firecrawlscrapewebsitetool)  `FirecrawlScrapeWebsiteTool`

## [​](https://docs.crewai.com/tools/firecrawlscrapewebsitetool\#description)  Description

[Firecrawl](https://firecrawl.dev/) is a platform for crawling and convert any website into clean markdown or structured data.

## [​](https://docs.crewai.com/tools/firecrawlscrapewebsitetool\#installation)  Installation

- Get an API key from [firecrawl.dev](https://firecrawl.dev/) and set it in environment variables ( `FIRECRAWL_API_KEY`).
- Install the [Firecrawl SDK](https://github.com/mendableai/firecrawl) along with `crewai[tools]` package:

Copy

```shell
pip install firecrawl-py 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/firecrawlscrapewebsitetool\#example)  Example

Utilize the FirecrawlScrapeWebsiteTool as follows to allow your agent to load websites:

Code

Copy

```python
from crewai_tools import FirecrawlScrapeWebsiteTool

tool = FirecrawlScrapeWebsiteTool(url='firecrawl.dev')

```

## [​](https://docs.crewai.com/tools/firecrawlscrapewebsitetool\#arguments)  Arguments

- `api_key`: Optional. Specifies Firecrawl API key. Defaults is the `FIRECRAWL_API_KEY` environment variable.
- `url`: The URL to scrape.
- `page_options`: Optional.

  - `onlyMainContent`: Optional. Only return the main content of the page excluding headers, navs, footers, etc.
  - `includeHtml`: Optional. Include the raw HTML content of the page. Will output a html key in the response.
- `extractor_options`: Optional. Options for LLM-based extraction of structured information from the page content

  - `mode`: The extraction mode to use, currently supports ‘llm-extraction’
  - `extractionPrompt`: Optional. A prompt describing what information to extract from the page
  - `extractionSchema`: Optional. The schema for the data to be extracted
- `timeout`: Optional. Timeout in milliseconds for the request

Was this page helpful?

YesNo

[Firecrawl Crawl Website](https://docs.crewai.com/tools/firecrawlcrawlwebsitetool) [Firecrawl Search](https://docs.crewai.com/tools/firecrawlsearchtool)

On this page

- [FirecrawlScrapeWebsiteTool](https://docs.crewai.com/tools/firecrawlscrapewebsitetool#firecrawlscrapewebsitetool)
- [Description](https://docs.crewai.com/tools/firecrawlscrapewebsitetool#description)
- [Installation](https://docs.crewai.com/tools/firecrawlscrapewebsitetool#installation)
- [Example](https://docs.crewai.com/tools/firecrawlscrapewebsitetool#example)
- [Arguments](https://docs.crewai.com/tools/firecrawlscrapewebsitetool#arguments)

# JSON RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

JSON RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/jsonsearchtool\#jsonsearchtool)  `JSONSearchTool`

The JSONSearchTool is currently in an experimental phase. This means the tool is under active development, and users might encounter unexpected behavior or changes.
We highly encourage feedback on any issues or suggestions for improvements.

## [​](https://docs.crewai.com/tools/jsonsearchtool\#description)  Description

The JSONSearchTool is designed to facilitate efficient and precise searches within JSON file contents. It utilizes a RAG (Retrieve and Generate) search mechanism, allowing users to specify a JSON path for targeted searches within a particular JSON file. This capability significantly improves the accuracy and relevance of search results.

## [​](https://docs.crewai.com/tools/jsonsearchtool\#installation)  Installation

To install the JSONSearchTool, use the following pip command:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/jsonsearchtool\#usage-examples)  Usage Examples

Here are updated examples on how to utilize the JSONSearchTool effectively for searching within JSON files. These examples take into account the current implementation and usage patterns identified in the codebase.

Code

Copy

```python
from crewai.json_tools import JSONSearchTool  # Updated import path

# General JSON content search
# This approach is suitable when the JSON path is either known beforehand or can be dynamically identified.
tool = JSONSearchTool()

# Restricting search to a specific JSON file
# Use this initialization method when you want to limit the search scope to a specific JSON file.
tool = JSONSearchTool(json_path='./path/to/your/file.json')

```

## [​](https://docs.crewai.com/tools/jsonsearchtool\#arguments)  Arguments

- `json_path` (str, optional): Specifies the path to the JSON file to be searched. This argument is not required if the tool is initialized for a general search. When provided, it confines the search to the specified JSON file.

## [​](https://docs.crewai.com/tools/jsonsearchtool\#configuration-options)  Configuration Options

The JSONSearchTool supports extensive customization through a configuration dictionary. This allows users to select different models for embeddings and summarization based on their requirements.

Code

Copy

```python
tool = JSONSearchTool(
    config={
        "llm": {
            "provider": "ollama",  # Other options include google, openai, anthropic, llama2, etc.
            "config": {
                "model": "llama2",
                # Additional optional configurations can be specified here.
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            },
        },
        "embedder": {
            "provider": "google", # or openai, ollama, ...
            "config": {
                "model": "models/embedding-001",
                "task_type": "retrieval_document",
                # Further customization options can be added here.
            },
        },
    }
)

```

Was this page helpful?

YesNo

[Google Serper Search](https://docs.crewai.com/tools/serperdevtool) [MDX RAG Search](https://docs.crewai.com/tools/mdxsearchtool)

On this page

- [JSONSearchTool](https://docs.crewai.com/tools/jsonsearchtool#jsonsearchtool)
- [Description](https://docs.crewai.com/tools/jsonsearchtool#description)
- [Installation](https://docs.crewai.com/tools/jsonsearchtool#installation)
- [Usage Examples](https://docs.crewai.com/tools/jsonsearchtool#usage-examples)
- [Arguments](https://docs.crewai.com/tools/jsonsearchtool#arguments)
- [Configuration Options](https://docs.crewai.com/tools/jsonsearchtool#configuration-options)

# PDF RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

PDF RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/pdfsearchtool\#pdfsearchtool)  `PDFSearchTool`

We are still working on improving tools, so there might be unexpected behavior or changes in the future.

## [​](https://docs.crewai.com/tools/pdfsearchtool\#description)  Description

The PDFSearchTool is a RAG tool designed for semantic searches within PDF content. It allows for inputting a search query and a PDF document, leveraging advanced search techniques to find relevant content efficiently.
This capability makes it especially useful for extracting specific information from large PDF files quickly.

## [​](https://docs.crewai.com/tools/pdfsearchtool\#installation)  Installation

To get started with the PDFSearchTool, first, ensure the crewai\_tools package is installed with the following command:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/pdfsearchtool\#example)  Example

Here’s how to use the PDFSearchTool to search within a PDF document:

Code

Copy

```python
from crewai_tools import PDFSearchTool

# Initialize the tool allowing for any PDF content search if the path is provided during execution
tool = PDFSearchTool()

# OR

# Initialize the tool with a specific PDF path for exclusive search within that document
tool = PDFSearchTool(pdf='path/to/your/document.pdf')

```

## [​](https://docs.crewai.com/tools/pdfsearchtool\#arguments)  Arguments

- `pdf`: **Optional** The PDF path for the search. Can be provided at initialization or within the `run` method’s arguments. If provided at initialization, the tool confines its search to the specified document.

## [​](https://docs.crewai.com/tools/pdfsearchtool\#custom-model-and-embeddings)  Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

Code

Copy

```python
tool = PDFSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[NL2SQL Tool](https://docs.crewai.com/tools/nl2sqltool) [PG RAG Search](https://docs.crewai.com/tools/pgsearchtool)

On this page

- [PDFSearchTool](https://docs.crewai.com/tools/pdfsearchtool#pdfsearchtool)
- [Description](https://docs.crewai.com/tools/pdfsearchtool#description)
- [Installation](https://docs.crewai.com/tools/pdfsearchtool#installation)
- [Example](https://docs.crewai.com/tools/pdfsearchtool#example)
- [Arguments](https://docs.crewai.com/tools/pdfsearchtool#arguments)
- [Custom model and embeddings](https://docs.crewai.com/tools/pdfsearchtool#custom-model-and-embeddings)

# Firecrawl Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Firecrawl Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/firecrawlsearchtool\#firecrawlsearchtool)  `FirecrawlSearchTool`

## [​](https://docs.crewai.com/tools/firecrawlsearchtool\#description)  Description

[Firecrawl](https://firecrawl.dev/) is a platform for crawling and convert any website into clean markdown or structured data.

## [​](https://docs.crewai.com/tools/firecrawlsearchtool\#installation)  Installation

- Get an API key from [firecrawl.dev](https://firecrawl.dev/) and set it in environment variables ( `FIRECRAWL_API_KEY`).
- Install the [Firecrawl SDK](https://github.com/mendableai/firecrawl) along with `crewai[tools]` package:

Copy

```shell
pip install firecrawl-py 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/firecrawlsearchtool\#example)  Example

Utilize the FirecrawlSearchTool as follows to allow your agent to load websites:

Code

Copy

```python
from crewai_tools import FirecrawlSearchTool

tool = FirecrawlSearchTool(query='what is firecrawl?')

```

## [​](https://docs.crewai.com/tools/firecrawlsearchtool\#arguments)  Arguments

- `api_key`: Optional. Specifies Firecrawl API key. Defaults is the `FIRECRAWL_API_KEY` environment variable.
- `query`: The search query string to be used for searching.
- `page_options`: Optional. Options for result formatting.

  - `onlyMainContent`: Optional. Only return the main content of the page excluding headers, navs, footers, etc.
  - `includeHtml`: Optional. Include the raw HTML content of the page. Will output a html key in the response.
  - `fetchPageContent`: Optional. Fetch the full content of the page.
- `search_options`: Optional. Options for controlling the crawling behavior.

  - `limit`: Optional. Maximum number of pages to crawl.

Was this page helpful?

YesNo

[Firecrawl Scrape Website](https://docs.crewai.com/tools/firecrawlscrapewebsitetool) [Github Search](https://docs.crewai.com/tools/githubsearchtool)

On this page

- [FirecrawlSearchTool](https://docs.crewai.com/tools/firecrawlsearchtool#firecrawlsearchtool)
- [Description](https://docs.crewai.com/tools/firecrawlsearchtool#description)
- [Installation](https://docs.crewai.com/tools/firecrawlsearchtool#installation)
- [Example](https://docs.crewai.com/tools/firecrawlsearchtool#example)
- [Arguments](https://docs.crewai.com/tools/firecrawlsearchtool#arguments)

# YouTube Channel RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

YouTube Channel RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/youtubechannelsearchtool\#youtubechannelsearchtool)  `YoutubeChannelSearchTool`

We are still working on improving tools, so there might be unexpected behavior or changes in the future.

## [​](https://docs.crewai.com/tools/youtubechannelsearchtool\#description)  Description

This tool is designed to perform semantic searches within a specific Youtube channel’s content.
Leveraging the RAG (Retrieval-Augmented Generation) methodology, it provides relevant search results,
making it invaluable for extracting information or finding specific content without the need to manually sift through videos.
It streamlines the search process within Youtube channels, catering to researchers, content creators, and viewers seeking specific information or topics.

## [​](https://docs.crewai.com/tools/youtubechannelsearchtool\#installation)  Installation

To utilize the YoutubeChannelSearchTool, the `crewai_tools` package must be installed. Execute the following command in your shell to install:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/youtubechannelsearchtool\#example)  Example

To begin using the YoutubeChannelSearchTool, follow the example below.
This demonstrates initializing the tool with a specific Youtube channel handle and conducting a search within that channel’s content.

Code

Copy

```python
from crewai_tools import YoutubeChannelSearchTool

# Initialize the tool to search within any Youtube channel's content the agent learns about during its execution
tool = YoutubeChannelSearchTool()

# OR

# Initialize the tool with a specific Youtube channel handle to target your search
tool = YoutubeChannelSearchTool(youtube_channel_handle='@exampleChannel')

```

## [​](https://docs.crewai.com/tools/youtubechannelsearchtool\#arguments)  Arguments

- `youtube_channel_handle` : A mandatory string representing the Youtube channel handle. This parameter is crucial for initializing the tool to specify the channel you want to search within. The tool is designed to only search within the content of the provided channel handle.

## [​](https://docs.crewai.com/tools/youtubechannelsearchtool\#custom-model-and-embeddings)  Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

Code

Copy

```python
tool = YoutubeChannelSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[XML RAG Search](https://docs.crewai.com/tools/xmlsearchtool) [YouTube Video RAG Search](https://docs.crewai.com/tools/youtubevideosearchtool)

On this page

- [YoutubeChannelSearchTool](https://docs.crewai.com/tools/youtubechannelsearchtool#youtubechannelsearchtool)
- [Description](https://docs.crewai.com/tools/youtubechannelsearchtool#description)
- [Installation](https://docs.crewai.com/tools/youtubechannelsearchtool#installation)
- [Example](https://docs.crewai.com/tools/youtubechannelsearchtool#example)
- [Arguments](https://docs.crewai.com/tools/youtubechannelsearchtool#arguments)
- [Custom model and embeddings](https://docs.crewai.com/tools/youtubechannelsearchtool#custom-model-and-embeddings)

# Crews - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Crews

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/crews\#what-is-a-crew%3F)  What is a Crew?

A crew in crewAI represents a collaborative group of agents working together to achieve a set of tasks. Each crew defines the strategy for task execution, agent collaboration, and the overall workflow.

## [​](https://docs.crewai.com/concepts/crews\#crew-attributes)  Crew Attributes

| Attribute | Parameters | Description |
| --- | --- | --- |
| **Tasks** | `tasks` | A list of tasks assigned to the crew. |
| **Agents** | `agents` | A list of agents that are part of the crew. |
| **Process** _(optional)_ | `process` | The process flow (e.g., sequential, hierarchical) the crew follows. Default is `sequential`. |
| **Verbose** _(optional)_ | `verbose` | The verbosity level for logging during execution. Defaults to `False`. |
| **Manager LLM** _(optional)_ | `manager_llm` | The language model used by the manager agent in a hierarchical process. **Required when using a hierarchical process.** |
| **Function Calling LLM** _(optional)_ | `function_calling_llm` | If passed, the crew will use this LLM to do function calling for tools for all agents in the crew. Each agent can have its own LLM, which overrides the crew’s LLM for function calling. |
| **Config** _(optional)_ | `config` | Optional configuration settings for the crew, in `Json` or `Dict[str, Any]` format. |
| **Max RPM** _(optional)_ | `max_rpm` | Maximum requests per minute the crew adheres to during execution. Defaults to `None`. |
| **Language** _(optional)_ | `language` | Language used for the crew, defaults to English. |
| **Language File** _(optional)_ | `language_file` | Path to the language file to be used for the crew. |
| **Memory** _(optional)_ | `memory` | Utilized for storing execution memories (short-term, long-term, entity memory). |
| **Memory Config** _(optional)_ | `memory_config` | Configuration for the memory provider to be used by the crew. |
| **Cache** _(optional)_ | `cache` | Specifies whether to use a cache for storing the results of tools’ execution. Defaults to `True`. |
| **Embedder** _(optional)_ | `embedder` | Configuration for the embedder to be used by the crew. Mostly used by memory for now. Default is `{"provider": "openai"}`. |
| **Full Output** _(optional)_ | `full_output` | Whether the crew should return the full output with all tasks outputs or just the final output. Defaults to `False`. |
| **Step Callback** _(optional)_ | `step_callback` | A function that is called after each step of every agent. This can be used to log the agent’s actions or to perform other operations; it won’t override the agent-specific `step_callback`. |
| **Task Callback** _(optional)_ | `task_callback` | A function that is called after the completion of each task. Useful for monitoring or additional operations post-task execution. |
| **Share Crew** _(optional)_ | `share_crew` | Whether you want to share the complete crew information and execution with the crewAI team to make the library better, and allow us to train models. |
| **Output Log File** _(optional)_ | `output_log_file` | Set to True to save logs as logs.txt in the current directory or provide a file path. Logs will be in JSON format if the filename ends in .json, otherwise .txt. Defautls to `None`. |
| **Manager Agent** _(optional)_ | `manager_agent` | `manager` sets a custom agent that will be used as a manager. |
| **Prompt File** _(optional)_ | `prompt_file` | Path to the prompt JSON file to be used for the crew. |
| **Planning** _(optional)_ | `planning` | Adds planning ability to the Crew. When activated before each Crew iteration, all Crew data is sent to an AgentPlanner that will plan the tasks and this plan will be added to each task description. |
| **Planning LLM** _(optional)_ | `planning_llm` | The language model used by the AgentPlanner in a planning process. |

**Crew Max RPM**: The `max_rpm` attribute sets the maximum number of requests per minute the crew can perform to avoid rate limits and will override individual agents’ `max_rpm` settings if you set it.

## [​](https://docs.crewai.com/concepts/crews\#creating-crews)  Creating Crews

There are two ways to create crews in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.

### [​](https://docs.crewai.com/concepts/crews\#yaml-configuration-recommended)  YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define crews and is consistent with how agents and tasks are defined in CrewAI projects.

After creating your CrewAI project as outlined in the [Installation](https://docs.crewai.com/installation) section, you can define your crew in a class that inherits from `CrewBase` and uses decorators to define agents, tasks, and the crew itself.

#### [​](https://docs.crewai.com/concepts/crews\#example-crew-class-with-decorators)  Example Crew Class with Decorators

code

Copy

```python
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, task, crew, before_kickoff, after_kickoff

@CrewBase
class YourCrewName:
    """Description of your crew"""

    # Paths to your YAML configuration files
    # To see an example agent and task defined in YAML, checkout the following:
    # - Task: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    # - Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @before_kickoff
    def prepare_inputs(self, inputs):
        # Modify inputs before the crew starts
        inputs['additional_data'] = "Some extra information"
        return inputs

    @after_kickoff
    def process_output(self, output):
        # Modify output after the crew finishes
        output.raw += "\nProcessed after kickoff."
        return output

    @agent
    def agent_one(self) -> Agent:
        return Agent(
            config=self.agents_config['agent_one'],
            verbose=True
        )

    @agent
    def agent_two(self) -> Agent:
        return Agent(
            config=self.agents_config['agent_two'],
            verbose=True
        )

    @task
    def task_one(self) -> Task:
        return Task(
            config=self.tasks_config['task_one']
        )

    @task
    def task_two(self) -> Task:
        return Task(
            config=self.tasks_config['task_two']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # Automatically collected by the @agent decorator
            tasks=self.tasks,    # Automatically collected by the @task decorator.
            process=Process.sequential,
            verbose=True,
        )

```

Tasks will be executed in the order they are defined.

The `CrewBase` class, along with these decorators, automates the collection of agents and tasks, reducing the need for manual management.

#### [​](https://docs.crewai.com/concepts/crews\#decorators-overview-from-annotations-py)  Decorators overview from `annotations.py`

CrewAI provides several decorators in the `annotations.py` file that are used to mark methods within your crew class for special handling:

- `@CrewBase`: Marks the class as a crew base class.
- `@agent`: Denotes a method that returns an `Agent` object.
- `@task`: Denotes a method that returns a `Task` object.
- `@crew`: Denotes the method that returns the `Crew` object.
- `@before_kickoff`: (Optional) Marks a method to be executed before the crew starts.
- `@after_kickoff`: (Optional) Marks a method to be executed after the crew finishes.

These decorators help in organizing your crew’s structure and automatically collecting agents and tasks without manually listing them.

### [​](https://docs.crewai.com/concepts/crews\#direct-code-definition-alternative)  Direct Code Definition (Alternative)

Alternatively, you can define the crew directly in code without using YAML configuration files.

code

Copy

```python
from crewai import Agent, Crew, Task, Process
from crewai_tools import YourCustomTool

class YourCrewName:
    def agent_one(self) -> Agent:
        return Agent(
            role="Data Analyst",
            goal="Analyze data trends in the market",
            backstory="An experienced data analyst with a background in economics",
            verbose=True,
            tools=[YourCustomTool()]
        )

    def agent_two(self) -> Agent:
        return Agent(
            role="Market Researcher",
            goal="Gather information on market dynamics",
            backstory="A diligent researcher with a keen eye for detail",
            verbose=True
        )

    def task_one(self) -> Task:
        return Task(
            description="Collect recent market data and identify trends.",
            expected_output="A report summarizing key trends in the market.",
            agent=self.agent_one()
        )

    def task_two(self) -> Task:
        return Task(
            description="Research factors affecting market dynamics.",
            expected_output="An analysis of factors influencing the market.",
            agent=self.agent_two()
        )

    def crew(self) -> Crew:
        return Crew(
            agents=[self.agent_one(), self.agent_two()],
            tasks=[self.task_one(), self.task_two()],
            process=Process.sequential,
            verbose=True
        )

```

In this example:

- Agents and tasks are defined directly within the class without decorators.
- We manually create and manage the list of agents and tasks.
- This approach provides more control but can be less maintainable for larger projects.

## [​](https://docs.crewai.com/concepts/crews\#crew-output)  Crew Output

The output of a crew in the CrewAI framework is encapsulated within the `CrewOutput` class.
This class provides a structured way to access results of the crew’s execution, including various formats such as raw strings, JSON, and Pydantic models.
The `CrewOutput` includes the results from the final task output, token usage, and individual task outputs.

### [​](https://docs.crewai.com/concepts/crews\#crew-output-attributes)  Crew Output Attributes

| Attribute | Parameters | Type | Description |
| --- | --- | --- | --- |
| **Raw** | `raw` | `str` | The raw output of the crew. This is the default format for the output. |
| **Pydantic** | `pydantic` | `Optional[BaseModel]` | A Pydantic model object representing the structured output of the crew. |
| **JSON Dict** | `json_dict` | `Optional[Dict[str, Any]]` | A dictionary representing the JSON output of the crew. |
| **Tasks Output** | `tasks_output` | `List[TaskOutput]` | A list of `TaskOutput` objects, each representing the output of a task in the crew. |
| **Token Usage** | `token_usage` | `Dict[str, Any]` | A summary of token usage, providing insights into the language model’s performance during execution. |

### [​](https://docs.crewai.com/concepts/crews\#crew-output-methods-and-properties)  Crew Output Methods and Properties

| Method/Property | Description |
| --- | --- |
| **json** | Returns the JSON string representation of the crew output if the output format is JSON. |
| **to\_dict** | Converts the JSON and Pydantic outputs to a dictionary. |
| \* **\*str\*\*** | Returns the string representation of the crew output, prioritizing Pydantic, then JSON, then raw. |

### [​](https://docs.crewai.com/concepts/crews\#accessing-crew-outputs)  Accessing Crew Outputs

Once a crew has been executed, its output can be accessed through the `output` attribute of the `Crew` object. The `CrewOutput` class provides various ways to interact with and present this output.

#### [​](https://docs.crewai.com/concepts/crews\#example)  Example

Code

Copy

```python
# Example crew execution
crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, write_article_task],
    verbose=True
)

crew_output = crew.kickoff()

# Accessing the crew output
print(f"Raw Output: {crew_output.raw}")
if crew_output.json_dict:
    print(f"JSON Output: {json.dumps(crew_output.json_dict, indent=2)}")
if crew_output.pydantic:
    print(f"Pydantic Output: {crew_output.pydantic}")
print(f"Tasks Output: {crew_output.tasks_output}")
print(f"Token Usage: {crew_output.token_usage}")

```

## [​](https://docs.crewai.com/concepts/crews\#accessing-crew-logs)  Accessing Crew Logs

You can see real time log of the crew execution, by setting `output_log_file` as a `True(Boolean)` or a `file_name(str)`. Supports logging of events as both `file_name.txt` and `file_name.json`.
In case of `True(Boolean)` will save as `logs.txt`.

In case of `output_log_file` is set as `False(Booelan)` or `None`, the logs will not be populated.

Code

Copy

```python
# Save crew logs
crew = Crew(output_log_file = True)  # Logs will be saved as logs.txt
crew = Crew(output_log_file = file_name)  # Logs will be saved as file_name.txt
crew = Crew(output_log_file = file_name.txt)  # Logs will be saved as file_name.txt
crew = Crew(output_log_file = file_name.json)  # Logs will be saved as file_name.json

```

## [​](https://docs.crewai.com/concepts/crews\#memory-utilization)  Memory Utilization

Crews can utilize memory (short-term, long-term, and entity memory) to enhance their execution and learning over time. This feature allows crews to store and recall execution memories, aiding in decision-making and task execution strategies.

## [​](https://docs.crewai.com/concepts/crews\#cache-utilization)  Cache Utilization

Caches can be employed to store the results of tools’ execution, making the process more efficient by reducing the need to re-execute identical tasks.

## [​](https://docs.crewai.com/concepts/crews\#crew-usage-metrics)  Crew Usage Metrics

After the crew execution, you can access the `usage_metrics` attribute to view the language model (LLM) usage metrics for all tasks executed by the crew. This provides insights into operational efficiency and areas for improvement.

Code

Copy

```python
# Access the crew's usage metrics
crew = Crew(agents=[agent1, agent2], tasks=[task1, task2])
crew.kickoff()
print(crew.usage_metrics)

```

## [​](https://docs.crewai.com/concepts/crews\#crew-execution-process)  Crew Execution Process

- **Sequential Process**: Tasks are executed one after another, allowing for a linear flow of work.
- **Hierarchical Process**: A manager agent coordinates the crew, delegating tasks and validating outcomes before proceeding. **Note**: A `manager_llm` or `manager_agent` is required for this process and it’s essential for validating the process flow.

### [​](https://docs.crewai.com/concepts/crews\#kicking-off-a-crew)  Kicking Off a Crew

Once your crew is assembled, initiate the workflow with the `kickoff()` method. This starts the execution process according to the defined process flow.

Code

Copy

```python
# Start the crew's task execution
result = my_crew.kickoff()
print(result)

```

### [​](https://docs.crewai.com/concepts/crews\#different-ways-to-kick-off-a-crew)  Different Ways to Kick Off a Crew

Once your crew is assembled, initiate the workflow with the appropriate kickoff method. CrewAI provides several methods for better control over the kickoff process: `kickoff()`, `kickoff_for_each()`, `kickoff_async()`, and `kickoff_for_each_async()`.

- `kickoff()`: Starts the execution process according to the defined process flow.
- `kickoff_for_each()`: Executes tasks sequentially for each provided input event or item in the collection.
- `kickoff_async()`: Initiates the workflow asynchronously.
- `kickoff_for_each_async()`: Executes tasks concurrently for each provided input event or item, leveraging asynchronous processing.

Code

Copy

```python
# Start the crew's task execution
result = my_crew.kickoff()
print(result)

# Example of using kickoff_for_each
inputs_array = [{'topic': 'AI in healthcare'}, {'topic': 'AI in finance'}]
results = my_crew.kickoff_for_each(inputs=inputs_array)
for result in results:
    print(result)

# Example of using kickoff_async
inputs = {'topic': 'AI in healthcare'}
async_result = my_crew.kickoff_async(inputs=inputs)
print(async_result)

# Example of using kickoff_for_each_async
inputs_array = [{'topic': 'AI in healthcare'}, {'topic': 'AI in finance'}]
async_results = my_crew.kickoff_for_each_async(inputs=inputs_array)
for async_result in async_results:
    print(async_result)

```

These methods provide flexibility in how you manage and execute tasks within your crew, allowing for both synchronous and asynchronous workflows tailored to your needs.

### [​](https://docs.crewai.com/concepts/crews\#replaying-from-a-specific-task)  Replaying from a Specific Task

You can now replay from a specific task using our CLI command `replay`.

The replay feature in CrewAI allows you to replay from a specific task using the command-line interface (CLI). By running the command `crewai replay -t <task_id>`, you can specify the `task_id` for the replay process.

Kickoffs will now save the latest kickoffs returned task outputs locally for you to be able to replay from.

### [​](https://docs.crewai.com/concepts/crews\#replaying-from-a-specific-task-using-the-cli)  Replaying from a Specific Task Using the CLI

To use the replay feature, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where your CrewAI project is located.
3. Run the following command:

To view the latest kickoff task IDs, use:

Copy

```shell
crewai log-tasks-outputs

```

Then, to replay from a specific task, use:

Copy

```shell
crewai replay -t <task_id>

```

These commands let you replay from your latest kickoff tasks, still retaining context from previously executed tasks.

Was this page helpful?

YesNo

[Tasks](https://docs.crewai.com/concepts/tasks) [Flows](https://docs.crewai.com/concepts/flows)

On this page

- [What is a Crew?](https://docs.crewai.com/concepts/crews#what-is-a-crew%3F)
- [Crew Attributes](https://docs.crewai.com/concepts/crews#crew-attributes)
- [Creating Crews](https://docs.crewai.com/concepts/crews#creating-crews)
- [YAML Configuration (Recommended)](https://docs.crewai.com/concepts/crews#yaml-configuration-recommended)
- [Example Crew Class with Decorators](https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators)
- [Decorators overview from annotations.py](https://docs.crewai.com/concepts/crews#decorators-overview-from-annotations-py)
- [Direct Code Definition (Alternative)](https://docs.crewai.com/concepts/crews#direct-code-definition-alternative)
- [Crew Output](https://docs.crewai.com/concepts/crews#crew-output)
- [Crew Output Attributes](https://docs.crewai.com/concepts/crews#crew-output-attributes)
- [Crew Output Methods and Properties](https://docs.crewai.com/concepts/crews#crew-output-methods-and-properties)
- [Accessing Crew Outputs](https://docs.crewai.com/concepts/crews#accessing-crew-outputs)
- [Example](https://docs.crewai.com/concepts/crews#example)
- [Accessing Crew Logs](https://docs.crewai.com/concepts/crews#accessing-crew-logs)
- [Memory Utilization](https://docs.crewai.com/concepts/crews#memory-utilization)
- [Cache Utilization](https://docs.crewai.com/concepts/crews#cache-utilization)
- [Crew Usage Metrics](https://docs.crewai.com/concepts/crews#crew-usage-metrics)
- [Crew Execution Process](https://docs.crewai.com/concepts/crews#crew-execution-process)
- [Kicking Off a Crew](https://docs.crewai.com/concepts/crews#kicking-off-a-crew)
- [Different Ways to Kick Off a Crew](https://docs.crewai.com/concepts/crews#different-ways-to-kick-off-a-crew)
- [Replaying from a Specific Task](https://docs.crewai.com/concepts/crews#replaying-from-a-specific-task)
- [Replaying from a Specific Task Using the CLI](https://docs.crewai.com/concepts/crews#replaying-from-a-specific-task-using-the-cli)

# Code Docs RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Code Docs RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/codedocssearchtool\#codedocssearchtool)  `CodeDocsSearchTool`

**Experimental**: We are still working on improving tools, so there might be unexpected behavior or changes in the future.

## [​](https://docs.crewai.com/tools/codedocssearchtool\#description)  Description

The CodeDocsSearchTool is a powerful RAG (Retrieval-Augmented Generation) tool designed for semantic searches within code documentation.
It enables users to efficiently find specific information or topics within code documentation. By providing a `docs_url` during initialization,
the tool narrows down the search to that particular documentation site. Alternatively, without a specific `docs_url`,
it searches across a wide array of code documentation known or discovered throughout its execution, making it versatile for various documentation search needs.

## [​](https://docs.crewai.com/tools/codedocssearchtool\#installation)  Installation

To start using the CodeDocsSearchTool, first, install the crewai\_tools package via pip:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/codedocssearchtool\#example)  Example

Utilize the CodeDocsSearchTool as follows to conduct searches within code documentation:

Code

Copy

```python
from crewai_tools import CodeDocsSearchTool

# To search any code documentation content
# if the URL is known or discovered during its execution:
tool = CodeDocsSearchTool()

# OR

# To specifically focus your search on a given documentation site
# by providing its URL:
tool = CodeDocsSearchTool(docs_url='https://docs.example.com/reference')

```

Substitute ‘ [https://docs.example.com/reference](https://docs.example.com/reference)’ with your target documentation URL
and ‘How to use search tool’ with the search query relevant to your needs.

## [​](https://docs.crewai.com/tools/codedocssearchtool\#arguments)  Arguments

The following parameters can be used to customize the `CodeDocsSearchTool`’s behavior:

| Argument | Type | Description |
| --- | --- | --- |
| **docs\_url** | `string` | _Optional_. Specifies the URL of the code documentation to be searched. |

## [​](https://docs.crewai.com/tools/codedocssearchtool\#custom-model-and-embeddings)  Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

Code

Copy

```python
tool = CodeDocsSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[Browserbase Web Loader](https://docs.crewai.com/tools/browserbaseloadtool) [Code Interpreter](https://docs.crewai.com/tools/codeinterpretertool)

On this page

- [CodeDocsSearchTool](https://docs.crewai.com/tools/codedocssearchtool#codedocssearchtool)
- [Description](https://docs.crewai.com/tools/codedocssearchtool#description)
- [Installation](https://docs.crewai.com/tools/codedocssearchtool#installation)
- [Example](https://docs.crewai.com/tools/codedocssearchtool#example)
- [Arguments](https://docs.crewai.com/tools/codedocssearchtool#arguments)
- [Custom model and embeddings](https://docs.crewai.com/tools/codedocssearchtool#custom-model-and-embeddings)

# Knowledge - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Knowledge

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/knowledge\#what-is-knowledge%3F)  What is Knowledge?

Knowledge in CrewAI is a powerful system that allows AI agents to access and utilize external information sources during their tasks.
Think of it as giving your agents a reference library they can consult while working.

Key benefits of using Knowledge:

- Enhance agents with domain-specific information
- Support decisions with real-world data
- Maintain context across conversations
- Ground responses in factual information

## [​](https://docs.crewai.com/concepts/knowledge\#supported-knowledge-sources)  Supported Knowledge Sources

CrewAI supports various types of knowledge sources out of the box:

## Text Sources

- Raw strings
- Text files (.txt)
- PDF documents

## Structured Data

- CSV files
- Excel spreadsheets
- JSON documents

## [​](https://docs.crewai.com/concepts/knowledge\#supported-knowledge-parameters)  Supported Knowledge Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `sources` | **List\[BaseKnowledgeSource\]** | Yes | List of knowledge sources that provide content to be stored and queried. Can include PDF, CSV, Excel, JSON, text files, or string content. |
| `collection_name` | **str** | No | Name of the collection where the knowledge will be stored. Used to identify different sets of knowledge. Defaults to “knowledge” if not provided. |
| `storage` | **Optional\[KnowledgeStorage\]** | No | Custom storage configuration for managing how the knowledge is stored and retrieved. If not provided, a default storage will be created. |

## [​](https://docs.crewai.com/concepts/knowledge\#quickstart-example)  Quickstart Example

For file-Based Knowledge Sources, make sure to place your files in a `knowledge` directory at the root of your project.
Also, use relative paths from the `knowledge` directory when creating the source.

Here’s an example using string-based knowledge:

Code

Copy

```python
from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

# Create a knowledge source
content = "Users name is John. He is 30 years old and lives in San Francisco."
string_source = StringKnowledgeSource(
    content=content,
)

# Create an LLM with a temperature of 0 to ensure deterministic outputs
llm = LLM(model="gpt-4o-mini", temperature=0)

# Create an agent with the knowledge store
agent = Agent(
    role="About User",
    goal="You know everything about the user.",
    backstory="""You are a master at understanding people and their preferences.""",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)
task = Task(
    description="Answer the following questions about the user: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[string_source], # Enable knowledge by adding the sources here. You can also add more sources to the sources list.
)

result = crew.kickoff(inputs={"question": "What city does John live in and how old is he?"})

```

Here’s another example with the `CrewDoclingSource`. The CrewDoclingSource is actually quite versatile and can handle multiple file formats including MD, PDF, DOCX, HTML, and more.

You need to install `docling` for the following example to work: `uv add docling`

Code

Copy

```python
from crewai import LLM, Agent, Crew, Process, Task
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource

# Create a knowledge source
content_source = CrewDoclingSource(
    file_paths=[\
        "https://lilianweng.github.io/posts/2024-11-28-reward-hacking",\
        "https://lilianweng.github.io/posts/2024-07-07-hallucination",\
    ],
)

# Create an LLM with a temperature of 0 to ensure deterministic outputs
llm = LLM(model="gpt-4o-mini", temperature=0)

# Create an agent with the knowledge store
agent = Agent(
    role="About papers",
    goal="You know everything about the papers.",
    backstory="""You are a master at understanding papers and their content.""",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)
task = Task(
    description="Answer the following questions about the papers: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[\
        content_source\
    ],  # Enable knowledge by adding the sources here. You can also add more sources to the sources list.
)

result = crew.kickoff(
    inputs={
        "question": "What is the reward hacking paper about? Be sure to provide sources."
    }
)

```

## [​](https://docs.crewai.com/concepts/knowledge\#more-examples)  More Examples

Here are examples of how to use different types of knowledge sources:

### [​](https://docs.crewai.com/concepts/knowledge\#text-file-knowledge-source)  Text File Knowledge Source

Copy

```python
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

# Create a text file knowledge source
text_source = TextFileKnowledgeSource(
    file_paths=["document.txt", "another.txt"]
)

# Create crew with text file source on agents or crew level
agent = Agent(
    ...
    knowledge_sources=[text_source]
)

crew = Crew(
    ...
    knowledge_sources=[text_source]
)

```

### [​](https://docs.crewai.com/concepts/knowledge\#pdf-knowledge-source)  PDF Knowledge Source

Copy

```python
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

# Create a PDF knowledge source
pdf_source = PDFKnowledgeSource(
    file_paths=["document.pdf", "another.pdf"]
)

# Create crew with PDF knowledge source on agents or crew level
agent = Agent(
    ...
    knowledge_sources=[pdf_source]
)

crew = Crew(
    ...
    knowledge_sources=[pdf_source]
)

```

### [​](https://docs.crewai.com/concepts/knowledge\#csv-knowledge-source)  CSV Knowledge Source

Copy

```python
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource

# Create a CSV knowledge source
csv_source = CSVKnowledgeSource(
    file_paths=["data.csv"]
)

# Create crew with CSV knowledge source or on agent level
agent = Agent(
    ...
    knowledge_sources=[csv_source]
)

crew = Crew(
    ...
    knowledge_sources=[csv_source]
)

```

### [​](https://docs.crewai.com/concepts/knowledge\#excel-knowledge-source)  Excel Knowledge Source

Copy

```python
from crewai.knowledge.source.excel_knowledge_source import ExcelKnowledgeSource

# Create an Excel knowledge source
excel_source = ExcelKnowledgeSource(
    file_paths=["spreadsheet.xlsx"]
)

# Create crew with Excel knowledge source on agents or crew level
agent = Agent(
    ...
    knowledge_sources=[excel_source]
)

crew = Crew(
    ...
    knowledge_sources=[excel_source]
)

```

### [​](https://docs.crewai.com/concepts/knowledge\#json-knowledge-source)  JSON Knowledge Source

Copy

```python
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource

# Create a JSON knowledge source
json_source = JSONKnowledgeSource(
    file_paths=["data.json"]
)

# Create crew with JSON knowledge source on agents or crew level
agent = Agent(
    ...
    knowledge_sources=[json_source]
)

crew = Crew(
    ...
    knowledge_sources=[json_source]
)

```

## [​](https://docs.crewai.com/concepts/knowledge\#knowledge-configuration)  Knowledge Configuration

### [​](https://docs.crewai.com/concepts/knowledge\#chunking-configuration)  Chunking Configuration

Knowledge sources automatically chunk content for better processing.
You can configure chunking behavior in your knowledge sources:

Copy

```python
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

source = StringKnowledgeSource(
    content="Your content here",
    chunk_size=4000,      # Maximum size of each chunk (default: 4000)
    chunk_overlap=200     # Overlap between chunks (default: 200)
)

```

The chunking configuration helps in:

- Breaking down large documents into manageable pieces
- Maintaining context through chunk overlap
- Optimizing retrieval accuracy

### [​](https://docs.crewai.com/concepts/knowledge\#embeddings-configuration)  Embeddings Configuration

You can also configure the embedder for the knowledge store.
This is useful if you want to use a different embedder for the knowledge store than the one used for the agents.
The `embedder` parameter supports various embedding model providers that include:

- `openai`: OpenAI’s embedding models
- `google`: Google’s text embedding models
- `azure`: Azure OpenAI embeddings
- `ollama`: Local embeddings with Ollama
- `vertexai`: Google Cloud VertexAI embeddings
- `cohere`: Cohere’s embedding models
- `voyageai`: VoyageAI’s embedding models
- `bedrock`: AWS Bedrock embeddings
- `huggingface`: Hugging Face models
- `watson`: IBM Watson embeddings

Here’s an example of how to configure the embedder for the knowledge store using Google’s `text-embedding-004` model:

Example

Output

Copy

```python
from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
import os

# Get the GEMINI API key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Create a knowledge source
content = "Users name is John. He is 30 years old and lives in San Francisco."
string_source = StringKnowledgeSource(
    content=content,
)

# Create an LLM with a temperature of 0 to ensure deterministic outputs
gemini_llm = LLM(
    model="gemini/gemini-1.5-pro-002",
    api_key=GEMINI_API_KEY,
    temperature=0,
)

# Create an agent with the knowledge store
agent = Agent(
    role="About User",
    goal="You know everything about the user.",
    backstory="""You are a master at understanding people and their preferences.""",
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm,
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)

task = Task(
    description="Answer the following questions about the user: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[string_source],
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)

result = crew.kickoff(inputs={"question": "What city does John live in and how old is he?"})

```

## [​](https://docs.crewai.com/concepts/knowledge\#clearing-knowledge)  Clearing Knowledge

If you need to clear the knowledge stored in CrewAI, you can use the `crewai reset-memories` command with the `--knowledge` option.

Command

Copy

```bash
crewai reset-memories --knowledge

```

This is useful when you’ve updated your knowledge sources and want to ensure that the agents are using the most recent information.

## [​](https://docs.crewai.com/concepts/knowledge\#agent-specific-knowledge)  Agent-Specific Knowledge

While knowledge can be provided at the crew level using `crew.knowledge_sources`, individual agents can also have their own knowledge sources using the `knowledge_sources` parameter:

Code

Copy

```python
from crewai import Agent, Task, Crew
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

# Create agent-specific knowledge about a product
product_specs = StringKnowledgeSource(
    content="""The XPS 13 laptop features:
    - 13.4-inch 4K display
    - Intel Core i7 processor
    - 16GB RAM
    - 512GB SSD storage
    - 12-hour battery life""",
    metadata={"category": "product_specs"}
)

# Create a support agent with product knowledge
support_agent = Agent(
    role="Technical Support Specialist",
    goal="Provide accurate product information and support.",
    backstory="You are an expert on our laptop products and specifications.",
    knowledge_sources=[product_specs]  # Agent-specific knowledge
)

# Create a task that requires product knowledge
support_task = Task(
    description="Answer this customer question: {question}",
    agent=support_agent
)

# Create and run the crew
crew = Crew(
    agents=[support_agent],
    tasks=[support_task]
)

# Get answer about the laptop's specifications
result = crew.kickoff(
    inputs={"question": "What is the storage capacity of the XPS 13?"}
)

```

Benefits of agent-specific knowledge:

- Give agents specialized information for their roles
- Maintain separation of concerns between agents
- Combine with crew-level knowledge for layered information access

## [​](https://docs.crewai.com/concepts/knowledge\#custom-knowledge-sources)  Custom Knowledge Sources

CrewAI allows you to create custom knowledge sources for any type of data by extending the `BaseKnowledgeSource` class. Let’s create a practical example that fetches and processes space news articles.

#### [​](https://docs.crewai.com/concepts/knowledge\#space-news-knowledge-source-example)  Space News Knowledge Source Example

Code

Output

Copy

```python
from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.base_knowledge_source import BaseKnowledgeSource
import requests
from datetime import datetime
from typing import Dict, Any
from pydantic import BaseModel, Field

class SpaceNewsKnowledgeSource(BaseKnowledgeSource):
    """Knowledge source that fetches data from Space News API."""

    api_endpoint: str = Field(description="API endpoint URL")
    limit: int = Field(default=10, description="Number of articles to fetch")

    def load_content(self) -> Dict[Any, str]:
        """Fetch and format space news articles."""
        try:
            response = requests.get(
                f"{self.api_endpoint}?limit={self.limit}"
            )
            response.raise_for_status()

            data = response.json()
            articles = data.get('results', [])

            formatted_data = self._format_articles(articles)
            return {self.api_endpoint: formatted_data}
        except Exception as e:
            raise ValueError(f"Failed to fetch space news: {str(e)}")

    def _format_articles(self, articles: list) -> str:
        """Format articles into readable text."""
        formatted = "Space News Articles:\n\n"
        for article in articles:
            formatted += f"""
                Title: {article['title']}
                Published: {article['published_at']}
                Summary: {article['summary']}
                News Site: {article['news_site']}
                URL: {article['url']}
                -------------------"""
        return formatted

    def add(self) -> None:
        """Process and store the articles."""
        content = self.load_content()
        for _, text in content.items():
            chunks = self._chunk_text(text)
            self.chunks.extend(chunks)

        self._save_documents()

# Create knowledge source
recent_news = SpaceNewsKnowledgeSource(
    api_endpoint="https://api.spaceflightnewsapi.net/v4/articles",
    limit=10,
)

# Create specialized agent
space_analyst = Agent(
    role="Space News Analyst",
    goal="Answer questions about space news accurately and comprehensively",
    backstory="""You are a space industry analyst with expertise in space exploration,
    satellite technology, and space industry trends. You excel at answering questions
    about space news and providing detailed, accurate information.""",
    knowledge_sources=[recent_news],
    llm=LLM(model="gpt-4", temperature=0.0)
)

# Create task that handles user questions
analysis_task = Task(
    description="Answer this question about space news: {user_question}",
    expected_output="A detailed answer based on the recent space news articles",
    agent=space_analyst
)

# Create and run the crew
crew = Crew(
    agents=[space_analyst],
    tasks=[analysis_task],
    verbose=True,
    process=Process.sequential
)

# Example usage
result = crew.kickoff(
    inputs={"user_question": "What are the latest developments in space exploration?"}
)

```

#### [​](https://docs.crewai.com/concepts/knowledge\#key-components-explained)  Key Components Explained

1. **Custom Knowledge Source ( `SpaceNewsKnowledgeSource`)**:
   - Extends `BaseKnowledgeSource` for integration with CrewAI
   - Configurable API endpoint and article limit
   - Implements three key methods:
     - `load_content()`: Fetches articles from the API
     - `_format_articles()`: Structures the articles into readable text
     - `add()`: Processes and stores the content
2. **Agent Configuration**:
   - Specialized role as a Space News Analyst
   - Uses the knowledge source to access space news
3. **Task Setup**:
   - Takes a user question as input through `{user_question}`
   - Designed to provide detailed answers based on the knowledge source
4. **Crew Orchestration**:
   - Manages the workflow between agent and task
   - Handles input/output through the kickoff method

This example demonstrates how to:

- Create a custom knowledge source that fetches real-time data
- Process and format external data for AI consumption
- Use the knowledge source to answer specific user questions
- Integrate everything seamlessly with CrewAI’s agent system

#### [​](https://docs.crewai.com/concepts/knowledge\#about-the-spaceflight-news-api)  About the Spaceflight News API

The example uses the [Spaceflight News API](https://api.spaceflightnewsapi.net/v4/docs/), which:

- Provides free access to space-related news articles
- Requires no authentication
- Returns structured data about space news
- Supports pagination and filtering

You can customize the API query by modifying the endpoint URL:

Copy

```python
# Fetch more articles
recent_news = SpaceNewsKnowledgeSource(
    api_endpoint="https://api.spaceflightnewsapi.net/v4/articles",
    limit=20,  # Increase the number of articles
)

# Add search parameters
recent_news = SpaceNewsKnowledgeSource(
    api_endpoint="https://api.spaceflightnewsapi.net/v4/articles?search=NASA", # Search for NASA news
    limit=10,
)

```

## [​](https://docs.crewai.com/concepts/knowledge\#best-practices)  Best Practices

Content Organization

- Keep chunk sizes appropriate for your content type
- Consider content overlap for context preservation
- Organize related information into separate knowledge sources

Performance Tips

- Adjust chunk sizes based on content complexity
- Configure appropriate embedding models
- Consider using local embedding providers for faster processing

Was this page helpful?

YesNo

[Flows](https://docs.crewai.com/concepts/flows) [LLMs](https://docs.crewai.com/concepts/llms)

On this page

- [What is Knowledge?](https://docs.crewai.com/concepts/knowledge#what-is-knowledge%3F)
- [Supported Knowledge Sources](https://docs.crewai.com/concepts/knowledge#supported-knowledge-sources)
- [Supported Knowledge Parameters](https://docs.crewai.com/concepts/knowledge#supported-knowledge-parameters)
- [Quickstart Example](https://docs.crewai.com/concepts/knowledge#quickstart-example)
- [More Examples](https://docs.crewai.com/concepts/knowledge#more-examples)
- [Text File Knowledge Source](https://docs.crewai.com/concepts/knowledge#text-file-knowledge-source)
- [PDF Knowledge Source](https://docs.crewai.com/concepts/knowledge#pdf-knowledge-source)
- [CSV Knowledge Source](https://docs.crewai.com/concepts/knowledge#csv-knowledge-source)
- [Excel Knowledge Source](https://docs.crewai.com/concepts/knowledge#excel-knowledge-source)
- [JSON Knowledge Source](https://docs.crewai.com/concepts/knowledge#json-knowledge-source)
- [Knowledge Configuration](https://docs.crewai.com/concepts/knowledge#knowledge-configuration)
- [Chunking Configuration](https://docs.crewai.com/concepts/knowledge#chunking-configuration)
- [Embeddings Configuration](https://docs.crewai.com/concepts/knowledge#embeddings-configuration)
- [Clearing Knowledge](https://docs.crewai.com/concepts/knowledge#clearing-knowledge)
- [Agent-Specific Knowledge](https://docs.crewai.com/concepts/knowledge#agent-specific-knowledge)
- [Custom Knowledge Sources](https://docs.crewai.com/concepts/knowledge#custom-knowledge-sources)
- [Space News Knowledge Source Example](https://docs.crewai.com/concepts/knowledge#space-news-knowledge-source-example)
- [Key Components Explained](https://docs.crewai.com/concepts/knowledge#key-components-explained)
- [About the Spaceflight News API](https://docs.crewai.com/concepts/knowledge#about-the-spaceflight-news-api)
- [Best Practices](https://docs.crewai.com/concepts/knowledge#best-practices)

# YouTube Video RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

YouTube Video RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/youtubevideosearchtool\#youtubevideosearchtool)  `YoutubeVideoSearchTool`

We are still working on improving tools, so there might be unexpected behavior or changes in the future.

## [​](https://docs.crewai.com/tools/youtubevideosearchtool\#description)  Description

This tool is part of the `crewai_tools` package and is designed to perform semantic searches within Youtube video content, utilizing Retrieval-Augmented Generation (RAG) techniques.
It is one of several “Search” tools in the package that leverage RAG for different sources.
The YoutubeVideoSearchTool allows for flexibility in searches; users can search across any Youtube video content without specifying a video URL,
or they can target their search to a specific Youtube video by providing its URL.

## [​](https://docs.crewai.com/tools/youtubevideosearchtool\#installation)  Installation

To utilize the `YoutubeVideoSearchTool`, you must first install the `crewai_tools` package.
This package contains the `YoutubeVideoSearchTool` among other utilities designed to enhance your data analysis and processing tasks.
Install the package by executing the following command in your terminal:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/youtubevideosearchtool\#example)  Example

To integrate the YoutubeVideoSearchTool into your Python projects, follow the example below.
This demonstrates how to use the tool both for general Youtube content searches and for targeted searches within a specific video’s content.

Code

Copy

```python
from crewai_tools import YoutubeVideoSearchTool

# General search across Youtube content without specifying a video URL,
# so the agent can search within any Youtube video content
# it learns about its url during its operation
tool = YoutubeVideoSearchTool()

# Targeted search within a specific Youtube video's content
tool = YoutubeVideoSearchTool(
    youtube_video_url='https://youtube.com/watch?v=example'
)

```

## [​](https://docs.crewai.com/tools/youtubevideosearchtool\#arguments)  Arguments

The YoutubeVideoSearchTool accepts the following initialization arguments:

- `youtube_video_url`: An optional argument at initialization but required if targeting a specific Youtube video. It specifies the Youtube video URL path you want to search within.

## [​](https://docs.crewai.com/tools/youtubevideosearchtool\#custom-model-and-embeddings)  Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

Code

Copy

```python
tool = YoutubeVideoSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[YouTube Channel RAG Search](https://docs.crewai.com/tools/youtubechannelsearchtool) [Telemetry](https://docs.crewai.com/telemetry)

On this page

- [YoutubeVideoSearchTool](https://docs.crewai.com/tools/youtubevideosearchtool#youtubevideosearchtool)
- [Description](https://docs.crewai.com/tools/youtubevideosearchtool#description)
- [Installation](https://docs.crewai.com/tools/youtubevideosearchtool#installation)
- [Example](https://docs.crewai.com/tools/youtubevideosearchtool#example)
- [Arguments](https://docs.crewai.com/tools/youtubevideosearchtool#arguments)
- [Custom model and embeddings](https://docs.crewai.com/tools/youtubevideosearchtool#custom-model-and-embeddings)

# Testing - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Testing

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/testing\#introduction)  Introduction

Testing is a crucial part of the development process, and it is essential to ensure that your crew is performing as expected. With crewAI, you can easily test your crew and evaluate its performance using the built-in testing capabilities.

### [​](https://docs.crewai.com/concepts/testing\#using-the-testing-feature)  Using the Testing Feature

We added the CLI command `crewai test` to make it easy to test your crew. This command will run your crew for a specified number of iterations and provide detailed performance metrics. The parameters are `n_iterations` and `model`, which are optional and default to 2 and `gpt-4o-mini` respectively. For now, the only provider available is OpenAI.

Copy

```bash
crewai test

```

If you want to run more iterations or use a different model, you can specify the parameters like this:

Copy

```bash
crewai test --n_iterations 5 --model gpt-4o

```

or using the short forms:

Copy

```bash
crewai test -n 5 -m gpt-4o

```

When you run the `crewai test` command, the crew will be executed for the specified number of iterations, and the performance metrics will be displayed at the end of the run.

A table of scores at the end will show the performance of the crew in terms of the following metrics:

| Tasks/Crew/Agents | Run 1 | Run 2 | Avg. Total | Agents | Additional Info |
| --- | --- | --- | --- | --- | --- |
| Task 1 | 9.0 | 9.5 | **9.2** | Professional Insights |  |
|  |  |  |  | Researcher |  |
| Task 2 | 9.0 | 10.0 | **9.5** | Company Profile Investigator |  |
| Task 3 | 9.0 | 9.0 | **9.0** | Automation Insights |  |
|  |  |  |  | Specialist |  |
| Task 4 | 9.0 | 9.0 | **9.0** | Final Report Compiler | Automation Insights Specialist |
| Crew | 9.00 | 9.38 | **9.2** |  |  |
| Execution Time (s) | 126 | 145 | **135** |  |  |

The example above shows the test results for two runs of the crew with two tasks, with the average total score for each task and the crew as a whole.

Was this page helpful?

YesNo

[Planning](https://docs.crewai.com/concepts/planning) [CLI](https://docs.crewai.com/concepts/cli)

On this page

- [Introduction](https://docs.crewai.com/concepts/testing#introduction)
- [Using the Testing Feature](https://docs.crewai.com/concepts/testing#using-the-testing-feature)

# Coding Agents - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Coding Agents

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/how-to/coding-agents\#introduction)  Introduction

CrewAI Agents now have the powerful ability to write and execute code, significantly enhancing their problem-solving capabilities. This feature is particularly useful for tasks that require computational or programmatic solutions.

## [​](https://docs.crewai.com/how-to/coding-agents\#enabling-code-execution)  Enabling Code Execution

To enable code execution for an agent, set the `allow_code_execution` parameter to `True` when creating the agent.

Here’s an example:

Code

Copy

```python
from crewai import Agent

coding_agent = Agent(
    role="Senior Python Developer",
    goal="Craft well-designed and thought-out code",
    backstory="You are a senior Python developer with extensive experience in software architecture and best practices.",
    allow_code_execution=True
)

```

Note that `allow_code_execution` parameter defaults to `False`.

## [​](https://docs.crewai.com/how-to/coding-agents\#important-considerations)  Important Considerations

1. **Model Selection**: It is strongly recommended to use more capable models like Claude 3.5 Sonnet and GPT-4 when enabling code execution.
These models have a better understanding of programming concepts and are more likely to generate correct and efficient code.

2. **Error Handling**: The code execution feature includes error handling. If executed code raises an exception, the agent will receive the error message and can attempt to correct the code or
provide alternative solutions. The `max_retry_limit` parameter, which defaults to 2, controls the maximum number of retries for a task.

3. **Dependencies**: To use the code execution feature, you need to install the `crewai_tools` package. If not installed, the agent will log an info message:
“Coding tools not available. Install crewai\_tools.”


## [​](https://docs.crewai.com/how-to/coding-agents\#code-execution-process)  Code Execution Process

When an agent with code execution enabled encounters a task requiring programming:

1

Task Analysis

The agent analyzes the task and determines that code execution is necessary.

2

Code Formulation

It formulates the Python code needed to solve the problem.

3

Code Execution

The code is sent to the internal code execution tool ( `CodeInterpreterTool`).

4

Result Interpretation

The agent interprets the result and incorporates it into its response or uses it for further problem-solving.

## [​](https://docs.crewai.com/how-to/coding-agents\#example-usage)  Example Usage

Here’s a detailed example of creating an agent with code execution capabilities and using it in a task:

Code

Copy

```python
from crewai import Agent, Task, Crew

# Create an agent with code execution enabled
coding_agent = Agent(
    role="Python Data Analyst",
    goal="Analyze data and provide insights using Python",
    backstory="You are an experienced data analyst with strong Python skills.",
    allow_code_execution=True
)

# Create a task that requires code execution
data_analysis_task = Task(
    description="Analyze the given dataset and calculate the average age of participants.",
    agent=coding_agent
)

# Create a crew and add the task
analysis_crew = Crew(
    agents=[coding_agent],
    tasks=[data_analysis_task]
)

# Execute the crew
result = analysis_crew.kickoff()

print(result)

```

In this example, the `coding_agent` can write and execute Python code to perform data analysis tasks.

Was this page helpful?

YesNo

[Using Multimodal Agents](https://docs.crewai.com/how-to/multimodal-agents) [Force Tool Output as Result](https://docs.crewai.com/how-to/force-tool-output-as-result)

On this page

- [Introduction](https://docs.crewai.com/how-to/coding-agents#introduction)
- [Enabling Code Execution](https://docs.crewai.com/how-to/coding-agents#enabling-code-execution)
- [Important Considerations](https://docs.crewai.com/how-to/coding-agents#important-considerations)
- [Code Execution Process](https://docs.crewai.com/how-to/coding-agents#code-execution-process)
- [Example Usage](https://docs.crewai.com/how-to/coding-agents#example-usage)

# CrewAI Examples - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Examples

CrewAI Examples

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

[**Marketing Strategy** \\
\\
Automate marketing strategy creation with CrewAI.](https://github.com/crewAIInc/crewAI-examples/tree/main/marketing_strategy) [**Surprise Trip** \\
\\
Create a surprise trip itinerary with CrewAI.](https://github.com/crewAIInc/crewAI-examples/tree/main/surprise_trip) [**Match Profile to Positions** \\
\\
Match a profile to jobpositions with CrewAI.](https://github.com/crewAIInc/crewAI-examples/tree/main/match_profile_to_positions) [**Create Job Posting** \\
\\
Create a job posting with CrewAI.](https://github.com/crewAIInc/crewAI-examples/tree/main/job-posting) [**Game Generator** \\
\\
Create a game with CrewAI.](https://github.com/crewAIInc/crewAI-examples/tree/main/game-builder-crew) [**Find Job Candidates** \\
\\
Find job candidates with CrewAI.](https://github.com/crewAIInc/crewAI-examples/tree/main/recruitment)

Was this page helpful?

YesNo

# Agent Monitoring with Portkey - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Agent Monitoring with Portkey

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

![Portkey CrewAI Header Image](https://raw.githubusercontent.com/siddharthsambharia-portkey/Portkey-Product-Images/main/Portkey-CrewAI.png)

[Portkey](https://portkey.ai/?utm_source=crewai&utm_medium=crewai&utm_campaign=crewai) is a 2-line upgrade to make your CrewAI agents reliable, cost-efficient, and fast.

Portkey adds 4 core production capabilities to any CrewAI agent:

1. Routing to **200+ LLMs**
2. Making each LLM call more robust
3. Full-stack tracing & cost, performance analytics
4. Real-time guardrails to enforce behavior

## [​](https://docs.crewai.com/how-to/portkey-observability\#getting-started)  Getting Started

1

Install CrewAI and Portkey

Copy

```bash
pip install -qU crewai portkey-ai

```

2

Configure the LLM Client

To build CrewAI Agents with Portkey, you’ll need two keys:

- **Portkey API Key**: Sign up on the [Portkey app](https://app.portkey.ai/?utm_source=crewai&utm_medium=crewai&utm_campaign=crewai) and copy your API key
- **Virtual Key**: Virtual Keys securely manage your LLM API keys in one place. Store your LLM provider API keys securely in Portkey’s vault

Copy

```python
from crewai import LLM
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

gpt_llm = LLM(
    model="gpt-4",
    base_url=PORTKEY_GATEWAY_URL,
    api_key="dummy", # We are using Virtual key
    extra_headers=createHeaders(
        api_key="YOUR_PORTKEY_API_KEY",
        virtual_key="YOUR_VIRTUAL_KEY", # Enter your Virtual key from Portkey
    )
)

```

3

Create and Run Your First Agent

Copy

```python
from crewai import Agent, Task, Crew

# Define your agents with roles and goals
coder = Agent(
    role='Software developer',
    goal='Write clear, concise code on demand',
    backstory='An expert coder with a keen eye for software trends.',
    llm=gpt_llm
)

# Create tasks for your agents
task1 = Task(
    description="Define the HTML for making a simple website with heading- Hello World! Portkey is working!",
    expected_output="A clear and concise HTML code",
    agent=coder
)

# Instantiate your crew
crew = Crew(
    agents=[coder],
    tasks=[task1],
)

result = crew.kickoff()
print(result)

```

## [​](https://docs.crewai.com/how-to/portkey-observability\#key-features)  Key Features

| Feature | Description |
| --- | --- |
| 🌐 Multi-LLM Support | Access OpenAI, Anthropic, Gemini, Azure, and 250+ providers through a unified interface |
| 🛡️ Production Reliability | Implement retries, timeouts, load balancing, and fallbacks |
| 📊 Advanced Observability | Track 40+ metrics including costs, tokens, latency, and custom metadata |
| 🔍 Comprehensive Logging | Debug with detailed execution traces and function call logs |
| 🚧 Security Controls | Set budget limits and implement role-based access control |
| 🔄 Performance Analytics | Capture and analyze feedback for continuous improvement |
| 💾 Intelligent Caching | Reduce costs and latency with semantic or simple caching |

## [​](https://docs.crewai.com/how-to/portkey-observability\#production-features-with-portkey-configs)  Production Features with Portkey Configs

All features mentioned below are through Portkey’s Config system. Portkey’s Config system allows you to define routing strategies using simple JSON objects in your LLM API calls. You can create and manage Configs directly in your code or through the Portkey Dashboard. Each Config has a unique ID for easy reference.

![](https://raw.githubusercontent.com/Portkey-AI/docs-core/refs/heads/main/images/libraries/libraries-3.avif)

### [​](https://docs.crewai.com/how-to/portkey-observability\#1-use-250%2B-llms)  1\. Use 250+ LLMs

Access various LLMs like Anthropic, Gemini, Mistral, Azure OpenAI, and more with minimal code changes. Switch between providers or use them together seamlessly. [Learn more about Universal API](https://portkey.ai/docs/product/ai-gateway/universal-api)

Easily switch between different LLM providers:

Copy

```python
# Anthropic Configuration
anthropic_llm = LLM(
    model="claude-3-5-sonnet-latest",
    base_url=PORTKEY_GATEWAY_URL,
    api_key="dummy",
    extra_headers=createHeaders(
        api_key="YOUR_PORTKEY_API_KEY",
        virtual_key="YOUR_ANTHROPIC_VIRTUAL_KEY", #You don't need provider when using Virtual keys
        trace_id="anthropic_agent"
    )
)

# Azure OpenAI Configuration
azure_llm = LLM(
    model="gpt-4",
    base_url=PORTKEY_GATEWAY_URL,
    api_key="dummy",
    extra_headers=createHeaders(
        api_key="YOUR_PORTKEY_API_KEY",
        virtual_key="YOUR_AZURE_VIRTUAL_KEY", #You don't need provider when using Virtual keys
        trace_id="azure_agent"
    )
)

```

### [​](https://docs.crewai.com/how-to/portkey-observability\#2-caching)  2\. Caching

Improve response times and reduce costs with two powerful caching modes:

- **Simple Cache**: Perfect for exact matches
- **Semantic Cache**: Matches responses for requests that are semantically similar
[Learn more about Caching](https://portkey.ai/docs/product/ai-gateway/cache-simple-and-semantic)

Copy

```py
config = {
    "cache": {
        "mode": "semantic",  # or "simple" for exact matching
    }
}

```

### [​](https://docs.crewai.com/how-to/portkey-observability\#3-production-reliability)  3\. Production Reliability

Portkey provides comprehensive reliability features:

- **Automatic Retries**: Handle temporary failures gracefully
- **Request Timeouts**: Prevent hanging operations
- **Conditional Routing**: Route requests based on specific conditions
- **Fallbacks**: Set up automatic provider failovers
- **Load Balancing**: Distribute requests efficiently

[Learn more about Reliability Features](https://portkey.ai/docs/product/ai-gateway/)

### [​](https://docs.crewai.com/how-to/portkey-observability\#4-metrics)  4\. Metrics

Agent runs are complex. Portkey automatically logs **40+ comprehensive metrics** for your AI agents, including cost, tokens used, latency, etc. Whether you need a broad overview or granular insights into your agent runs, Portkey’s customizable filters provide the metrics you need.

- Cost per agent interaction
- Response times and latency
- Token usage and efficiency
- Success/failure rates
- Cache hit rates

![Portkey Dashboard](https://github.com/siddharthsambharia-portkey/Portkey-Product-Images/blob/main/Portkey-Dashboard.png?raw=true)

### [​](https://docs.crewai.com/how-to/portkey-observability\#5-detailed-logging)  5\. Detailed Logging

Logs are essential for understanding agent behavior, diagnosing issues, and improving performance. They provide a detailed record of agent activities and tool use, which is crucial for debugging and optimizing processes.

Access a dedicated section to view records of agent executions, including parameters, outcomes, function calls, and errors. Filter logs based on multiple parameters such as trace ID, model, tokens used, and metadata.

### [​](https://docs.crewai.com/how-to/portkey-observability\#6-enterprise-security-features)  6\. Enterprise Security Features

- Set budget limit and rate limts per Virtual Key (disposable API keys)
- Implement role-based access control
- Track system changes with audit logs
- Configure data retention policies

For detailed information on creating and managing Configs, visit the [Portkey documentation](https://docs.portkey.ai/product/ai-gateway/configs).

## [​](https://docs.crewai.com/how-to/portkey-observability\#resources)  Resources

- [📘 Portkey Documentation](https://docs.portkey.ai/)
- [📊 Portkey Dashboard](https://app.portkey.ai/?utm_source=crewai&utm_medium=crewai&utm_campaign=crewai)
- [🐦 Twitter](https://twitter.com/portkeyai)
- [💬 Discord Community](https://discord.gg/DD7vgKK299)

Was this page helpful?

YesNo

[Agent Monitoring with OpenLIT](https://docs.crewai.com/how-to/openlit-observability) [Agent Monitoring with Langfuse](https://docs.crewai.com/how-to/langfuse-observability)

On this page

- [Getting Started](https://docs.crewai.com/how-to/portkey-observability#getting-started)
- [Key Features](https://docs.crewai.com/how-to/portkey-observability#key-features)
- [Production Features with Portkey Configs](https://docs.crewai.com/how-to/portkey-observability#production-features-with-portkey-configs)
- [1\. Use 250+ LLMs](https://docs.crewai.com/how-to/portkey-observability#1-use-250%2B-llms)
- [2\. Caching](https://docs.crewai.com/how-to/portkey-observability#2-caching)
- [3\. Production Reliability](https://docs.crewai.com/how-to/portkey-observability#3-production-reliability)
- [4\. Metrics](https://docs.crewai.com/how-to/portkey-observability#4-metrics)
- [5\. Detailed Logging](https://docs.crewai.com/how-to/portkey-observability#5-detailed-logging)
- [6\. Enterprise Security Features](https://docs.crewai.com/how-to/portkey-observability#6-enterprise-security-features)
- [Resources](https://docs.crewai.com/how-to/portkey-observability#resources)

![Portkey CrewAI Header Image](https://docs.crewai.com/how-to/portkey-observability)

![](https://docs.crewai.com/how-to/portkey-observability)

![Portkey Dashboard](https://docs.crewai.com/how-to/portkey-observability)

# Telemetry - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Telemetry

Telemetry

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/telemetry\#telemetry)  Telemetry

By default, we collect no data that would be considered personal information under GDPR and other privacy regulations.
We do collect Tool’s names and Agent’s roles, so be advised not to include any personal information in the tool’s names or the Agent’s roles.
Because no personal information is collected, it’s not necessary to worry about data residency.
When `share_crew` is enabled, additional data is collected which may contain personal information if included by the user.
Users should exercise caution when enabling this feature to ensure compliance with privacy regulations.

CrewAI utilizes anonymous telemetry to gather usage statistics with the primary goal of enhancing the library.
Our focus is on improving and developing the features, integrations, and tools most utilized by our users.

It’s pivotal to understand that by default, **NO personal data is collected** concerning prompts, task descriptions, agents’ backstories or goals,
usage of tools, API calls, responses, any data processed by the agents, or secrets and environment variables.
When the `share_crew` feature is enabled, detailed data including task descriptions, agents’ backstories or goals, and other specific attributes are collected
to provide deeper insights. This expanded data collection may include personal information if users have incorporated it into their crews or tasks.
Users should carefully consider the content of their crews and tasks before enabling `share_crew`.
Users can disable telemetry by setting the environment variable `OTEL_SDK_DISABLED` to `true`.

### [​](https://docs.crewai.com/telemetry\#data-explanation%3A)  Data Explanation:

| Defaulted | Data | Reason and Specifics |
| --- | --- | --- |
| Yes | CrewAI and Python Version | Tracks software versions. Example: CrewAI v1.2.3, Python 3.8.10. No personal data. |
| Yes | Crew Metadata | Includes: randomly generated key and ID, process type (e.g., ‘sequential’, ‘parallel’), boolean flag for memory usage (true/false), count of tasks, count of agents. All non-personal. |
| Yes | Agent Data | Includes: randomly generated key and ID, role name (should not include personal info), boolean settings (verbose, delegation enabled, code execution allowed), max iterations, max RPM, max retry limit, LLM info (see LLM Attributes), list of tool names (should not include personal info). No personal data. |
| Yes | Task Metadata | Includes: randomly generated key and ID, boolean execution settings (async\_execution, human\_input), associated agent’s role and key, list of tool names. All non-personal. |
| Yes | Tool Usage Statistics | Includes: tool name (should not include personal info), number of usage attempts (integer), LLM attributes used. No personal data. |
| Yes | Test Execution Data | Includes: crew’s randomly generated key and ID, number of iterations, model name used, quality score (float), execution time (in seconds). All non-personal. |
| Yes | Task Lifecycle Data | Includes: creation and execution start/end times, crew and task identifiers. Stored as spans with timestamps. No personal data. |
| Yes | LLM Attributes | Includes: name, model\_name, model, top\_k, temperature, and class name of the LLM. All technical, non-personal data. |
| Yes | Crew Deployment attempt using crewAI CLI | Includes: The fact a deploy is being made and crew id, and if it’s trying to pull logs, no other data. |
| No | Agent’s Expanded Data | Includes: goal description, backstory text, i18n prompt file identifier. Users should ensure no personal info is included in text fields. |
| No | Detailed Task Information | Includes: task description, expected output description, context references. Users should ensure no personal info is included in these fields. |
| No | Environment Information | Includes: platform, release, system, version, and CPU count. Example: ‘Windows 10’, ‘x86\_64’. No personal data. |
| No | Crew and Task Inputs and Outputs | Includes: input parameters and output results as non-identifiable data. Users should ensure no personal info is included. |
| No | Comprehensive Crew Execution Data | Includes: detailed logs of crew operations, all agents and tasks data, final output. All non-personal and technical in nature. |

“No” in the “Defaulted” column indicates that this data is only collected when `share_crew` is set to `true`.

### [​](https://docs.crewai.com/telemetry\#opt-in-further-telemetry-sharing)  Opt-In Further Telemetry Sharing

Users can choose to share their complete telemetry data by enabling the `share_crew` attribute to `True` in their crew configurations.
Enabling `share_crew` results in the collection of detailed crew and task execution data, including `goal`, `backstory`, `context`, and `output` of tasks.
This enables a deeper insight into usage patterns.

If you enable `share_crew`, the collected data may include personal information if it has been incorporated into crew configurations, task descriptions, or outputs.
Users should carefully review their data and ensure compliance with GDPR and other applicable privacy regulations before enabling this feature.

Was this page helpful?

YesNo

[YouTube Video RAG Search](https://docs.crewai.com/tools/youtubevideosearchtool)

On this page

- [Telemetry](https://docs.crewai.com/telemetry#telemetry)
- [Data Explanation:](https://docs.crewai.com/telemetry#data-explanation%3A)
- [Opt-In Further Telemetry Sharing](https://docs.crewai.com/telemetry#opt-in-further-telemetry-sharing)

# Memory - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Memory

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/memory\#introduction-to-memory-systems-in-crewai)  Introduction to Memory Systems in CrewAI

The crewAI framework introduces a sophisticated memory system designed to significantly enhance the capabilities of AI agents.
This system comprises `short-term memory`, `long-term memory`, `entity memory`, and `contextual memory`, each serving a unique purpose in aiding agents to remember,
reason, and learn from past interactions.

## [​](https://docs.crewai.com/concepts/memory\#memory-system-components)  Memory System Components

| Component | Description |
| --- | --- |
| **Short-Term Memory** | Temporarily stores recent interactions and outcomes using `RAG`, enabling agents to recall and utilize information relevant to their current context during the current executions. |
| **Long-Term Memory** | Preserves valuable insights and learnings from past executions, allowing agents to build and refine their knowledge over time. |
| **Entity Memory** | Captures and organizes information about entities (people, places, concepts) encountered during tasks, facilitating deeper understanding and relationship mapping. Uses `RAG` for storing entity information. |
| **Contextual Memory** | Maintains the context of interactions by combining `ShortTermMemory`, `LongTermMemory`, and `EntityMemory`, aiding in the coherence and relevance of agent responses over a sequence of tasks or a conversation. |
| **User Memory** | Stores user-specific information and preferences, enhancing personalization and user experience. |

## [​](https://docs.crewai.com/concepts/memory\#how-memory-systems-empower-agents)  How Memory Systems Empower Agents

1. **Contextual Awareness**: With short-term and contextual memory, agents gain the ability to maintain context over a conversation or task sequence, leading to more coherent and relevant responses.

2. **Experience Accumulation**: Long-term memory allows agents to accumulate experiences, learning from past actions to improve future decision-making and problem-solving.

3. **Entity Understanding**: By maintaining entity memory, agents can recognize and remember key entities, enhancing their ability to process and interact with complex information.


## [​](https://docs.crewai.com/concepts/memory\#implementing-memory-in-your-crew)  Implementing Memory in Your Crew

When configuring a crew, you can enable and customize each memory component to suit the crew’s objectives and the nature of tasks it will perform.
By default, the memory system is disabled, and you can ensure it is active by setting `memory=True` in the crew configuration.
The memory will use OpenAI embeddings by default, but you can change it by setting `embedder` to a different model.
It’s also possible to initialize the memory instance with your own instance.

The ‘embedder’ only applies to **Short-Term Memory** which uses Chroma for RAG.
The **Long-Term Memory** uses SQLite3 to store task results. Currently, there is no way to override these storage implementations.
The data storage files are saved into a platform-specific location found using the appdirs package,
and the name of the project can be overridden using the **CREWAI\_STORAGE\_DIR** environment variable.

### [​](https://docs.crewai.com/concepts/memory\#example%3A-configuring-memory-for-a-crew)  Example: Configuring Memory for a Crew

Code

Copy

```python
from crewai import Crew, Agent, Task, Process

# Assemble your crew with memory capabilities
my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True
)

```

### [​](https://docs.crewai.com/concepts/memory\#example%3A-use-custom-memory-instances-e-g-faiss-as-the-vectordb)  Example: Use Custom Memory Instances e.g FAISS as the VectorDB

Code

Copy

```python
from crewai import Crew, Process
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
from crewai.memory.storage import LTMSQLiteStorage, RAGStorage
from typing import List, Optional

# Assemble your crew with memory capabilities
my_crew: Crew = Crew(
    agents = [...],
    tasks = [...],
    process = Process.sequential,
    memory = True,
    # Long-term memory for persistent storage across sessions
    long_term_memory = LongTermMemory(
        storage=LTMSQLiteStorage(
            db_path="/my_crew1/long_term_memory_storage.db"
        )
    ),
    # Short-term memory for current context using RAG
    short_term_memory = ShortTermMemory(
        storage = RAGStorage(
                embedder_config={
                    "provider": "openai",
                    "config": {
                        "model": 'text-embedding-3-small'
                    }
                },
                type="short_term",
                path="/my_crew1/"
            )
        ),
    ),
    # Entity memory for tracking key information about entities
    entity_memory = EntityMemory(
        storage=RAGStorage(
            embedder_config={
                "provider": "openai",
                "config": {
                    "model": 'text-embedding-3-small'
                }
            },
            type="short_term",
            path="/my_crew1/"
        )
    ),
    verbose=True,
)

```

## [​](https://docs.crewai.com/concepts/memory\#security-considerations)  Security Considerations

When configuring memory storage:

- Use environment variables for storage paths (e.g., `CREWAI_STORAGE_DIR`)
- Never hardcode sensitive information like database credentials
- Consider access permissions for storage directories
- Use relative paths when possible to maintain portability

Example using environment variables:

Copy

```python
import os
from crewai import Crew
from crewai.memory import LongTermMemory
from crewai.memory.storage import LTMSQLiteStorage

# Configure storage path using environment variable
storage_path = os.getenv("CREWAI_STORAGE_DIR", "./storage")
crew = Crew(
    memory=True,
    long_term_memory=LongTermMemory(
        storage=LTMSQLiteStorage(
            db_path="{storage_path}/memory.db".format(storage_path=storage_path)
        )
    )
)

```

## [​](https://docs.crewai.com/concepts/memory\#configuration-examples)  Configuration Examples

### [​](https://docs.crewai.com/concepts/memory\#basic-memory-configuration)  Basic Memory Configuration

Copy

```python
from crewai import Crew
from crewai.memory import LongTermMemory

# Simple memory configuration
crew = Crew(memory=True)  # Uses default storage locations

```

### [​](https://docs.crewai.com/concepts/memory\#custom-storage-configuration)  Custom Storage Configuration

Copy

```python
from crewai import Crew
from crewai.memory import LongTermMemory
from crewai.memory.storage import LTMSQLiteStorage

# Configure custom storage paths
crew = Crew(
    memory=True,
    long_term_memory=LongTermMemory(
        storage=LTMSQLiteStorage(db_path="./memory.db")
    )
)

```

## [​](https://docs.crewai.com/concepts/memory\#integrating-mem0-for-enhanced-user-memory)  Integrating Mem0 for Enhanced User Memory

[Mem0](https://mem0.ai/) is a self-improving memory layer for LLM applications, enabling personalized AI experiences.

To include user-specific memory you can get your API key [here](https://app.mem0.ai/dashboard/api-keys) and refer the [docs](https://docs.mem0.ai/platform/quickstart#4-1-create-memories) for adding user preferences.

Code

Copy

```python
import os
from crewai import Crew, Process
from mem0 import MemoryClient

# Set environment variables for Mem0
os.environ["MEM0_API_KEY"] = "m0-xx"

# Step 1: Record preferences based on past conversation or user input
client = MemoryClient()
messages = [\
    {"role": "user", "content": "Hi there! I'm planning a vacation and could use some advice."},\
    {"role": "assistant", "content": "Hello! I'd be happy to help with your vacation planning. What kind of destination do you prefer?"},\
    {"role": "user", "content": "I am more of a beach person than a mountain person."},\
    {"role": "assistant", "content": "That's interesting. Do you like hotels or Airbnb?"},\
    {"role": "user", "content": "I like Airbnb more."},\
]
client.add(messages, user_id="john")

# Step 2: Create a Crew with User Memory

crew = Crew(
    agents=[...],
    tasks=[...],
    verbose=True,
    process=Process.sequential,
    memory=True,
    memory_config={
        "provider": "mem0",
        "config": {"user_id": "john"},
    },
)

```

## [​](https://docs.crewai.com/concepts/memory\#memory-configuration-options)  Memory Configuration Options

If you want to access a specific organization and project, you can set the `org_id` and `project_id` parameters in the memory configuration.

Code

Copy

```python
from crewai import Crew

crew = Crew(
    agents=[...],
    tasks=[...],
    verbose=True,
    memory=True,
    memory_config={
        "provider": "mem0",
        "config": {"user_id": "john", "org_id": "my_org_id", "project_id": "my_project_id"},
    },
)

```

## [​](https://docs.crewai.com/concepts/memory\#additional-embedding-providers)  Additional Embedding Providers

### [​](https://docs.crewai.com/concepts/memory\#using-openai-embeddings-already-default)  Using OpenAI embeddings (already default)

Code

Copy

```python
from crewai import Crew, Agent, Task, Process

my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True,
    embedder={
        "provider": "openai",
        "config": {
            "model": 'text-embedding-3-small'
        }
    }
)

```

Alternatively, you can directly pass the OpenAIEmbeddingFunction to the embedder parameter.

Example:

Code

Copy

```python
from crewai import Crew, Agent, Task, Process
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True,
    embedder={
        "provider": "openai",
        "config": {
            "model": 'text-embedding-3-small'
        }
    }
)

```

### [​](https://docs.crewai.com/concepts/memory\#using-ollama-embeddings)  Using Ollama embeddings

Code

Copy

```python
from crewai import Crew, Agent, Task, Process

my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True,
    embedder={
        "provider": "ollama",
        "config": {
            "model": "mxbai-embed-large"
        }
    }
)

```

### [​](https://docs.crewai.com/concepts/memory\#using-google-ai-embeddings)  Using Google AI embeddings

#### [​](https://docs.crewai.com/concepts/memory\#prerequisites)  Prerequisites

Before using Google AI embeddings, ensure you have:

- Access to the Gemini API
- The necessary API keys and permissions

You will need to update your _pyproject.toml_ dependencies:

Copy

```YAML
dependencies = [\
    "google-generativeai>=0.8.4", #main version in January/2025 - crewai v.0.100.0 and crewai-tools 0.33.0\
    "crewai[tools]>=0.100.0,<1.0.0"\
]

```

Code

Copy

```python
from crewai import Crew, Agent, Task, Process

my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True,
    embedder={
        "provider": "google",
        "config": {
            "api_key": "<YOUR_API_KEY>",
            "model": "<model_name>"
        }
    }
)

```

### [​](https://docs.crewai.com/concepts/memory\#using-azure-openai-embeddings)  Using Azure OpenAI embeddings

Code

Copy

```python
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from crewai import Crew, Agent, Task, Process

my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True,
    embedder={
        "provider": "openai",
        "config": {
            "api_key": "YOUR_API_KEY",
            "api_base": "YOUR_API_BASE_PATH",
            "api_version": "YOUR_API_VERSION",
            "model_name": 'text-embedding-3-small'
        }
    }
)

```

### [​](https://docs.crewai.com/concepts/memory\#using-vertex-ai-embeddings)  Using Vertex AI embeddings

Code

Copy

```python
from chromadb.utils.embedding_functions import GoogleVertexEmbeddingFunction
from crewai import Crew, Agent, Task, Process

my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True,
    embedder={
        "provider": "vertexai",
        "config": {
            "project_id"="YOUR_PROJECT_ID",
            "region"="YOUR_REGION",
            "api_key"="YOUR_API_KEY",
            "model_name"="textembedding-gecko"
        }
    }
)

```

### [​](https://docs.crewai.com/concepts/memory\#using-cohere-embeddings)  Using Cohere embeddings

Code

Copy

```python
from crewai import Crew, Agent, Task, Process

my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True,
    embedder={
        "provider": "cohere",
        "config": {
            "api_key": "YOUR_API_KEY",
            "model": "<model_name>"
        }
    }
)

```

### [​](https://docs.crewai.com/concepts/memory\#using-voyageai-embeddings)  Using VoyageAI embeddings

Code

Copy

```python
from crewai import Crew, Agent, Task, Process

my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True,
    embedder={
        "provider": "voyageai",
        "config": {
            "api_key": "YOUR_API_KEY",
            "model": "<model_name>"
        }
    }
)

```

### [​](https://docs.crewai.com/concepts/memory\#using-huggingface-embeddings)  Using HuggingFace embeddings

Code

Copy

```python
from crewai import Crew, Agent, Task, Process

my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True,
    embedder={
        "provider": "huggingface",
        "config": {
            "api_url": "<api_url>",
        }
    }
)

```

### [​](https://docs.crewai.com/concepts/memory\#using-watson-embeddings)  Using Watson embeddings

Code

Copy

```python
from crewai import Crew, Agent, Task, Process

# Note: Ensure you have installed and imported `ibm_watsonx_ai` for Watson embeddings to work.

my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True,
    embedder={
        "provider": "watson",
        "config": {
            "model": "<model_name>",
            "api_url": "<api_url>",
            "api_key": "<YOUR_API_KEY>",
            "project_id": "<YOUR_PROJECT_ID>",
        }
    }
)

```

### [​](https://docs.crewai.com/concepts/memory\#using-amazon-bedrock-embeddings)  Using Amazon Bedrock embeddings

Code

Copy

```python
# Note: Ensure you have installed `boto3` for Bedrock embeddings to work.

import os
import boto3
from crewai import Crew, Agent, Task, Process

boto3_session = boto3.Session(
    region_name=os.environ.get("AWS_REGION_NAME"),
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
)

my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    embedder={
    "provider": "bedrock",
        "config":{
            "session": boto3_session,
            "model": "amazon.titan-embed-text-v2:0",
            "vector_dimension": 1024
        }
    }
    verbose=True
)

```

### [​](https://docs.crewai.com/concepts/memory\#adding-custom-embedding-function)  Adding Custom Embedding Function

Code

Copy

```python
from crewai import Crew, Agent, Task, Process
from chromadb import Documents, EmbeddingFunction, Embeddings

# Create a custom embedding function
class CustomEmbedder(EmbeddingFunction):
    def __call__(self, input: Documents) -> Embeddings:
        # generate embeddings
        return [1, 2, 3] # this is a dummy embedding

my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True,
    embedder={
        "provider": "custom",
        "config": {
            "embedder": CustomEmbedder()
        }
    }
)

```

### [​](https://docs.crewai.com/concepts/memory\#resetting-memory)  Resetting Memory

Copy

```shell
crewai reset-memories [OPTIONS]

```

#### [​](https://docs.crewai.com/concepts/memory\#resetting-memory-options)  Resetting Memory Options

| Option | Description | Type | Default |
| --- | --- | --- | --- |
| `-l`, `--long` | Reset LONG TERM memory. | Flag (boolean) | False |
| `-s`, `--short` | Reset SHORT TERM memory. | Flag (boolean) | False |
| `-e`, `--entities` | Reset ENTITIES memory. | Flag (boolean) | False |
| `-k`, `--kickoff-outputs` | Reset LATEST KICKOFF TASK OUTPUTS. | Flag (boolean) | False |
| `-a`, `--all` | Reset ALL memories. | Flag (boolean) | False |

## [​](https://docs.crewai.com/concepts/memory\#benefits-of-using-crewai%E2%80%99s-memory-system)  Benefits of Using CrewAI’s Memory System

- 🦾 **Adaptive Learning:** Crews become more efficient over time, adapting to new information and refining their approach to tasks.
- 🫡 **Enhanced Personalization:** Memory enables agents to remember user preferences and historical interactions, leading to personalized experiences.
- 🧠 **Improved Problem Solving:** Access to a rich memory store aids agents in making more informed decisions, drawing on past learnings and contextual insights.

## [​](https://docs.crewai.com/concepts/memory\#conclusion)  Conclusion

Integrating CrewAI’s memory system into your projects is straightforward. By leveraging the provided memory components and configurations,
you can quickly empower your agents with the ability to remember, reason, and learn from their interactions, unlocking new levels of intelligence and capability.

Was this page helpful?

YesNo

[Training](https://docs.crewai.com/concepts/training) [Planning](https://docs.crewai.com/concepts/planning)

On this page

- [Introduction to Memory Systems in CrewAI](https://docs.crewai.com/concepts/memory#introduction-to-memory-systems-in-crewai)
- [Memory System Components](https://docs.crewai.com/concepts/memory#memory-system-components)
- [How Memory Systems Empower Agents](https://docs.crewai.com/concepts/memory#how-memory-systems-empower-agents)
- [Implementing Memory in Your Crew](https://docs.crewai.com/concepts/memory#implementing-memory-in-your-crew)
- [Example: Configuring Memory for a Crew](https://docs.crewai.com/concepts/memory#example%3A-configuring-memory-for-a-crew)
- [Example: Use Custom Memory Instances e.g FAISS as the VectorDB](https://docs.crewai.com/concepts/memory#example%3A-use-custom-memory-instances-e-g-faiss-as-the-vectordb)
- [Security Considerations](https://docs.crewai.com/concepts/memory#security-considerations)
- [Configuration Examples](https://docs.crewai.com/concepts/memory#configuration-examples)
- [Basic Memory Configuration](https://docs.crewai.com/concepts/memory#basic-memory-configuration)
- [Custom Storage Configuration](https://docs.crewai.com/concepts/memory#custom-storage-configuration)
- [Integrating Mem0 for Enhanced User Memory](https://docs.crewai.com/concepts/memory#integrating-mem0-for-enhanced-user-memory)
- [Memory Configuration Options](https://docs.crewai.com/concepts/memory#memory-configuration-options)
- [Additional Embedding Providers](https://docs.crewai.com/concepts/memory#additional-embedding-providers)
- [Using OpenAI embeddings (already default)](https://docs.crewai.com/concepts/memory#using-openai-embeddings-already-default)
- [Using Ollama embeddings](https://docs.crewai.com/concepts/memory#using-ollama-embeddings)
- [Using Google AI embeddings](https://docs.crewai.com/concepts/memory#using-google-ai-embeddings)
- [Prerequisites](https://docs.crewai.com/concepts/memory#prerequisites)
- [Using Azure OpenAI embeddings](https://docs.crewai.com/concepts/memory#using-azure-openai-embeddings)
- [Using Vertex AI embeddings](https://docs.crewai.com/concepts/memory#using-vertex-ai-embeddings)
- [Using Cohere embeddings](https://docs.crewai.com/concepts/memory#using-cohere-embeddings)
- [Using VoyageAI embeddings](https://docs.crewai.com/concepts/memory#using-voyageai-embeddings)
- [Using HuggingFace embeddings](https://docs.crewai.com/concepts/memory#using-huggingface-embeddings)
- [Using Watson embeddings](https://docs.crewai.com/concepts/memory#using-watson-embeddings)
- [Using Amazon Bedrock embeddings](https://docs.crewai.com/concepts/memory#using-amazon-bedrock-embeddings)
- [Adding Custom Embedding Function](https://docs.crewai.com/concepts/memory#adding-custom-embedding-function)
- [Resetting Memory](https://docs.crewai.com/concepts/memory#resetting-memory)
- [Resetting Memory Options](https://docs.crewai.com/concepts/memory#resetting-memory-options)
- [Benefits of Using CrewAI’s Memory System](https://docs.crewai.com/concepts/memory#benefits-of-using-crewai%E2%80%99s-memory-system)
- [Conclusion](https://docs.crewai.com/concepts/memory#conclusion)

# Quickstart - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Get Started

Quickstart

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/quickstart\#build-your-first-crewai-agent)  Build your first CrewAI Agent

Let’s create a simple crew that will help us `research` and `report` on the `latest AI developments` for a given topic or subject.

Before we proceed, make sure you have `crewai` and `crewai-tools` installed.
If you haven’t installed them yet, you can do so by following the [installation guide](https://docs.crewai.com/installation).

Follow the steps below to get crewing! 🚣‍♂️

1

Create your crew

Create a new crew project by running the following command in your terminal.
This will create a new directory called `latest-ai-development` with the basic structure for your crew.

Terminal

Copy

```shell
crewai create crew latest-ai-development

```

2

Modify your \`agents.yaml\` file

You can also modify the agents as needed to fit your use case or copy and paste as is to your project.
Any variable interpolated in your `agents.yaml` and `tasks.yaml` files like `{topic}` will be replaced by the value of the variable in the `main.py` file.

agents.yaml

Copy

```yaml
# src/latest_ai_development/config/agents.yaml
researcher:
  role: >
    {topic} Senior Data Researcher
  goal: >
    Uncover cutting-edge developments in {topic}
  backstory: >
    You're a seasoned researcher with a knack for uncovering the latest
    developments in {topic}. Known for your ability to find the most relevant
    information and present it in a clear and concise manner.

reporting_analyst:
  role: >
    {topic} Reporting Analyst
  goal: >
    Create detailed reports based on {topic} data analysis and research findings
  backstory: >
    You're a meticulous analyst with a keen eye for detail. You're known for
    your ability to turn complex data into clear and concise reports, making
    it easy for others to understand and act on the information you provide.

```

3

Modify your \`tasks.yaml\` file

tasks.yaml

Copy

````yaml
# src/latest_ai_development/config/tasks.yaml
research_task:
  description: >
    Conduct a thorough research about {topic}
    Make sure you find any interesting and relevant information given
    the current year is 2025.
  expected_output: >
    A list with 10 bullet points of the most relevant information about {topic}
  agent: researcher

reporting_task:
  description: >
    Review the context you got and expand each topic into a full section for a report.
    Make sure the report is detailed and contains any and all relevant information.
  expected_output: >
    A fully fledge reports with the mains topics, each with a full section of information.
    Formatted as markdown without '```'
  agent: reporting_analyst
  output_file: report.md

````

4

Modify your \`crew.py\` file

crew.py

Copy

```python
# src/latest_ai_development/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class LatestAiDevelopmentCrew():
  """LatestAiDevelopment crew"""

  @agent
  def researcher(self) -> Agent:
    return Agent(
      config=self.agents_config['researcher'],
      verbose=True,
      tools=[SerperDevTool()]
    )

  @agent
  def reporting_analyst(self) -> Agent:
    return Agent(
      config=self.agents_config['reporting_analyst'],
      verbose=True
    )

  @task
  def research_task(self) -> Task:
    return Task(
      config=self.tasks_config['research_task'],
    )

  @task
  def reporting_task(self) -> Task:
    return Task(
      config=self.tasks_config['reporting_task'],
      output_file='output/report.md' # This is the file that will be contain the final report.
    )

  @crew
  def crew(self) -> Crew:
    """Creates the LatestAiDevelopment crew"""
    return Crew(
      agents=self.agents, # Automatically created by the @agent decorator
      tasks=self.tasks, # Automatically created by the @task decorator
      process=Process.sequential,
      verbose=True,
    )

```

5

\[Optional\] Add before and after crew functions

crew.py

Copy

```python
# src/latest_ai_development/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai_tools import SerperDevTool

@CrewBase
class LatestAiDevelopmentCrew():
  """LatestAiDevelopment crew"""

  @before_kickoff
  def before_kickoff_function(self, inputs):
    print(f"Before kickoff function with inputs: {inputs}")
    return inputs # You can return the inputs or modify them as needed

  @after_kickoff
  def after_kickoff_function(self, result):
    print(f"After kickoff function with result: {result}")
    return result # You can return the result or modify it as needed

  # ... remaining code

```

6

Feel free to pass custom inputs to your crew

For example, you can pass the `topic` input to your crew to customize the research and reporting.

main.py

Copy

```python
#!/usr/bin/env python
# src/latest_ai_development/main.py
import sys
from latest_ai_development.crew import LatestAiDevelopmentCrew

def run():
  """
  Run the crew.
  """
  inputs = {
    'topic': 'AI Agents'
  }
  LatestAiDevelopmentCrew().crew().kickoff(inputs=inputs)

```

7

Set your environment variables

Before running your crew, make sure you have the following keys set as environment variables in your `.env` file:

- An [OpenAI API key](https://platform.openai.com/account/api-keys) (or other LLM API key): `OPENAI_API_KEY=sk-...`
- A [Serper.dev](https://serper.dev/) API key: `SERPER_API_KEY=YOUR_KEY_HERE`

8

Lock and install the dependencies

Lock the dependencies and install them by using the CLI command but first, navigate to your project directory:

Terminal

Copy

```shell
cd latest-ai-development
crewai install

```

9

Run your crew

To run your crew, execute the following command in the root of your project:

Terminal

Copy

```bash
crewai run

```

10

View your final report

You should see the output in the console and the `report.md` file should be created in the root of your project with the final report.

Here’s an example of what the report should look like:

output/report.md

Copy

```markdown
# Comprehensive Report on the Rise and Impact of AI Agents in 2025

## 1. Introduction to AI Agents
In 2025, Artificial Intelligence (AI) agents are at the forefront of innovation across various industries. As intelligent systems that can perform tasks typically requiring human cognition, AI agents are paving the way for significant advancements in operational efficiency, decision-making, and overall productivity within sectors like Human Resources (HR) and Finance. This report aims to detail the rise of AI agents, their frameworks, applications, and potential implications on the workforce.

## 2. Benefits of AI Agents
AI agents bring numerous advantages that are transforming traditional work environments. Key benefits include:

- **Task Automation**: AI agents can carry out repetitive tasks such as data entry, scheduling, and payroll processing without human intervention, greatly reducing the time and resources spent on these activities.
- **Improved Efficiency**: By quickly processing large datasets and performing analyses that would take humans significantly longer, AI agents enhance operational efficiency. This allows teams to focus on strategic tasks that require higher-level thinking.
- **Enhanced Decision-Making**: AI agents can analyze trends and patterns in data, provide insights, and even suggest actions, helping stakeholders make informed decisions based on factual data rather than intuition alone.

## 3. Popular AI Agent Frameworks
Several frameworks have emerged to facilitate the development of AI agents, each with its own unique features and capabilities. Some of the most popular frameworks include:

- **Autogen**: A framework designed to streamline the development of AI agents through automation of code generation.
- **Semantic Kernel**: Focuses on natural language processing and understanding, enabling agents to comprehend user intentions better.
- **Promptflow**: Provides tools for developers to create conversational agents that can navigate complex interactions seamlessly.
- **Langchain**: Specializes in leveraging various APIs to ensure agents can access and utilize external data effectively.
- **CrewAI**: Aimed at collaborative environments, CrewAI strengthens teamwork by facilitating communication through AI-driven insights.
- **MemGPT**: Combines memory-optimized architectures with generative capabilities, allowing for more personalized interactions with users.

These frameworks empower developers to build versatile and intelligent agents that can engage users, perform advanced analytics, and execute various tasks aligned with organizational goals.

## 4. AI Agents in Human Resources
AI agents are revolutionizing HR practices by automating and optimizing key functions:

- **Recruiting**: AI agents can screen resumes, schedule interviews, and even conduct initial assessments, thus accelerating the hiring process while minimizing biases.
- **Succession Planning**: AI systems analyze employee performance data and potential, helping organizations identify future leaders and plan appropriate training.
- **Employee Engagement**: Chatbots powered by AI can facilitate feedback loops between employees and management, promoting an open culture and addressing concerns promptly.

As AI continues to evolve, HR departments leveraging these agents can realize substantial improvements in both efficiency and employee satisfaction.

## 5. AI Agents in Finance
The finance sector is seeing extensive integration of AI agents that enhance financial practices:

- **Expense Tracking**: Automated systems manage and monitor expenses, flagging anomalies and offering recommendations based on spending patterns.
- **Risk Assessment**: AI models assess credit risk and uncover potential fraud by analyzing transaction data and behavioral patterns.
- **Investment Decisions**: AI agents provide stock predictions and analytics based on historical data and current market conditions, empowering investors with informative insights.

The incorporation of AI agents into finance is fostering a more responsive and risk-aware financial landscape.

## 6. Market Trends and Investments
The growth of AI agents has attracted significant investment, especially amidst the rising popularity of chatbots and generative AI technologies. Companies and entrepreneurs are eager to explore the potential of these systems, recognizing their ability to streamline operations and improve customer engagement.

Conversely, corporations like Microsoft are taking strides to integrate AI agents into their product offerings, with enhancements to their Copilot 365 applications. This strategic move emphasizes the importance of AI literacy in the modern workplace and indicates the stabilizing of AI agents as essential business tools.

## 7. Future Predictions and Implications
Experts predict that AI agents will transform essential aspects of work life. As we look toward the future, several anticipated changes include:

- Enhanced integration of AI agents across all business functions, creating interconnected systems that leverage data from various departmental silos for comprehensive decision-making.
- Continued advancement of AI technologies, resulting in smarter, more adaptable agents capable of learning and evolving from user interactions.
- Increased regulatory scrutiny to ensure ethical use, especially concerning data privacy and employee surveillance as AI agents become more prevalent.

To stay competitive and harness the full potential of AI agents, organizations must remain vigilant about latest developments in AI technology and consider continuous learning and adaptation in their strategic planning.

## 8. Conclusion
The emergence of AI agents is undeniably reshaping the workplace landscape in 5. With their ability to automate tasks, enhance efficiency, and improve decision-making, AI agents are critical in driving operational success. Organizations must embrace and adapt to AI developments to thrive in an increasingly digital business environment.

```

### [​](https://docs.crewai.com/quickstart\#note-on-consistency-in-naming)  Note on Consistency in Naming

The names you use in your YAML files ( `agents.yaml` and `tasks.yaml`) should match the method names in your Python code.
For example, you can reference the agent for specific tasks from `tasks.yaml` file.
This naming consistency allows CrewAI to automatically link your configurations with your code; otherwise, your task won’t recognize the reference properly.

#### [​](https://docs.crewai.com/quickstart\#example-references)  Example References

Note how we use the same name for the agent in the `agents.yaml` ( `email_summarizer`) file as the method name in the `crew.py` ( `email_summarizer`) file.

agents.yaml

Copy

```yaml
email_summarizer:
    role: >
      Email Summarizer
    goal: >
      Summarize emails into a concise and clear summary
    backstory: >
      You will create a 5 bullet point summary of the report
    llm: openai/gpt-4o

```

Note how we use the same name for the agent in the `tasks.yaml` ( `email_summarizer_task`) file as the method name in the `crew.py` ( `email_summarizer_task`) file.

tasks.yaml

Copy

```yaml
email_summarizer_task:
    description: >
      Summarize the email into a 5 bullet point summary
    expected_output: >
      A 5 bullet point summary of the email
    agent: email_summarizer
    context:
      - reporting_task
      - research_task

```

Use the annotations to properly reference the agent and task in the `crew.py` file.

### [​](https://docs.crewai.com/quickstart\#annotations-include%3A)  Annotations include:

Here are examples of how to use each annotation in your CrewAI project, and when you should use them:

#### [​](https://docs.crewai.com/quickstart\#%40agent)  @agent

Used to define an agent in your crew. Use this when:

- You need to create a specialized AI agent with a specific role
- You want the agent to be automatically collected and managed by the crew
- You need to reuse the same agent configuration across multiple tasks

Copy

```python
@agent
def research_agent(self) -> Agent:
    return Agent(
        role="Research Analyst",
        goal="Conduct thorough research on given topics",
        backstory="Expert researcher with years of experience in data analysis",
        tools=[SerperDevTool()],
        verbose=True
    )

```

#### [​](https://docs.crewai.com/quickstart\#%40task)  @task

Used to define a task that can be executed by agents. Use this when:

- You need to define a specific piece of work for an agent
- You want tasks to be automatically sequenced and managed
- You need to establish dependencies between different tasks

Copy

```python
@task
def research_task(self) -> Task:
    return Task(
        description="Research the latest developments in AI technology",
        expected_output="A comprehensive report on AI advancements",
        agent=self.research_agent(),
        output_file="output/research.md"
    )

```

#### [​](https://docs.crewai.com/quickstart\#%40crew)  @crew

Used to define your crew configuration. Use this when:

- You want to automatically collect all @agent and @task definitions
- You need to specify how tasks should be processed (sequential or hierarchical)
- You want to set up crew-wide configurations

Copy

```python
@crew
def research_crew(self) -> Crew:
    return Crew(
        agents=self.agents,  # Automatically collected from @agent methods
        tasks=self.tasks,    # Automatically collected from @task methods
        process=Process.sequential,
        verbose=True
    )

```

#### [​](https://docs.crewai.com/quickstart\#%40tool)  @tool

Used to create custom tools for your agents. Use this when:

- You need to give agents specific capabilities (like web search, data analysis)
- You want to encapsulate external API calls or complex operations
- You need to share functionality across multiple agents

Copy

```python
@tool
def web_search_tool(query: str, max_results: int = 5) -> list[str]:
    """
    Search the web for information.

    Args:
        query: The search query
        max_results: Maximum number of results to return

    Returns:
        List of search results
    """
    # Implement your search logic here
    return [f"Result {i} for: {query}" for i in range(max_results)]

```

#### [​](https://docs.crewai.com/quickstart\#%40before-kickoff)  @before\_kickoff

Used to execute logic before the crew starts. Use this when:

- You need to validate or preprocess input data
- You want to set up resources or configurations before execution
- You need to perform any initialization logic

Copy

```python
@before_kickoff
def validate_inputs(self, inputs: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """Validate and preprocess inputs before the crew starts."""
    if inputs is None:
        return None

    if 'topic' not in inputs:
        raise ValueError("Topic is required")

    # Add additional context
    inputs['timestamp'] = datetime.now().isoformat()
    inputs['topic'] = inputs['topic'].strip().lower()
    return inputs

```

#### [​](https://docs.crewai.com/quickstart\#%40after-kickoff)  @after\_kickoff

Used to process results after the crew completes. Use this when:

- You need to format or transform the final output
- You want to perform cleanup operations
- You need to save or log the results in a specific way

Copy

```python
@after_kickoff
def process_results(self, result: CrewOutput) -> CrewOutput:
    """Process and format the results after the crew completes."""
    result.raw = result.raw.strip()
    result.raw = f"""
    # Research Results
    Generated on: {datetime.now().isoformat()}

    {result.raw}
    """
    return result

```

#### [​](https://docs.crewai.com/quickstart\#%40callback)  @callback

Used to handle events during crew execution. Use this when:

- You need to monitor task progress
- You want to log intermediate results
- You need to implement custom progress tracking or metrics

Copy

```python
@callback
def log_task_completion(self, task: Task, output: str):
    """Log task completion details for monitoring."""
    print(f"Task '{task.description}' completed")
    print(f"Output length: {len(output)} characters")
    print(f"Agent used: {task.agent.role}")
    print("-" * 50)

```

#### [​](https://docs.crewai.com/quickstart\#%40cache-handler)  @cache\_handler

Used to implement custom caching for task results. Use this when:

- You want to avoid redundant expensive operations
- You need to implement custom cache storage or expiration logic
- You want to persist results between runs

Copy

```python
@cache_handler
def custom_cache(self, key: str) -> Optional[str]:
    """Custom cache implementation for storing task results."""
    cache_file = f"cache/{key}.json"

    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            data = json.load(f)
            # Check if cache is still valid (e.g., not expired)
            if datetime.fromisoformat(data['timestamp']) > datetime.now() - timedelta(days=1):
                return data['result']
    return None

```

These decorators are part of the CrewAI framework and help organize your crew’s structure by automatically collecting agents, tasks, and handling various lifecycle events.
They should be used within a class decorated with `@CrewBase`.

### [​](https://docs.crewai.com/quickstart\#replay-tasks-from-latest-crew-kickoff)  Replay Tasks from Latest Crew Kickoff

CrewAI now includes a replay feature that allows you to list the tasks from the last run and replay from a specific one. To use this feature, run.

Copy

```shell
crewai replay <task_id>

```

Replace `<task_id>` with the ID of the task you want to replay.

### [​](https://docs.crewai.com/quickstart\#reset-crew-memory)  Reset Crew Memory

If you need to reset the memory of your crew before running it again, you can do so by calling the reset memory feature:

Copy

```shell
crewai reset-memories --all

```

This will clear the crew’s memory, allowing for a fresh start.

## [​](https://docs.crewai.com/quickstart\#deploying-your-project)  Deploying Your Project

The easiest way to deploy your crew is through CrewAI Enterprise, where you can deploy your crew in a few clicks.

[**Deploy on Enterprise** \\
\\
Get started with CrewAI Enterprise and deploy your crew in a production environment with just a few clicks.](http://app.crewai.com/) [**Join the Community** \\
\\
Join our open source community to discuss ideas, share your projects, and connect with other CrewAI developers.](https://community.crewai.com/)

Was this page helpful?

YesNo

[Installation](https://docs.crewai.com/installation) [Agents](https://docs.crewai.com/concepts/agents)

On this page

- [Build your first CrewAI Agent](https://docs.crewai.com/quickstart#build-your-first-crewai-agent)
- [Note on Consistency in Naming](https://docs.crewai.com/quickstart#note-on-consistency-in-naming)
- [Example References](https://docs.crewai.com/quickstart#example-references)
- [Annotations include:](https://docs.crewai.com/quickstart#annotations-include%3A)
- [@agent](https://docs.crewai.com/quickstart#%40agent)
- [@task](https://docs.crewai.com/quickstart#%40task)
- [@crew](https://docs.crewai.com/quickstart#%40crew)
- [@tool](https://docs.crewai.com/quickstart#%40tool)
- [@before\_kickoff](https://docs.crewai.com/quickstart#%40before-kickoff)
- [@after\_kickoff](https://docs.crewai.com/quickstart#%40after-kickoff)
- [@callback](https://docs.crewai.com/quickstart#%40callback)
- [@cache\_handler](https://docs.crewai.com/quickstart#%40cache-handler)
- [Replay Tasks from Latest Crew Kickoff](https://docs.crewai.com/quickstart#replay-tasks-from-latest-crew-kickoff)
- [Reset Crew Memory](https://docs.crewai.com/quickstart#reset-crew-memory)
- [Deploying Your Project](https://docs.crewai.com/quickstart#deploying-your-project)

# Scrape Website - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Scrape Website

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/scrapewebsitetool\#scrapewebsitetool)  `ScrapeWebsiteTool`

We are still working on improving tools, so there might be unexpected behavior or changes in the future.

## [​](https://docs.crewai.com/tools/scrapewebsitetool\#description)  Description

A tool designed to extract and read the content of a specified website. It is capable of handling various types of web pages by making HTTP requests and parsing the received HTML content.
This tool can be particularly useful for web scraping tasks, data collection, or extracting specific information from websites.

## [​](https://docs.crewai.com/tools/scrapewebsitetool\#installation)  Installation

Install the crewai\_tools package

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/scrapewebsitetool\#example)  Example

Copy

```python
from crewai_tools import ScrapeWebsiteTool

# To enable scrapping any website it finds during it's execution
tool = ScrapeWebsiteTool()

# Initialize the tool with the website URL,
# so the agent can only scrap the content of the specified website
tool = ScrapeWebsiteTool(website_url='https://www.example.com')

# Extract the text from the site
text = tool.run()
print(text)

```

## [​](https://docs.crewai.com/tools/scrapewebsitetool\#arguments)  Arguments

| Argument | Type | Description |
| --- | --- | --- |
| **website\_url** | `string` | **Mandatory** website URL to read the file. This is the primary input for the tool, specifying which website’s content should be scraped and read. |

Was this page helpful?

YesNo

[PG RAG Search](https://docs.crewai.com/tools/pgsearchtool) [Selenium Scraper](https://docs.crewai.com/tools/seleniumscrapingtool)

On this page

- [ScrapeWebsiteTool](https://docs.crewai.com/tools/scrapewebsitetool#scrapewebsitetool)
- [Description](https://docs.crewai.com/tools/scrapewebsitetool#description)
- [Installation](https://docs.crewai.com/tools/scrapewebsitetool#installation)
- [Example](https://docs.crewai.com/tools/scrapewebsitetool#example)
- [Arguments](https://docs.crewai.com/tools/scrapewebsitetool#arguments)

# Processes - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Processes

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/processes\#understanding-processes)  Understanding Processes

Processes orchestrate the execution of tasks by agents, akin to project management in human teams.
These processes ensure tasks are distributed and executed efficiently, in alignment with a predefined strategy.

## [​](https://docs.crewai.com/concepts/processes\#process-implementations)  Process Implementations

- **Sequential**: Executes tasks sequentially, ensuring tasks are completed in an orderly progression.
- **Hierarchical**: Organizes tasks in a managerial hierarchy, where tasks are delegated and executed based on a structured chain of command. A manager language model ( `manager_llm`) or a custom manager agent ( `manager_agent`) must be specified in the crew to enable the hierarchical process, facilitating the creation and management of tasks by the manager.
- **Consensual Process (Planned)**: Aiming for collaborative decision-making among agents on task execution, this process type introduces a democratic approach to task management within CrewAI. It is planned for future development and is not currently implemented in the codebase.

## [​](https://docs.crewai.com/concepts/processes\#the-role-of-processes-in-teamwork)  The Role of Processes in Teamwork

Processes enable individual agents to operate as a cohesive unit, streamlining their efforts to achieve common objectives with efficiency and coherence.

## [​](https://docs.crewai.com/concepts/processes\#assigning-processes-to-a-crew)  Assigning Processes to a Crew

To assign a process to a crew, specify the process type upon crew creation to set the execution strategy. For a hierarchical process, ensure to define `manager_llm` or `manager_agent` for the manager agent.

Copy

```python
from crewai import Crew, Process

# Example: Creating a crew with a sequential process
crew = Crew(
    agents=my_agents,
    tasks=my_tasks,
    process=Process.sequential
)

# Example: Creating a crew with a hierarchical process
# Ensure to provide a manager_llm or manager_agent
crew = Crew(
    agents=my_agents,
    tasks=my_tasks,
    process=Process.hierarchical,
    manager_llm="gpt-4o"
    # or
    # manager_agent=my_manager_agent
)

```

**Note:** Ensure `my_agents` and `my_tasks` are defined prior to creating a `Crew` object, and for the hierarchical process, either `manager_llm` or `manager_agent` is also required.

## [​](https://docs.crewai.com/concepts/processes\#sequential-process)  Sequential Process

This method mirrors dynamic team workflows, progressing through tasks in a thoughtful and systematic manner. Task execution follows the predefined order in the task list, with the output of one task serving as context for the next.

To customize task context, utilize the `context` parameter in the `Task` class to specify outputs that should be used as context for subsequent tasks.

## [​](https://docs.crewai.com/concepts/processes\#hierarchical-process)  Hierarchical Process

Emulates a corporate hierarchy, CrewAI allows specifying a custom manager agent or automatically creates one, requiring the specification of a manager language model ( `manager_llm`). This agent oversees task execution, including planning, delegation, and validation. Tasks are not pre-assigned; the manager allocates tasks to agents based on their capabilities, reviews outputs, and assesses task completion.

## [​](https://docs.crewai.com/concepts/processes\#process-class%3A-detailed-overview)  Process Class: Detailed Overview

The `Process` class is implemented as an enumeration ( `Enum`), ensuring type safety and restricting process values to the defined types ( `sequential`, `hierarchical`). The consensual process is planned for future inclusion, emphasizing our commitment to continuous development and innovation.

## [​](https://docs.crewai.com/concepts/processes\#conclusion)  Conclusion

The structured collaboration facilitated by processes within CrewAI is crucial for enabling systematic teamwork among agents.
This documentation has been updated to reflect the latest features, enhancements, and the planned integration of the Consensual Process, ensuring users have access to the most current and comprehensive information.

Was this page helpful?

YesNo

[LLMs](https://docs.crewai.com/concepts/llms) [Collaboration](https://docs.crewai.com/concepts/collaboration)

On this page

- [Understanding Processes](https://docs.crewai.com/concepts/processes#understanding-processes)
- [Process Implementations](https://docs.crewai.com/concepts/processes#process-implementations)
- [The Role of Processes in Teamwork](https://docs.crewai.com/concepts/processes#the-role-of-processes-in-teamwork)
- [Assigning Processes to a Crew](https://docs.crewai.com/concepts/processes#assigning-processes-to-a-crew)
- [Sequential Process](https://docs.crewai.com/concepts/processes#sequential-process)
- [Hierarchical Process](https://docs.crewai.com/concepts/processes#hierarchical-process)
- [Process Class: Detailed Overview](https://docs.crewai.com/concepts/processes#process-class%3A-detailed-overview)
- [Conclusion](https://docs.crewai.com/concepts/processes#conclusion)

# File Read - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

File Read

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/filereadtool\#filereadtool)  `FileReadTool`

We are still working on improving tools, so there might be unexpected behavior or changes in the future.

## [​](https://docs.crewai.com/tools/filereadtool\#description)  Description

The FileReadTool conceptually represents a suite of functionalities within the crewai\_tools package aimed at facilitating file reading and content retrieval.
This suite includes tools for processing batch text files, reading runtime configuration files, and importing data for analytics.
It supports a variety of text-based file formats such as `.txt`, `.csv`, `.json`, and more. Depending on the file type, the suite offers specialized functionality,
such as converting JSON content into a Python dictionary for ease of use.

## [​](https://docs.crewai.com/tools/filereadtool\#installation)  Installation

To utilize the functionalities previously attributed to the FileReadTool, install the crewai\_tools package:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/filereadtool\#usage-example)  Usage Example

To get started with the FileReadTool:

Code

Copy

```python
from crewai_tools import FileReadTool

# Initialize the tool to read any files the agents knows or lean the path for
file_read_tool = FileReadTool()

# OR

# Initialize the tool with a specific file path, so the agent can only read the content of the specified file
file_read_tool = FileReadTool(file_path='path/to/your/file.txt')

```

## [​](https://docs.crewai.com/tools/filereadtool\#arguments)  Arguments

- `file_path`: The path to the file you want to read. It accepts both absolute and relative paths. Ensure the file exists and you have the necessary permissions to access it.

Was this page helpful?

YesNo

[EXA Search Web Loader](https://docs.crewai.com/tools/exasearchtool) [File Write](https://docs.crewai.com/tools/filewritetool)

On this page

- [FileReadTool](https://docs.crewai.com/tools/filereadtool#filereadtool)
- [Description](https://docs.crewai.com/tools/filereadtool#description)
- [Installation](https://docs.crewai.com/tools/filereadtool#installation)
- [Usage Example](https://docs.crewai.com/tools/filereadtool#usage-example)
- [Arguments](https://docs.crewai.com/tools/filereadtool#arguments)

# CLI - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

CLI

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/concepts/cli\#crewai-cli-documentation)  CrewAI CLI Documentation

The CrewAI CLI provides a set of commands to interact with CrewAI, allowing you to create, train, run, and manage crews & flows.

## [​](https://docs.crewai.com/concepts/cli\#installation)  Installation

To use the CrewAI CLI, make sure you have CrewAI installed:

Terminal

Copy

```shell
pip install crewai

```

## [​](https://docs.crewai.com/concepts/cli\#basic-usage)  Basic Usage

The basic structure of a CrewAI CLI command is:

Terminal

Copy

```shell
crewai [COMMAND] [OPTIONS] [ARGUMENTS]

```

## [​](https://docs.crewai.com/concepts/cli\#available-commands)  Available Commands

### [​](https://docs.crewai.com/concepts/cli\#1-create)  1\. Create

Create a new crew or flow.

Terminal

Copy

```shell
crewai create [OPTIONS] TYPE NAME

```

- `TYPE`: Choose between “crew” or “flow”
- `NAME`: Name of the crew or flow

Example:

Terminal

Copy

```shell
crewai create crew my_new_crew
crewai create flow my_new_flow

```

### [​](https://docs.crewai.com/concepts/cli\#2-version)  2\. Version

Show the installed version of CrewAI.

Terminal

Copy

```shell
crewai version [OPTIONS]

```

- `--tools`: (Optional) Show the installed version of CrewAI tools

Example:

Terminal

Copy

```shell
crewai version
crewai version --tools

```

### [​](https://docs.crewai.com/concepts/cli\#3-train)  3\. Train

Train the crew for a specified number of iterations.

Terminal

Copy

```shell
crewai train [OPTIONS]

```

- `-n, --n_iterations INTEGER`: Number of iterations to train the crew (default: 5)
- `-f, --filename TEXT`: Path to a custom file for training (default: “trained\_agents\_data.pkl”)

Example:

Terminal

Copy

```shell
crewai train -n 10 -f my_training_data.pkl

```

### [​](https://docs.crewai.com/concepts/cli\#4-replay)  4\. Replay

Replay the crew execution from a specific task.

Terminal

Copy

```shell
crewai replay [OPTIONS]

```

- `-t, --task_id TEXT`: Replay the crew from this task ID, including all subsequent tasks

Example:

Terminal

Copy

```shell
crewai replay -t task_123456

```

### [​](https://docs.crewai.com/concepts/cli\#5-log-tasks-outputs)  5\. Log-tasks-outputs

Retrieve your latest crew.kickoff() task outputs.

Terminal

Copy

```shell
crewai log-tasks-outputs

```

### [​](https://docs.crewai.com/concepts/cli\#6-reset-memories)  6\. Reset-memories

Reset the crew memories (long, short, entity, latest\_crew\_kickoff\_outputs).

Terminal

Copy

```shell
crewai reset-memories [OPTIONS]

```

- `-l, --long`: Reset LONG TERM memory
- `-s, --short`: Reset SHORT TERM memory
- `-e, --entities`: Reset ENTITIES memory
- `-k, --kickoff-outputs`: Reset LATEST KICKOFF TASK OUTPUTS
- `-a, --all`: Reset ALL memories

Example:

Terminal

Copy

```shell
crewai reset-memories --long --short
crewai reset-memories --all

```

### [​](https://docs.crewai.com/concepts/cli\#7-test)  7\. Test

Test the crew and evaluate the results.

Terminal

Copy

```shell
crewai test [OPTIONS]

```

- `-n, --n_iterations INTEGER`: Number of iterations to test the crew (default: 3)
- `-m, --model TEXT`: LLM Model to run the tests on the Crew (default: “gpt-4o-mini”)

Example:

Terminal

Copy

```shell
crewai test -n 5 -m gpt-3.5-turbo

```

### [​](https://docs.crewai.com/concepts/cli\#8-run)  8\. Run

Run the crew.

Terminal

Copy

```shell
crewai run

```

Make sure to run these commands from the directory where your CrewAI project is set up.
Some commands may require additional configuration or setup within your project structure.

### [​](https://docs.crewai.com/concepts/cli\#9-chat)  9\. Chat

Starting in version `0.98.0`, when you run the `crewai chat` command, you start an interactive session with your crew. The AI assistant will guide you by asking for necessary inputs to execute the crew. Once all inputs are provided, the crew will execute its tasks.

After receiving the results, you can continue interacting with the assistant for further instructions or questions.

Terminal

Copy

```shell
crewai chat

```

Ensure you execute these commands from your CrewAI project’s root directory.

IMPORTANT: Set the `chat_llm` property in your `crew.py` file to enable this command.

Copy

```python
@crew
def crew(self) -> Crew:
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        process=Process.sequential,
        verbose=True,
        chat_llm="gpt-4o",  # LLM for chat orchestration
    )

```

### [​](https://docs.crewai.com/concepts/cli\#10-api-keys)  10\. API Keys

When running `crewai create crew` command, the CLI will first show you the top 5 most common LLM providers and ask you to select one.

Once you’ve selected an LLM provider, you will be prompted for API keys.

#### [​](https://docs.crewai.com/concepts/cli\#initial-api-key-providers)  Initial API key providers

The CLI will initially prompt for API keys for the following services:

- OpenAI
- Groq
- Anthropic
- Google Gemini
- SambaNova

When you select a provider, the CLI will prompt you to enter your API key.

#### [​](https://docs.crewai.com/concepts/cli\#other-options)  Other Options

If you select option 6, you will be able to select from a list of LiteLLM supported providers.

When you select a provider, the CLI will prompt you to enter the Key name and the API key.

See the following link for each provider’s key name:

- [LiteLLM Providers](https://docs.litellm.ai/docs/providers)

Was this page helpful?

YesNo

[Testing](https://docs.crewai.com/concepts/testing) [Tools](https://docs.crewai.com/concepts/tools)

On this page

- [CrewAI CLI Documentation](https://docs.crewai.com/concepts/cli#crewai-cli-documentation)
- [Installation](https://docs.crewai.com/concepts/cli#installation)
- [Basic Usage](https://docs.crewai.com/concepts/cli#basic-usage)
- [Available Commands](https://docs.crewai.com/concepts/cli#available-commands)
- [1\. Create](https://docs.crewai.com/concepts/cli#1-create)
- [2\. Version](https://docs.crewai.com/concepts/cli#2-version)
- [3\. Train](https://docs.crewai.com/concepts/cli#3-train)
- [4\. Replay](https://docs.crewai.com/concepts/cli#4-replay)
- [5\. Log-tasks-outputs](https://docs.crewai.com/concepts/cli#5-log-tasks-outputs)
- [6\. Reset-memories](https://docs.crewai.com/concepts/cli#6-reset-memories)
- [7\. Test](https://docs.crewai.com/concepts/cli#7-test)
- [8\. Run](https://docs.crewai.com/concepts/cli#8-run)
- [9\. Chat](https://docs.crewai.com/concepts/cli#9-chat)
- [10\. API Keys](https://docs.crewai.com/concepts/cli#10-api-keys)
- [Initial API key providers](https://docs.crewai.com/concepts/cli#initial-api-key-providers)
- [Other Options](https://docs.crewai.com/concepts/cli#other-options)

# Directory Read - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Directory Read

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/directoryreadtool\#directoryreadtool)  `DirectoryReadTool`

We are still working on improving tools, so there might be unexpected behavior or changes in the future.

## [​](https://docs.crewai.com/tools/directoryreadtool\#description)  Description

The DirectoryReadTool is a powerful utility designed to provide a comprehensive listing of directory contents.
It can recursively navigate through the specified directory, offering users a detailed enumeration of all files, including those within subdirectories.
This tool is crucial for tasks that require a thorough inventory of directory structures or for validating the organization of files within directories.

## [​](https://docs.crewai.com/tools/directoryreadtool\#installation)  Installation

To utilize the DirectoryReadTool in your project, install the `crewai_tools` package. If this package is not yet part of your environment, you can install it using pip with the command below:

Copy

```shell
pip install 'crewai[tools]'

```

This command installs the latest version of the `crewai_tools` package, granting access to the DirectoryReadTool among other utilities.

## [​](https://docs.crewai.com/tools/directoryreadtool\#example)  Example

Employing the DirectoryReadTool is straightforward. The following code snippet demonstrates how to set it up and use the tool to list the contents of a specified directory:

Code

Copy

```python
from crewai_tools import DirectoryReadTool

# Initialize the tool so the agent can read any directory's content
# it learns about during execution
tool = DirectoryReadTool()

# OR

# Initialize the tool with a specific directory,
# so the agent can only read the content of the specified directory
tool = DirectoryReadTool(directory='/path/to/your/directory')

```

## [​](https://docs.crewai.com/tools/directoryreadtool\#arguments)  Arguments

The following parameters can be used to customize the `DirectoryReadTool`’s behavior:

| Argument | Type | Description |
| --- | --- | --- |
| **directory** | `string` | _Optional_. An argument that specifies the path to the directory whose contents you wish to list. It accepts both absolute and relative paths, guiding the tool to the desired directory for content listing. |

Was this page helpful?

YesNo

[Directory RAG Search](https://docs.crewai.com/tools/directorysearchtool) [DOCX RAG Search](https://docs.crewai.com/tools/docxsearchtool)

On this page

- [DirectoryReadTool](https://docs.crewai.com/tools/directoryreadtool#directoryreadtool)
- [Description](https://docs.crewai.com/tools/directoryreadtool#description)
- [Installation](https://docs.crewai.com/tools/directoryreadtool#installation)
- [Example](https://docs.crewai.com/tools/directoryreadtool#example)
- [Arguments](https://docs.crewai.com/tools/directoryreadtool#arguments)

# Spider Scraper - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Spider Scraper

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/spidertool\#spidertool)  `SpiderTool`

## [​](https://docs.crewai.com/tools/spidertool\#description)  Description

[Spider](https://spider.cloud/?ref=crewai) is the [fastest](https://github.com/spider-rs/spider/blob/main/benches/BENCHMARKS.md#benchmark-results)
open source scraper and crawler that returns LLM-ready data.
It converts any website into pure HTML, markdown, metadata or text while enabling you to crawl with custom actions using AI.

## [​](https://docs.crewai.com/tools/spidertool\#installation)  Installation

To use the `SpiderTool` you need to download the [Spider SDK](https://pypi.org/project/spider-client/)
and the `crewai[tools]` SDK too:

Copy

```shell
pip install spider-client 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/spidertool\#example)  Example

This example shows you how you can use the `SpiderTool` to enable your agent to scrape and crawl websites.
The data returned from the Spider API is already LLM-ready, so no need to do any cleaning there.

Code

Copy

```python
from crewai_tools import SpiderTool

def main():
    spider_tool = SpiderTool()

    searcher = Agent(
        role="Web Research Expert",
        goal="Find related information from specific URL's",
        backstory="An expert web researcher that uses the web extremely well",
        tools=[spider_tool],
        verbose=True,
    )

    return_metadata = Task(
        description="Scrape https://spider.cloud with a limit of 1 and enable metadata",
        expected_output="Metadata and 10 word summary of spider.cloud",
        agent=searcher
    )

    crew = Crew(
        agents=[searcher],
        tasks=[\
            return_metadata,\
        ],
        verbose=2
    )

    crew.kickoff()

if __name__ == "__main__":
    main()

```

## [​](https://docs.crewai.com/tools/spidertool\#arguments)  Arguments

| Argument | Type | Description |
| --- | --- | --- |
| **api\_key** | `string` | Specifies Spider API key. If not specified, it looks for `SPIDER_API_KEY` in environment variables. |
| **params** | `object` | Optional parameters for the request. Defaults to `{"return_format": "markdown"}` to optimize content for LLMs. |
| **request** | `string` | Type of request to perform ( `http`, `chrome`, `smart`). `smart` defaults to HTTP, switching to JavaScript rendering if needed. |
| **limit** | `int` | Max pages to crawl per website. Set to `0` or omit for unlimited. |
| **depth** | `int` | Max crawl depth. Set to `0` for no limit. |
| **cache** | `bool` | Enables HTTP caching to speed up repeated runs. Default is `true`. |
| **budget** | `object` | Sets path-based limits for crawled pages, e.g., `{"*":1}` for root page only. |
| **locale** | `string` | Locale for the request, e.g., `en-US`. |
| **cookies** | `string` | HTTP cookies for the request. |
| **stealth** | `bool` | Enables stealth mode for Chrome requests to avoid detection. Default is `true`. |
| **headers** | `object` | HTTP headers as a map of key-value pairs for all requests. |
| **metadata** | `bool` | Stores metadata about pages and content, aiding AI interoperability. Defaults to `false`. |
| **viewport** | `object` | Sets Chrome viewport dimensions. Default is `800x600`. |
| **encoding** | `string` | Specifies encoding type, e.g., `UTF-8`, `SHIFT_JIS`. |
| **subdomains** | `bool` | Includes subdomains in the crawl. Default is `false`. |
| **user\_agent** | `string` | Custom HTTP user agent. Defaults to a random agent. |
| **store\_data** | `bool` | Enables data storage for the request. Overrides `storageless` when set. Default is `false`. |
| **gpt\_config** | `object` | Allows AI to generate crawl actions, with optional chaining steps via an array for `"prompt"`. |
| **fingerprint** | `bool` | Enables advanced fingerprinting for Chrome. |
| **storageless** | `bool` | Prevents all data storage, including AI embeddings. Default is `false`. |
| **readability** | `bool` | Pre-processes content for reading via [Mozilla’s readability](https://github.com/mozilla/readability). Improves content for LLMs. |
| **return\_format** | `string` | Format to return data: `markdown`, `raw`, `text`, `html2text`. Use `raw` for default page format. |
| **proxy\_enabled** | `bool` | Enables high-performance proxies to avoid network-level blocking. |
| **query\_selector** | `string` | CSS query selector for content extraction from markup. |
| **full\_resources** | `bool` | Downloads all resources linked to the website. |
| **request\_timeout** | `int` | Timeout in seconds for requests (5-60). Default is `30`. |
| **run\_in\_background** | `bool` | Runs the request in the background, useful for data storage and triggering dashboard crawls. No effect if `storageless` is set. |

Was this page helpful?

YesNo

[Selenium Scraper](https://docs.crewai.com/tools/seleniumscrapingtool) [TXT RAG Search](https://docs.crewai.com/tools/txtsearchtool)

On this page

- [SpiderTool](https://docs.crewai.com/tools/spidertool#spidertool)
- [Description](https://docs.crewai.com/tools/spidertool#description)
- [Installation](https://docs.crewai.com/tools/spidertool#installation)
- [Example](https://docs.crewai.com/tools/spidertool#example)
- [Arguments](https://docs.crewai.com/tools/spidertool#arguments)

# Agent Monitoring with MLflow - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Agent Monitoring with MLflow

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/how-to/mlflow-observability\#mlflow-overview)  MLflow Overview

[MLflow](https://mlflow.org/) is an open-source platform to assist machine learning practitioners and teams in handling the complexities of the machine learning process.

It provides a tracing feature that enhances LLM observability in your Generative AI applications by capturing detailed information about the execution of your application’s services.
Tracing provides a way to record the inputs, outputs, and metadata associated with each intermediate step of a request, enabling you to easily pinpoint the source of bugs and unexpected behaviors.

![Overview of MLflow crewAI tracing usage](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/mlflow-tracing.gif)

### [​](https://docs.crewai.com/how-to/mlflow-observability\#features)  Features

- **Tracing Dashboard**: Monitor activities of your crewAI agents with detailed dashboards that include inputs, outputs and metadata of spans.
- **Automated Tracing**: A fully automated integration with crewAI, which can be enabled by running `mlflow.crewai.autolog()`.
- **Manual Trace Instrumentation with minor efforts**: Customize trace instrumentation through MLflow’s high-level fluent APIs such as decorators, function wrappers and context managers.
- **OpenTelemetry Compatibility**: MLflow Tracing supports exporting traces to an OpenTelemetry Collector, which can then be used to export traces to various backends such as Jaeger, Zipkin, and AWS X-Ray.
- **Package and Deploy Agents**: Package and deploy your crewAI agents to an inference server with a variety of deployment targets.
- **Securely Host LLMs**: Host multiple LLM from various providers in one unified endpoint through MFflow gateway.
- **Evaluation**: Evaluate your crewAI agents with a wide range of metrics using a convenient API `mlflow.evaluate()`.

## [​](https://docs.crewai.com/how-to/mlflow-observability\#setup-instructions)  Setup Instructions

1

Install MLflow package

Copy

```shell
# The crewAI integration is available in mlflow>=2.19.0
pip install mlflow

```

2

Start MFflow tracking server

Copy

```shell
# This process is optional, but it is recommended to use MLflow tracking server for better visualization and broader features.
mlflow server

```

3

Initialize MLflow in Your Application

Add the following two lines to your application code:

Copy

```python
import mlflow

mlflow.crewai.autolog()

# Optional: Set a tracking URI and an experiment name if you have a tracking server
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("CrewAI")

```

Example Usage for tracing CrewAI Agents:

Copy

```python
from crewai import Agent, Crew, Task
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from crewai_tools import SerperDevTool, WebsiteSearchTool

from textwrap import dedent

content = "Users name is John. He is 30 years old and lives in San Francisco."
string_source = StringKnowledgeSource(
    content=content, metadata={"preference": "personal"}
)

search_tool = WebsiteSearchTool()

class TripAgents:
    def city_selection_agent(self):
        return Agent(
            role="City Selection Expert",
            goal="Select the best city based on weather, season, and prices",
            backstory="An expert in analyzing travel data to pick ideal destinations",
            tools=[\
                search_tool,\
            ],
            verbose=True,
        )

    def local_expert(self):
        return Agent(
            role="Local Expert at this city",
            goal="Provide the BEST insights about the selected city",
            backstory="""A knowledgeable local guide with extensive information
        about the city, it's attractions and customs""",
            tools=[search_tool],
            verbose=True,
        )

class TripTasks:
    def identify_task(self, agent, origin, cities, interests, range):
        return Task(
            description=dedent(
                f"""
                Analyze and select the best city for the trip based
                on specific criteria such as weather patterns, seasonal
                events, and travel costs. This task involves comparing
                multiple cities, considering factors like current weather
                conditions, upcoming cultural or seasonal events, and
                overall travel expenses.
                Your final answer must be a detailed
                report on the chosen city, and everything you found out
                about it, including the actual flight costs, weather
                forecast and attractions.

                Traveling from: {origin}
                City Options: {cities}
                Trip Date: {range}
                Traveler Interests: {interests}
            """
            ),
            agent=agent,
            expected_output="Detailed report on the chosen city including flight costs, weather forecast, and attractions",
        )

    def gather_task(self, agent, origin, interests, range):
        return Task(
            description=dedent(
                f"""
                As a local expert on this city you must compile an
                in-depth guide for someone traveling there and wanting
                to have THE BEST trip ever!
                Gather information about key attractions, local customs,
                special events, and daily activity recommendations.
                Find the best spots to go to, the kind of place only a
                local would know.
                This guide should provide a thorough overview of what
                the city has to offer, including hidden gems, cultural
                hotspots, must-visit landmarks, weather forecasts, and
                high level costs.
                The final answer must be a comprehensive city guide,
                rich in cultural insights and practical tips,
                tailored to enhance the travel experience.

                Trip Date: {range}
                Traveling from: {origin}
                Traveler Interests: {interests}
            """
            ),
            agent=agent,
            expected_output="Comprehensive city guide including hidden gems, cultural hotspots, and practical travel tips",
        )

class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.cities = cities
        self.origin = origin
        self.interests = interests
        self.date_range = date_range

    def run(self):
        agents = TripAgents()
        tasks = TripTasks()

        city_selector_agent = agents.city_selection_agent()
        local_expert_agent = agents.local_expert()

        identify_task = tasks.identify_task(
            city_selector_agent,
            self.origin,
            self.cities,
            self.interests,
            self.date_range,
        )
        gather_task = tasks.gather_task(
            local_expert_agent, self.origin, self.interests, self.date_range
        )

        crew = Crew(
            agents=[city_selector_agent, local_expert_agent],
            tasks=[identify_task, gather_task],
            verbose=True,
            memory=True,
            knowledge={
                "sources": [string_source],
                "metadata": {"preference": "personal"},
            },
        )

        result = crew.kickoff()
        return result

trip_crew = TripCrew("California", "Tokyo", "Dec 12 - Dec 20", "sports")
result = trip_crew.run()

print(result)

```

Refer to [MLflow Tracing Documentation](https://mlflow.org/docs/latest/llms/tracing/index.html) for more configurations and use cases.

4

Visualize Activities of Agents

Now traces for your crewAI agents are captured by MLflow.
Let’s visit MLflow tracking server to view the traces and get insights into your Agents.

Open `127.0.0.1:5000` on your browser to visit MLflow tracking server.

![MLflow tracing example with crewai](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/mlflow1.png)

MLflow Tracing Dashboard

Was this page helpful?

YesNo

[Agent Monitoring with Langtrace](https://docs.crewai.com/how-to/langtrace-observability) [Agent Monitoring with OpenLIT](https://docs.crewai.com/how-to/openlit-observability)

On this page

- [MLflow Overview](https://docs.crewai.com/how-to/mlflow-observability#mlflow-overview)
- [Features](https://docs.crewai.com/how-to/mlflow-observability#features)
- [Setup Instructions](https://docs.crewai.com/how-to/mlflow-observability#setup-instructions)

![MLflow tracing example with crewai](https://docs.crewai.com/how-to/mlflow-observability)

# Sequential Processes - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Sequential Processes

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/how-to/sequential-process\#introduction)  Introduction

CrewAI offers a flexible framework for executing tasks in a structured manner, supporting both sequential and hierarchical processes.
This guide outlines how to effectively implement these processes to ensure efficient task execution and project completion.

## [​](https://docs.crewai.com/how-to/sequential-process\#sequential-process-overview)  Sequential Process Overview

The sequential process ensures tasks are executed one after the other, following a linear progression.
This approach is ideal for projects requiring tasks to be completed in a specific order.

### [​](https://docs.crewai.com/how-to/sequential-process\#key-features)  Key Features

- **Linear Task Flow**: Ensures orderly progression by handling tasks in a predetermined sequence.
- **Simplicity**: Best suited for projects with clear, step-by-step tasks.
- **Easy Monitoring**: Facilitates easy tracking of task completion and project progress.

## [​](https://docs.crewai.com/how-to/sequential-process\#implementing-the-sequential-process)  Implementing the Sequential Process

To use the sequential process, assemble your crew and define tasks in the order they need to be executed.

Code

Copy

```python
from crewai import Crew, Process, Agent, Task, TaskOutput, CrewOutput

# Define your agents
researcher = Agent(
  role='Researcher',
  goal='Conduct foundational research',
  backstory='An experienced researcher with a passion for uncovering insights'
)
analyst = Agent(
  role='Data Analyst',
  goal='Analyze research findings',
  backstory='A meticulous analyst with a knack for uncovering patterns'
)
writer = Agent(
  role='Writer',
  goal='Draft the final report',
  backstory='A skilled writer with a talent for crafting compelling narratives'
)

# Define your tasks
research_task = Task(
  description='Gather relevant data...',
  agent=researcher,
  expected_output='Raw Data'
)
analysis_task = Task(
  description='Analyze the data...',
  agent=analyst,
  expected_output='Data Insights'
)
writing_task = Task(
  description='Compose the report...',
  agent=writer,
  expected_output='Final Report'
)

# Form the crew with a sequential process
report_crew = Crew(
  agents=[researcher, analyst, writer],
  tasks=[research_task, analysis_task, writing_task],
  process=Process.sequential
)

# Execute the crew
result = report_crew.kickoff()

# Accessing the type-safe output
task_output: TaskOutput = result.tasks[0].output
crew_output: CrewOutput = result.output

```

### [​](https://docs.crewai.com/how-to/sequential-process\#note%3A)  Note:

Each task in a sequential process **must** have an agent assigned. Ensure that every `Task` includes an `agent` parameter.

### [​](https://docs.crewai.com/how-to/sequential-process\#workflow-in-action)  Workflow in Action

1. **Initial Task**: In a sequential process, the first agent completes their task and signals completion.
2. **Subsequent Tasks**: Agents pick up their tasks based on the process type, with outcomes of preceding tasks or directives guiding their execution.
3. **Completion**: The process concludes once the final task is executed, leading to project completion.

## [​](https://docs.crewai.com/how-to/sequential-process\#advanced-features)  Advanced Features

### [​](https://docs.crewai.com/how-to/sequential-process\#task-delegation)  Task Delegation

In sequential processes, if an agent has `allow_delegation` set to `True`, they can delegate tasks to other agents in the crew.
This feature is automatically set up when there are multiple agents in the crew.

### [​](https://docs.crewai.com/how-to/sequential-process\#asynchronous-execution)  Asynchronous Execution

Tasks can be executed asynchronously, allowing for parallel processing when appropriate.
To create an asynchronous task, set `async_execution=True` when defining the task.

### [​](https://docs.crewai.com/how-to/sequential-process\#memory-and-caching)  Memory and Caching

CrewAI supports both memory and caching features:

- **Memory**: Enable by setting `memory=True` when creating the Crew. This allows agents to retain information across tasks.
- **Caching**: By default, caching is enabled. Set `cache=False` to disable it.

### [​](https://docs.crewai.com/how-to/sequential-process\#callbacks)  Callbacks

You can set callbacks at both the task and step level:

- `task_callback`: Executed after each task completion.
- `step_callback`: Executed after each step in an agent’s execution.

### [​](https://docs.crewai.com/how-to/sequential-process\#usage-metrics)  Usage Metrics

CrewAI tracks token usage across all tasks and agents. You can access these metrics after execution.

## [​](https://docs.crewai.com/how-to/sequential-process\#best-practices-for-sequential-processes)  Best Practices for Sequential Processes

1. **Order Matters**: Arrange tasks in a logical sequence where each task builds upon the previous one.
2. **Clear Task Descriptions**: Provide detailed descriptions for each task to guide the agents effectively.
3. **Appropriate Agent Selection**: Match agents’ skills and roles to the requirements of each task.
4. **Use Context**: Leverage the context from previous tasks to inform subsequent ones.

This updated documentation ensures that details accurately reflect the latest changes in the codebase and clearly describes how to leverage new features and configurations.
The content is kept simple and direct to ensure easy understanding.

Was this page helpful?

YesNo

[Create Custom Tools](https://docs.crewai.com/how-to/create-custom-tools) [Hierarchical Process](https://docs.crewai.com/how-to/hierarchical-process)

On this page

- [Introduction](https://docs.crewai.com/how-to/sequential-process#introduction)
- [Sequential Process Overview](https://docs.crewai.com/how-to/sequential-process#sequential-process-overview)
- [Key Features](https://docs.crewai.com/how-to/sequential-process#key-features)
- [Implementing the Sequential Process](https://docs.crewai.com/how-to/sequential-process#implementing-the-sequential-process)
- [Note:](https://docs.crewai.com/how-to/sequential-process#note%3A)
- [Workflow in Action](https://docs.crewai.com/how-to/sequential-process#workflow-in-action)
- [Advanced Features](https://docs.crewai.com/how-to/sequential-process#advanced-features)
- [Task Delegation](https://docs.crewai.com/how-to/sequential-process#task-delegation)
- [Asynchronous Execution](https://docs.crewai.com/how-to/sequential-process#asynchronous-execution)
- [Memory and Caching](https://docs.crewai.com/how-to/sequential-process#memory-and-caching)
- [Callbacks](https://docs.crewai.com/how-to/sequential-process#callbacks)
- [Usage Metrics](https://docs.crewai.com/how-to/sequential-process#usage-metrics)
- [Best Practices for Sequential Processes](https://docs.crewai.com/how-to/sequential-process#best-practices-for-sequential-processes)

# Customize Agents - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Customize Agents

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/how-to/customizing-agents\#customizable-attributes)  Customizable Attributes

Crafting an efficient CrewAI team hinges on the ability to dynamically tailor your AI agents to meet the unique requirements of any project. This section covers the foundational attributes you can customize.

### [​](https://docs.crewai.com/how-to/customizing-agents\#key-attributes-for-customization)  Key Attributes for Customization

| Attribute | Description |
| --- | --- |
| **Role** | Specifies the agent’s job within the crew, such as ‘Analyst’ or ‘Customer Service Rep’. |
| **Goal** | Defines the agent’s objectives, aligned with its role and the crew’s overarching mission. |
| **Backstory** | Provides depth to the agent’s persona, enhancing motivations and engagements within the crew. |
| **Tools** _(Optional)_ | Represents the capabilities or methods the agent uses for tasks, from simple functions to complex integrations. |
| **Cache** _(Optional)_ | Determines if the agent should use a cache for tool usage. |
| **Max RPM** | Sets the maximum requests per minute ( `max_rpm`). Can be set to `None` for unlimited requests to external services. |
| **Verbose** _(Optional)_ | Enables detailed logging for debugging and optimization, providing insights into execution processes. |
| **Allow Delegation** _(Optional)_ | Controls task delegation to other agents, default is `False`. |
| **Max Iter** _(Optional)_ | Limits the maximum number of iterations ( `max_iter`) for a task to prevent infinite loops, with a default of 25. |
| **Max Execution Time** _(Optional)_ | Sets the maximum time allowed for an agent to complete a task. |
| **System Template** _(Optional)_ | Defines the system format for the agent. |
| **Prompt Template** _(Optional)_ | Defines the prompt format for the agent. |
| **Response Template** _(Optional)_ | Defines the response format for the agent. |
| **Use System Prompt** _(Optional)_ | Controls whether the agent will use a system prompt during task execution. |
| **Respect Context Window** | Enables a sliding context window by default, maintaining context size. |
| **Max Retry Limit** | Sets the maximum number of retries ( `max_retry_limit`) for an agent in case of errors. |

## [​](https://docs.crewai.com/how-to/customizing-agents\#advanced-customization-options)  Advanced Customization Options

Beyond the basic attributes, CrewAI allows for deeper customization to enhance an agent’s behavior and capabilities significantly.

### [​](https://docs.crewai.com/how-to/customizing-agents\#language-model-customization)  Language Model Customization

Agents can be customized with specific language models ( `llm`) and function-calling language models ( `function_calling_llm`), offering advanced control over their processing and decision-making abilities.
It’s important to note that setting the `function_calling_llm` allows for overriding the default crew function-calling language model, providing a greater degree of customization.

## [​](https://docs.crewai.com/how-to/customizing-agents\#performance-and-debugging-settings)  Performance and Debugging Settings

Adjusting an agent’s performance and monitoring its operations are crucial for efficient task execution.

### [​](https://docs.crewai.com/how-to/customizing-agents\#verbose-mode-and-rpm-limit)  Verbose Mode and RPM Limit

- **Verbose Mode**: Enables detailed logging of an agent’s actions, useful for debugging and optimization. Specifically, it provides insights into agent execution processes, aiding in the optimization of performance.
- **RPM Limit**: Sets the maximum number of requests per minute ( `max_rpm`). This attribute is optional and can be set to `None` for no limit, allowing for unlimited queries to external services if needed.

### [​](https://docs.crewai.com/how-to/customizing-agents\#maximum-iterations-for-task-execution)  Maximum Iterations for Task Execution

The `max_iter` attribute allows users to define the maximum number of iterations an agent can perform for a single task, preventing infinite loops or excessively long executions.
The default value is set to 25, providing a balance between thoroughness and efficiency. Once the agent approaches this number, it will try its best to give a good answer.

## [​](https://docs.crewai.com/how-to/customizing-agents\#customizing-agents-and-tools)  Customizing Agents and Tools

Agents are customized by defining their attributes and tools during initialization. Tools are critical for an agent’s functionality, enabling them to perform specialized tasks.
The `tools` attribute should be an array of tools the agent can utilize, and it’s initialized as an empty list by default. Tools can be added or modified post-agent initialization to adapt to new requirements.

Copy

```shell
pip install 'crewai[tools]'

```

### [​](https://docs.crewai.com/how-to/customizing-agents\#example%3A-assigning-tools-to-an-agent)  Example: Assigning Tools to an Agent

Code

Copy

```python
import os
from crewai import Agent
from crewai_tools import SerperDevTool

# Set API keys for tool initialization
os.environ["OPENAI_API_KEY"] = "Your Key"
os.environ["SERPER_API_KEY"] = "Your Key"

# Initialize a search tool
search_tool = SerperDevTool()

# Initialize the agent with advanced options
agent = Agent(
  role='Research Analyst',
  goal='Provide up-to-date market analysis',
  backstory='An expert analyst with a keen eye for market trends.',
  tools=[search_tool],
  memory=True, # Enable memory
  verbose=True,
  max_rpm=None, # No limit on requests per minute
  max_iter=25, # Default value for maximum iterations
)

```

## [​](https://docs.crewai.com/how-to/customizing-agents\#delegation-and-autonomy)  Delegation and Autonomy

Controlling an agent’s ability to delegate tasks or ask questions is vital for tailoring its autonomy and collaborative dynamics within the CrewAI framework. By default,
the `allow_delegation` attribute is now set to `False`, disabling agents to seek assistance or delegate tasks as needed. This default behavior can be changed to promote collaborative problem-solving and
efficiency within the CrewAI ecosystem. If needed, delegation can be enabled to suit specific operational requirements.

### [​](https://docs.crewai.com/how-to/customizing-agents\#example%3A-disabling-delegation-for-an-agent)  Example: Disabling Delegation for an Agent

Code

Copy

```python
agent = Agent(
  role='Content Writer',
  goal='Write engaging content on market trends',
  backstory='A seasoned writer with expertise in market analysis.',
  allow_delegation=True # Enabling delegation
)

```

## [​](https://docs.crewai.com/how-to/customizing-agents\#conclusion)  Conclusion

Customizing agents in CrewAI by setting their roles, goals, backstories, and tools, alongside advanced options like language model customization, memory, performance settings, and delegation preferences,
equips a nuanced and capable AI team ready for complex challenges.

Was this page helpful?

YesNo

[Connect to any LLM](https://docs.crewai.com/how-to/llm-connections) [Using Multimodal Agents](https://docs.crewai.com/how-to/multimodal-agents)

On this page

- [Customizable Attributes](https://docs.crewai.com/how-to/customizing-agents#customizable-attributes)
- [Key Attributes for Customization](https://docs.crewai.com/how-to/customizing-agents#key-attributes-for-customization)
- [Advanced Customization Options](https://docs.crewai.com/how-to/customizing-agents#advanced-customization-options)
- [Language Model Customization](https://docs.crewai.com/how-to/customizing-agents#language-model-customization)
- [Performance and Debugging Settings](https://docs.crewai.com/how-to/customizing-agents#performance-and-debugging-settings)
- [Verbose Mode and RPM Limit](https://docs.crewai.com/how-to/customizing-agents#verbose-mode-and-rpm-limit)
- [Maximum Iterations for Task Execution](https://docs.crewai.com/how-to/customizing-agents#maximum-iterations-for-task-execution)
- [Customizing Agents and Tools](https://docs.crewai.com/how-to/customizing-agents#customizing-agents-and-tools)
- [Example: Assigning Tools to an Agent](https://docs.crewai.com/how-to/customizing-agents#example%3A-assigning-tools-to-an-agent)
- [Delegation and Autonomy](https://docs.crewai.com/how-to/customizing-agents#delegation-and-autonomy)
- [Example: Disabling Delegation for an Agent](https://docs.crewai.com/how-to/customizing-agents#example%3A-disabling-delegation-for-an-agent)
- [Conclusion](https://docs.crewai.com/how-to/customizing-agents#conclusion)

# Composio Tool - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Composio Tool

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/composiotool\#composiotoolset)  `ComposioToolSet`

## [​](https://docs.crewai.com/tools/composiotool\#description)  Description

Composio is an integration platform that allows you to connect your AI agents to 250+ tools. Key features include:

- **Enterprise-Grade Authentication**: Built-in support for OAuth, API Keys, JWT with automatic token refresh
- **Full Observability**: Detailed tool usage logs, execution timestamps, and more

## [​](https://docs.crewai.com/tools/composiotool\#installation)  Installation

To incorporate Composio tools into your project, follow the instructions below:

Copy

```shell
pip install composio-crewai
pip install crewai

```

After the installation is complete, either run `composio login` or export your composio API key as `COMPOSIO_API_KEY`. Get your Composio API key from [here](https://app.composio.dev/)

## [​](https://docs.crewai.com/tools/composiotool\#example)  Example

The following example demonstrates how to initialize the tool and execute a github action:

1. Initialize Composio toolset

Code

Copy

```python
from composio_crewai import ComposioToolSet, App, Action
from crewai import Agent, Task, Crew

toolset = ComposioToolSet()

```

2. Connect your GitHub account

CLI

Code

Copy

```shell
composio add github

```

3. Get Tools

- Retrieving all the tools from an app (not recommended for production):

Code

Copy

```python
tools = toolset.get_tools(apps=[App.GITHUB])

```

- Filtering tools based on tags:

Code

Copy

```python
tag = "users"

filtered_action_enums = toolset.find_actions_by_tags(
    App.GITHUB,
    tags=[tag],
)

tools = toolset.get_tools(actions=filtered_action_enums)

```

- Filtering tools based on use case:

Code

Copy

```python
use_case = "Star a repository on GitHub"

filtered_action_enums = toolset.find_actions_by_use_case(
    App.GITHUB, use_case=use_case, advanced=False
)

tools = toolset.get_tools(actions=filtered_action_enums)

```

Set `advanced` to True to get actions for complex use cases

- Using specific tools:

In this demo, we will use the `GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER` action from the GitHub app.

Code

Copy

```python
tools = toolset.get_tools(
    actions=[Action.GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER]
)

```

Learn more about filtering actions [here](https://docs.composio.dev/patterns/tools/use-tools/use-specific-actions)

4. Define agent

Code

Copy

```python
crewai_agent = Agent(
    role="GitHub Agent",
    goal="You take action on GitHub using GitHub APIs",
    backstory="You are AI agent that is responsible for taking actions on GitHub on behalf of users using GitHub APIs",
    verbose=True,
    tools=tools,
    llm= # pass an llm
)

```

5. Execute task

Code

Copy

```python
task = Task(
    description="Star a repo composiohq/composio on GitHub",
    agent=crewai_agent,
    expected_output="Status of the operation",
)

crew = Crew(agents=[crewai_agent], tasks=[task])

crew.kickoff()

```

- More detailed list of tools can be found [here](https://app.composio.dev/)

Was this page helpful?

YesNo

[Code Interpreter](https://docs.crewai.com/tools/codeinterpretertool) [CSV RAG Search](https://docs.crewai.com/tools/csvsearchtool)

On this page

- [ComposioToolSet](https://docs.crewai.com/tools/composiotool#composiotoolset)
- [Description](https://docs.crewai.com/tools/composiotool#description)
- [Installation](https://docs.crewai.com/tools/composiotool#installation)
- [Example](https://docs.crewai.com/tools/composiotool#example)

# Human Input on Execution - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Human Input on Execution

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/how-to/human-input-on-execution\#human-input-in-agent-execution)  Human input in agent execution

Human input is critical in several agent execution scenarios, allowing agents to request additional information or clarification when necessary.
This feature is especially useful in complex decision-making processes or when agents require more details to complete a task effectively.

## [​](https://docs.crewai.com/how-to/human-input-on-execution\#using-human-input-with-crewai)  Using human input with CrewAI

To integrate human input into agent execution, set the `human_input` flag in the task definition. When enabled, the agent prompts the user for input before delivering its final answer.
This input can provide extra context, clarify ambiguities, or validate the agent’s output.

### [​](https://docs.crewai.com/how-to/human-input-on-execution\#example%3A)  Example:

Copy

```shell
pip install crewai

```

Code

Copy

```python
import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

os.environ["SERPER_API_KEY"] = "Your Key"  # serper.dev API key
os.environ["OPENAI_API_KEY"] = "Your Key"

# Loading Tools
search_tool = SerperDevTool()

# Define your agents with roles, goals, tools, and additional attributes
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in AI and data science',
    backstory=(
        "You are a Senior Research Analyst at a leading tech think tank. "
        "Your expertise lies in identifying emerging trends and technologies in AI and data science. "
        "You have a knack for dissecting complex data and presenting actionable insights."
    ),
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)
writer = Agent(
    role='Tech Content Strategist',
    goal='Craft compelling content on tech advancements',
    backstory=(
        "You are a renowned Tech Content Strategist, known for your insightful and engaging articles on technology and innovation. "
        "With a deep understanding of the tech industry, you transform complex concepts into compelling narratives."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[search_tool],
    cache=False,  # Disable cache for this agent
)

# Create tasks for your agents
task1 = Task(
    description=(
        "Conduct a comprehensive analysis of the latest advancements in AI in 2025. "
        "Identify key trends, breakthrough technologies, and potential industry impacts. "
        "Compile your findings in a detailed report. "
        "Make sure to check with a human if the draft is good before finalizing your answer."
    ),
    expected_output='A comprehensive full report on the latest AI advancements in 2025, leave nothing out',
    agent=researcher,
    human_input=True
)

task2 = Task(
    description=(
        "Using the insights from the researcher\'s report, develop an engaging blog post that highlights the most significant AI advancements. "
        "Your post should be informative yet accessible, catering to a tech-savvy audience. "
        "Aim for a narrative that captures the essence of these breakthroughs and their implications for the future."
    ),
    expected_output='A compelling 3 paragraphs blog post formatted as markdown about the latest AI advancements in 2025',
    agent=writer,
    human_input=True
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True,
    memory=True,
    planning=True  # Enable planning feature for the crew
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)

```

Was this page helpful?

YesNo

[Force Tool Output as Result](https://docs.crewai.com/how-to/force-tool-output-as-result) [Kickoff Crew Asynchronously](https://docs.crewai.com/how-to/kickoff-async)

On this page

- [Human input in agent execution](https://docs.crewai.com/how-to/human-input-on-execution#human-input-in-agent-execution)
- [Using human input with CrewAI](https://docs.crewai.com/how-to/human-input-on-execution#using-human-input-with-crewai)
- [Example:](https://docs.crewai.com/how-to/human-input-on-execution#example%3A)

# Directory RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Directory RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/directorysearchtool\#directorysearchtool)  `DirectorySearchTool`

**Experimental**: The DirectorySearchTool is under continuous development. Features and functionalities might evolve, and unexpected behavior may occur as we refine the tool.

## [​](https://docs.crewai.com/tools/directorysearchtool\#description)  Description

The DirectorySearchTool enables semantic search within the content of specified directories, leveraging the Retrieval-Augmented Generation (RAG) methodology for efficient navigation through files. Designed for flexibility, it allows users to dynamically specify search directories at runtime or set a fixed directory during initial setup.

## [​](https://docs.crewai.com/tools/directorysearchtool\#installation)  Installation

To use the DirectorySearchTool, begin by installing the crewai\_tools package. Execute the following command in your terminal:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/directorysearchtool\#initialization-and-usage)  Initialization and Usage

Import the DirectorySearchTool from the `crewai_tools` package to start. You can initialize the tool without specifying a directory, enabling the setting of the search directory at runtime. Alternatively, the tool can be initialized with a predefined directory.

Code

Copy

```python
from crewai_tools import DirectorySearchTool

# For dynamic directory specification at runtime
tool = DirectorySearchTool()

# For fixed directory searches
tool = DirectorySearchTool(directory='/path/to/directory')

```

## [​](https://docs.crewai.com/tools/directorysearchtool\#arguments)  Arguments

- `directory`: A string argument that specifies the search directory. This is optional during initialization but required for searches if not set initially.

## [​](https://docs.crewai.com/tools/directorysearchtool\#custom-model-and-embeddings)  Custom Model and Embeddings

The DirectorySearchTool uses OpenAI for embeddings and summarization by default. Customization options for these settings include changing the model provider and configuration, enhancing flexibility for advanced users.

Code

Copy

```python
tool = DirectorySearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # Options include ollama, google, anthropic, llama2, and more
            config=dict(
                model="llama2",
                # Additional configurations here
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[DALL-E Tool](https://docs.crewai.com/tools/dalletool) [Directory Read](https://docs.crewai.com/tools/directoryreadtool)

On this page

- [DirectorySearchTool](https://docs.crewai.com/tools/directorysearchtool#directorysearchtool)
- [Description](https://docs.crewai.com/tools/directorysearchtool#description)
- [Installation](https://docs.crewai.com/tools/directorysearchtool#installation)
- [Initialization and Usage](https://docs.crewai.com/tools/directorysearchtool#initialization-and-usage)
- [Arguments](https://docs.crewai.com/tools/directorysearchtool#arguments)
- [Custom Model and Embeddings](https://docs.crewai.com/tools/directorysearchtool#custom-model-and-embeddings)

# Using LlamaIndex Tools - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Using LlamaIndex Tools

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/llamaindex-tools\#using-llamaindex-tools)  Using LlamaIndex Tools

CrewAI seamlessly integrates with LlamaIndex’s comprehensive toolkit for RAG (Retrieval-Augmented Generation) and agentic pipelines, enabling advanced search-based queries and more.

Here are the available built-in tools offered by LlamaIndex.

Code

Copy

```python
from crewai import Agent
from crewai_tools import LlamaIndexTool

# Example 1: Initialize from FunctionTool
from llama_index.core.tools import FunctionTool

your_python_function = lambda ...: ...
og_tool = FunctionTool.from_defaults(
    your_python_function,
    name="<name>",
    description='<description>'
)
tool = LlamaIndexTool.from_tool(og_tool)

# Example 2: Initialize from LlamaHub Tools
from llama_index.tools.wolfram_alpha import WolframAlphaToolSpec
wolfram_spec = WolframAlphaToolSpec(app_id="<app_id>")
wolfram_tools = wolfram_spec.to_tool_list()
tools = [LlamaIndexTool.from_tool(t) for t in wolfram_tools]

# Example 3: Initialize Tool from a LlamaIndex Query Engine
query_engine = index.as_query_engine()
query_tool = LlamaIndexTool.from_query_engine(
    query_engine,
    name="Uber 2019 10K Query Tool",
    description="Use this tool to lookup the 2019 Uber 10K Annual Report"
)

# Create and assign the tools to an agent
agent = Agent(
    role='Research Analyst',
    goal='Provide up-to-date market analysis',
    backstory='An expert analyst with a keen eye for market trends.',
    tools=[tool, *tools, query_tool]
)

# rest of the code ...

```

## [​](https://docs.crewai.com/concepts/llamaindex-tools\#steps-to-get-started)  Steps to Get Started

To effectively use the LlamaIndexTool, follow these steps:

1

Package Installation

Make sure that `crewai[tools]` package is installed in your Python environment:

Terminal

Copy

```shell
pip install 'crewai[tools]'

```

2

Install and Use LlamaIndex

Follow the LlamaIndex documentation [LlamaIndex Documentation](https://docs.llamaindex.ai/) to set up a RAG/agent pipeline.

Was this page helpful?

YesNo

[Using LangChain Tools](https://docs.crewai.com/concepts/langchain-tools) [Create Custom Tools](https://docs.crewai.com/how-to/create-custom-tools)

On this page

- [Using LlamaIndex Tools](https://docs.crewai.com/concepts/llamaindex-tools#using-llamaindex-tools)
- [Steps to Get Started](https://docs.crewai.com/concepts/llamaindex-tools#steps-to-get-started)

# DOCX RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

DOCX RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/docxsearchtool\#docxsearchtool)  `DOCXSearchTool`

We are still working on improving tools, so there might be unexpected behavior or changes in the future.

## [​](https://docs.crewai.com/tools/docxsearchtool\#description)  Description

The `DOCXSearchTool` is a RAG tool designed for semantic searching within DOCX documents.
It enables users to effectively search and extract relevant information from DOCX files using query-based searches.
This tool is invaluable for data analysis, information management, and research tasks,
streamlining the process of finding specific information within large document collections.

## [​](https://docs.crewai.com/tools/docxsearchtool\#installation)  Installation

Install the crewai\_tools package by running the following command in your terminal:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/docxsearchtool\#example)  Example

The following example demonstrates initializing the DOCXSearchTool to search within any DOCX file’s content or with a specific DOCX file path.

Code

Copy

```python
from crewai_tools import DOCXSearchTool

# Initialize the tool to search within any DOCX file's content
tool = DOCXSearchTool()

# OR

# Initialize the tool with a specific DOCX file,
# so the agent can only search the content of the specified DOCX file
tool = DOCXSearchTool(docx='path/to/your/document.docx')

```

## [​](https://docs.crewai.com/tools/docxsearchtool\#arguments)  Arguments

The following parameters can be used to customize the `DOCXSearchTool`’s behavior:

| Argument | Type | Description |
| --- | --- | --- |
| **docx** | `string` | _Optional_. An argument that specifies the path to the DOCX file you want to search. If not provided during initialization, the tool allows for later specification of any DOCX file’s content path for searching. |

## [​](https://docs.crewai.com/tools/docxsearchtool\#custom-model-and-embeddings)  Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

Code

Copy

```python
tool = DOCXSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[Directory Read](https://docs.crewai.com/tools/directoryreadtool) [EXA Search Web Loader](https://docs.crewai.com/tools/exasearchtool)

On this page

- [DOCXSearchTool](https://docs.crewai.com/tools/docxsearchtool#docxsearchtool)
- [Description](https://docs.crewai.com/tools/docxsearchtool#description)
- [Installation](https://docs.crewai.com/tools/docxsearchtool#installation)
- [Example](https://docs.crewai.com/tools/docxsearchtool#example)
- [Arguments](https://docs.crewai.com/tools/docxsearchtool#arguments)
- [Custom model and embeddings](https://docs.crewai.com/tools/docxsearchtool#custom-model-and-embeddings)

# Training - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Training

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/training\#introduction)  Introduction

The training feature in CrewAI allows you to train your AI agents using the command-line interface (CLI).
By running the command `crewai train -n <n_iterations>`, you can specify the number of iterations for the training process.

During training, CrewAI utilizes techniques to optimize the performance of your agents along with human feedback.
This helps the agents improve their understanding, decision-making, and problem-solving abilities.

### [​](https://docs.crewai.com/concepts/training\#training-your-crew-using-the-cli)  Training Your Crew Using the CLI

To use the training feature, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where your CrewAI project is located.
3. Run the following command:

Copy

```shell
crewai train -n <n_iterations> <filename> (optional)

```

Replace `<n_iterations>` with the desired number of training iterations and `<filename>` with the appropriate filename ending with `.pkl`.

### [​](https://docs.crewai.com/concepts/training\#training-your-crew-programmatically)  Training Your Crew Programmatically

To train your crew programmatically, use the following steps:

1. Define the number of iterations for training.
2. Specify the input parameters for the training process.
3. Execute the training command within a try-except block to handle potential errors.

Code

Copy

```python
n_iterations = 2
inputs = {"topic": "CrewAI Training"}
filename = "your_model.pkl"

try:
    YourCrewName_Crew().crew().train(
      n_iterations=n_iterations,
      inputs=inputs,
      filename=filename
    )

except Exception as e:
    raise Exception(f"An error occurred while training the crew: {e}")

```

### [​](https://docs.crewai.com/concepts/training\#key-points-to-note)  Key Points to Note

- **Positive Integer Requirement:** Ensure that the number of iterations ( `n_iterations`) is a positive integer. The code will raise a `ValueError` if this condition is not met.
- **Filename Requirement:** Ensure that the filename ends with `.pkl`. The code will raise a `ValueError` if this condition is not met.
- **Error Handling:** The code handles subprocess errors and unexpected exceptions, providing error messages to the user.

It is important to note that the training process may take some time, depending on the complexity of your agents and will also require your feedback on each iteration.

Once the training is complete, your agents will be equipped with enhanced capabilities and knowledge, ready to tackle complex tasks and provide more consistent and valuable insights.

Remember to regularly update and retrain your agents to ensure they stay up-to-date with the latest information and advancements in the field.

Happy training with CrewAI! 🚀

Was this page helpful?

YesNo

[Collaboration](https://docs.crewai.com/concepts/collaboration) [Memory](https://docs.crewai.com/concepts/memory)

On this page

- [Introduction](https://docs.crewai.com/concepts/training#introduction)
- [Training Your Crew Using the CLI](https://docs.crewai.com/concepts/training#training-your-crew-using-the-cli)
- [Training Your Crew Programmatically](https://docs.crewai.com/concepts/training#training-your-crew-programmatically)
- [Key Points to Note](https://docs.crewai.com/concepts/training#key-points-to-note)

# PG RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

PG RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/pgsearchtool\#pgsearchtool)  `PGSearchTool`

The PGSearchTool is currently under development. This document outlines the intended functionality and interface.
As development progresses, please be aware that some features may not be available or could change.

## [​](https://docs.crewai.com/tools/pgsearchtool\#description)  Description

The PGSearchTool is envisioned as a powerful tool for facilitating semantic searches within PostgreSQL database tables. By leveraging advanced Retrieve and Generate (RAG) technology,
it aims to provide an efficient means for querying database table content, specifically tailored for PostgreSQL databases.
The tool’s goal is to simplify the process of finding relevant data through semantic search queries, offering a valuable resource for users needing to conduct advanced queries on
extensive datasets within a PostgreSQL environment.

## [​](https://docs.crewai.com/tools/pgsearchtool\#installation)  Installation

The `crewai_tools` package, which will include the PGSearchTool upon its release, can be installed using the following command:

Copy

```shell
pip install 'crewai[tools]'

```

The PGSearchTool is not yet available in the current version of the `crewai_tools` package. This installation command will be updated once the tool is released.

## [​](https://docs.crewai.com/tools/pgsearchtool\#example-usage)  Example Usage

Below is a proposed example showcasing how to use the PGSearchTool for conducting a semantic search on a table within a PostgreSQL database:

Code

Copy

```python
from crewai_tools import PGSearchTool

# Initialize the tool with the database URI and the target table name
tool = PGSearchTool(
    db_uri='postgresql://user:password@localhost:5432/mydatabase',
    table_name='employees'
)

```

## [​](https://docs.crewai.com/tools/pgsearchtool\#arguments)  Arguments

The PGSearchTool is designed to require the following arguments for its operation:

| Argument | Type | Description |
| --- | --- | --- |
| **db\_uri** | `string` | **Mandatory**. A string representing the URI of the PostgreSQL database to be queried. This argument will be mandatory and must include the necessary authentication details and the location of the database. |
| **table\_name** | `string` | **Mandatory**. A string specifying the name of the table within the database on which the semantic search will be performed. This argument will also be mandatory. |

## [​](https://docs.crewai.com/tools/pgsearchtool\#custom-model-and-embeddings)  Custom Model and Embeddings

The tool intends to use OpenAI for both embeddings and summarization by default. Users will have the option to customize the model using a config dictionary as follows:

Code

Copy

```python
tool = PGSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[PDF RAG Search](https://docs.crewai.com/tools/pdfsearchtool) [Scrape Website](https://docs.crewai.com/tools/scrapewebsitetool)

On this page

- [PGSearchTool](https://docs.crewai.com/tools/pgsearchtool#pgsearchtool)
- [Description](https://docs.crewai.com/tools/pgsearchtool#description)
- [Installation](https://docs.crewai.com/tools/pgsearchtool#installation)
- [Example Usage](https://docs.crewai.com/tools/pgsearchtool#example-usage)
- [Arguments](https://docs.crewai.com/tools/pgsearchtool#arguments)
- [Custom Model and Embeddings](https://docs.crewai.com/tools/pgsearchtool#custom-model-and-embeddings)

# XML RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

XML RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/xmlsearchtool\#xmlsearchtool)  `XMLSearchTool`

We are still working on improving tools, so there might be unexpected behavior or changes in the future.

## [​](https://docs.crewai.com/tools/xmlsearchtool\#description)  Description

The XMLSearchTool is a cutting-edge RAG tool engineered for conducting semantic searches within XML files.
Ideal for users needing to parse and extract information from XML content efficiently, this tool supports inputting a search query and an optional XML file path.
By specifying an XML path, users can target their search more precisely to the content of that file, thereby obtaining more relevant search outcomes.

## [​](https://docs.crewai.com/tools/xmlsearchtool\#installation)  Installation

To start using the XMLSearchTool, you must first install the crewai\_tools package. This can be easily done with the following command:

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/xmlsearchtool\#example)  Example

Here are two examples demonstrating how to use the XMLSearchTool.
The first example shows searching within a specific XML file, while the second example illustrates initiating a search without predefining an XML path, providing flexibility in search scope.

Code

Copy

```python
from crewai_tools import XMLSearchTool

# Allow agents to search within any XML file's content
#as it learns about their paths during execution
tool = XMLSearchTool()

# OR

# Initialize the tool with a specific XML file path
#for exclusive search within that document
tool = XMLSearchTool(xml='path/to/your/xmlfile.xml')

```

## [​](https://docs.crewai.com/tools/xmlsearchtool\#arguments)  Arguments

- `xml`: This is the path to the XML file you wish to search.
It is an optional parameter during the tool’s initialization but must be provided either at initialization or as part of the `run` method’s arguments to execute a search.

## [​](https://docs.crewai.com/tools/xmlsearchtool\#custom-model-and-embeddings)  Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

Code

Copy

```python
tool = XMLSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[Website RAG Search](https://docs.crewai.com/tools/websitesearchtool) [YouTube Channel RAG Search](https://docs.crewai.com/tools/youtubechannelsearchtool)

On this page

- [XMLSearchTool](https://docs.crewai.com/tools/xmlsearchtool#xmlsearchtool)
- [Description](https://docs.crewai.com/tools/xmlsearchtool#description)
- [Installation](https://docs.crewai.com/tools/xmlsearchtool#installation)
- [Example](https://docs.crewai.com/tools/xmlsearchtool#example)
- [Arguments](https://docs.crewai.com/tools/xmlsearchtool#arguments)
- [Custom model and embeddings](https://docs.crewai.com/tools/xmlsearchtool#custom-model-and-embeddings)

# Website RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Website RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/websitesearchtool\#websitesearchtool)  `WebsiteSearchTool`

The WebsiteSearchTool is currently in an experimental phase. We are actively working on incorporating this tool into our suite of offerings and will update the documentation accordingly.

## [​](https://docs.crewai.com/tools/websitesearchtool\#description)  Description

The WebsiteSearchTool is designed as a concept for conducting semantic searches within the content of websites.
It aims to leverage advanced machine learning models like Retrieval-Augmented Generation (RAG) to navigate and extract information from specified URLs efficiently.
This tool intends to offer flexibility, allowing users to perform searches across any website or focus on specific websites of interest.
Please note, the current implementation details of the WebsiteSearchTool are under development, and its functionalities as described may not yet be accessible.

## [​](https://docs.crewai.com/tools/websitesearchtool\#installation)  Installation

To prepare your environment for when the WebsiteSearchTool becomes available, you can install the foundational package with:

Copy

```shell
pip install 'crewai[tools]'

```

This command installs the necessary dependencies to ensure that once the tool is fully integrated, users can start using it immediately.

## [​](https://docs.crewai.com/tools/websitesearchtool\#example-usage)  Example Usage

Below are examples of how the WebsiteSearchTool could be utilized in different scenarios. Please note, these examples are illustrative and represent planned functionality:

Code

Copy

```python
from crewai_tools import WebsiteSearchTool

# Example of initiating tool that agents can use
# to search across any discovered websites
tool = WebsiteSearchTool()

# Example of limiting the search to the content of a specific website,
# so now agents can only search within that website
tool = WebsiteSearchTool(website='https://example.com')

```

## [​](https://docs.crewai.com/tools/websitesearchtool\#arguments)  Arguments

- `website`: An optional argument intended to specify the website URL for focused searches. This argument is designed to enhance the tool’s flexibility by allowing targeted searches when necessary.

## [​](https://docs.crewai.com/tools/websitesearchtool\#customization-options)  Customization Options

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

Code

Copy

```python
tool = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[Vision Tool](https://docs.crewai.com/tools/visiontool) [XML RAG Search](https://docs.crewai.com/tools/xmlsearchtool)

On this page

- [WebsiteSearchTool](https://docs.crewai.com/tools/websitesearchtool#websitesearchtool)
- [Description](https://docs.crewai.com/tools/websitesearchtool#description)
- [Installation](https://docs.crewai.com/tools/websitesearchtool#installation)
- [Example Usage](https://docs.crewai.com/tools/websitesearchtool#example-usage)
- [Arguments](https://docs.crewai.com/tools/websitesearchtool#arguments)
- [Customization Options](https://docs.crewai.com/tools/websitesearchtool#customization-options)

# CSV RAG Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

CSV RAG Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/csvsearchtool\#csvsearchtool)  `CSVSearchTool`

**Experimental**: We are still working on improving tools, so there might be unexpected behavior or changes in the future.

## [​](https://docs.crewai.com/tools/csvsearchtool\#description)  Description

This tool is used to perform a RAG (Retrieval-Augmented Generation) search within a CSV file’s content. It allows users to semantically search for queries in the content of a specified CSV file.
This feature is particularly useful for extracting information from large CSV datasets where traditional search methods might be inefficient. All tools with “Search” in their name, including CSVSearchTool,
are RAG tools designed for searching different sources of data.

## [​](https://docs.crewai.com/tools/csvsearchtool\#installation)  Installation

Install the crewai\_tools package

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/csvsearchtool\#example)  Example

Code

Copy

```python
from crewai_tools import CSVSearchTool

# Initialize the tool with a specific CSV file.
# This setup allows the agent to only search the given CSV file.
tool = CSVSearchTool(csv='path/to/your/csvfile.csv')

# OR

# Initialize the tool without a specific CSV file.
# Agent will need to provide the CSV path at runtime.
tool = CSVSearchTool()

```

## [​](https://docs.crewai.com/tools/csvsearchtool\#arguments)  Arguments

The following parameters can be used to customize the `CSVSearchTool`’s behavior:

| Argument | Type | Description |
| --- | --- | --- |
| **csv** | `string` | _Optional_. The path to the CSV file you want to search. This is a mandatory argument if the tool was initialized without a specific CSV file; otherwise, it is optional. |

## [​](https://docs.crewai.com/tools/csvsearchtool\#custom-model-and-embeddings)  Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

Code

Copy

```python
tool = CSVSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[Composio Tool](https://docs.crewai.com/tools/composiotool) [DALL-E Tool](https://docs.crewai.com/tools/dalletool)

On this page

- [CSVSearchTool](https://docs.crewai.com/tools/csvsearchtool#csvsearchtool)
- [Description](https://docs.crewai.com/tools/csvsearchtool#description)
- [Installation](https://docs.crewai.com/tools/csvsearchtool#installation)
- [Example](https://docs.crewai.com/tools/csvsearchtool#example)
- [Arguments](https://docs.crewai.com/tools/csvsearchtool#arguments)
- [Custom model and embeddings](https://docs.crewai.com/tools/csvsearchtool#custom-model-and-embeddings)

# Planning - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Planning

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/planning\#introduction)  Introduction

The planning feature in CrewAI allows you to add planning capability to your crew. When enabled, before each Crew iteration,
all Crew information is sent to an AgentPlanner that will plan the tasks step by step, and this plan will be added to each task description.

### [​](https://docs.crewai.com/concepts/planning\#using-the-planning-feature)  Using the Planning Feature

Getting started with the planning feature is very easy, the only step required is to add `planning=True` to your Crew:

Code

Copy

```python
from crewai import Crew, Agent, Task, Process

# Assemble your crew with planning capabilities
my_crew = Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.sequential,
    planning=True,
)

```

From this point on, your crew will have planning enabled, and the tasks will be planned before each iteration.

#### [​](https://docs.crewai.com/concepts/planning\#planning-llm)  Planning LLM

Now you can define the LLM that will be used to plan the tasks.

When running the base case example, you will see something like the output below, which represents the output of the `AgentPlanner`
responsible for creating the step-by-step logic to add to the Agents’ tasks.

Code

Result

Copy

```python
from crewai import Crew, Agent, Task, Process

# Assemble your crew with planning capabilities and custom LLM
my_crew = Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.sequential,
    planning=True,
    planning_llm="gpt-4o"
)

# Run the crew
my_crew.kickoff()

```

Was this page helpful?

YesNo

[Memory](https://docs.crewai.com/concepts/memory) [Testing](https://docs.crewai.com/concepts/testing)

On this page

- [Introduction](https://docs.crewai.com/concepts/planning#introduction)
- [Using the Planning Feature](https://docs.crewai.com/concepts/planning#using-the-planning-feature)
- [Planning LLM](https://docs.crewai.com/concepts/planning#planning-llm)

# Force Tool Output as Result - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Force Tool Output as Result

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/how-to/force-tool-output-as-result\#introduction)  Introduction

In CrewAI, you can force the output of a tool as the result of an agent’s task.
This feature is useful when you want to ensure that the tool output is captured and returned as the task result, avoiding any agent modification during the task execution.

## [​](https://docs.crewai.com/how-to/force-tool-output-as-result\#forcing-tool-output-as-result)  Forcing Tool Output as Result

To force the tool output as the result of an agent’s task, you need to set the `result_as_answer` parameter to `True` when adding a tool to the agent.
This parameter ensures that the tool output is captured and returned as the task result, without any modifications by the agent.

Here’s an example of how to force the tool output as the result of an agent’s task:

Code

Copy

```python
from crewai.agent import Agent
from my_tool import MyCustomTool

# Create a coding agent with the custom tool
coding_agent = Agent(
        role="Data Scientist",
        goal="Produce amazing reports on AI",
        backstory="You work with data and AI",
        tools=[MyCustomTool(result_as_answer=True)],
    )

# Assuming the tool's execution and result population occurs within the system
task_result = coding_agent.execute_task(task)

```

## [​](https://docs.crewai.com/how-to/force-tool-output-as-result\#workflow-in-action)  Workflow in Action

1

Task Execution

The agent executes the task using the tool provided.

2

Tool Output

The tool generates the output, which is captured as the task result.

3

Agent Interaction

The agent may reflect and take learnings from the tool but the output is not modified.

4

Result Return

The tool output is returned as the task result without any modifications.

Was this page helpful?

YesNo

[Coding Agents](https://docs.crewai.com/how-to/coding-agents) [Human Input on Execution](https://docs.crewai.com/how-to/human-input-on-execution)

On this page

- [Introduction](https://docs.crewai.com/how-to/force-tool-output-as-result#introduction)
- [Forcing Tool Output as Result](https://docs.crewai.com/how-to/force-tool-output-as-result#forcing-tool-output-as-result)
- [Workflow in Action](https://docs.crewai.com/how-to/force-tool-output-as-result#workflow-in-action)

# Kickoff Crew for Each - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Kickoff Crew for Each

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/how-to/kickoff-for-each\#introduction)  Introduction

CrewAI provides the ability to kickoff a crew for each item in a list, allowing you to execute the crew for each item in the list.
This feature is particularly useful when you need to perform the same set of tasks for multiple items.

## [​](https://docs.crewai.com/how-to/kickoff-for-each\#kicking-off-a-crew-for-each-item)  Kicking Off a Crew for Each Item

To kickoff a crew for each item in a list, use the `kickoff_for_each()` method.
This method executes the crew for each item in the list, allowing you to process multiple items efficiently.

Here’s an example of how to kickoff a crew for each item in a list:

Code

Copy

```python
from crewai import Crew, Agent, Task

# Create an agent with code execution enabled
coding_agent = Agent(
    role="Python Data Analyst",
    goal="Analyze data and provide insights using Python",
    backstory="You are an experienced data analyst with strong Python skills.",
    allow_code_execution=True
)

# Create a task that requires code execution
data_analysis_task = Task(
    description="Analyze the given dataset and calculate the average age of participants. Ages: {ages}",
    agent=coding_agent,
    expected_output="The average age calculated from the dataset"
)

# Create a crew and add the task
analysis_crew = Crew(
    agents=[coding_agent],
    tasks=[data_analysis_task],
    verbose=True,
    memory=False,
    respect_context_window=True  # enable by default
)

datasets = [\
  { "ages": [25, 30, 35, 40, 45] },\
  { "ages": [20, 25, 30, 35, 40] },\
  { "ages": [30, 35, 40, 45, 50] }\
]

# Execute the crew
result = analysis_crew.kickoff_for_each(inputs=datasets)

```

Was this page helpful?

YesNo

[Kickoff Crew Asynchronously](https://docs.crewai.com/how-to/kickoff-async) [Replay Tasks from Latest Crew Kickoff](https://docs.crewai.com/how-to/replay-tasks-from-latest-crew-kickoff)

On this page

- [Introduction](https://docs.crewai.com/how-to/kickoff-for-each#introduction)
- [Kicking Off a Crew for Each Item](https://docs.crewai.com/how-to/kickoff-for-each#kicking-off-a-crew-for-each-item)

# Kickoff Crew Asynchronously - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Kickoff Crew Asynchronously

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/how-to/kickoff-async\#introduction)  Introduction

CrewAI provides the ability to kickoff a crew asynchronously, allowing you to start the crew execution in a non-blocking manner.
This feature is particularly useful when you want to run multiple crews concurrently or when you need to perform other tasks while the crew is executing.

## [​](https://docs.crewai.com/how-to/kickoff-async\#asynchronous-crew-execution)  Asynchronous Crew Execution

To kickoff a crew asynchronously, use the `kickoff_async()` method. This method initiates the crew execution in a separate thread, allowing the main thread to continue executing other tasks.

### [​](https://docs.crewai.com/how-to/kickoff-async\#method-signature)  Method Signature

Code

Copy

```python
def kickoff_async(self, inputs: dict) -> CrewOutput:

```

### [​](https://docs.crewai.com/how-to/kickoff-async\#parameters)  Parameters

- `inputs` (dict): A dictionary containing the input data required for the tasks.

### [​](https://docs.crewai.com/how-to/kickoff-async\#returns)  Returns

- `CrewOutput`: An object representing the result of the crew execution.

## [​](https://docs.crewai.com/how-to/kickoff-async\#potential-use-cases)  Potential Use Cases

- **Parallel Content Generation**: Kickoff multiple independent crews asynchronously, each responsible for generating content on different topics. For example, one crew might research and draft an article on AI trends, while another crew generates social media posts about a new product launch. Each crew operates independently, allowing content production to scale efficiently.

- **Concurrent Market Research Tasks**: Launch multiple crews asynchronously to conduct market research in parallel. One crew might analyze industry trends, while another examines competitor strategies, and yet another evaluates consumer sentiment. Each crew independently completes its task, enabling faster and more comprehensive insights.

- **Independent Travel Planning Modules**: Execute separate crews to independently plan different aspects of a trip. One crew might handle flight options, another handles accommodation, and a third plans activities. Each crew works asynchronously, allowing various components of the trip to be planned simultaneously and independently for faster results.


## [​](https://docs.crewai.com/how-to/kickoff-async\#example%3A-single-asynchronous-crew-execution)  Example: Single Asynchronous Crew Execution

Here’s an example of how to kickoff a crew asynchronously using asyncio and awaiting the result:

Code

Copy

```python
import asyncio
from crewai import Crew, Agent, Task

# Create an agent with code execution enabled
coding_agent = Agent(
    role="Python Data Analyst",
    goal="Analyze data and provide insights using Python",
    backstory="You are an experienced data analyst with strong Python skills.",
    allow_code_execution=True
)

# Create a task that requires code execution
data_analysis_task = Task(
    description="Analyze the given dataset and calculate the average age of participants. Ages: {ages}",
    agent=coding_agent
)

# Create a crew and add the task
analysis_crew = Crew(
    agents=[coding_agent],
    tasks=[data_analysis_task]
)

# Async function to kickoff the crew asynchronously
async def async_crew_execution():
    result = await analysis_crew.kickoff_async(inputs={"ages": [25, 30, 35, 40, 45]})
    print("Crew Result:", result)

# Run the async function
asyncio.run(async_crew_execution())

```

## [​](https://docs.crewai.com/how-to/kickoff-async\#example%3A-multiple-asynchronous-crew-executions)  Example: Multiple Asynchronous Crew Executions

In this example, we’ll show how to kickoff multiple crews asynchronously and wait for all of them to complete using `asyncio.gather()`:

Code

Copy

```python
import asyncio
from crewai import Crew, Agent, Task

# Create an agent with code execution enabled
coding_agent = Agent(
    role="Python Data Analyst",
    goal="Analyze data and provide insights using Python",
    backstory="You are an experienced data analyst with strong Python skills.",
    allow_code_execution=True
)

# Create tasks that require code execution
task_1 = Task(
    description="Analyze the first dataset and calculate the average age of participants. Ages: {ages}",
    agent=coding_agent
)

task_2 = Task(
    description="Analyze the second dataset and calculate the average age of participants. Ages: {ages}",
    agent=coding_agent
)

# Create two crews and add tasks
crew_1 = Crew(agents=[coding_agent], tasks=[task_1])
crew_2 = Crew(agents=[coding_agent], tasks=[task_2])

# Async function to kickoff multiple crews asynchronously and wait for all to finish
async def async_multiple_crews():
    result_1 = crew_1.kickoff_async(inputs={"ages": [25, 30, 35, 40, 45]})
    result_2 = crew_2.kickoff_async(inputs={"ages": [20, 22, 24, 28, 30]})

    # Wait for both crews to finish
    results = await asyncio.gather(result_1, result_2)

    for i, result in enumerate(results, 1):
        print(f"Crew {i} Result:", result)

# Run the async function
asyncio.run(async_multiple_crews())

```

Was this page helpful?

YesNo

[Human Input on Execution](https://docs.crewai.com/how-to/human-input-on-execution) [Kickoff Crew for Each](https://docs.crewai.com/how-to/kickoff-for-each)

On this page

- [Introduction](https://docs.crewai.com/how-to/kickoff-async#introduction)
- [Asynchronous Crew Execution](https://docs.crewai.com/how-to/kickoff-async#asynchronous-crew-execution)
- [Method Signature](https://docs.crewai.com/how-to/kickoff-async#method-signature)
- [Parameters](https://docs.crewai.com/how-to/kickoff-async#parameters)
- [Returns](https://docs.crewai.com/how-to/kickoff-async#returns)
- [Potential Use Cases](https://docs.crewai.com/how-to/kickoff-async#potential-use-cases)
- [Example: Single Asynchronous Crew Execution](https://docs.crewai.com/how-to/kickoff-async#example%3A-single-asynchronous-crew-execution)
- [Example: Multiple Asynchronous Crew Executions](https://docs.crewai.com/how-to/kickoff-async#example%3A-multiple-asynchronous-crew-executions)

# Github Search - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Github Search

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/githubsearchtool\#githubsearchtool)  `GithubSearchTool`

We are still working on improving tools, so there might be unexpected behavior or changes in the future.

## [​](https://docs.crewai.com/tools/githubsearchtool\#description)  Description

The GithubSearchTool is a Retrieval-Augmented Generation (RAG) tool specifically designed for conducting semantic searches within GitHub repositories. Utilizing advanced semantic search capabilities, it sifts through code, pull requests, issues, and repositories, making it an essential tool for developers, researchers, or anyone in need of precise information from GitHub.

## [​](https://docs.crewai.com/tools/githubsearchtool\#installation)  Installation

To use the GithubSearchTool, first ensure the crewai\_tools package is installed in your Python environment:

Copy

```shell
pip install 'crewai[tools]'

```

This command installs the necessary package to run the GithubSearchTool along with any other tools included in the crewai\_tools package.

## [​](https://docs.crewai.com/tools/githubsearchtool\#example)  Example

Here’s how you can use the GithubSearchTool to perform semantic searches within a GitHub repository:

Code

Copy

```python
from crewai_tools import GithubSearchTool

# Initialize the tool for semantic searches within a specific GitHub repository
tool = GithubSearchTool(
	github_repo='https://github.com/example/repo',
	gh_token='your_github_personal_access_token',
	content_types=['code', 'issue'] # Options: code, repo, pr, issue
)

# OR

# Initialize the tool for semantic searches within a specific GitHub repository, so the agent can search any repository if it learns about during its execution
tool = GithubSearchTool(
	gh_token='your_github_personal_access_token',
	content_types=['code', 'issue'] # Options: code, repo, pr, issue
)

```

## [​](https://docs.crewai.com/tools/githubsearchtool\#arguments)  Arguments

- `github_repo` : The URL of the GitHub repository where the search will be conducted. This is a mandatory field and specifies the target repository for your search.
- `gh_token` : Your GitHub Personal Access Token (PAT) required for authentication. You can create one in your GitHub account settings under Developer Settings > Personal Access Tokens.
- `content_types` : Specifies the types of content to include in your search. You must provide a list of content types from the following options: `code` for searching within the code,
`repo` for searching within the repository’s general information, `pr` for searching within pull requests, and `issue` for searching within issues.
This field is mandatory and allows tailoring the search to specific content types within the GitHub repository.

## [​](https://docs.crewai.com/tools/githubsearchtool\#custom-model-and-embeddings)  Custom model and embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

Code

Copy

```python
tool = GithubSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

```

Was this page helpful?

YesNo

[Firecrawl Search](https://docs.crewai.com/tools/firecrawlsearchtool) [Google Serper Search](https://docs.crewai.com/tools/serperdevtool)

On this page

- [GithubSearchTool](https://docs.crewai.com/tools/githubsearchtool#githubsearchtool)
- [Description](https://docs.crewai.com/tools/githubsearchtool#description)
- [Installation](https://docs.crewai.com/tools/githubsearchtool#installation)
- [Example](https://docs.crewai.com/tools/githubsearchtool#example)
- [Arguments](https://docs.crewai.com/tools/githubsearchtool#arguments)
- [Custom model and embeddings](https://docs.crewai.com/tools/githubsearchtool#custom-model-and-embeddings)

# Tasks - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Tasks

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/tasks\#overview-of-a-task)  Overview of a Task

In the CrewAI framework, a `Task` is a specific assignment completed by an `Agent`.

Tasks provide all necessary details for execution, such as a description, the agent responsible, required tools, and more, facilitating a wide range of action complexities.

Tasks within CrewAI can be collaborative, requiring multiple agents to work together. This is managed through the task properties and orchestrated by the Crew’s process, enhancing teamwork and efficiency.

### [​](https://docs.crewai.com/concepts/tasks\#task-execution-flow)  Task Execution Flow

Tasks can be executed in two ways:

- **Sequential**: Tasks are executed in the order they are defined
- **Hierarchical**: Tasks are assigned to agents based on their roles and expertise

The execution flow is defined when creating the crew:

Code

Copy

```python
crew = Crew(
    agents=[agent1, agent2],
    tasks=[task1, task2],
    process=Process.sequential  # or Process.hierarchical
)

```

## [​](https://docs.crewai.com/concepts/tasks\#task-attributes)  Task Attributes

| Attribute | Parameters | Type | Description |
| --- | --- | --- | --- |
| **Description** | `description` | `str` | A clear, concise statement of what the task entails. |
| **Expected Output** | `expected_output` | `str` | A detailed description of what the task’s completion looks like. |
| **Name** _(optional)_ | `name` | `Optional[str]` | A name identifier for the task. |
| **Agent** _(optional)_ | `agent` | `Optional[BaseAgent]` | The agent responsible for executing the task. |
| **Tools** _(optional)_ | `tools` | `List[BaseTool]` | The tools/resources the agent is limited to use for this task. |
| **Context** _(optional)_ | `context` | `Optional[List["Task"]]` | Other tasks whose outputs will be used as context for this task. |
| **Async Execution** _(optional)_ | `async_execution` | `Optional[bool]` | Whether the task should be executed asynchronously. Defaults to False. |
| **Human Input** _(optional)_ | `human_input` | `Optional[bool]` | Whether the task should have a human review the final answer of the agent. Defaults to False. |
| **Config** _(optional)_ | `config` | `Optional[Dict[str, Any]]` | Task-specific configuration parameters. |
| **Output File** _(optional)_ | `output_file` | `Optional[str]` | File path for storing the task output. |
| **Output JSON** _(optional)_ | `output_json` | `Optional[Type[BaseModel]]` | A Pydantic model to structure the JSON output. |
| **Output Pydantic** _(optional)_ | `output_pydantic` | `Optional[Type[BaseModel]]` | A Pydantic model for task output. |
| **Callback** _(optional)_ | `callback` | `Optional[Any]` | Function/object to be executed after task completion. |

## [​](https://docs.crewai.com/concepts/tasks\#creating-tasks)  Creating Tasks

There are two ways to create tasks in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.

### [​](https://docs.crewai.com/concepts/tasks\#yaml-configuration-recommended)  YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define tasks. We strongly recommend using this approach to define tasks in your CrewAI projects.

After creating your CrewAI project as outlined in the [Installation](https://docs.crewai.com/installation) section, navigate to the `src/latest_ai_development/config/tasks.yaml` file and modify the template to match your specific task requirements.

Variables in your YAML files (like `{topic}`) will be replaced with values from your inputs when running the crew:

Code

Copy

```python
crew.kickoff(inputs={'topic': 'AI Agents'})

```

Here’s an example of how to configure tasks using YAML:

tasks.yaml

Copy

````yaml
research_task:
  description: >
    Conduct a thorough research about {topic}
    Make sure you find any interesting and relevant information given
    the current year is 2025.
  expected_output: >
    A list with 10 bullet points of the most relevant information about {topic}
  agent: researcher

reporting_task:
  description: >
    Review the context you got and expand each topic into a full section for a report.
    Make sure the report is detailed and contains any and all relevant information.
  expected_output: >
    A fully fledge reports with the mains topics, each with a full section of information.
    Formatted as markdown without '```'
  agent: reporting_analyst
  output_file: report.md

````

To use this YAML configuration in your code, create a crew class that inherits from `CrewBase`:

crew.py

Copy

```python
# src/latest_ai_development/crew.py

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class LatestAiDevelopmentCrew():
  """LatestAiDevelopment crew"""

  @agent
  def researcher(self) -> Agent:
    return Agent(
      config=self.agents_config['researcher'],
      verbose=True,
      tools=[SerperDevTool()]
    )

  @agent
  def reporting_analyst(self) -> Agent:
    return Agent(
      config=self.agents_config['reporting_analyst'],
      verbose=True
    )

  @task
  def research_task(self) -> Task:
    return Task(
      config=self.tasks_config['research_task']
    )

  @task
  def reporting_task(self) -> Task:
    return Task(
      config=self.tasks_config['reporting_task']
    )

  @crew
  def crew(self) -> Crew:
    return Crew(
      agents=[\
        self.researcher(),\
        self.reporting_analyst()\
      ],
      tasks=[\
        self.research_task(),\
        self.reporting_task()\
      ],
      process=Process.sequential
    )

```

The names you use in your YAML files ( `agents.yaml` and `tasks.yaml`) should match the method names in your Python code.

### [​](https://docs.crewai.com/concepts/tasks\#direct-code-definition-alternative)  Direct Code Definition (Alternative)

Alternatively, you can define tasks directly in your code without using YAML configuration:

task.py

Copy

````python
from crewai import Task

research_task = Task(
    description="""
        Conduct a thorough research about AI Agents.
        Make sure you find any interesting and relevant information given
        the current year is 2025.
    """,
    expected_output="""
        A list with 10 bullet points of the most relevant information about AI Agents
    """,
    agent=researcher
)

reporting_task = Task(
    description="""
        Review the context you got and expand each topic into a full section for a report.
        Make sure the report is detailed and contains any and all relevant information.
    """,
    expected_output="""
        A fully fledge reports with the mains topics, each with a full section of information.
        Formatted as markdown without '```'
    """,
    agent=reporting_analyst,
    output_file="report.md"
)

````

Directly specify an `agent` for assignment or let the `hierarchical` CrewAI’s process decide based on roles, availability, etc.

## [​](https://docs.crewai.com/concepts/tasks\#task-output)  Task Output

Understanding task outputs is crucial for building effective AI workflows. CrewAI provides a structured way to handle task results through the `TaskOutput` class, which supports multiple output formats and can be easily passed between tasks.

The output of a task in CrewAI framework is encapsulated within the `TaskOutput` class. This class provides a structured way to access results of a task, including various formats such as raw output, JSON, and Pydantic models.

By default, the `TaskOutput` will only include the `raw` output. A `TaskOutput` will only include the `pydantic` or `json_dict` output if the original `Task` object was configured with `output_pydantic` or `output_json`, respectively.

### [​](https://docs.crewai.com/concepts/tasks\#task-output-attributes)  Task Output Attributes

| Attribute | Parameters | Type | Description |
| --- | --- | --- | --- |
| **Description** | `description` | `str` | Description of the task. |
| **Summary** | `summary` | `Optional[str]` | Summary of the task, auto-generated from the first 10 words of the description. |
| **Raw** | `raw` | `str` | The raw output of the task. This is the default format for the output. |
| **Pydantic** | `pydantic` | `Optional[BaseModel]` | A Pydantic model object representing the structured output of the task. |
| **JSON Dict** | `json_dict` | `Optional[Dict[str, Any]]` | A dictionary representing the JSON output of the task. |
| **Agent** | `agent` | `str` | The agent that executed the task. |
| **Output Format** | `output_format` | `OutputFormat` | The format of the task output, with options including RAW, JSON, and Pydantic. The default is RAW. |

### [​](https://docs.crewai.com/concepts/tasks\#task-methods-and-properties)  Task Methods and Properties

| Method/Property | Description |
| --- | --- |
| **json** | Returns the JSON string representation of the task output if the output format is JSON. |
| **to\_dict** | Converts the JSON and Pydantic outputs to a dictionary. |
| **str** | Returns the string representation of the task output, prioritizing Pydantic, then JSON, then raw. |

### [​](https://docs.crewai.com/concepts/tasks\#accessing-task-outputs)  Accessing Task Outputs

Once a task has been executed, its output can be accessed through the `output` attribute of the `Task` object. The `TaskOutput` class provides various ways to interact with and present this output.

#### [​](https://docs.crewai.com/concepts/tasks\#example)  Example

Code

Copy

```python
# Example task
task = Task(
    description='Find and summarize the latest AI news',
    expected_output='A bullet list summary of the top 5 most important AI news',
    agent=research_agent,
    tools=[search_tool]
)

# Execute the crew
crew = Crew(
    agents=[research_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()

# Accessing the task output
task_output = task.output

print(f"Task Description: {task_output.description}")
print(f"Task Summary: {task_output.summary}")
print(f"Raw Output: {task_output.raw}")
if task_output.json_dict:
    print(f"JSON Output: {json.dumps(task_output.json_dict, indent=2)}")
if task_output.pydantic:
    print(f"Pydantic Output: {task_output.pydantic}")

```

## [​](https://docs.crewai.com/concepts/tasks\#task-dependencies-and-context)  Task Dependencies and Context

Tasks can depend on the output of other tasks using the `context` attribute. For example:

Code

Copy

```python
research_task = Task(
    description="Research the latest developments in AI",
    expected_output="A list of recent AI developments",
    agent=researcher
)

analysis_task = Task(
    description="Analyze the research findings and identify key trends",
    expected_output="Analysis report of AI trends",
    agent=analyst,
    context=[research_task]  # This task will wait for research_task to complete
)

```

## [​](https://docs.crewai.com/concepts/tasks\#task-guardrails)  Task Guardrails

Task guardrails provide a way to validate and transform task outputs before they
are passed to the next task. This feature helps ensure data quality and provides
feedback to agents when their output doesn’t meet specific criteria.

### [​](https://docs.crewai.com/concepts/tasks\#using-task-guardrails)  Using Task Guardrails

To add a guardrail to a task, provide a validation function through the `guardrail` parameter:

Code

Copy

```python
from typing import Tuple, Union, Dict, Any

def validate_blog_content(result: str) -> Tuple[bool, Union[Dict[str, Any], str]]:
    """Validate blog content meets requirements."""
    try:
        # Check word count
        word_count = len(result.split())
        if word_count > 200:
            return (False, {
                "error": "Blog content exceeds 200 words",
                "code": "WORD_COUNT_ERROR",
                "context": {"word_count": word_count}
            })

        # Additional validation logic here
        return (True, result.strip())
    except Exception as e:
        return (False, {
            "error": "Unexpected error during validation",
            "code": "SYSTEM_ERROR"
        })

blog_task = Task(
    description="Write a blog post about AI",
    expected_output="A blog post under 200 words",
    agent=blog_agent,
    guardrail=validate_blog_content  # Add the guardrail function
)

```

### [​](https://docs.crewai.com/concepts/tasks\#guardrail-function-requirements)  Guardrail Function Requirements

1. **Function Signature**:
   - Must accept exactly one parameter (the task output)
   - Should return a tuple of `(bool, Any)`
   - Type hints are recommended but optional
2. **Return Values**:
   - Success: Return `(True, validated_result)`
   - Failure: Return `(False, error_details)`

### [​](https://docs.crewai.com/concepts/tasks\#error-handling-best-practices)  Error Handling Best Practices

1. **Structured Error Responses**:

Code

Copy

```python
def validate_with_context(result: str) -> Tuple[bool, Union[Dict[str, Any], str]]:
    try:
        # Main validation logic
        validated_data = perform_validation(result)
        return (True, validated_data)
    except ValidationError as e:
        return (False, {
            "error": str(e),
            "code": "VALIDATION_ERROR",
            "context": {"input": result}
        })
    except Exception as e:
        return (False, {
            "error": "Unexpected error",
            "code": "SYSTEM_ERROR"
        })

```

2. **Error Categories**:
   - Use specific error codes
   - Include relevant context
   - Provide actionable feedback
3. **Validation Chain**:


Code

Copy

```python
from typing import Any, Dict, List, Tuple, Union

def complex_validation(result: str) -> Tuple[bool, Union[str, Dict[str, Any]]]:
    """Chain multiple validation steps."""
    # Step 1: Basic validation
    if not result:
        return (False, {"error": "Empty result", "code": "EMPTY_INPUT"})

    # Step 2: Content validation
    try:
        validated = validate_content(result)
        if not validated:
            return (False, {"error": "Invalid content", "code": "CONTENT_ERROR"})

        # Step 3: Format validation
        formatted = format_output(validated)
        return (True, formatted)
    except Exception as e:
        return (False, {
            "error": str(e),
            "code": "VALIDATION_ERROR",
            "context": {"step": "content_validation"}
        })

```

### [​](https://docs.crewai.com/concepts/tasks\#handling-guardrail-results)  Handling Guardrail Results

When a guardrail returns `(False, error)`:

1. The error is sent back to the agent
2. The agent attempts to fix the issue
3. The process repeats until:
   - The guardrail returns `(True, result)`
   - Maximum retries are reached

Example with retry handling:

Code

Copy

```python
from typing import Optional, Tuple, Union

def validate_json_output(result: str) -> Tuple[bool, Union[Dict[str, Any], str]]:
    """Validate and parse JSON output."""
    try:
        # Try to parse as JSON
        data = json.loads(result)
        return (True, data)
    except json.JSONDecodeError as e:
        return (False, {
            "error": "Invalid JSON format",
            "code": "JSON_ERROR",
            "context": {"line": e.lineno, "column": e.colno}
        })

task = Task(
    description="Generate a JSON report",
    expected_output="A valid JSON object",
    agent=analyst,
    guardrail=validate_json_output,
    max_retries=3  # Limit retry attempts
)

```

## [​](https://docs.crewai.com/concepts/tasks\#getting-structured-consistent-outputs-from-tasks)  Getting Structured Consistent Outputs from Tasks

It’s also important to note that the output of the final task of a crew becomes the final output of the actual crew itself.

### [​](https://docs.crewai.com/concepts/tasks\#using-output-pydantic)  Using `output_pydantic`

The `output_pydantic` property allows you to define a Pydantic model that the task output should conform to. This ensures that the output is not only structured but also validated according to the Pydantic model.

Here’s an example demonstrating how to use output\_pydantic:

Code

Copy

```python
import json

from crewai import Agent, Crew, Process, Task
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    content: str

blog_agent = Agent(
    role="Blog Content Generator Agent",
    goal="Generate a blog title and content",
    backstory="""You are an expert content creator, skilled in crafting engaging and informative blog posts.""",
    verbose=False,
    allow_delegation=False,
    llm="gpt-4o",
)

task1 = Task(
    description="""Create a blog title and content on a given topic. Make sure the content is under 200 words.""",
    expected_output="A compelling blog title and well-written content.",
    agent=blog_agent,
    output_pydantic=Blog,
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[blog_agent],
    tasks=[task1],
    verbose=True,
    process=Process.sequential,
)

result = crew.kickoff()

# Option 1: Accessing Properties Using Dictionary-Style Indexing
print("Accessing Properties - Option 1")
title = result["title"]
content = result["content"]
print("Title:", title)
print("Content:", content)

# Option 2: Accessing Properties Directly from the Pydantic Model
print("Accessing Properties - Option 2")
title = result.pydantic.title
content = result.pydantic.content
print("Title:", title)
print("Content:", content)

# Option 3: Accessing Properties Using the to_dict() Method
print("Accessing Properties - Option 3")
output_dict = result.to_dict()
title = output_dict["title"]
content = output_dict["content"]
print("Title:", title)
print("Content:", content)

# Option 4: Printing the Entire Blog Object
print("Accessing Properties - Option 5")
print("Blog:", result)

```

In this example:

- A Pydantic model Blog is defined with title and content fields.
- The task task1 uses the output\_pydantic property to specify that its output should conform to the Blog model.
- After executing the crew, you can access the structured output in multiple ways as shown.

#### [​](https://docs.crewai.com/concepts/tasks\#explanation-of-accessing-the-output)  Explanation of Accessing the Output

1. Dictionary-Style Indexing: You can directly access the fields using result\[“field\_name”\]. This works because the CrewOutput class implements the **getitem** method.
2. Directly from Pydantic Model: Access the attributes directly from the result.pydantic object.
3. Using to\_dict() Method: Convert the output to a dictionary and access the fields.
4. Printing the Entire Object: Simply print the result object to see the structured output.

### [​](https://docs.crewai.com/concepts/tasks\#using-output-json)  Using `output_json`

The `output_json` property allows you to define the expected output in JSON format. This ensures that the task’s output is a valid JSON structure that can be easily parsed and used in your application.

Here’s an example demonstrating how to use `output_json`:

Code

Copy

```python
import json

from crewai import Agent, Crew, Process, Task
from pydantic import BaseModel

# Define the Pydantic model for the blog
class Blog(BaseModel):
    title: str
    content: str

# Define the agent
blog_agent = Agent(
    role="Blog Content Generator Agent",
    goal="Generate a blog title and content",
    backstory="""You are an expert content creator, skilled in crafting engaging and informative blog posts.""",
    verbose=False,
    allow_delegation=False,
    llm="gpt-4o",
)

# Define the task with output_json set to the Blog model
task1 = Task(
    description="""Create a blog title and content on a given topic. Make sure the content is under 200 words.""",
    expected_output="A JSON object with 'title' and 'content' fields.",
    agent=blog_agent,
    output_json=Blog,
)

# Instantiate the crew with a sequential process
crew = Crew(
    agents=[blog_agent],
    tasks=[task1],
    verbose=True,
    process=Process.sequential,
)

# Kickoff the crew to execute the task
result = crew.kickoff()

# Option 1: Accessing Properties Using Dictionary-Style Indexing
print("Accessing Properties - Option 1")
title = result["title"]
content = result["content"]
print("Title:", title)
print("Content:", content)

# Option 2: Printing the Entire Blog Object
print("Accessing Properties - Option 2")
print("Blog:", result)

```

In this example:

- A Pydantic model Blog is defined with title and content fields, which is used to specify the structure of the JSON output.
- The task task1 uses the output\_json property to indicate that it expects a JSON output conforming to the Blog model.
- After executing the crew, you can access the structured JSON output in two ways as shown.

#### [​](https://docs.crewai.com/concepts/tasks\#explanation-of-accessing-the-output-2)  Explanation of Accessing the Output

1. Accessing Properties Using Dictionary-Style Indexing: You can access the fields directly using result\[“field\_name”\]. This is possible because the CrewOutput class implements the **getitem** method, allowing you to treat the output like a dictionary. In this option, we’re retrieving the title and content from the result.
2. Printing the Entire Blog Object: By printing result, you get the string representation of the CrewOutput object. Since the **str** method is implemented to return the JSON output, this will display the entire output as a formatted string representing the Blog object.

* * *

By using output\_pydantic or output\_json, you ensure that your tasks produce outputs in a consistent and structured format, making it easier to process and utilize the data within your application or across multiple tasks.

## [​](https://docs.crewai.com/concepts/tasks\#integrating-tools-with-tasks)  Integrating Tools with Tasks

Leverage tools from the [CrewAI Toolkit](https://github.com/joaomdmoura/crewai-tools) and [LangChain Tools](https://python.langchain.com/docs/integrations/tools) for enhanced task performance and agent interaction.

## [​](https://docs.crewai.com/concepts/tasks\#creating-a-task-with-tools)  Creating a Task with Tools

Code

Copy

```python
import os
os.environ["OPENAI_API_KEY"] = "Your Key"
os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key

from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

research_agent = Agent(
  role='Researcher',
  goal='Find and summarize the latest AI news',
  backstory="""You're a researcher at a large company.
  You're responsible for analyzing data and providing insights
  to the business.""",
  verbose=True
)

# to perform a semantic search for a specified query from a text's content across the internet
search_tool = SerperDevTool()

task = Task(
  description='Find and summarize the latest AI news',
  expected_output='A bullet list summary of the top 5 most important AI news',
  agent=research_agent,
  tools=[search_tool]
)

crew = Crew(
    agents=[research_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()
print(result)

```

This demonstrates how tasks with specific tools can override an agent’s default set for tailored task execution.

## [​](https://docs.crewai.com/concepts/tasks\#referring-to-other-tasks)  Referring to Other Tasks

In CrewAI, the output of one task is automatically relayed into the next one, but you can specifically define what tasks’ output, including multiple, should be used as context for another task.

This is useful when you have a task that depends on the output of another task that is not performed immediately after it. This is done through the `context` attribute of the task:

Code

Copy

```python
# ...

research_ai_task = Task(
    description="Research the latest developments in AI",
    expected_output="A list of recent AI developments",
    async_execution=True,
    agent=research_agent,
    tools=[search_tool]
)

research_ops_task = Task(
    description="Research the latest developments in AI Ops",
    expected_output="A list of recent AI Ops developments",
    async_execution=True,
    agent=research_agent,
    tools=[search_tool]
)

write_blog_task = Task(
    description="Write a full blog post about the importance of AI and its latest news",
    expected_output="Full blog post that is 4 paragraphs long",
    agent=writer_agent,
    context=[research_ai_task, research_ops_task]
)

#...

```

## [​](https://docs.crewai.com/concepts/tasks\#asynchronous-execution)  Asynchronous Execution

You can define a task to be executed asynchronously. This means that the crew will not wait for it to be completed to continue with the next task. This is useful for tasks that take a long time to be completed, or that are not crucial for the next tasks to be performed.

You can then use the `context` attribute to define in a future task that it should wait for the output of the asynchronous task to be completed.

Code

Copy

```python
#...

list_ideas = Task(
    description="List of 5 interesting ideas to explore for an article about AI.",
    expected_output="Bullet point list of 5 ideas for an article.",
    agent=researcher,
    async_execution=True # Will be executed asynchronously
)

list_important_history = Task(
    description="Research the history of AI and give me the 5 most important events.",
    expected_output="Bullet point list of 5 important events.",
    agent=researcher,
    async_execution=True # Will be executed asynchronously
)

write_article = Task(
    description="Write an article about AI, its history, and interesting ideas.",
    expected_output="A 4 paragraph article about AI.",
    agent=writer,
    context=[list_ideas, list_important_history] # Will wait for the output of the two tasks to be completed
)

#...

```

## [​](https://docs.crewai.com/concepts/tasks\#callback-mechanism)  Callback Mechanism

The callback function is executed after the task is completed, allowing for actions or notifications to be triggered based on the task’s outcome.

Code

Copy

```python
# ...

def callback_function(output: TaskOutput):
    # Do something after the task is completed
    # Example: Send an email to the manager
    print(f"""
        Task completed!
        Task: {output.description}
        Output: {output.raw}
    """)

research_task = Task(
    description='Find and summarize the latest AI news',
    expected_output='A bullet list summary of the top 5 most important AI news',
    agent=research_agent,
    tools=[search_tool],
    callback=callback_function
)

#...

```

## [​](https://docs.crewai.com/concepts/tasks\#accessing-a-specific-task-output)  Accessing a Specific Task Output

Once a crew finishes running, you can access the output of a specific task by using the `output` attribute of the task object:

Code

Copy

```python
# ...
task1 = Task(
    description='Find and summarize the latest AI news',
    expected_output='A bullet list summary of the top 5 most important AI news',
    agent=research_agent,
    tools=[search_tool]
)

#...

crew = Crew(
    agents=[research_agent],
    tasks=[task1, task2, task3],
    verbose=True
)

result = crew.kickoff()

# Returns a TaskOutput object with the description and results of the task
print(f"""
    Task completed!
    Task: {task1.output.description}
    Output: {task1.output.raw}
""")

```

## [​](https://docs.crewai.com/concepts/tasks\#tool-override-mechanism)  Tool Override Mechanism

Specifying tools in a task allows for dynamic adaptation of agent capabilities, emphasizing CrewAI’s flexibility.

## [​](https://docs.crewai.com/concepts/tasks\#error-handling-and-validation-mechanisms)  Error Handling and Validation Mechanisms

While creating and executing tasks, certain validation mechanisms are in place to ensure the robustness and reliability of task attributes. These include but are not limited to:

- Ensuring only one output type is set per task to maintain clear output expectations.
- Preventing the manual assignment of the `id` attribute to uphold the integrity of the unique identifier system.

These validations help in maintaining the consistency and reliability of task executions within the crewAI framework.

## [​](https://docs.crewai.com/concepts/tasks\#task-guardrails-2)  Task Guardrails

Task guardrails provide a powerful way to validate, transform, or filter task outputs before they are passed to the next task. Guardrails are optional functions that execute before the next task starts, allowing you to ensure that task outputs meet specific requirements or formats.

### [​](https://docs.crewai.com/concepts/tasks\#basic-usage)  Basic Usage

Code

Copy

```python
from typing import Tuple, Union
from crewai import Task

def validate_json_output(result: str) -> Tuple[bool, Union[dict, str]]:
    """Validate that the output is valid JSON."""
    try:
        json_data = json.loads(result)
        return (True, json_data)
    except json.JSONDecodeError:
        return (False, "Output must be valid JSON")

task = Task(
    description="Generate JSON data",
    expected_output="Valid JSON object",
    guardrail=validate_json_output
)

```

### [​](https://docs.crewai.com/concepts/tasks\#how-guardrails-work)  How Guardrails Work

1. **Optional Attribute**: Guardrails are an optional attribute at the task level, allowing you to add validation only where needed.
2. **Execution Timing**: The guardrail function is executed before the next task starts, ensuring valid data flow between tasks.
3. **Return Format**: Guardrails must return a tuple of `(success, data)`:

   - If `success` is `True`, `data` is the validated/transformed result
   - If `success` is `False`, `data` is the error message
4. **Result Routing**:

   - On success ( `True`), the result is automatically passed to the next task
   - On failure ( `False`), the error is sent back to the agent to generate a new answer

### [​](https://docs.crewai.com/concepts/tasks\#common-use-cases)  Common Use Cases

#### [​](https://docs.crewai.com/concepts/tasks\#data-format-validation)  Data Format Validation

Code

Copy

```python
def validate_email_format(result: str) -> Tuple[bool, Union[str, str]]:
    """Ensure the output contains a valid email address."""
    import re
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(email_pattern, result.strip()):
        return (True, result.strip())
    return (False, "Output must be a valid email address")

```

#### [​](https://docs.crewai.com/concepts/tasks\#content-filtering)  Content Filtering

Code

Copy

```python
def filter_sensitive_info(result: str) -> Tuple[bool, Union[str, str]]:
    """Remove or validate sensitive information."""
    sensitive_patterns = ['SSN:', 'password:', 'secret:']
    for pattern in sensitive_patterns:
        if pattern.lower() in result.lower():
            return (False, f"Output contains sensitive information ({pattern})")
    return (True, result)

```

#### [​](https://docs.crewai.com/concepts/tasks\#data-transformation)  Data Transformation

Code

Copy

```python
def normalize_phone_number(result: str) -> Tuple[bool, Union[str, str]]:
    """Ensure phone numbers are in a consistent format."""
    import re
    digits = re.sub(r'\D', '', result)
    if len(digits) == 10:
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        return (True, formatted)
    return (False, "Output must be a 10-digit phone number")

```

### [​](https://docs.crewai.com/concepts/tasks\#advanced-features)  Advanced Features

#### [​](https://docs.crewai.com/concepts/tasks\#chaining-multiple-validations)  Chaining Multiple Validations

Code

Copy

```python
def chain_validations(*validators):
    """Chain multiple validators together."""
    def combined_validator(result):
        for validator in validators:
            success, data = validator(result)
            if not success:
                return (False, data)
            result = data
        return (True, result)
    return combined_validator

# Usage
task = Task(
    description="Get user contact info",
    expected_output="Email and phone",
    guardrail=chain_validations(
        validate_email_format,
        filter_sensitive_info
    )
)

```

#### [​](https://docs.crewai.com/concepts/tasks\#custom-retry-logic)  Custom Retry Logic

Code

Copy

```python
task = Task(
    description="Generate data",
    expected_output="Valid data",
    guardrail=validate_data,
    max_retries=5  # Override default retry limit
)

```

## [​](https://docs.crewai.com/concepts/tasks\#creating-directories-when-saving-files)  Creating Directories when Saving Files

You can now specify if a task should create directories when saving its output to a file. This is particularly useful for organizing outputs and ensuring that file paths are correctly structured.

Code

Copy

```python
# ...

save_output_task = Task(
    description='Save the summarized AI news to a file',
    expected_output='File saved successfully',
    agent=research_agent,
    tools=[file_save_tool],
    output_file='outputs/ai_news_summary.txt',
    create_directory=True
)

#...

```

## [​](https://docs.crewai.com/concepts/tasks\#conclusion)  Conclusion

Tasks are the driving force behind the actions of agents in CrewAI.
By properly defining tasks and their outcomes, you set the stage for your AI agents to work effectively, either independently or as a collaborative unit.
Equipping tasks with appropriate tools, understanding the execution process, and following robust validation practices are crucial for maximizing CrewAI’s potential,
ensuring agents are effectively prepared for their assignments and that tasks are executed as intended.

Was this page helpful?

YesNo

[Agents](https://docs.crewai.com/concepts/agents) [Crews](https://docs.crewai.com/concepts/crews)

On this page

- [Overview of a Task](https://docs.crewai.com/concepts/tasks#overview-of-a-task)
- [Task Execution Flow](https://docs.crewai.com/concepts/tasks#task-execution-flow)
- [Task Attributes](https://docs.crewai.com/concepts/tasks#task-attributes)
- [Creating Tasks](https://docs.crewai.com/concepts/tasks#creating-tasks)
- [YAML Configuration (Recommended)](https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended)
- [Direct Code Definition (Alternative)](https://docs.crewai.com/concepts/tasks#direct-code-definition-alternative)
- [Task Output](https://docs.crewai.com/concepts/tasks#task-output)
- [Task Output Attributes](https://docs.crewai.com/concepts/tasks#task-output-attributes)
- [Task Methods and Properties](https://docs.crewai.com/concepts/tasks#task-methods-and-properties)
- [Accessing Task Outputs](https://docs.crewai.com/concepts/tasks#accessing-task-outputs)
- [Example](https://docs.crewai.com/concepts/tasks#example)
- [Task Dependencies and Context](https://docs.crewai.com/concepts/tasks#task-dependencies-and-context)
- [Task Guardrails](https://docs.crewai.com/concepts/tasks#task-guardrails)
- [Using Task Guardrails](https://docs.crewai.com/concepts/tasks#using-task-guardrails)
- [Guardrail Function Requirements](https://docs.crewai.com/concepts/tasks#guardrail-function-requirements)
- [Error Handling Best Practices](https://docs.crewai.com/concepts/tasks#error-handling-best-practices)
- [Handling Guardrail Results](https://docs.crewai.com/concepts/tasks#handling-guardrail-results)
- [Getting Structured Consistent Outputs from Tasks](https://docs.crewai.com/concepts/tasks#getting-structured-consistent-outputs-from-tasks)
- [Using output\_pydantic](https://docs.crewai.com/concepts/tasks#using-output-pydantic)
- [Explanation of Accessing the Output](https://docs.crewai.com/concepts/tasks#explanation-of-accessing-the-output)
- [Using output\_json](https://docs.crewai.com/concepts/tasks#using-output-json)
- [Explanation of Accessing the Output](https://docs.crewai.com/concepts/tasks#explanation-of-accessing-the-output-2)
- [Integrating Tools with Tasks](https://docs.crewai.com/concepts/tasks#integrating-tools-with-tasks)
- [Creating a Task with Tools](https://docs.crewai.com/concepts/tasks#creating-a-task-with-tools)
- [Referring to Other Tasks](https://docs.crewai.com/concepts/tasks#referring-to-other-tasks)
- [Asynchronous Execution](https://docs.crewai.com/concepts/tasks#asynchronous-execution)
- [Callback Mechanism](https://docs.crewai.com/concepts/tasks#callback-mechanism)
- [Accessing a Specific Task Output](https://docs.crewai.com/concepts/tasks#accessing-a-specific-task-output)
- [Tool Override Mechanism](https://docs.crewai.com/concepts/tasks#tool-override-mechanism)
- [Error Handling and Validation Mechanisms](https://docs.crewai.com/concepts/tasks#error-handling-and-validation-mechanisms)
- [Task Guardrails](https://docs.crewai.com/concepts/tasks#task-guardrails-2)
- [Basic Usage](https://docs.crewai.com/concepts/tasks#basic-usage)
- [How Guardrails Work](https://docs.crewai.com/concepts/tasks#how-guardrails-work)
- [Common Use Cases](https://docs.crewai.com/concepts/tasks#common-use-cases)
- [Data Format Validation](https://docs.crewai.com/concepts/tasks#data-format-validation)
- [Content Filtering](https://docs.crewai.com/concepts/tasks#content-filtering)
- [Data Transformation](https://docs.crewai.com/concepts/tasks#data-transformation)
- [Advanced Features](https://docs.crewai.com/concepts/tasks#advanced-features)
- [Chaining Multiple Validations](https://docs.crewai.com/concepts/tasks#chaining-multiple-validations)
- [Custom Retry Logic](https://docs.crewai.com/concepts/tasks#custom-retry-logic)
- [Creating Directories when Saving Files](https://docs.crewai.com/concepts/tasks#creating-directories-when-saving-files)
- [Conclusion](https://docs.crewai.com/concepts/tasks#conclusion)

# Tools - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Tools

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/tools\#introduction)  Introduction

CrewAI tools empower agents with capabilities ranging from web searching and data analysis to collaboration and delegating tasks among coworkers.
This documentation outlines how to create, integrate, and leverage these tools within the CrewAI framework, including a new focus on collaboration tools.

## [​](https://docs.crewai.com/concepts/tools\#what-is-a-tool%3F)  What is a Tool?

A tool in CrewAI is a skill or function that agents can utilize to perform various actions.
This includes tools from the [CrewAI Toolkit](https://github.com/joaomdmoura/crewai-tools) and [LangChain Tools](https://python.langchain.com/docs/integrations/tools),
enabling everything from simple searches to complex interactions and effective teamwork among agents.

## [​](https://docs.crewai.com/concepts/tools\#key-characteristics-of-tools)  Key Characteristics of Tools

- **Utility**: Crafted for tasks such as web searching, data analysis, content generation, and agent collaboration.
- **Integration**: Boosts agent capabilities by seamlessly integrating tools into their workflow.
- **Customizability**: Provides the flexibility to develop custom tools or utilize existing ones, catering to the specific needs of agents.
- **Error Handling**: Incorporates robust error handling mechanisms to ensure smooth operation.
- **Caching Mechanism**: Features intelligent caching to optimize performance and reduce redundant operations.

## [​](https://docs.crewai.com/concepts/tools\#using-crewai-tools)  Using CrewAI Tools

To enhance your agents’ capabilities with crewAI tools, begin by installing our extra tools package:

Copy

```bash
pip install 'crewai[tools]'

```

Here’s an example demonstrating their use:

Code

Copy

```python
import os
from crewai import Agent, Task, Crew
# Importing crewAI tools
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

# Set up API keys
os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key
os.environ["OPENAI_API_KEY"] = "Your Key"

# Instantiate tools
docs_tool = DirectoryReadTool(directory='./blog-posts')
file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

# Create agents
researcher = Agent(
    role='Market Research Analyst',
    goal='Provide up-to-date market analysis of the AI industry',
    backstory='An expert analyst with a keen eye for market trends.',
    tools=[search_tool, web_rag_tool],
    verbose=True
)

writer = Agent(
    role='Content Writer',
    goal='Craft engaging blog posts about the AI industry',
    backstory='A skilled writer with a passion for technology.',
    tools=[docs_tool, file_tool],
    verbose=True
)

# Define tasks
research = Task(
    description='Research the latest trends in the AI industry and provide a summary.',
    expected_output='A summary of the top 3 trending developments in the AI industry with a unique perspective on their significance.',
    agent=researcher
)

write = Task(
    description='Write an engaging blog post about the AI industry, based on the research analyst’s summary. Draw inspiration from the latest blog posts in the directory.',
    expected_output='A 4-paragraph blog post formatted in markdown with engaging, informative, and accessible content, avoiding complex jargon.',
    agent=writer,
    output_file='blog-posts/new_post.md'  # The final blog post will be saved here
)

# Assemble a crew with planning enabled
crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write],
    verbose=True,
    planning=True,  # Enable planning feature
)

# Execute tasks
crew.kickoff()

```

## [​](https://docs.crewai.com/concepts/tools\#available-crewai-tools)  Available CrewAI Tools

- **Error Handling**: All tools are built with error handling capabilities, allowing agents to gracefully manage exceptions and continue their tasks.
- **Caching Mechanism**: All tools support caching, enabling agents to efficiently reuse previously obtained results, reducing the load on external resources and speeding up the execution time. You can also define finer control over the caching mechanism using the `cache_function` attribute on the tool.

Here is a list of the available tools and their descriptions:

| Tool | Description |
| --- | --- |
| **BrowserbaseLoadTool** | A tool for interacting with and extracting data from web browsers. |
| **CodeDocsSearchTool** | A RAG tool optimized for searching through code documentation and related technical documents. |
| **CodeInterpreterTool** | A tool for interpreting python code. |
| **ComposioTool** | Enables use of Composio tools. |
| **CSVSearchTool** | A RAG tool designed for searching within CSV files, tailored to handle structured data. |
| **DALL-E Tool** | A tool for generating images using the DALL-E API. |
| **DirectorySearchTool** | A RAG tool for searching within directories, useful for navigating through file systems. |
| **DOCXSearchTool** | A RAG tool aimed at searching within DOCX documents, ideal for processing Word files. |
| **DirectoryReadTool** | Facilitates reading and processing of directory structures and their contents. |
| **EXASearchTool** | A tool designed for performing exhaustive searches across various data sources. |
| **FileReadTool** | Enables reading and extracting data from files, supporting various file formats. |
| **FirecrawlSearchTool** | A tool to search webpages using Firecrawl and return the results. |
| **FirecrawlCrawlWebsiteTool** | A tool for crawling webpages using Firecrawl. |
| **FirecrawlScrapeWebsiteTool** | A tool for scraping webpages URL using Firecrawl and returning its contents. |
| **GithubSearchTool** | A RAG tool for searching within GitHub repositories, useful for code and documentation search. |
| **SerperDevTool** | A specialized tool for development purposes, with specific functionalities under development. |
| **TXTSearchTool** | A RAG tool focused on searching within text (.txt) files, suitable for unstructured data. |
| **JSONSearchTool** | A RAG tool designed for searching within JSON files, catering to structured data handling. |
| **LlamaIndexTool** | Enables the use of LlamaIndex tools. |
| **MDXSearchTool** | A RAG tool tailored for searching within Markdown (MDX) files, useful for documentation. |
| **PDFSearchTool** | A RAG tool aimed at searching within PDF documents, ideal for processing scanned documents. |
| **PGSearchTool** | A RAG tool optimized for searching within PostgreSQL databases, suitable for database queries. |
| **Vision Tool** | A tool for generating images using the DALL-E API. |
| **RagTool** | A general-purpose RAG tool capable of handling various data sources and types. |
| **ScrapeElementFromWebsiteTool** | Enables scraping specific elements from websites, useful for targeted data extraction. |
| **ScrapeWebsiteTool** | Facilitates scraping entire websites, ideal for comprehensive data collection. |
| **WebsiteSearchTool** | A RAG tool for searching website content, optimized for web data extraction. |
| **XMLSearchTool** | A RAG tool designed for searching within XML files, suitable for structured data formats. |
| **YoutubeChannelSearchTool** | A RAG tool for searching within YouTube channels, useful for video content analysis. |
| **YoutubeVideoSearchTool** | A RAG tool aimed at searching within YouTube videos, ideal for video data extraction. |

## [​](https://docs.crewai.com/concepts/tools\#creating-your-own-tools)  Creating your own Tools

Developers can craft `custom tools` tailored for their agent’s needs or
utilize pre-built options.

There are two main ways for one to create a CrewAI tool:

### [​](https://docs.crewai.com/concepts/tools\#subclassing-basetool)  Subclassing `BaseTool`

Code

Copy

```python
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class MyToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = "What this tool does. It's vital for effective utilization."
    args_schema: Type[BaseModel] = MyToolInput

    def _run(self, argument: str) -> str:
        # Your tool's logic here
        return "Tool's result"

```

### [​](https://docs.crewai.com/concepts/tools\#utilizing-the-tool-decorator)  Utilizing the `tool` Decorator

Code

Copy

```python
from crewai.tools import tool
@tool("Name of my tool")
def my_tool(question: str) -> str:
    """Clear description for what this tool is useful for, your agent will need this information to use it."""
    # Function logic here
    return "Result from your custom tool"

```

### [​](https://docs.crewai.com/concepts/tools\#structured-tools)  Structured Tools

The `StructuredTool` class wraps functions as tools, providing flexibility and validation while reducing boilerplate. It supports custom schemas and dynamic logic for seamless integration of complex functionalities.

#### [​](https://docs.crewai.com/concepts/tools\#example%3A)  Example:

Using `StructuredTool.from_function`, you can wrap a function that interacts with an external API or system, providing a structured interface. This enables robust validation and consistent execution, making it easier to integrate complex functionalities into your applications as demonstrated in the following example:

Copy

```python
from crewai.tools.structured_tool import CrewStructuredTool
from pydantic import BaseModel

# Define the schema for the tool's input using Pydantic
class APICallInput(BaseModel):
    endpoint: str
    parameters: dict

# Wrapper function to execute the API call
def tool_wrapper(*args, **kwargs):
    # Here, you would typically call the API using the parameters
    # For demonstration, we'll return a placeholder string
    return f"Call the API at {kwargs['endpoint']} with parameters {kwargs['parameters']}"

# Create and return the structured tool
def create_structured_tool():
    return CrewStructuredTool.from_function(
        name='Wrapper API',
        description="A tool to wrap API calls with structured input.",
        args_schema=APICallInput,
        func=tool_wrapper,
    )

# Example usage
structured_tool = create_structured_tool()

# Execute the tool with structured input
result = structured_tool._run(**{
    "endpoint": "https://example.com/api",
    "parameters": {"key1": "value1", "key2": "value2"}
})
print(result)  # Output: Call the API at https://example.com/api with parameters {'key1': 'value1', 'key2': 'value2'}

```

### [​](https://docs.crewai.com/concepts/tools\#custom-caching-mechanism)  Custom Caching Mechanism

Tools can optionally implement a `cache_function` to fine-tune caching
behavior. This function determines when to cache results based on specific
conditions, offering granular control over caching logic.

Code

Copy

```python
from crewai.tools import tool

@tool
def multiplication_tool(first_number: int, second_number: int) -> str:
    """Useful for when you need to multiply two numbers together."""
    return first_number * second_number

def cache_func(args, result):
    # In this case, we only cache the result if it's a multiple of 2
    cache = result % 2 == 0
    return cache

multiplication_tool.cache_function = cache_func

writer1 = Agent(
        role="Writer",
        goal="You write lessons of math for kids.",
        backstory="You're an expert in writing and you love to teach kids but you know nothing of math.",
        tools=[multiplication_tool],
        allow_delegation=False,
    )
    #...

```

## [​](https://docs.crewai.com/concepts/tools\#conclusion)  Conclusion

Tools are pivotal in extending the capabilities of CrewAI agents, enabling them to undertake a broad spectrum of tasks and collaborate effectively.
When building solutions with CrewAI, leverage both custom and existing tools to empower your agents and enhance the AI ecosystem. Consider utilizing error handling,
caching mechanisms, and the flexibility of tool arguments to optimize your agents’ performance and capabilities.

Was this page helpful?

YesNo

[CLI](https://docs.crewai.com/concepts/cli) [Using LangChain Tools](https://docs.crewai.com/concepts/langchain-tools)

On this page

- [Introduction](https://docs.crewai.com/concepts/tools#introduction)
- [What is a Tool?](https://docs.crewai.com/concepts/tools#what-is-a-tool%3F)
- [Key Characteristics of Tools](https://docs.crewai.com/concepts/tools#key-characteristics-of-tools)
- [Using CrewAI Tools](https://docs.crewai.com/concepts/tools#using-crewai-tools)
- [Available CrewAI Tools](https://docs.crewai.com/concepts/tools#available-crewai-tools)
- [Creating your own Tools](https://docs.crewai.com/concepts/tools#creating-your-own-tools)
- [Subclassing BaseTool](https://docs.crewai.com/concepts/tools#subclassing-basetool)
- [Utilizing the tool Decorator](https://docs.crewai.com/concepts/tools#utilizing-the-tool-decorator)
- [Structured Tools](https://docs.crewai.com/concepts/tools#structured-tools)
- [Example:](https://docs.crewai.com/concepts/tools#example%3A)
- [Custom Caching Mechanism](https://docs.crewai.com/concepts/tools#custom-caching-mechanism)
- [Conclusion](https://docs.crewai.com/concepts/tools#conclusion)

# Firecrawl Crawl Website - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Firecrawl Crawl Website

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/firecrawlcrawlwebsitetool\#firecrawlcrawlwebsitetool)  `FirecrawlCrawlWebsiteTool`

## [​](https://docs.crewai.com/tools/firecrawlcrawlwebsitetool\#description)  Description

[Firecrawl](https://firecrawl.dev/) is a platform for crawling and convert any website into clean markdown or structured data.

## [​](https://docs.crewai.com/tools/firecrawlcrawlwebsitetool\#installation)  Installation

- Get an API key from [firecrawl.dev](https://firecrawl.dev/) and set it in environment variables ( `FIRECRAWL_API_KEY`).
- Install the [Firecrawl SDK](https://github.com/mendableai/firecrawl) along with `crewai[tools]` package:

Copy

```shell
pip install firecrawl-py 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/firecrawlcrawlwebsitetool\#example)  Example

Utilize the FirecrawlScrapeFromWebsiteTool as follows to allow your agent to load websites:

Code

Copy

```python
from crewai_tools import FirecrawlCrawlWebsiteTool

tool = FirecrawlCrawlWebsiteTool(url='firecrawl.dev')

```

## [​](https://docs.crewai.com/tools/firecrawlcrawlwebsitetool\#arguments)  Arguments

- `api_key`: Optional. Specifies Firecrawl API key. Defaults is the `FIRECRAWL_API_KEY` environment variable.
- `url`: The base URL to start crawling from.
- `page_options`: Optional.

  - `onlyMainContent`: Optional. Only return the main content of the page excluding headers, navs, footers, etc.
  - `includeHtml`: Optional. Include the raw HTML content of the page. Will output a html key in the response.
- `crawler_options`: Optional. Options for controlling the crawling behavior.

  - `includes`: Optional. URL patterns to include in the crawl.
  - `exclude`: Optional. URL patterns to exclude from the crawl.
  - `generateImgAltText`: Optional. Generate alt text for images using LLMs (requires a paid plan).
  - `returnOnlyUrls`: Optional. If true, returns only the URLs as a list in the crawl status. Note: the response will be a list of URLs inside the data, not a list of documents.
  - `maxDepth`: Optional. Maximum depth to crawl. Depth 1 is the base URL, depth 2 includes the base URL and its direct children, and so on.
  - `mode`: Optional. The crawling mode to use. Fast mode crawls 4x faster on websites without a sitemap but may not be as accurate and shouldn’t be used on heavily JavaScript-rendered websites.
  - `limit`: Optional. Maximum number of pages to crawl.
  - `timeout`: Optional. Timeout in milliseconds for the crawling operation.

Was this page helpful?

YesNo

[File Write](https://docs.crewai.com/tools/filewritetool) [Firecrawl Scrape Website](https://docs.crewai.com/tools/firecrawlscrapewebsitetool)

On this page

- [FirecrawlCrawlWebsiteTool](https://docs.crewai.com/tools/firecrawlcrawlwebsitetool#firecrawlcrawlwebsitetool)
- [Description](https://docs.crewai.com/tools/firecrawlcrawlwebsitetool#description)
- [Installation](https://docs.crewai.com/tools/firecrawlcrawlwebsitetool#installation)
- [Example](https://docs.crewai.com/tools/firecrawlcrawlwebsitetool#example)
- [Arguments](https://docs.crewai.com/tools/firecrawlcrawlwebsitetool#arguments)

# Using Multimodal Agents - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Using Multimodal Agents

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/how-to/multimodal-agents\#using-multimodal-agents)  Using Multimodal Agents

CrewAI supports multimodal agents that can process both text and non-text content like images. This guide will show you how to enable and use multimodal capabilities in your agents.

### [​](https://docs.crewai.com/how-to/multimodal-agents\#enabling-multimodal-capabilities)  Enabling Multimodal Capabilities

To create a multimodal agent, simply set the `multimodal` parameter to `True` when initializing your agent:

Copy

```python
from crewai import Agent

agent = Agent(
    role="Image Analyst",
    goal="Analyze and extract insights from images",
    backstory="An expert in visual content interpretation with years of experience in image analysis",
    multimodal=True  # This enables multimodal capabilities
)

```

When you set `multimodal=True`, the agent is automatically configured with the necessary tools for handling non-text content, including the `AddImageTool`.

### [​](https://docs.crewai.com/how-to/multimodal-agents\#working-with-images)  Working with Images

The multimodal agent comes pre-configured with the `AddImageTool`, which allows it to process images. You don’t need to manually add this tool - it’s automatically included when you enable multimodal capabilities.

Here’s a complete example showing how to use a multimodal agent to analyze an image:

Copy

```python
from crewai import Agent, Task, Crew

# Create a multimodal agent
image_analyst = Agent(
    role="Product Analyst",
    goal="Analyze product images and provide detailed descriptions",
    backstory="Expert in visual product analysis with deep knowledge of design and features",
    multimodal=True
)

# Create a task for image analysis
task = Task(
    description="Analyze the product image at https://example.com/product.jpg and provide a detailed description",
    expected_output="A detailed description of the product image",
    agent=image_analyst
)

# Create and run the crew
crew = Crew(
    agents=[image_analyst],
    tasks=[task]
)

result = crew.kickoff()

```

### [​](https://docs.crewai.com/how-to/multimodal-agents\#advanced-usage-with-context)  Advanced Usage with Context

You can provide additional context or specific questions about the image when creating tasks for multimodal agents. The task description can include specific aspects you want the agent to focus on:

Copy

```python
from crewai import Agent, Task, Crew

# Create a multimodal agent for detailed analysis
expert_analyst = Agent(
    role="Visual Quality Inspector",
    goal="Perform detailed quality analysis of product images",
    backstory="Senior quality control expert with expertise in visual inspection",
    multimodal=True  # AddImageTool is automatically included
)

# Create a task with specific analysis requirements
inspection_task = Task(
    description="""
    Analyze the product image at https://example.com/product.jpg with focus on:
    1. Quality of materials
    2. Manufacturing defects
    3. Compliance with standards
    Provide a detailed report highlighting any issues found.
    """,
    expected_output="A detailed report highlighting any issues found",
    agent=expert_analyst
)

# Create and run the crew
crew = Crew(
    agents=[expert_analyst],
    tasks=[inspection_task]
)

result = crew.kickoff()

```

### [​](https://docs.crewai.com/how-to/multimodal-agents\#tool-details)  Tool Details

When working with multimodal agents, the `AddImageTool` is automatically configured with the following schema:

Copy

```python
class AddImageToolSchema:
    image_url: str  # Required: The URL or path of the image to process
    action: Optional[str] = None  # Optional: Additional context or specific questions about the image

```

The multimodal agent will automatically handle the image processing through its built-in tools, allowing it to:

- Access images via URLs or local file paths
- Process image content with optional context or specific questions
- Provide analysis and insights based on the visual information and task requirements

### [​](https://docs.crewai.com/how-to/multimodal-agents\#best-practices)  Best Practices

When working with multimodal agents, keep these best practices in mind:

1. **Image Access**
   - Ensure your images are accessible via URLs that the agent can reach
   - For local images, consider hosting them temporarily or using absolute file paths
   - Verify that image URLs are valid and accessible before running tasks
2. **Task Description**
   - Be specific about what aspects of the image you want the agent to analyze
   - Include clear questions or requirements in the task description
   - Consider using the optional `action` parameter for focused analysis
3. **Resource Management**
   - Image processing may require more computational resources than text-only tasks
   - Some language models may require base64 encoding for image data
   - Consider batch processing for multiple images to optimize performance
4. **Environment Setup**
   - Verify that your environment has the necessary dependencies for image processing
   - Ensure your language model supports multimodal capabilities
   - Test with small images first to validate your setup
5. **Error Handling**
   - Implement proper error handling for image loading failures
   - Have fallback strategies for when image processing fails
   - Monitor and log image processing operations for debugging

Was this page helpful?

YesNo

[Customize Agents](https://docs.crewai.com/how-to/customizing-agents) [Coding Agents](https://docs.crewai.com/how-to/coding-agents)

On this page

- [Using Multimodal Agents](https://docs.crewai.com/how-to/multimodal-agents#using-multimodal-agents)
- [Enabling Multimodal Capabilities](https://docs.crewai.com/how-to/multimodal-agents#enabling-multimodal-capabilities)
- [Working with Images](https://docs.crewai.com/how-to/multimodal-agents#working-with-images)
- [Advanced Usage with Context](https://docs.crewai.com/how-to/multimodal-agents#advanced-usage-with-context)
- [Tool Details](https://docs.crewai.com/how-to/multimodal-agents#tool-details)
- [Best Practices](https://docs.crewai.com/how-to/multimodal-agents#best-practices)

# Replay Tasks from Latest Crew Kickoff - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

How to Guides

Replay Tasks from Latest Crew Kickoff

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/how-to/replay-tasks-from-latest-crew-kickoff\#introduction)  Introduction

CrewAI provides the ability to replay from a task specified from the latest crew kickoff. This feature is particularly useful when you’ve finished a kickoff and may want to retry certain tasks or don’t need to refetch data over and your agents already have the context saved from the kickoff execution so you just need to replay the tasks you want to.

You must run `crew.kickoff()` before you can replay a task.
Currently, only the latest kickoff is supported, so if you use `kickoff_for_each`, it will only allow you to replay from the most recent crew run.

Here’s an example of how to replay from a task:

### [​](https://docs.crewai.com/how-to/replay-tasks-from-latest-crew-kickoff\#replaying-from-specific-task-using-the-cli)  Replaying from Specific Task Using the CLI

To use the replay feature, follow these steps:

1

Open your terminal or command prompt.

2

Navigate to the directory where your CrewAI project is located.

3

Run the following commands:

To view the latest kickoff task\_ids use:

Copy

```shell
crewai log-tasks-outputs

```

Once you have your `task_id` to replay, use:

Copy

```shell
crewai replay -t <task_id>

```

Ensure `crewai` is installed and configured correctly in your development environment.

### [​](https://docs.crewai.com/how-to/replay-tasks-from-latest-crew-kickoff\#replaying-from-a-task-programmatically)  Replaying from a Task Programmatically

To replay from a task programmatically, use the following steps:

1

Specify the \`task\_id\` and input parameters for the replay process.

Specify the `task_id` and input parameters for the replay process.

2

Execute the replay command within a try-except block to handle potential errors.

Execute the replay command within a try-except block to handle potential errors.

Code

Copy

```python
  def replay():
  """
  Replay the crew execution from a specific task.
  """
  task_id = '<task_id>'
  inputs = {"topic": "CrewAI Training"}  # This is optional; you can pass in the inputs you want to replay; otherwise, it uses the previous kickoff's inputs.
  try:
      YourCrewName_Crew().crew().replay(task_id=task_id, inputs=inputs)

  except subprocess.CalledProcessError as e:
      raise Exception(f"An error occurred while replaying the crew: {e}")

  except Exception as e:
      raise Exception(f"An unexpected error occurred: {e}")

```

## [​](https://docs.crewai.com/how-to/replay-tasks-from-latest-crew-kickoff\#conclusion)  Conclusion

With the above enhancements and detailed functionality, replaying specific tasks in CrewAI has been made more efficient and robust.
Ensure you follow the commands and steps precisely to make the most of these features.

Was this page helpful?

YesNo

[Kickoff Crew for Each](https://docs.crewai.com/how-to/kickoff-for-each) [Conditional Tasks](https://docs.crewai.com/how-to/conditional-tasks)

On this page

- [Introduction](https://docs.crewai.com/how-to/replay-tasks-from-latest-crew-kickoff#introduction)
- [Replaying from Specific Task Using the CLI](https://docs.crewai.com/how-to/replay-tasks-from-latest-crew-kickoff#replaying-from-specific-task-using-the-cli)
- [Replaying from a Task Programmatically](https://docs.crewai.com/how-to/replay-tasks-from-latest-crew-kickoff#replaying-from-a-task-programmatically)
- [Conclusion](https://docs.crewai.com/how-to/replay-tasks-from-latest-crew-kickoff#conclusion)

# Browserbase Web Loader - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Browserbase Web Loader

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/browserbaseloadtool\#browserbaseloadtool)  `BrowserbaseLoadTool`

## [​](https://docs.crewai.com/tools/browserbaseloadtool\#description)  Description

[Browserbase](https://browserbase.com/) is a developer platform to reliably run, manage, and monitor headless browsers.

Power your AI data retrievals with:

- [Serverless Infrastructure](https://docs.browserbase.com/under-the-hood) providing reliable browsers to extract data from complex UIs
- [Stealth Mode](https://docs.browserbase.com/features/stealth-mode) with included fingerprinting tactics and automatic captcha solving
- [Session Debugger](https://docs.browserbase.com/features/sessions) to inspect your Browser Session with networks timeline and logs
- [Live Debug](https://docs.browserbase.com/guides/session-debug-connection/browser-remote-control) to quickly debug your automation

## [​](https://docs.crewai.com/tools/browserbaseloadtool\#installation)  Installation

- Get an API key and Project ID from [browserbase.com](https://browserbase.com/) and set it in environment variables ( `BROWSERBASE_API_KEY`, `BROWSERBASE_PROJECT_ID`).
- Install the [Browserbase SDK](http://github.com/browserbase/python-sdk) along with `crewai[tools]` package:

Copy

```shell
pip install browserbase 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/browserbaseloadtool\#example)  Example

Utilize the BrowserbaseLoadTool as follows to allow your agent to load websites:

Code

Copy

```python
from crewai_tools import BrowserbaseLoadTool

# Initialize the tool with the Browserbase API key and Project ID
tool = BrowserbaseLoadTool()

```

## [​](https://docs.crewai.com/tools/browserbaseloadtool\#arguments)  Arguments

The following parameters can be used to customize the `BrowserbaseLoadTool`’s behavior:

| Argument | Type | Description |
| --- | --- | --- |
| **api\_key** | `string` | _Optional_. Browserbase API key. Default is `BROWSERBASE_API_KEY` env variable. |
| **project\_id** | `string` | _Optional_. Browserbase Project ID. Default is `BROWSERBASE_PROJECT_ID` env variable. |
| **text\_content** | `bool` | _Optional_. Retrieve only text content. Default is `False`. |
| **session\_id** | `string` | _Optional_. Provide an existing Session ID. |
| **proxy** | `bool` | _Optional_. Enable/Disable Proxies. Default is `False`. |

Was this page helpful?

YesNo

[Agent Monitoring with Langfuse](https://docs.crewai.com/how-to/langfuse-observability) [Code Docs RAG Search](https://docs.crewai.com/tools/codedocssearchtool)

On this page

- [BrowserbaseLoadTool](https://docs.crewai.com/tools/browserbaseloadtool#browserbaseloadtool)
- [Description](https://docs.crewai.com/tools/browserbaseloadtool#description)
- [Installation](https://docs.crewai.com/tools/browserbaseloadtool#installation)
- [Example](https://docs.crewai.com/tools/browserbaseloadtool#example)
- [Arguments](https://docs.crewai.com/tools/browserbaseloadtool#arguments)

# Agents - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Core Concepts

Agents

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

## [​](https://docs.crewai.com/concepts/agents\#overview-of-an-agent)  Overview of an Agent

In the CrewAI framework, an `Agent` is an autonomous unit that can:

- Perform specific tasks
- Make decisions based on its role and goal
- Use tools to accomplish objectives
- Communicate and collaborate with other agents
- Maintain memory of interactions
- Delegate tasks when allowed

Think of an agent as a specialized team member with specific skills, expertise, and responsibilities. For example, a `Researcher` agent might excel at gathering and analyzing information, while a `Writer` agent might be better at creating content.

## [​](https://docs.crewai.com/concepts/agents\#agent-attributes)  Agent Attributes

| Attribute | Parameter | Type | Description |
| --- | --- | --- | --- |
| **Role** | `role` | `str` | Defines the agent’s function and expertise within the crew. |
| **Goal** | `goal` | `str` | The individual objective that guides the agent’s decision-making. |
| **Backstory** | `backstory` | `str` | Provides context and personality to the agent, enriching interactions. |
| **LLM** _(optional)_ | `llm` | `Union[str, LLM, Any]` | Language model that powers the agent. Defaults to the model specified in `OPENAI_MODEL_NAME` or “gpt-4”. |
| **Tools** _(optional)_ | `tools` | `List[BaseTool]` | Capabilities or functions available to the agent. Defaults to an empty list. |
| **Function Calling LLM** _(optional)_ | `function_calling_llm` | `Optional[Any]` | Language model for tool calling, overrides crew’s LLM if specified. |
| **Max Iterations** _(optional)_ | `max_iter` | `int` | Maximum iterations before the agent must provide its best answer. Default is 20. |
| **Max RPM** _(optional)_ | `max_rpm` | `Optional[int]` | Maximum requests per minute to avoid rate limits. |
| **Max Execution Time** _(optional)_ | `max_execution_time` | `Optional[int]` | Maximum time (in seconds) for task execution. |
| **Memory** _(optional)_ | `memory` | `bool` | Whether the agent should maintain memory of interactions. Default is True. |
| **Verbose** _(optional)_ | `verbose` | `bool` | Enable detailed execution logs for debugging. Default is False. |
| **Allow Delegation** _(optional)_ | `allow_delegation` | `bool` | Allow the agent to delegate tasks to other agents. Default is False. |
| **Step Callback** _(optional)_ | `step_callback` | `Optional[Any]` | Function called after each agent step, overrides crew callback. |
| **Cache** _(optional)_ | `cache` | `bool` | Enable caching for tool usage. Default is True. |
| **System Template** _(optional)_ | `system_template` | `Optional[str]` | Custom system prompt template for the agent. |
| **Prompt Template** _(optional)_ | `prompt_template` | `Optional[str]` | Custom prompt template for the agent. |
| **Response Template** _(optional)_ | `response_template` | `Optional[str]` | Custom response template for the agent. |
| **Allow Code Execution** _(optional)_ | `allow_code_execution` | `Optional[bool]` | Enable code execution for the agent. Default is False. |
| **Max Retry Limit** _(optional)_ | `max_retry_limit` | `int` | Maximum number of retries when an error occurs. Default is 2. |
| **Respect Context Window** _(optional)_ | `respect_context_window` | `bool` | Keep messages under context window size by summarizing. Default is True. |
| **Code Execution Mode** _(optional)_ | `code_execution_mode` | `Literal["safe", "unsafe"]` | Mode for code execution: ‘safe’ (using Docker) or ‘unsafe’ (direct). Default is ‘safe’. |
| **Embedder** _(optional)_ | `embedder` | `Optional[Dict[str, Any]]` | Configuration for the embedder used by the agent. |
| **Knowledge Sources** _(optional)_ | `knowledge_sources` | `Optional[List[BaseKnowledgeSource]]` | Knowledge sources available to the agent. |
| **Use System Prompt** _(optional)_ | `use_system_prompt` | `Optional[bool]` | Whether to use system prompt (for o1 model support). Default is True. |

## [​](https://docs.crewai.com/concepts/agents\#creating-agents)  Creating Agents

There are two ways to create agents in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.

### [​](https://docs.crewai.com/concepts/agents\#yaml-configuration-recommended)  YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define agents. We strongly recommend using this approach in your CrewAI projects.

After creating your CrewAI project as outlined in the [Installation](https://docs.crewai.com/installation) section, navigate to the `src/latest_ai_development/config/agents.yaml` file and modify the template to match your requirements.

Variables in your YAML files (like `{topic}`) will be replaced with values from your inputs when running the crew:

Code

Copy

```python
crew.kickoff(inputs={'topic': 'AI Agents'})

```

Here’s an example of how to configure agents using YAML:

agents.yaml

Copy

```yaml
# src/latest_ai_development/config/agents.yaml
researcher:
  role: >
    {topic} Senior Data Researcher
  goal: >
    Uncover cutting-edge developments in {topic}
  backstory: >
    You're a seasoned researcher with a knack for uncovering the latest
    developments in {topic}. Known for your ability to find the most relevant
    information and present it in a clear and concise manner.

reporting_analyst:
  role: >
    {topic} Reporting Analyst
  goal: >
    Create detailed reports based on {topic} data analysis and research findings
  backstory: >
    You're a meticulous analyst with a keen eye for detail. You're known for
    your ability to turn complex data into clear and concise reports, making
    it easy for others to understand and act on the information you provide.

```

To use this YAML configuration in your code, create a crew class that inherits from `CrewBase`:

Code

Copy

```python
# src/latest_ai_development/crew.py
from crewai import Agent, Crew, Process
from crewai.project import CrewBase, agent, crew
from crewai_tools import SerperDevTool

@CrewBase
class LatestAiDevelopmentCrew():
  """LatestAiDevelopment crew"""

  agents_config = "config/agents.yaml"

  @agent
  def researcher(self) -> Agent:
    return Agent(
      config=self.agents_config['researcher'],
      verbose=True,
      tools=[SerperDevTool()]
    )

  @agent
  def reporting_analyst(self) -> Agent:
    return Agent(
      config=self.agents_config['reporting_analyst'],
      verbose=True
    )

```

The names you use in your YAML files ( `agents.yaml`) should match the method names in your Python code.

### [​](https://docs.crewai.com/concepts/agents\#direct-code-definition)  Direct Code Definition

You can create agents directly in code by instantiating the `Agent` class. Here’s a comprehensive example showing all available parameters:

Code

Copy

```python
from crewai import Agent
from crewai_tools import SerperDevTool

# Create an agent with all available parameters
agent = Agent(
    role="Senior Data Scientist",
    goal="Analyze and interpret complex datasets to provide actionable insights",
    backstory="With over 10 years of experience in data science and machine learning, "
              "you excel at finding patterns in complex datasets.",
    llm="gpt-4",  # Default: OPENAI_MODEL_NAME or "gpt-4"
    function_calling_llm=None,  # Optional: Separate LLM for tool calling
    memory=True,  # Default: True
    verbose=False,  # Default: False
    allow_delegation=False,  # Default: False
    max_iter=20,  # Default: 20 iterations
    max_rpm=None,  # Optional: Rate limit for API calls
    max_execution_time=None,  # Optional: Maximum execution time in seconds
    max_retry_limit=2,  # Default: 2 retries on error
    allow_code_execution=False,  # Default: False
    code_execution_mode="safe",  # Default: "safe" (options: "safe", "unsafe")
    respect_context_window=True,  # Default: True
    use_system_prompt=True,  # Default: True
    tools=[SerperDevTool()],  # Optional: List of tools
    knowledge_sources=None,  # Optional: List of knowledge sources
    embedder=None,  # Optional: Custom embedder configuration
    system_template=None,  # Optional: Custom system prompt template
    prompt_template=None,  # Optional: Custom prompt template
    response_template=None,  # Optional: Custom response template
    step_callback=None,  # Optional: Callback function for monitoring
)

```

Let’s break down some key parameter combinations for common use cases:

#### [​](https://docs.crewai.com/concepts/agents\#basic-research-agent)  Basic Research Agent

Code

Copy

```python
research_agent = Agent(
    role="Research Analyst",
    goal="Find and summarize information about specific topics",
    backstory="You are an experienced researcher with attention to detail",
    tools=[SerperDevTool()],
    verbose=True  # Enable logging for debugging
)

```

#### [​](https://docs.crewai.com/concepts/agents\#code-development-agent)  Code Development Agent

Code

Copy

```python
dev_agent = Agent(
    role="Senior Python Developer",
    goal="Write and debug Python code",
    backstory="Expert Python developer with 10 years of experience",
    allow_code_execution=True,
    code_execution_mode="safe",  # Uses Docker for safety
    max_execution_time=300,  # 5-minute timeout
    max_retry_limit=3  # More retries for complex code tasks
)

```

#### [​](https://docs.crewai.com/concepts/agents\#long-running-analysis-agent)  Long-Running Analysis Agent

Code

Copy

```python
analysis_agent = Agent(
    role="Data Analyst",
    goal="Perform deep analysis of large datasets",
    backstory="Specialized in big data analysis and pattern recognition",
    memory=True,
    respect_context_window=True,
    max_rpm=10,  # Limit API calls
    function_calling_llm="gpt-4o-mini"  # Cheaper model for tool calls
)

```

#### [​](https://docs.crewai.com/concepts/agents\#custom-template-agent)  Custom Template Agent

Code

Copy

```python
custom_agent = Agent(
    role="Customer Service Representative",
    goal="Assist customers with their inquiries",
    backstory="Experienced in customer support with a focus on satisfaction",
    system_template="""<|start_header_id|>system<|end_header_id|>
                        {{ .System }}<|eot_id|>""",
    prompt_template="""<|start_header_id|>user<|end_header_id|>
                        {{ .Prompt }}<|eot_id|>""",
    response_template="""<|start_header_id|>assistant<|end_header_id|>
                        {{ .Response }}<|eot_id|>""",
)

```

### [​](https://docs.crewai.com/concepts/agents\#parameter-details)  Parameter Details

#### [​](https://docs.crewai.com/concepts/agents\#critical-parameters)  Critical Parameters

- `role`, `goal`, and `backstory` are required and shape the agent’s behavior
- `llm` determines the language model used (default: OpenAI’s GPT-4)

#### [​](https://docs.crewai.com/concepts/agents\#memory-and-context)  Memory and Context

- `memory`: Enable to maintain conversation history
- `respect_context_window`: Prevents token limit issues
- `knowledge_sources`: Add domain-specific knowledge bases

#### [​](https://docs.crewai.com/concepts/agents\#execution-control)  Execution Control

- `max_iter`: Maximum attempts before giving best answer
- `max_execution_time`: Timeout in seconds
- `max_rpm`: Rate limiting for API calls
- `max_retry_limit`: Retries on error

#### [​](https://docs.crewai.com/concepts/agents\#code-execution)  Code Execution

- `allow_code_execution`: Must be True to run code
- `code_execution_mode`:

  - `"safe"`: Uses Docker (recommended for production)
  - `"unsafe"`: Direct execution (use only in trusted environments)

#### [​](https://docs.crewai.com/concepts/agents\#templates)  Templates

- `system_template`: Defines agent’s core behavior
- `prompt_template`: Structures input format
- `response_template`: Formats agent responses

When using custom templates, you can use variables like `{role}`, `{goal}`, and `{input}` in your templates. These will be automatically populated during execution.

## [​](https://docs.crewai.com/concepts/agents\#agent-tools)  Agent Tools

Agents can be equipped with various tools to enhance their capabilities. CrewAI supports tools from:

- [CrewAI Toolkit](https://github.com/joaomdmoura/crewai-tools)
- [LangChain Tools](https://python.langchain.com/docs/integrations/tools)

Here’s how to add tools to an agent:

Code

Copy

```python
from crewai import Agent
from crewai_tools import SerperDevTool, WikipediaTools

# Create tools
search_tool = SerperDevTool()
wiki_tool = WikipediaTools()

# Add tools to agent
researcher = Agent(
    role="AI Technology Researcher",
    goal="Research the latest AI developments",
    tools=[search_tool, wiki_tool],
    verbose=True
)

```

## [​](https://docs.crewai.com/concepts/agents\#agent-memory-and-context)  Agent Memory and Context

Agents can maintain memory of their interactions and use context from previous tasks. This is particularly useful for complex workflows where information needs to be retained across multiple tasks.

Code

Copy

```python
from crewai import Agent

analyst = Agent(
    role="Data Analyst",
    goal="Analyze and remember complex data patterns",
    memory=True,  # Enable memory
    verbose=True
)

```

When `memory` is enabled, the agent will maintain context across multiple interactions, improving its ability to handle complex, multi-step tasks.

## [​](https://docs.crewai.com/concepts/agents\#important-considerations-and-best-practices)  Important Considerations and Best Practices

### [​](https://docs.crewai.com/concepts/agents\#security-and-code-execution)  Security and Code Execution

- When using `allow_code_execution`, be cautious with user input and always validate it
- Use `code_execution_mode: "safe"` (Docker) in production environments
- Consider setting appropriate `max_execution_time` limits to prevent infinite loops

### [​](https://docs.crewai.com/concepts/agents\#performance-optimization)  Performance Optimization

- Use `respect_context_window: true` to prevent token limit issues
- Set appropriate `max_rpm` to avoid rate limiting
- Enable `cache: true` to improve performance for repetitive tasks
- Adjust `max_iter` and `max_retry_limit` based on task complexity

### [​](https://docs.crewai.com/concepts/agents\#memory-and-context-management)  Memory and Context Management

- Use `memory: true` for tasks requiring historical context
- Leverage `knowledge_sources` for domain-specific information
- Configure `embedder_config` when using custom embedding models
- Use custom templates ( `system_template`, `prompt_template`, `response_template`) for fine-grained control over agent behavior

### [​](https://docs.crewai.com/concepts/agents\#agent-collaboration)  Agent Collaboration

- Enable `allow_delegation: true` when agents need to work together
- Use `step_callback` to monitor and log agent interactions
- Consider using different LLMs for different purposes:
  - Main `llm` for complex reasoning
  - `function_calling_llm` for efficient tool usage

### [​](https://docs.crewai.com/concepts/agents\#model-compatibility)  Model Compatibility

- Set `use_system_prompt: false` for older models that don’t support system messages
- Ensure your chosen `llm` supports the features you need (like function calling)

## [​](https://docs.crewai.com/concepts/agents\#troubleshooting-common-issues)  Troubleshooting Common Issues

1. **Rate Limiting**: If you’re hitting API rate limits:
   - Implement appropriate `max_rpm`
   - Use caching for repetitive operations
   - Consider batching requests
2. **Context Window Errors**: If you’re exceeding context limits:
   - Enable `respect_context_window`
   - Use more efficient prompts
   - Clear agent memory periodically
3. **Code Execution Issues**: If code execution fails:
   - Verify Docker is installed for safe mode
   - Check execution permissions
   - Review code sandbox settings
4. **Memory Issues**: If agent responses seem inconsistent:
   - Verify memory is enabled
   - Check knowledge source configuration
   - Review conversation history management

Remember that agents are most effective when configured according to their specific use case. Take time to understand your requirements and adjust these parameters accordingly.

Was this page helpful?

YesNo

[Quickstart](https://docs.crewai.com/quickstart) [Tasks](https://docs.crewai.com/concepts/tasks)

On this page

- [Overview of an Agent](https://docs.crewai.com/concepts/agents#overview-of-an-agent)
- [Agent Attributes](https://docs.crewai.com/concepts/agents#agent-attributes)
- [Creating Agents](https://docs.crewai.com/concepts/agents#creating-agents)
- [YAML Configuration (Recommended)](https://docs.crewai.com/concepts/agents#yaml-configuration-recommended)
- [Direct Code Definition](https://docs.crewai.com/concepts/agents#direct-code-definition)
- [Basic Research Agent](https://docs.crewai.com/concepts/agents#basic-research-agent)
- [Code Development Agent](https://docs.crewai.com/concepts/agents#code-development-agent)
- [Long-Running Analysis Agent](https://docs.crewai.com/concepts/agents#long-running-analysis-agent)
- [Custom Template Agent](https://docs.crewai.com/concepts/agents#custom-template-agent)
- [Parameter Details](https://docs.crewai.com/concepts/agents#parameter-details)
- [Critical Parameters](https://docs.crewai.com/concepts/agents#critical-parameters)
- [Memory and Context](https://docs.crewai.com/concepts/agents#memory-and-context)
- [Execution Control](https://docs.crewai.com/concepts/agents#execution-control)
- [Code Execution](https://docs.crewai.com/concepts/agents#code-execution)
- [Templates](https://docs.crewai.com/concepts/agents#templates)
- [Agent Tools](https://docs.crewai.com/concepts/agents#agent-tools)
- [Agent Memory and Context](https://docs.crewai.com/concepts/agents#agent-memory-and-context)
- [Important Considerations and Best Practices](https://docs.crewai.com/concepts/agents#important-considerations-and-best-practices)
- [Security and Code Execution](https://docs.crewai.com/concepts/agents#security-and-code-execution)
- [Performance Optimization](https://docs.crewai.com/concepts/agents#performance-optimization)
- [Memory and Context Management](https://docs.crewai.com/concepts/agents#memory-and-context-management)
- [Agent Collaboration](https://docs.crewai.com/concepts/agents#agent-collaboration)
- [Model Compatibility](https://docs.crewai.com/concepts/agents#model-compatibility)
- [Troubleshooting Common Issues](https://docs.crewai.com/concepts/agents#troubleshooting-common-issues)

# Code Interpreter - CrewAI

[CrewAI home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/crewai/crew_only_logo.png)](https://docs.crewai.com/)

Search CrewAI docs

Ctrl K

Search...

Navigation

Tools

Code Interpreter

[Get Started](https://docs.crewai.com/introduction) [Examples](https://docs.crewai.com/examples/example)

# [​](https://docs.crewai.com/tools/codeinterpretertool\#codeinterpretertool)  `CodeInterpreterTool`

## [​](https://docs.crewai.com/tools/codeinterpretertool\#description)  Description

This tool enables the Agent to execute Python 3 code that it has generated autonomously. The code is run in a secure, isolated environment, ensuring safety regardless of the content.

This functionality is particularly valuable as it allows the Agent to create code, execute it within the same ecosystem,
obtain the results, and utilize that information to inform subsequent decisions and actions.

## [​](https://docs.crewai.com/tools/codeinterpretertool\#requirements)  Requirements

- Docker

## [​](https://docs.crewai.com/tools/codeinterpretertool\#installation)  Installation

Install the `crewai_tools` package

Copy

```shell
pip install 'crewai[tools]'

```

## [​](https://docs.crewai.com/tools/codeinterpretertool\#example)  Example

Remember that when using this tool, the code must be generated by the Agent itself.
The code must be a Python3 code. And it will take some time for the first time to run
because it needs to build the Docker image.

Code

Copy

```python
from crewai import Agent
from crewai_tools import CodeInterpreterTool

Agent(
    ...
    tools=[CodeInterpreterTool()],
)

```

We also provide a simple way to use it directly from the Agent.

Code

Copy

```python
from crewai import Agent

agent = Agent(
    ...
    allow_code_execution=True,
)

```

Was this page helpful?

YesNo

[Code Docs RAG Search](https://docs.crewai.com/tools/codedocssearchtool) [Composio Tool](https://docs.crewai.com/tools/composiotool)

On this page

- [CodeInterpreterTool](https://docs.crewai.com/tools/codeinterpretertool#codeinterpretertool)
- [Description](https://docs.crewai.com/tools/codeinterpretertool#description)
- [Requirements](https://docs.crewai.com/tools/codeinterpretertool#requirements)
- [Installation](https://docs.crewai.com/tools/codeinterpretertool#installation)
- [Example](https://docs.crewai.com/tools/codeinterpretertool#example)

