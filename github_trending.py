import datetime
import requests


def get_date_last_week_started():
    today = datetime.date.today()
    week = datetime.timedelta(days=7)
    return today - week


def get_trending_repositories(top_size):
    min_created_date = get_date_last_week_started()
    github_search_request = \
        'https://api.github.com/search/repositories?q=language:python+created:>%s&sort=stars&order=desc' % min_created_date
    response = requests.get(github_search_request)
    return response.json()['items'][:top_size]


def print_trending_repositories(trending_repositories):
    output_message = '''Количество звёзд %d, количество открытых задач %d,
    ссылка на репозитарий %s'''
    for repo in trending_repositories:
        print(output_message % (repo['stargazers_count'],
                                repo['open_issues'], repo['html_url']))


if __name__ == '__main__':
    trending_repositories = get_trending_repositories(20)
    print_trending_repositories(trending_repositories)
