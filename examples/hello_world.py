from pydantic_ai import Agent

agent = Agent(  
    'anthropic:claude-haiku-4-5',
    instructions='Be detailed and comprehensive in your response.',  
)

result = agent.run_sync('Whats the best way to be profitable in 2026?')  
print(result.output)

