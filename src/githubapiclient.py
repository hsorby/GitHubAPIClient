
import datetime
from github import Github


def main():

    with open('my_private_token.txt') as f:
        my_token = f.read()

    g = Github(my_token)

    # Get list of contributors from the LibCellML repository in the CellML organisation.
    o = g.get_organization('cellml')
    r = o.get_repo('libcellml')
    contributors = r.get_contributors()
    contributor_names = []
    contributor_html_urls = []

    for c in contributors:
        contributor_names.append(c.name)
        contributor_html_urls.append(c.html_url)

    combined_sorted_contributor_names = sorted(zip(contributor_names, contributor_html_urls), key=lambda pair: pair[0].split(" ")[-1])

    today = datetime.date.today()
    print('')
    print('List of Contributors')
    print('====================')
    print('')
    print('The following is a list of contributors(in surname alphabetical order) who have contributed lines of')
    print('source code to the LibCellML project on or before {0}.'.format(today))
    print('')
    for combined_data in combined_sorted_contributor_names:
        print(' * `{0} <{1}>`_'.format(combined_data[0],combined_data[1]))
    print('')
    print('For an up-to-date list of contributors see https://github.com/cellml/libcellml/graphs/contributors.')
    print('')


if __name__ == "__main__":
    main()
