## Scraped Comments Analysis
This Django project scrapes comments from a specified YouTube video using the Google API and performs sentiment analysis on each comment using the TextBlob library. The resulting comments and sentiment data are displayed in a beautiful analysis table on a web page.

### Libraries Used
1. Django
2. Google API Python Client
3. TextBlob
4. Bootstrap

### Installation and Setup
1. Clone the repository to your local machine
2. Install the required libraries using pip install -r requirements.txt
3. Run python manage.py makemigrations to make migrations
4. Then migrate using python manage.py migrate
5. Run the Django server using python manage.py runserver
6. Navigate to http://localhost:8000/ in your web browser

### License
This project is licensed under the MIT License - see the LICENSE file for details.
