from cactus.agent import Cactus
import subprocess
def main():
    # Initialize the Cactus API model
    api_model = Cactus(model_name="gpt-3.5-turbo", model_type="api")
    

    # Example command to execute on Windows
    command = "reinvent -l sampling.log sampling.toml"

    # Run the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Check the result
    if result.returncode == 0:
        print("Command executed successfully.")
        print("Output:")
        print(result.stdout)
    else:
        print("Command failed. Error output:")
        print(result.stderr)

    # Take user input for the query
    user_query = input("How can I help you? ")
    
    # Run the model with the user query
    response = api_model.run(user_query)
    
    # Print the response
    print(response)

if __name__ == "__main__":
    main()
