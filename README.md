# File Uploader

File Uploader is a web application that allows users to register, upload files, and browse their uploaded files in a file browser.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python (3.7+)
- Django (3.2+)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mojnomiya/file_uploader.git
   ```

2. Navigate to the project directory:

   ```bash
   cd file_uploader
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser account to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

9. Access the application at http://localhost:8000/ in your web browser.

You will be in :
![Welcome Page](https://i.postimg.cc/SK2qcTHF/Screenshot-2023-09-24-at-5-22-58-PM.png
)

## Features

- User registration and authentication.
- File upload functionality with secure storage.
- File browser to view uploaded files.
- Bootstrap-based user-friendly interface.
- Responsive design for mobile and desktop.

## Usage

1. Register as a new user or log in with your existing credentials.
![Register Page](https://i.postimg.cc/Qtc3yBXf/Screenshot-2023-09-24-at-5-23-19-PM.png)
2. Navigate to the "Upload" page.
![Upload Page](https://i.postimg.cc/BnvJnQgv/Screenshot-2023-09-24-at-5-23-48-PM.png)
3. Choose a file to upload and click the "Upload" button.
4. View your uploaded files in the file browser on the "File Browser" page.
5. Click the "View File" button to open and view the uploaded file.
## More Screenshots
![Login Page](https://i.postimg.cc/qvZ4hVbx/Screenshot-2023-09-24-at-5-23-11-PM.png)
## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.