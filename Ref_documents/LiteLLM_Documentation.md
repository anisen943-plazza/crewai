# Anthropic | liteLLM

[Skip to main content](https://docs.litellm.ai/docs/providers/anthropic#__docusaurus_skipToContent_fallback)

On this page

# Anthropic

LiteLLM supports all anthropic models.

- `claude-3.5` ( `claude-3-5-sonnet-20240620`)
- `claude-3` ( `claude-3-haiku-20240307`, `claude-3-opus-20240229`, `claude-3-sonnet-20240229`)
- `claude-2`
- `claude-2.1`
- `claude-instant-1.2`

| Property | Details |
| --- | --- |
| Description | Claude is a highly performant, trustworthy, and intelligent AI platform built by Anthropic. Claude excels at tasks involving language, reasoning, analysis, coding, and more. |
| Provider Route on LiteLLM | `anthropic/` (add this prefix to the model name, to route any requests to Anthropic - e.g. `anthropic/claude-3-5-sonnet-20240620`) |
| Provider Doc | [Anthropic ↗](https://docs.anthropic.com/en/docs/build-with-claude/overview) |
| API Endpoint for Provider | [https://api.anthropic.com](https://api.anthropic.com/) |
| Supported Endpoints | `/chat/completions` |

## Supported OpenAI Parameters [​](https://docs.litellm.ai/docs/providers/anthropic\#supported-openai-parameters "Direct link to Supported OpenAI Parameters")

Check this in code, [here](https://docs.litellm.ai/docs/completion/input#translated-openai-params)

```codeBlockLines_e6Vv
"stream",
"stop",
"temperature",
"top_p",
"max_tokens",
"max_completion_tokens",
"tools",
"tool_choice",
"extra_headers",
"parallel_tool_calls",
"response_format",
"user"

```

info

Anthropic API fails requests when `max_tokens` are not passed. Due to this litellm passes `max_tokens=4096` when no `max_tokens` are passed.

## API Keys [​](https://docs.litellm.ai/docs/providers/anthropic\#api-keys "Direct link to API Keys")

```codeBlockLines_e6Vv
import os

os.environ["ANTHROPIC_API_KEY"] = "your-api-key"
# os.environ["ANTHROPIC_API_BASE"] = "" # [OPTIONAL] or 'ANTHROPIC_BASE_URL'

```

## Usage [​](https://docs.litellm.ai/docs/providers/anthropic\#usage "Direct link to Usage")

```codeBlockLines_e6Vv
import os
from litellm import completion

# set env - [OPTIONAL] replace with your anthropic key
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

messages = [{"role": "user", "content": "Hey! how's it going?"}]
response = completion(model="claude-3-opus-20240229", messages=messages)
print(response)

```

## Usage - Streaming [​](https://docs.litellm.ai/docs/providers/anthropic\#usage---streaming "Direct link to Usage - Streaming")

Just set `stream=True` when calling completion.

```codeBlockLines_e6Vv
import os
from litellm import completion

# set env
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

messages = [{"role": "user", "content": "Hey! how's it going?"}]
response = completion(model="claude-3-opus-20240229", messages=messages, stream=True)
for chunk in response:
    print(chunk["choices"][0]["delta"]["content"])  # same as openai format

```

## Usage with LiteLLM Proxy [​](https://docs.litellm.ai/docs/providers/anthropic\#usage-with-litellm-proxy "Direct link to Usage with LiteLLM Proxy")

Here's how to call Anthropic with the LiteLLM Proxy Server

### 1\. Save key in your environment [​](https://docs.litellm.ai/docs/providers/anthropic\#1-save-key-in-your-environment "Direct link to 1. Save key in your environment")

```codeBlockLines_e6Vv
export ANTHROPIC_API_KEY="your-api-key"

```

### 2\. Start the proxy [​](https://docs.litellm.ai/docs/providers/anthropic\#2-start-the-proxy "Direct link to 2. Start the proxy")

- config.yaml
- config - default all Anthropic Model
- cli

```codeBlockLines_e6Vv
model_list:
  - model_name: claude-3 ### RECEIVED MODEL NAME ###
    litellm_params: # all params accepted by litellm.completion() - https://docs.litellm.ai/docs/completion/input
      model: claude-3-opus-20240229 ### MODEL NAME sent to `litellm.completion()` ###
      api_key: "os.environ/ANTHROPIC_API_KEY" # does os.getenv("AZURE_API_KEY_EU")

```

```codeBlockLines_e6Vv
litellm --config /path/to/config.yaml

```

Use this if you want to make requests to `claude-3-haiku-20240307`, `claude-3-opus-20240229`, `claude-2.1` without defining them on the config.yaml

#### Required env variables [​](https://docs.litellm.ai/docs/providers/anthropic\#required-env-variables "Direct link to Required env variables")

```codeBlockLines_e6Vv
ANTHROPIC_API_KEY=sk-ant****

```

```codeBlockLines_e6Vv
model_list:
  - model_name: "*"
    litellm_params:
      model: "*"

```

```codeBlockLines_e6Vv
litellm --config /path/to/config.yaml

```

Example Request for this config.yaml

**Ensure you use `anthropic/` prefix to route the request to Anthropic API**

```codeBlockLines_e6Vv
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "anthropic/claude-3-haiku-20240307",
      "messages": [\
        {\
          "role": "user",\
          "content": "what llm are you"\
        }\
      ]
    }
'

```

```codeBlockLines_e6Vv
$ litellm --model claude-3-opus-20240229

# Server running on http://0.0.0.0:4000

```

### 3\. Test it [​](https://docs.litellm.ai/docs/providers/anthropic\#3-test-it "Direct link to 3. Test it")

- Curl Request
- OpenAI v1.0.0+
- Langchain

```codeBlockLines_e6Vv
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "claude-3",
      "messages": [\
        {\
          "role": "user",\
          "content": "what llm are you"\
        }\
      ]
    }
'

```

```codeBlockLines_e6Vv
import openai
client = openai.OpenAI(
    api_key="anything",
    base_url="http://0.0.0.0:4000"
)

# request sent to model set on litellm proxy, `litellm --model`
response = client.chat.completions.create(model="claude-3", messages = [\
    {\
        "role": "user",\
        "content": "this is a test request, write a short poem"\
    }\
])

print(response)

```

```codeBlockLines_e6Vv
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage

chat = ChatOpenAI(
    openai_api_base="http://0.0.0.0:4000", # set openai_api_base to the LiteLLM Proxy
    model = "claude-3",
    temperature=0.1
)

messages = [\
    SystemMessage(\
        content="You are a helpful assistant that im using to make a test request to."\
    ),\
    HumanMessage(\
        content="test from litellm. tell me why it's amazing in 1 sentence"\
    ),\
]
response = chat(messages)

print(response)

```

## Supported Models [​](https://docs.litellm.ai/docs/providers/anthropic\#supported-models "Direct link to Supported Models")

`Model Name` 👉 Human-friendly name.

`Function Call` 👉 How to call the model in LiteLLM.

| Model Name | Function Call |
| --- | --- |
| claude-3-5-sonnet | `completion('claude-3-5-sonnet-20240620', messages)` |
| claude-3-haiku | `completion('claude-3-haiku-20240307', messages)` |
| claude-3-opus | `completion('claude-3-opus-20240229', messages)` |
| claude-3-5-sonnet-20240620 | `completion('claude-3-5-sonnet-20240620', messages)` |
| claude-3-sonnet | `completion('claude-3-sonnet-20240229', messages)` |
| claude-2.1 | `completion('claude-2.1', messages)` |
| claude-2 | `completion('claude-2', messages)` |
| claude-instant-1.2 | `completion('claude-instant-1.2', messages)` |
| claude-instant-1 | `completion('claude-instant-1', messages)` |

## **Prompt Caching** [​](https://docs.litellm.ai/docs/providers/anthropic\#prompt-caching "Direct link to prompt-caching")

Use Anthropic Prompt Caching

[Relevant Anthropic API Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)

note

Here's what a sample Raw Request from LiteLLM for Anthropic Context Caching looks like:

```codeBlockLines_e6Vv
POST Request Sent from LiteLLM:
curl -X POST \
https://api.anthropic.com/v1/messages \
-H 'accept: application/json' -H 'anthropic-version: 2023-06-01' -H 'content-type: application/json' -H 'x-api-key: sk-...' -H 'anthropic-beta: prompt-caching-2024-07-31' \
-d '{'model': 'claude-3-5-sonnet-20240620', [\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "text",\
          "text": "What are the key terms and conditions in this agreement?",\
          "cache_control": {\
            "type": "ephemeral"\
          }\
        }\
      ]\
    },\
    {\
      "role": "assistant",\
      "content": [\
        {\
          "type": "text",\
          "text": "Certainly! The key terms and conditions are the following: the contract is 1 year long for $10/mo"\
        }\
      ]\
    }\
  ],
  "temperature": 0.2,
  "max_tokens": 10
}'

```

### Caching - Large Context Caching [​](https://docs.litellm.ai/docs/providers/anthropic\#caching---large-context-caching "Direct link to Caching - Large Context Caching")

This example demonstrates basic Prompt Caching usage, caching the full text of the legal agreement as a prefix while keeping the user instruction uncached.

- LiteLLM SDK
- LiteLLM Proxy

```codeBlockLines_e6Vv
response = await litellm.acompletion(
    model="anthropic/claude-3-5-sonnet-20240620",
    messages=[\
        {\
            "role": "system",\
            "content": [\
                {\
                    "type": "text",\
                    "text": "You are an AI assistant tasked with analyzing legal documents.",\
                },\
                {\
                    "type": "text",\
                    "text": "Here is the full text of a complex legal agreement",\
                    "cache_control": {"type": "ephemeral"},\
                },\
            ],\
        },\
        {\
            "role": "user",\
            "content": "what are the key terms and conditions in this agreement?",\
        },\
    ]
)

```

info

LiteLLM Proxy is OpenAI compatible

This is an example using the OpenAI Python SDK sending a request to LiteLLM Proxy

Assuming you have a model= `anthropic/claude-3-5-sonnet-20240620` on the [litellm proxy config.yaml](https://docs.litellm.ai/docs/providers/anthropic#usage-with-litellm-proxy)

```codeBlockLines_e6Vv
import openai
client = openai.AsyncOpenAI(
    api_key="anything",            # litellm proxy api key
    base_url="http://0.0.0.0:4000" # litellm proxy base url
)

response = await client.chat.completions.create(
    model="anthropic/claude-3-5-sonnet-20240620",
    messages=[\
        {\
            "role": "system",\
            "content": [\
                {\
                    "type": "text",\
                    "text": "You are an AI assistant tasked with analyzing legal documents.",\
                },\
                {\
                    "type": "text",\
                    "text": "Here is the full text of a complex legal agreement",\
                    "cache_control": {"type": "ephemeral"},\
                },\
            ],\
        },\
        {\
            "role": "user",\
            "content": "what are the key terms and conditions in this agreement?",\
        },\
    ]
)

```

### Caching - Tools definitions [​](https://docs.litellm.ai/docs/providers/anthropic\#caching---tools-definitions "Direct link to Caching - Tools definitions")

In this example, we demonstrate caching tool definitions.

The cache\_control parameter is placed on the final tool

- LiteLLM SDK
- LiteLLM Proxy

```codeBlockLines_e6Vv
import litellm

response = await litellm.acompletion(
    model="anthropic/claude-3-5-sonnet-20240620",
    messages = [{"role": "user", "content": "What's the weather like in Boston today?"}]
    tools = [\
        {\
            "type": "function",\
            "function": {\
                "name": "get_current_weather",\
                "description": "Get the current weather in a given location",\
                "parameters": {\
                    "type": "object",\
                    "properties": {\
                        "location": {\
                            "type": "string",\
                            "description": "The city and state, e.g. San Francisco, CA",\
                        },\
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},\
                    },\
                    "required": ["location"],\
                },\
                "cache_control": {"type": "ephemeral"}\
            },\
        }\
    ]
)

```

info

LiteLLM Proxy is OpenAI compatible

This is an example using the OpenAI Python SDK sending a request to LiteLLM Proxy

Assuming you have a model= `anthropic/claude-3-5-sonnet-20240620` on the [litellm proxy config.yaml](https://docs.litellm.ai/docs/providers/anthropic#usage-with-litellm-proxy)

```codeBlockLines_e6Vv
import openai
client = openai.AsyncOpenAI(
    api_key="anything",            # litellm proxy api key
    base_url="http://0.0.0.0:4000" # litellm proxy base url
)

response = await client.chat.completions.create(
    model="anthropic/claude-3-5-sonnet-20240620",
    messages = [{"role": "user", "content": "What's the weather like in Boston today?"}]
    tools = [\
        {\
            "type": "function",\
            "function": {\
                "name": "get_current_weather",\
                "description": "Get the current weather in a given location",\
                "parameters": {\
                    "type": "object",\
                    "properties": {\
                        "location": {\
                            "type": "string",\
                            "description": "The city and state, e.g. San Francisco, CA",\
                        },\
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},\
                    },\
                    "required": ["location"],\
                },\
                "cache_control": {"type": "ephemeral"}\
            },\
        }\
    ]
)

```

### Caching - Continuing Multi-Turn Convo [​](https://docs.litellm.ai/docs/providers/anthropic\#caching---continuing-multi-turn-convo "Direct link to Caching - Continuing Multi-Turn Convo")

In this example, we demonstrate how to use Prompt Caching in a multi-turn conversation.

The cache\_control parameter is placed on the system message to designate it as part of the static prefix.

The conversation history (previous messages) is included in the messages array. The final turn is marked with cache-control, for continuing in followups. The second-to-last user message is marked for caching with the cache\_control parameter, so that this checkpoint can read from the previous cache.

- LiteLLM SDK
- LiteLLM Proxy

```codeBlockLines_e6Vv
import litellm

response = await litellm.acompletion(
    model="anthropic/claude-3-5-sonnet-20240620",
    messages=[\
        # System Message\
        {\
            "role": "system",\
            "content": [\
                {\
                    "type": "text",\
                    "text": "Here is the full text of a complex legal agreement"\
                    * 400,\
                    "cache_control": {"type": "ephemeral"},\
                }\
            ],\
        },\
        # marked for caching with the cache_control parameter, so that this checkpoint can read from the previous cache.\
        {\
            "role": "user",\
            "content": [\
                {\
                    "type": "text",\
                    "text": "What are the key terms and conditions in this agreement?",\
                    "cache_control": {"type": "ephemeral"},\
                }\
            ],\
        },\
        {\
            "role": "assistant",\
            "content": "Certainly! the key terms and conditions are the following: the contract is 1 year long for $10/mo",\
        },\
        # The final turn is marked with cache-control, for continuing in followups.\
        {\
            "role": "user",\
            "content": [\
                {\
                    "type": "text",\
                    "text": "What are the key terms and conditions in this agreement?",\
                    "cache_control": {"type": "ephemeral"},\
                }\
            ],\
        },\
    ]
)

```

info

LiteLLM Proxy is OpenAI compatible

This is an example using the OpenAI Python SDK sending a request to LiteLLM Proxy

Assuming you have a model= `anthropic/claude-3-5-sonnet-20240620` on the [litellm proxy config.yaml](https://docs.litellm.ai/docs/providers/anthropic#usage-with-litellm-proxy)

```codeBlockLines_e6Vv
import openai
client = openai.AsyncOpenAI(
    api_key="anything",            # litellm proxy api key
    base_url="http://0.0.0.0:4000" # litellm proxy base url
)

response = await client.chat.completions.create(
    model="anthropic/claude-3-5-sonnet-20240620",
    messages=[\
        # System Message\
        {\
            "role": "system",\
            "content": [\
                {\
                    "type": "text",\
                    "text": "Here is the full text of a complex legal agreement"\
                    * 400,\
                    "cache_control": {"type": "ephemeral"},\
                }\
            ],\
        },\
        # marked for caching with the cache_control parameter, so that this checkpoint can read from the previous cache.\
        {\
            "role": "user",\
            "content": [\
                {\
                    "type": "text",\
                    "text": "What are the key terms and conditions in this agreement?",\
                    "cache_control": {"type": "ephemeral"},\
                }\
            ],\
        },\
        {\
            "role": "assistant",\
            "content": "Certainly! the key terms and conditions are the following: the contract is 1 year long for $10/mo",\
        },\
        # The final turn is marked with cache-control, for continuing in followups.\
        {\
            "role": "user",\
            "content": [\
                {\
                    "type": "text",\
                    "text": "What are the key terms and conditions in this agreement?",\
                    "cache_control": {"type": "ephemeral"},\
                }\
            ],\
        },\
    ]
)

```

## **Function/Tool Calling** [​](https://docs.litellm.ai/docs/providers/anthropic\#functiontool-calling "Direct link to functiontool-calling")

info

LiteLLM now uses Anthropic's 'tool' param 🎉 (v1.34.29+)

```codeBlockLines_e6Vv
from litellm import completion

# set env
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

tools = [\
    {\
        "type": "function",\
        "function": {\
            "name": "get_current_weather",\
            "description": "Get the current weather in a given location",\
            "parameters": {\
                "type": "object",\
                "properties": {\
                    "location": {\
                        "type": "string",\
                        "description": "The city and state, e.g. San Francisco, CA",\
                    },\
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},\
                },\
                "required": ["location"],\
            },\
        },\
    }\
]
messages = [{"role": "user", "content": "What's the weather like in Boston today?"}]

response = completion(
    model="anthropic/claude-3-opus-20240229",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)
# Add any assertions, here to check response args
print(response)
assert isinstance(response.choices[0].message.tool_calls[0].function.name, str)
assert isinstance(
    response.choices[0].message.tool_calls[0].function.arguments, str
)

```

### Forcing Anthropic Tool Use [​](https://docs.litellm.ai/docs/providers/anthropic\#forcing-anthropic-tool-use "Direct link to Forcing Anthropic Tool Use")

If you want Claude to use a specific tool to answer the user’s question

You can do this by specifying the tool in the `tool_choice` field like so:

```codeBlockLines_e6Vv
response = completion(
    model="anthropic/claude-3-opus-20240229",
    messages=messages,
    tools=tools,
    tool_choice={"type": "tool", "name": "get_weather"},
)

```

### Parallel Function Calling [​](https://docs.litellm.ai/docs/providers/anthropic\#parallel-function-calling "Direct link to Parallel Function Calling")

Here's how to pass the result of a function call back to an anthropic model:

```codeBlockLines_e6Vv
from litellm import completion
import os

os.environ["ANTHROPIC_API_KEY"] = "sk-ant.."

litellm.set_verbose = True

### 1ST FUNCTION CALL ###
tools = [\
    {\
        "type": "function",\
        "function": {\
            "name": "get_current_weather",\
            "description": "Get the current weather in a given location",\
            "parameters": {\
                "type": "object",\
                "properties": {\
                    "location": {\
                        "type": "string",\
                        "description": "The city and state, e.g. San Francisco, CA",\
                    },\
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},\
                },\
                "required": ["location"],\
            },\
        },\
    }\
]
messages = [\
    {\
        "role": "user",\
        "content": "What's the weather like in Boston today in Fahrenheit?",\
    }\
]
try:
    # test without max tokens
    response = completion(
        model="anthropic/claude-3-opus-20240229",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    # Add any assertions, here to check response args
    print(response)
    assert isinstance(response.choices[0].message.tool_calls[0].function.name, str)
    assert isinstance(
        response.choices[0].message.tool_calls[0].function.arguments, str
    )

    messages.append(
        response.choices[0].message.model_dump()
    )  # Add assistant tool invokes
    tool_result = (
        '{"location": "Boston", "temperature": "72", "unit": "fahrenheit"}'
    )
    # Add user submitted tool results in the OpenAI format
    messages.append(
        {
            "tool_call_id": response.choices[0].message.tool_calls[0].id,
            "role": "tool",
            "name": response.choices[0].message.tool_calls[0].function.name,
            "content": tool_result,
        }
    )
    ### 2ND FUNCTION CALL ###
    # In the second response, Claude should deduce answer from tool results
    second_response = completion(
        model="anthropic/claude-3-opus-20240229",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    print(second_response)
except Exception as e:
    print(f"An error occurred - {str(e)}")

```

s/o @ [Shekhar Patnaik](https://www.linkedin.com/in/patnaikshekhar) for requesting this!

### Computer Tools [​](https://docs.litellm.ai/docs/providers/anthropic\#computer-tools "Direct link to Computer Tools")

```codeBlockLines_e6Vv
from litellm import completion

tools = [\
    {\
        "type": "computer_20241022",\
        "function": {\
            "name": "computer",\
            "parameters": {\
                "display_height_px": 100,\
                "display_width_px": 100,\
                "display_number": 1,\
            },\
        },\
    }\
]
model = "claude-3-5-sonnet-20241022"
messages = [{"role": "user", "content": "Save a picture of a cat to my desktop."}]

resp = completion(
    model=model,
    messages=messages,
    tools=tools,
    # headers={"anthropic-beta": "computer-use-2024-10-22"},
)

print(resp)

```

## Usage - Vision [​](https://docs.litellm.ai/docs/providers/anthropic\#usage---vision "Direct link to Usage - Vision")

```codeBlockLines_e6Vv
from litellm import completion

# set env
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

def encode_image(image_path):
    import base64

    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_path = "../proxy/cached_logo.jpg"
# Getting the base64 string
base64_image = encode_image(image_path)
resp = litellm.completion(
    model="anthropic/claude-3-opus-20240229",
    messages=[\
        {\
            "role": "user",\
            "content": [\
                {"type": "text", "text": "Whats in this image?"},\
                {\
                    "type": "image_url",\
                    "image_url": {\
                        "url": "data:image/jpeg;base64," + base64_image\
                    },\
                },\
            ],\
        }\
    ],
)
print(f"\nResponse: {resp}")

```

## Usage - Thinking / `reasoning_content` [​](https://docs.litellm.ai/docs/providers/anthropic\#usage---thinking--reasoning_content "Direct link to usage---thinking--reasoning_content")

- SDK
- PROXY

```codeBlockLines_e6Vv
from litellm import completion

resp = completion(
    model="anthropic/claude-3-7-sonnet-20250219",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
    thinking={"type": "enabled", "budget_tokens": 1024},
)

```

1. Setup config.yaml

```codeBlockLines_e6Vv
- model_name: claude-3-7-sonnet-20250219
  litellm_params:
    model: anthropic/claude-3-7-sonnet-20250219
    api_key: os.environ/ANTHROPIC_API_KEY

```

2. Start proxy

```codeBlockLines_e6Vv
litellm --config /path/to/config.yaml

```

3. Test it!

```codeBlockLines_e6Vv
curl http://0.0.0.0:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <YOUR-LITELLM-KEY>" \
  -d '{
    "model": "claude-3-7-sonnet-20250219",
    "messages": [{"role": "user", "content": "What is the capital of France?"}],
    "thinking": {"type": "enabled", "budget_tokens": 1024}
  }'

```

**Expected Response**

```codeBlockLines_e6Vv
ModelResponse(
    id='chatcmpl-c542d76d-f675-4e87-8e5f-05855f5d0f5e',
    created=1740470510,
    model='claude-3-7-sonnet-20250219',
    object='chat.completion',
    system_fingerprint=None,
    choices=[\
        Choices(\
            finish_reason='stop',\
            index=0,\
            message=Message(\
                content="The capital of France is Paris.",\
                role='assistant',\
                tool_calls=None,\
                function_call=None,\
                provider_specific_fields={\
                    'citations': None,\
                    'thinking_blocks': [\
                        {\
                            'type': 'thinking',\
                            'thinking': 'The capital of France is Paris. This is a very straightforward factual question.',\
                            'signature': 'EuYBCkQYAiJAy6...'\
                        }\
                    ]\
                }\
            ),\
            thinking_blocks=[\
                {\
                    'type': 'thinking',\
                    'thinking': 'The capital of France is Paris. This is a very straightforward factual question.',\
                    'signature': 'EuYBCkQYAiJAy6AGB...'\
                }\
            ],\
            reasoning_content='The capital of France is Paris. This is a very straightforward factual question.'\
        )\
    ],
    usage=Usage(
        completion_tokens=68,
        prompt_tokens=42,
        total_tokens=110,
        completion_tokens_details=None,
        prompt_tokens_details=PromptTokensDetailsWrapper(
            audio_tokens=None,
            cached_tokens=0,
            text_tokens=None,
            image_tokens=None
        ),
        cache_creation_input_tokens=0,
        cache_read_input_tokens=0
    )
)

```

## **Passing Extra Headers to Anthropic API** [​](https://docs.litellm.ai/docs/providers/anthropic\#passing-extra-headers-to-anthropic-api "Direct link to passing-extra-headers-to-anthropic-api")

Pass `extra_headers: dict` to `litellm.completion`

```codeBlockLines_e6Vv
from litellm import completion
messages = [{"role": "user", "content": "What is Anthropic?"}]
response = completion(
    model="claude-3-5-sonnet-20240620",
    messages=messages,
    extra_headers={"anthropic-beta": "max-tokens-3-5-sonnet-2024-07-15"}
)

```

## Usage - "Assistant Pre-fill" [​](https://docs.litellm.ai/docs/providers/anthropic\#usage---assistant-pre-fill "Direct link to Usage - \"Assistant Pre-fill\"")

You can "put words in Claude's mouth" by including an `assistant` role message as the last item in the `messages` array.

> \[!IMPORTANT\]
> The returned completion will _not_ include your "pre-fill" text, since it is part of the prompt itself. Make sure to prefix Claude's completion with your pre-fill.

```codeBlockLines_e6Vv
import os
from litellm import completion

# set env - [OPTIONAL] replace with your anthropic key
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

messages = [\
    {"role": "user", "content": "How do you say 'Hello' in German? Return your answer as a JSON object, like this:\n\n{ \"Hello\": \"Hallo\" }"},\
    {"role": "assistant", "content": "{"},\
]
response = completion(model="claude-2.1", messages=messages)
print(response)

```

#### Example prompt sent to Claude [​](https://docs.litellm.ai/docs/providers/anthropic\#example-prompt-sent-to-claude "Direct link to Example prompt sent to Claude")

```codeBlockLines_e6Vv

Human: How do you say 'Hello' in German? Return your answer as a JSON object, like this:

{ "Hello": "Hallo" }

Assistant: {

```

## Usage - "System" messages [​](https://docs.litellm.ai/docs/providers/anthropic\#usage---system-messages "Direct link to Usage - \"System\" messages")

If you're using Anthropic's Claude 2.1, `system` role messages are properly formatted for you.

```codeBlockLines_e6Vv
import os
from litellm import completion

# set env - [OPTIONAL] replace with your anthropic key
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

messages = [\
    {"role": "system", "content": "You are a snarky assistant."},\
    {"role": "user", "content": "How do I boil water?"},\
]
response = completion(model="claude-2.1", messages=messages)

```

#### Example prompt sent to Claude [​](https://docs.litellm.ai/docs/providers/anthropic\#example-prompt-sent-to-claude-1 "Direct link to Example prompt sent to Claude")

```codeBlockLines_e6Vv
You are a snarky assistant.

Human: How do I boil water?

Assistant:

```

## Usage - PDF [​](https://docs.litellm.ai/docs/providers/anthropic\#usage---pdf "Direct link to Usage - PDF")

Pass base64 encoded PDF files to Anthropic models using the `image_url` field.

- SDK
- proxy

### **using base64** [​](https://docs.litellm.ai/docs/providers/anthropic\#using-base64 "Direct link to using-base64")

```codeBlockLines_e6Vv
from litellm import completion, supports_pdf_input
import base64
import requests

# URL of the file
url = "https://storage.googleapis.com/cloud-samples-data/generative-ai/pdf/2403.05530.pdf"

# Download the file
response = requests.get(url)
file_data = response.content

encoded_file = base64.b64encode(file_data).decode("utf-8")

## check if model supports pdf input - (2024/11/11) only claude-3-5-haiku-20241022 supports it
supports_pdf_input("anthropic/claude-3-5-haiku-20241022") # True

response = completion(
    model="anthropic/claude-3-5-haiku-20241022",
    messages=[\
        {\
            "role": "user",\
            "content": [\
                {"type": "text", "text": "You are a very professional document summarization specialist. Please summarize the given document."},\
                {\
                    "type": "image_url",\
                    "image_url": f"data:application/pdf;base64,{encoded_file}", # 👈 PDF\
                },\
            ],\
        }\
    ],
    max_tokens=300,
)

print(response.choices[0])

```

1. Add model to config

```codeBlockLines_e6Vv
- model_name: claude-3-5-haiku-20241022
  litellm_params:
    model: anthropic/claude-3-5-haiku-20241022
    api_key: os.environ/ANTHROPIC_API_KEY

```

2. Start Proxy

```codeBlockLines_e6Vv
litellm --config /path/to/config.yaml

```

3. Test it!

```codeBlockLines_e6Vv
curl http://0.0.0.0:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <YOUR-LITELLM-KEY>" \
  -d '{
    "model": "claude-3-5-haiku-20241022",
    "messages": [\
      {\
        "role": "user",\
        "content": [\
          {\
            "type": "text",\
            "text": "You are a very professional document summarization specialist. Please summarize the given document"\
          },\
          {\
                "type": "image_url",\
                "image_url": "data:application/pdf;base64,{encoded_file}" # 👈 PDF\
            }\
          }\
        ]\
      }\
    ],
    "max_tokens": 300
  }'

```

## \[BETA\] Citations API [​](https://docs.litellm.ai/docs/providers/anthropic\#beta-citations-api "Direct link to beta-citations-api")

Pass `citations: {"enabled": true}` to Anthropic, to get citations on your document responses.

Note: This interface is in BETA. If you have feedback on how citations should be returned, please [tell us here](https://github.com/BerriAI/litellm/issues/7970#issuecomment-2644437943)

- SDK
- PROXY

```codeBlockLines_e6Vv
from litellm import completion

resp = completion(
    model="claude-3-5-sonnet-20241022",
    messages=[\
        {\
            "role": "user",\
            "content": [\
                {\
                    "type": "document",\
                    "source": {\
                        "type": "text",\
                        "media_type": "text/plain",\
                        "data": "The grass is green. The sky is blue.",\
                    },\
                    "title": "My Document",\
                    "context": "This is a trustworthy document.",\
                    "citations": {"enabled": True},\
                },\
                {\
                    "type": "text",\
                    "text": "What color is the grass and sky?",\
                },\
            ],\
        }\
    ],
)

citations = resp.choices[0].message.provider_specific_fields["citations"]

assert citations is not None

```

1. Setup config.yaml

```codeBlockLines_e6Vv
model_list:
    - model_name: anthropic-claude
      litellm_params:
        model: anthropic/claude-3-5-sonnet-20241022
        api_key: os.environ/ANTHROPIC_API_KEY

```

2. Start proxy

```codeBlockLines_e6Vv
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000

```

3. Test it!

```codeBlockLines_e6Vv
curl -L -X POST 'http://0.0.0.0:4000/v1/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{
  "model": "anthropic-claude",
  "messages": [\
    {\
        "role": "user",\
        "content": [\
            {\
                "type": "document",\
                "source": {\
                    "type": "text",\
                    "media_type": "text/plain",\
                    "data": "The grass is green. The sky is blue.",\
                },\
                "title": "My Document",\
                "context": "This is a trustworthy document.",\
                "citations": {"enabled": True},\
            },\
            {\
                "type": "text",\
                "text": "What color is the grass and sky?",\
            },\
        ],\
    }\
  ]
}'

```

## Usage - passing 'user\_id' to Anthropic [​](https://docs.litellm.ai/docs/providers/anthropic\#usage---passing-user_id-to-anthropic "Direct link to Usage - passing 'user_id' to Anthropic")

LiteLLM translates the OpenAI `user` param to Anthropic's `metadata[user_id]` param.

- SDK
- PROXY

```codeBlockLines_e6Vv
response = completion(
    model="claude-3-5-sonnet-20240620",
    messages=messages,
    user="user_123",
)

```

1. Setup config.yaml

```codeBlockLines_e6Vv
model_list:
    - model_name: claude-3-5-sonnet-20240620
      litellm_params:
        model: anthropic/claude-3-5-sonnet-20240620
        api_key: os.environ/ANTHROPIC_API_KEY

```

2. Start Proxy

```codeBlockLines_e6Vv
litellm --config /path/to/config.yaml

```

3. Test it!

```codeBlockLines_e6Vv
curl http://0.0.0.0:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <YOUR-LITELLM-KEY>" \
  -d '{
    "model": "claude-3-5-sonnet-20240620",
    "messages": [{"role": "user", "content": "What is Anthropic?"}],
    "user": "user_123"
  }'

```

- [Supported OpenAI Parameters](https://docs.litellm.ai/docs/providers/anthropic#supported-openai-parameters)
- [API Keys](https://docs.litellm.ai/docs/providers/anthropic#api-keys)
- [Usage](https://docs.litellm.ai/docs/providers/anthropic#usage)
- [Usage - Streaming](https://docs.litellm.ai/docs/providers/anthropic#usage---streaming)
- [Usage with LiteLLM Proxy](https://docs.litellm.ai/docs/providers/anthropic#usage-with-litellm-proxy)
  - [1\. Save key in your environment](https://docs.litellm.ai/docs/providers/anthropic#1-save-key-in-your-environment)
  - [2\. Start the proxy](https://docs.litellm.ai/docs/providers/anthropic#2-start-the-proxy)
  - [3\. Test it](https://docs.litellm.ai/docs/providers/anthropic#3-test-it)
- [Supported Models](https://docs.litellm.ai/docs/providers/anthropic#supported-models)
- [**Prompt Caching**](https://docs.litellm.ai/docs/providers/anthropic#prompt-caching)
  - [Caching - Large Context Caching](https://docs.litellm.ai/docs/providers/anthropic#caching---large-context-caching)
  - [Caching - Tools definitions](https://docs.litellm.ai/docs/providers/anthropic#caching---tools-definitions)
  - [Caching - Continuing Multi-Turn Convo](https://docs.litellm.ai/docs/providers/anthropic#caching---continuing-multi-turn-convo)
- [**Function/Tool Calling**](https://docs.litellm.ai/docs/providers/anthropic#functiontool-calling)
  - [Forcing Anthropic Tool Use](https://docs.litellm.ai/docs/providers/anthropic#forcing-anthropic-tool-use)
  - [Parallel Function Calling](https://docs.litellm.ai/docs/providers/anthropic#parallel-function-calling)
  - [Computer Tools](https://docs.litellm.ai/docs/providers/anthropic#computer-tools)
- [Usage - Vision](https://docs.litellm.ai/docs/providers/anthropic#usage---vision)
- [Usage - Thinking / `reasoning_content`](https://docs.litellm.ai/docs/providers/anthropic#usage---thinking--reasoning_content)
- [**Passing Extra Headers to Anthropic API**](https://docs.litellm.ai/docs/providers/anthropic#passing-extra-headers-to-anthropic-api)
- [Usage - "Assistant Pre-fill"](https://docs.litellm.ai/docs/providers/anthropic#usage---assistant-pre-fill)
- [Usage - "System" messages](https://docs.litellm.ai/docs/providers/anthropic#usage---system-messages)
- [Usage - PDF](https://docs.litellm.ai/docs/providers/anthropic#usage---pdf)
  - [**using base64**](https://docs.litellm.ai/docs/providers/anthropic#using-base64)
- [BETA Citations API](https://docs.litellm.ai/docs/providers/anthropic#beta-citations-api)
- [Usage - passing 'user\_id' to Anthropic](https://docs.litellm.ai/docs/providers/anthropic#usage---passing-user_id-to-anthropic)

