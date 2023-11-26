import requests

if __name__ == "__main__":
    get_response = requests.get("https://jsonplaceholder.typicode.com/posts")
    post_response = requests.post("https://jsonplaceholder.typicode.com/posts")
    put_response = requests.put("https://jsonplaceholder.typicode.com/posts/1")
    delete_response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

    filteredByTitle = []
    filterdByBody = []
    for data in get_response.json():
        if len(data['title'].split()) > 6:
            filteredByTitle.append(data)
        if len(data['body'].splitlines()) > 3:
            filterdByBody.append(data)