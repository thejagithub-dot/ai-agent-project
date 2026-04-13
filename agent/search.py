import requests

def search_web(query):
    url = "https://serpapi.com/search.json"

    params = {
        "q": query,
        "api_key": "serp_api_key"
    }

    response = requests.get(url, params=params)
    data = response.json()

    results = []

    for item in data.get("organic_results", [])[:5]:
        title = item.get("title", "")
        snippet = item.get("snippet", "")
        link = item.get("link", "")

        results.append(f"{title}\n{snippet}\n{link}")

    return results