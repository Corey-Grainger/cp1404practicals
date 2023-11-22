"""CP1404 Week 10 Pracs
Basic Wikipedia Search Program
"""

import wikipedia


def main():
    """Search and display results for wikipedia pages"""
    search_term = input("Enter a search term for wikipedia: ")
    while search_term != "":
        try:
            selected_page = wikipedia.page(search_term, auto_suggest=False)
            print(selected_page.title, selected_page.summary, selected_page.url, sep="\n")
        except wikipedia.DisambiguationError as disambiguation_error:
            print(disambiguation_error)
        except wikipedia.PageError as page_error:
            print(page_error)
        search_term = input("Enter a search term for wikipedia: ")
    print("Hope you learned something!")


main()
