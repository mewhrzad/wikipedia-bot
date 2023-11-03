import aiohttp

def isEnglish(input):
    try:
        input.encode(encoding="utf-8").decode("ascii")
    except UnicodeDecodeError:
        return "fa"
    else:
        return "en"


async def fetch_search_results(session, search_term):
    lang = isEnglish(search_term)
    url = f"https://api.wikimedia.org/core/v1/wikipedia/{lang}/search/title"
    number_of_results = 5
    parameters = {"q": search_term, "limit": number_of_results}
    headers = {"User-Agent": "project_name (example@gmail.com)"}
    async with session.get(url, headers=headers, params=parameters) as response:
        data = await response.json()
        results = []
    for page in data["pages"]:
        title = page["title"]
        thumbnail = None
        try:
            thumbnail = "https:" + page["thumbnail"]["url"]
        except:
            thumbnail = None
        description = page["description"]
        page = f"https://{lang}.wikipedia.org/wiki/" + page["key"]

        results.append([title,thumbnail,description,page])
    return results


async def search(search_term):
    async with aiohttp.ClientSession() as session:
        results = await fetch_search_results(session, search_term)
        return results
