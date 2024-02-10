from 


class Crawler:
    """
    This is the base class for all crawlers.
    """
    def crawl(self, keyword: str, output_dir: str) -> None:
        """
        Crawl the website and return the data.
        """
        raise NotImplementedError
