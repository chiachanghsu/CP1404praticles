import wikipedia

title = input('>>> ').title()
while title != '':
    try:
        info = wikipedia.page(title)
        print(info.title)
        print(info.content)
        print(info.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print('We need a more specific title. Try one of the following, or a new search:')
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(f'Page id "{title}" does not match any pages. Try another id!')
    title = input('>>> ').title()
print('Thank you.')
