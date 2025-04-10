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

