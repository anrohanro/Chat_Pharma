# Chat_Pharma
# Project Title

Inspite of the robust research being carried out in fields of gene- disease correlations and protein- ligand interactions for drug design, the identification of the correct target genes and potential compounds which alter the effects of the corresponding target proteins has always remained one of the most  difficult tasks in the entire  process of drug designing. DrugPred attempts to leverage the decision making capabilities of LLM Agents for the entire process of searching, filtering and optimization of genes targets, protein analogs and potential drugs molecules. DrugPred searches for gene- disease correlations and protein- ligand binding pairs from the DISGENET and ChEMBL databases by calling their respective APIs. The LLM Agent being the central decision maker uses a variety of tools that calculate bio-chemical characteristics of molecules to filter most potent drug molecules. The model also takes these set of potential drug candidates( scaffolds) and builds libraries of similiar compounds using mol2mol transformations in the scaffold. This gives us a larger pool of potential drug candidates to choose from.
DrugPred is built by integrating different tools like REINVENT and ChEMBL and DISGENET APIs into a central framework of the LLM Agent, CACTUS.

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

