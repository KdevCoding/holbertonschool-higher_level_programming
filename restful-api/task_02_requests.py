import requests
import csv

def fetch_and_print_posts():
    """print title fields from https://jsonplaceholder.typicode.com/posts
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    for o in r.json():
        print(o['title'])

def fetch_and_save_posts():
    """saves id, title, body fields from https://jsonplaceholder.typicode.com/posts
    """
    posts = []
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        for post in r.json():
            posts.append({'id': post['id'],'title': post['title'],'body': post['body']})
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({'id': post['id'],'title': post['title'],'body': post['body']})

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()