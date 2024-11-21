# Image Captioning and Translation Project

This project provides an API for generating captions for images and translating those captions from English to Arabic. The project consists of two main components:

1. **Backend**: A FastAPI application that handles image uploads, generates captions using the BLIP model, and translates captions using the MarianMT model.
2. **Frontend**: A Next.js application that provides a user interface for uploading images and displaying the generated captions.

## Table of Contents

- [Introduction](#introduction)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Usage](#usage)

## Introduction

The Image Captioning and Translation Project allows users to upload images, generate captions for those images using a pre-trained BLIP model, and translate the captions from English to Arabic using a fine-tuned MarianMT model. The project is divided into two main parts: the backend API and the frontend user interface.

## Backend Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/your-repo.git
    cd your-repo/backend
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Running the Backend

1. Start the FastAPI server:

    ```sh
    uvicorn main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`.

### Training the MarianMT Model

1. Navigate to the `backend/model` directory:

    ```sh
    cd backend/model
    ```

2. Run the training script:

    ```sh
    python train.py
    ```

3. The trained model will be saved in the `fine_tuned_model` directory.

## Frontend Setup

### Prerequisites

- Node.js 14 or higher
- npm (Node package manager) or yarn

### Installation

1. Navigate to the `frontend` directory:

    ```sh
    cd frontend
    ```

2. Install the required dependencies:

    ```sh
    npm install
    # or
    yarn install
    ```

### Running the Frontend

1. Start the Next.js development server:

    ```sh
    npm run dev
    # or
    yarn dev
    ```

2. Open your browser and navigate to `http://localhost:3000` to view the application.

## Usage

1. Open the frontend application in your browser.
2. Upload an image using the provided interface.
3. The application will display the generated caption in English and its translation in Arabic.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.