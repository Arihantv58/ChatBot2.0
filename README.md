# Hiking Chatbot using Azure OpenAI

This is a conversational chatbot designed to help users discover hiking trails in their area. The chatbot is designed to provide three hiking suggestions varying in length and shares interesting facts about the local nature on the hikes. If no location is specified, it defaults to areas near Rainier National Park. The project uses Azure OpenAI for generating responses.

## Features
- Conversational chatbot powered by Azure OpenAI
- Provides hiking suggestions based on user input
- Shares interesting facts about local nature
- Defaults to Rainier National Park if no location is specified
- UI for an interactive user experience

## Tech Stack
- **Backend:** Python, Azure OpenAI
- **Frontend:** [Mention the framework or technology used, e.g., React, HTML/CSS, etc.]
- **Environment Variables:** Managed using `dotenv`

## Prerequisites
Before running this project, ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Azure OpenAI API key and endpoint
- dotenv package (`pip install python-dotenv`)
- Azure OpenAI package (`pip install openai`)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Arihantv58/ChatBot2.0
    cd ChatBot2.0
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the project root directory.
    - Add the following variables:
        ```
        AZURE_OAI_ENDPOINT=your_azure_endpoint
        AZURE_OAI_KEY=your_api_key
        AZURE_OAI_DEPLOYMENT=your_deployment_name
        ```

## Usage
To start the chatbot:
```bash
python main.py
```

- Enter your prompt to receive hiking suggestions and interesting facts.
- Type `quit` to exit the chatbot.

## Example
```
Enter the prompt (or type 'quit' to exit): Recommend a hike near Seattle
Summary: Here are three hikes near Seattle...
```

## UI
This project includes a user interface to enhance the conversational experience. The UI is built using [mention framework/technology used] and provides an interactive way to communicate with the chatbot.

## Project Structure
```
├── main.py                 # Main script to run the chatbot
├── .env                    # Environment variables (not included in repo)
├── requirements.txt        # List of dependencies
├── frontend/                # Frontend UI code
└── README.md                # Project documentation
```

## Contributing
Contributions are welcome! If you want to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add your feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.
