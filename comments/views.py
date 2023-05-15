import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.shortcuts import render
from .forms import CommentForm
from .models import Comment

def scrape_comments(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            no_of_comments = form.cleaned_data['no_of_comments']
            additional_params = form.cleaned_data['additional_params']
            data = []
            with Chrome(executable_path=r"C:\Users\anude\Downloads\chromedriver.exe") as driver:
                wait = WebDriverWait(driver, 15)
                driver.get(link)
                for item in range(no_of_comments // 20):
                    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
                    time.sleep(5)
                for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
                    text = comment.text
                    sentiment = "positive" # perform sentiment analysis here
                    comment_obj = Comment(text=text, sentiment=sentiment)
                    comment_obj.save()
                    data.append(comment_obj)
            return render(request, 'comments.html', {'data': data})
    else:
        form = CommentForm()
    return render(request, r'index.html', {'form': form})

def comments(request):
    data = Comment.objects.all()
    
    return render(request, 'comments.html', {'data': data})

def home(request):
    return render(request, 'index.html')
