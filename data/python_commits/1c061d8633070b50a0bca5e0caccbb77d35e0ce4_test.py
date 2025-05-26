
    """
the following is written by gptchat. it needs some work to integrate it with this library, 
I just wanted to copy it here to work on later

it's 3 classes to create identities that can have conversations with each other and remember them. 
it's a bit of a mess. I'll clean it up later. if you run stuff on it now it just generates an ever lengthening prompt,
that repeats itself over and over until you reach the token limit. maybe use the GPTtext.get_summary() function to get a 
summary of the conversation that stays under the token limit?


class Memory:
    def __init__(self):
        self.data = {}  # Initialize the data attribute as an empty dictionary

    def add_interaction(self, text: str, response: str):
        # Store the current interaction in the data attribute
        self.data[time.time()] = {
            "input": text,
            "output": response
        }

    def generate_summary(self) -> str:
        # Generate a summary of past interactions by concatenating the input and output of each interaction
        summary = ""
        for index, interaction in self.data.items():
            summary += f"{interaction['input']}\n{interaction['output']}\n"
        return summary


class GPT3Identity:
    def __init__(self, name: str):
        self.name = name
        self.memory = Memory()  # Initialize the memory attribute as an instance of the Memory class

    def generate_response(self, text: str, ai) -> str:
        # Generate a summary of past interactions
        summary = self.memory.generate_summary()

        # Use the name attribute and summary of past interactions to specify the prompt for the GPT-3 model
        prompt = f"{summary}\nWho are you?\n{self.name}\n{text}"
        response = ai.generate_text(prompt=prompt, max_tokens=1024)

        # Store the current interaction in the memory attribute
        self.memory.add_interaction(text, response)
        return response


class Conversation:
    def __init__(self, *identities: GPT3Identity, master_prompt: str, ai):
        self.identities = identities
        self.master_prompt = master_prompt
        self.ai = ai

    def run_conversation(self, num_iterations: int):
        # Create a loop to generate responses between the identities for the specified number of iterations
        for i in range(num_iterations):
            for identity in self.identities:
                # Generate a response from the current identity to the most recent response from all other identities
                prompt = self.generate_prompt(identity)
                response = identity.generate_response(prompt, self.ai)
                print(response)

    def generate_prompt(self, identity: GPT3Identity) -> str:
        # Generate a summary of past interactions for all identities except the current one
        summary = ""
        for other_identity in self.identities:
            if other_identity != identity:
                summary += other_identity.memory.generate_summary()

        # Use the master prompt and summary of past interactions to specify the prompt for the GPT-3 model
        prompt = f"{summary}\n{self.master_prompt}\n"
        return prompt
        
        """