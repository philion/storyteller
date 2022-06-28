#!/usr/bin/env python3

import os
import csv
import logging
import datetime
import requests

from bs4 import BeautifulSoup
from libzim.writer import Creator, Item, StringProvider, FileProvider, Hint

logger = logging.getLogger()#(__name__)

# A list of categories to search for
DEFAULT_CATAGORIES = ["Children's Literature"]

PG_FILE_BASE = "https://www.gutenberg.org/files"
PG_HTML_URL = PG_FILE_BASE + "/{0}/{0}-h/{0}-h.htm" # Note: {0} is the catalog number, first col of the CSV
PG_TXT_URL = PG_FILE_BASE + "{0}/{0}.txt"

CATALOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "catalog")
CATALOG_FILE = os.path.join(CATALOG_DIR, "pg_catalog.csv")

# Stores metadata about each book/Item
class zitem(Item):
    def __init__(self, title, path, content = "", fpath = None):
        super().__init__()
        self.path = path
        self.title = title
        self.content = content
        self.fpath = fpath

    def get_path(self):
        return self.path

    def get_title(self):
        return self.title

    def get_mimetype(self):
        return "text/html"

    def get_contentprovider(self):
        if self.fpath is not None:
            return FileProvider(self.fpath)
        return StringProvider(self.content)
       
    def get_hints(self):
        return {Hint.FRONT_ARTICLE: True}


DEFAULT_ZIM_PATH = "home"

# This scraper is designed to pull childrens books from Protect Gutenberg
# And store them in a ZIM file
# Only HTML format is used.
class scraper():
    def __init__(self, categories=DEFAULT_CATAGORIES):
        self.categories = categories

    # Create a ZIM file with default categ
    def build_zim(self, zimfile):
        # open a ZIM file and setup from metadata
        with Creator(zimfile).config_indexing(True, "eng") as zimmer:
            zimmer.set_mainpath(DEFAULT_ZIM_PATH)
            zimmer.add_metadata("title", "test zim") # FIXME build metadata from python/git metadata
            zimmer.add_metadata("created", str(datetime.datetime.now())) # FIXME build metadata from python/git metadata
            zimmer.add_metadata("categories", str(self.categories))
            logger.info("opened ZIM file for writing", zimfile)

            # check the catalog for the files you want
            for id in self.load_catalog():
                title, content = self.load_file(id)
                if title:
                    #print("title:", title, "len:", len(content))
                    try: 
                        item = zitem(title, DEFAULT_ZIM_PATH, content)
                        zimmer.add_item(item)
                        print("-- added:", item.title)

                    except Exception as e:
                        #print(e)
                        logger.warning("FIXME skip duplicate: {}".format(title))
                else:
                    logger.warning("unable to load file for id: {}".format(id))

        logger.info("added items to ZIM")

    # Add the file contents to the zim file
    def load_file(self, fileId):
        # build the url, load it into content, capture the title
        url = PG_HTML_URL.format(fileId)
        logger.info("loading", url)
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string
            content = soup.prettify()
            #print("--", title, len(content))
            return title.strip(), content.strip()
        else:
            logger.error("Status code:{} for {}".format(response.status_code, url))
            # TODO : In future, check for TXT
            return None, None

    # Loads the catalog file, searchs for matching categories 
    # and returns a list of found items
    def load_catalog(self, filename=CATALOG_FILE):
        matched = [] # array of catalog IDs

        # load the CSV file
        with open(filename) as f:
            reader = csv.reader(f)
            logger.info("reading catalog from: " + f)
            try:
                for row in reader:
                    # for each row get:
                    # first column (col 0): catalog ID
                    id = row[0]
                    # last (col 8): 'Bookshelves'
                    shelves = row[8] # this is a ';' separated list in a string
                                     # but it is being used as a simple string for
                                     # cheap string-match using python's 'in'.
                    for category in self.categories:
                        if category in shelves:
                            logger.info("Found: {} {}".format(id, category))
                            matched.append(id) # TODO: This should be a set of IDs, not a list
                            break; # found one, that's enough
            except csv.Error as e:
                logger.error('file {}, line {}: {}'.format(filename, reader.line_num, e))
        return matched

    
def main():
    #scraper().load_catalog(os.path.join(CATALOG_DIR, "test.csv"))
    scraper().build_zim("test.zim")

if __name__ == '__main__':
    main()