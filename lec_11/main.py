import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()
   
filteredTitles = []
filteredPosts = []
for item in data:
    if len(item["title"].split()) > 6:
        filteredTitles.append(item["title"])
    if len(item["body"].split('\n')) > 3:
        filteredPosts.append(item)

print("Filtred titles with more than 6 words:")

for title in filteredTitles:
    print(title)  

print("\nPosts with body containing more than 3 lines of description:")
for post in filteredPosts:
    print(f"\nTitle: {post["title"]}")
    print(f"Body:\n{post["body"]}")

newPost = {"title": "Programming", "body": "Python is a programming language.", "id" : 101}
response = requests.post(url, newPost)
if response.status_code >= 200 and response.status_code <= 299:
    print("The new post has been added!")

newPostUpdated = {"title": "Programming", "body": "C++ is a programming language."}
response = requests.put(f"{url}/10",newPostUpdated)
if response.status_code >= 200 and response.status_code <= 299:
    print("The new post has been updated!")

response = requests.delete(f"{url}/101")
if response.status_code >= 200 and response.status_code <= 299:
    print("The new post has been deleted!")

