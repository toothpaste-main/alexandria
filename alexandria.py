from pathlib import Path

REFERENCE_FILE_SUFFIX = '.txt'

# Allowed list of journals.
# 
# https://adsabs.harvard.edu/abs_doc/refereed.html
JOURNALS = {
    'A&A': 'Astronomy and Astrophysics',
    'A&ARv': 'Astronomy and Astrophysics Review',
    'A&AS': 'Astronomy and Astrophysics Supplement Series',
    'ApJ': 'The Astrophysical Journal',
    'ApJS': 'The Astrophysical Journal Supplement Series',
    'iSci': 'iScience',
    'MNRAS': 'Monthly Notices of the Royal Astronomical Society',
}

def reference_decompiler(reference):
    """Deconstructs reference into primary parts.
    
    Assumes 
    [AAS Journal format](https://journals.aas.org/references/#examples).
    """
    print(reference)
    reference = reference.split(', ')
    print(reference)
    author = reference[0]
    year = reference[-4]
    journal = reference[-3]
    volume = reference[-2]
    page = reference[-1]

    return author, year, journal, volume, page

def new():
    print('Enter reference:')
    reference = input('>')

    reference_t = reference_decompiler(reference)

    reference_file_name = '_'.join(reference_t) + REFERENCE_FILE_SUFFIX

    # NOTE: enconding might not be necessary.
    with open(reference_file_name, mode='w', encoding='utf-8') as f:
        f.write(reference)

        print('Article Title:')
        f.write('\n' + input('>'))

        f.write('\n')

        print('Enter description:')
        f.write('\n' + input('>'))

        # TODO: text editor / writing multiple lines.

    print(f'New reference saved to: {reference_file_name}')


def main_menu():
    user_input = input('>')
    match user_input:
        case 'new':
            # TODO: allow typing 'new Author Year Journal Vol pp'
            new()
        case 'search':
            pass
        case 'list':
            pass
        case 'edit':
            # Edit menu lets you delete entry.
            pass
        case 'exit':
            return False
        case _:
            print(f'Unknown command: {user_input}')
        
    return True


if __name__ == '__main__':
    is_alive = True
    while is_alive:
        is_alive = main_menu()
