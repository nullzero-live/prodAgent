import tools
import agents
import storage

#init_llm()

def get_chat_history(chain_memory):
    memory_key = chain_memory.memory_key
    chat_history = chain_memory.load_memory_variables(memory_key)[memory_key]
    return chat_history

def get_new_instructions(meta_output):
    delimiter = 'Insightts: '
    new_instructions = meta_output[meta_output.find(delimiter)+len(delimiter):]
    return new_instructions


def main(task, max_iters=3, max_meta_iters=5):
    
    
    instructions = 'None'
    for i in range(max_meta_iters):
        print(f'[Episode {i+1}/{max_meta_iters}]')
        chain = agents.interviewer(instructions, memory=None)
        output = chain.predict(founder_input=task)
        for j in range(max_iters):
            print(f'(Step {j+1}/{max_iters})')
            print(f'Expert: {output}')
            print(f'Founder: ')
            
            output = chain.predict(founder_input=task)
        
        meta_chain = agents.initialize_expert_chain()
        meta_output = meta_chain.predict(chat_history=get_chat_history(chain.memory))
        print(f'Feedback: {meta_output}')
        instructions = get_new_instructions(meta_output)
        print(f'New Instructions: {instructions}')
        print('\n'+'#'*80+'\n')
    print('Done!')
    # write a one shot agent to summarize the findings
    
task = "My startup idea is to create a new social media platform that is more private and secure than Facebook."

main(task)