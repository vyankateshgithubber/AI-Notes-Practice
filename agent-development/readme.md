# Google Gen AI  

####  Day 1
1a -- Single Agent Creation
1b -- multi agent with patterns (deep dive)


####  Day 2 

n Tools => m api 
Tool --> function or program 
agent tool --> conversation is not handoff --> subagents 
human in loop --> 
documentation is paramount -> user clear descriptive name  
describe the action 
keep it task focused --> designe
return uri, structured output  
mcp --> lcp 

JSON RPC 2.0 -- MCP 

RAG on tools 

2a - agent tools (implmentations)
2b - long running tool & MCP tool implmentation     


ADK Tools Types
- Custom Tools
    - function tool 
    - Human in loop (long  running)
    - Agent tool => AgentTool(agent=)
    - MCP Tools
    - OpenAPI tools

- Built-in Tools
    - Gemini Tools (eg. BuiltInCodeExcutor,google_search)
    - Google Cloud Tools (BigQueryToolset, SpannerToolset ,APIHubToolset)
    - Third Party Tools  (Hugging Face, Firecrawl, GitHub Tools)



#### Day 3

Sessions  -- short term (single converstion)
    - it has Event and State
    - Event is building block of conversion history 
    - State is agent scratchpad, stores and updates dynmaic details needed during coverstion 
Memory -- longer term  (across multiple conversations)

 Session: They remember what you said 10 minutes ago in THIS conversation
🧠 Memory: They remember your preferences from conversations LAST WEEK

Session Service  -- storage layer
Runner -- orchestration layer 
    -  manages user and bot  converstion  

persistent session

Context Compaction - the act of compacting (summarizing) older conversation to reduce the size of the context that's sent to the model

InMemoryMemoryService ---> testing

VertexAiMemoryBankService --> Test

Ingest data using add_session_to_memory()
Enable retrieval by giving your agent memory tools (load_memory or preload_memory)



#### Day 4
Agent Observability  -  logs, traces and Metrics

1. logs - a record of single event, telling **what** happened at specific moment
2. Traces - A trace connects the logs into a single story, showing you **why** final result occurred by revealing the entire sequence of steps.
3. Metrics - Metrics are the summary numbers (like averages and error rates) that tell you **how** well the agent is performing overall.


[href] https://storage.googleapis.com/github-repo/kaggle-5days-ai/day4/observability-intro.png


Development debugging? → Use adk web --log_level DEBUG
Common production observability? → Use LoggingPlugin()
Custom requirements? → Build Custom Callbacks and Plugins

Which means assessing the agent's entire decision-making process - including the final response and the path it took to get the response (trajectory)!

