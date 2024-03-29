import asyncio

from sources.git_scraper import scrape_github_angular,scrape_github_symfony
from sources.raw_github_scraper import scrape_raw_github_vuejs
from sources.wiki_scraper import scrape_wiki_python,scrape_wiki_php,scrape_wiki_typescript,scrape_wiki_java,scrape_wiki_javascript
from logs.cron_logs import log_cron_scrapers_execution
from database.database_connection import MongoDB
from core.config import mongo_uri

async def launch_scrape_algos():
    url_symphony = "https://github.com/symfony/symfony/releases"
    url_angular = "https://github.com/angular/angular/releases"
    url_python = "https://en.wikipedia.org/wiki/History_of_Python"
    url_php = "https://en.wikipedia.org/wiki/PHP"
    url_typescript = 'https://en.wikipedia.org/wiki/TypeScript'
    url_java = 'https://en.wikipedia.org/wiki/Java_version_history'
    url_javascript = 'https://en.wikipedia.org/wiki/ECMAScript_version_history'
    url_vuejs = "https://raw.githubusercontent.com/vuejs/core/main/CHANGELOG.md"

    await scrape_github_symfony(url_symphony)
    await scrape_github_angular(url_angular)
    await scrape_raw_github_vuejs(url_vuejs)
    await scrape_wiki_python(url_python)
    await scrape_wiki_php(url_php)
    await scrape_wiki_typescript(url_typescript)
    await scrape_wiki_java(url_java)
    await scrape_wiki_javascript(url_javascript)

async def run_async_functions():
    try:
        await MongoDB.initialize(mongo_uri)
        await launch_scrape_algos()
        await log_cron_scrapers_execution()
    except Exception as e:
        await log_cron_scrapers_execution(status='Failure', message=str(e))

if __name__ == "__main__":
    asyncio.run(run_async_functions())
