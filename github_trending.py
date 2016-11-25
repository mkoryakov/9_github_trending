import datetime
import requests


def get_date_last_week_started():
    today = datetime.date.today()
    count_day_in_week = 7
    week = datetime.timedelta(days=count_day_in_week)
    return today - week


def get_trending_repositories(top_size):
    min_created_date = get_date_last_week_started()
    github_request_params = {'q': 'created:>%s' % min_created_date,
                             'sort': 'stars', 'order': 'desc'}
    github_search_request = 'https://api.github.com/search/repositories'
    response = requests.get(github_search_request, github_request_params)
    return response.json()['items'][:top_size]


def print_trending_repositories(trending_repositories):
    output_message = '''Количество звёзд %d, количество открытых задач %d,
    ссылка на репозитарий %s'''
    for repo in trending_repositories:
        print(output_message % (repo['stargazers_count'],
                                repo['open_issues'], repo['html_url']))


if __name__ == '__main__':
    count_trending_repos = 20
    trending_repositories = get_trending_repositories(count_trending_repos)
    print_trending_repositories(trending_repositories)
