import wikipedia

while True:
    title = input("Enter a page title or search phrase (leave blank to exit): ")
    if not title:
        break

    try:
        page = wikipedia.page(title, auto_suggest=False)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation page found, please be more specific.")
    except Exception as e:
        print("An error occurred:", e)