# Chat_Pharma
# Project Title

 leverages an advanced LLM agent, CACTUS, to make critical decisions throughout the drug discovery process, supported by a set of specialized tools. Here’s how it works:

Decision-Making by LLM Agent (CACTUS):

CACTUS is the core component that drives the entire process. It takes disease information as input and decides how to proceed with finding potential drug candidates.
Using Specialized Tools:

Gene Target Identification: CACTUS uses the get_targets tool, which connects to the DISGENET API to find genes associated with the disease and retrieves their association scores.
Finding Drug Compounds: The get_ligands tool interfaces with the ChEMBL API to identify compounds that can bind to the target proteins.
Generating New Molecules: The Mol2Mol tool from the REINVENT 4 platform is used to create new molecules based on the identified compounds. It generates variations of these molecules to explore new drug possibilities.
Evaluating Drug-Likeness:

CACTUS also uses an inbuilt tool to calculate the Quantitative Estimate of Drug-likeness (QED) for the generated molecules. This metric helps assess how promising these molecules are as potential drugs.
In essence, CACTUS, the LLM agent, makes all the key decisions, while the specialized tools handle specific tasks such as identifying gene targets, finding compounds, generating new molecules, and evaluating drug-likeness. This integration streamlines the drug discovery process, making it more efficient and focused.
## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Introduction

Provide a brief overview of your project. Explain the purpose and objectives.

## Getting Started

### Prerequisites

List any software or packages required for running the project.

### Installation

Step-by-step instructions to get your project up and running:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    ```

2. Install the dependencies:
    ```bash
    from cactus.agent import Cactus

    api_model = Cactus(model_name="gpt-3.5-turbo", model_type="api")
    api_model.run("What is the molecular weight of the smiles: OCC1OC(O)C(C(C1O)O)O")
    ```

## Usage

Here's how to use your project:

1. **Step 1**: Description of step 1.

2. **Step 2**: Description of step 2.

### Example

To illustrate how the project works, here’s an example:

![Example Image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FSteve_Jobs&psig=AOvVaw3hNFVLmxl9TvJ2isMCwF4M&ust=1724092860272000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJjX8MWY_4cDFQAAAAAdAAAAABAE)

You can also embed local images using the following syntax:

![Local Image](./images/img1.jpg)

## Contributing

We welcome contributions! Please refer to our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

