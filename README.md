
# ShareMe

ShareMe is a web-based file-sharing platform inspired by WeTransfer. It enables users to upload files and generate shareable links for easy file sharing. Built with Django on the backend and modern front-end technologies, ShareMe is designed for simplicity, security, and efficiency.


## Features

- File Upload: Upload files directly to the platform.
- Shareable Links: Generate unique URLs for sharing files with others.
- Secure Downloads: Files are securely stored, ensuring user privacy.
- Expiration Time: Set an expiration time for the shared link.
- Responsive Design: Optimized for mobile and desktop devices


## Technologies Used
### Backend
- Django: Framework for building the backend.
- MySQL: Database for storing file metadata and user details.
- Python: Programming language used for server-side logic.

### Frontend
- HTML, CSS, JavaScript: For structuring, styling, and interactivity.
- Bootstrap/Tailwind CSS (choose based on what you're using): For responsive design.
- AJAX: For seamless user experience.

### Hosting

for now we are Hosting this project locally
## Installation

Follow these steps to get the project running locally:

1. #### Clone the Repository:
```bash
git clone https://github.com/yourusername/shareme.git
cd shareme
```
2. #### Set Up Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
3. #### Install Dependencies:
```bash
pip install -r requirements.txt
```
4. #### Configure Database:
- Update the settings.py file in your Django app to configure MySQL.
- Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. #### Run the Server:
```bash
python manage.py runserver
```
    
## Usage

1. #### upload file:
- Navigate to the home page.
- Select a file to upload.
- Submit to generate a shareable link

2. #### Share Links:
- Copy the generated URL and share it with others.
3. #### Download Files:
- Open the shareable link in any browser to download the file.
## Project Structure
```csharp 
ShareMe/
├── myapp/                 # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # Application logic
│   ├── templates/         # HTML templates
│   ├── static/            # CSS, JS, and images
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```
## Future Enhancements

- User authentication for personal accounts.
- File encryption for enhanced security.
- Progress bar during file upload.
## Contributing

Contributions are always welcome!

1. Fork the repository.

2. Create a feature branch

```bash
git checkout -b feature-name
```
3. Commit your changes:
```bash
git commit -m "Add feature-name"
```
4. Push to the branch:
```bash
git push origin feature-name
```
5. Submit a pull request.