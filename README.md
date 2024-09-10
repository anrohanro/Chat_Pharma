# Chat_Pharma

**Chat_Pharma** leverages an advanced LLM agent, CACTUS, to make critical decisions throughout the drug discovery process, supported by a set of specialized tools. This integration streamlines the discovery of potential drug candidates, making the process more efficient and focused.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Drug development broadly happens in four stages: discovery, preclinical studies, clinical development, and market approval. The discovery stage is the most crucial from our perspective, as it’s when we design drugs based on disease proliferation mechanisms and tailor the molecular structure of potential drugs.

However, drug discovery is an expensive and time-consuming process. It typically takes 12-15 years for a drug to reach the market, with development costs ranging between $900 million and $2 billion. This is largely due to the identification, characterization, and screening of 5,000 to 10,000 potential drug molecules, with only one making it to market.

**Chat_Pharma** helps researchers narrow down potential drug candidates, cutting down on time and resources. It integrates generative AI with molecular design tools like REINVENT 4, gene-disease association databases like DISGENET, and protein-ligand databases like ChEMBL.

At the heart of the software is the LLM agent **CACTUS**, which is trained using a Thought-Action-Observation model. CACTUS makes all the key decisions, such as:
- Identifying gene targets using the DISGENET API, which provides a list of genes associated with a disease and their Gene-Disease Association scores.
- Finding drug compounds using the ChEMBL API, which retrieves ligands that bind to target proteins.
- Generating new molecules with the Mol2Mol tool from REINVENT 4.
- Evaluating drug-likeness using the Quantitative Estimate of Drug-likeness (QED).

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- DISGENET API access
- ChEMBL API access
- REINVENT 4 platform
- Required Python libraries (e.g., requests, pandas, etc.)


### Installation

Step-by-step instructions to get your project up and running:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    ```

2. Install the dependencies:
    ```python
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

