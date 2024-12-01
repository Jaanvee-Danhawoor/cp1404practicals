import wikipedia


def main():
    """Prompt the user for a page title and display details about the page until the user enters blank input."""
    page_title = input("Enter page title: ")
    while page_title:
        try:
            page = wikipedia.page(page_title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print("Page id", page_title, "does not match any pages. Try another id!")
        page_title = input("Enter page title: ")
    print("Thank you.")


main()
