import wikipedia

page_title = input("Enter page title: ")
while page_title:
    print(wikipedia.summary(page_title, auto_suggest=False))
    page_title = input("Enter page title: ")
print("Thank you.")
