from notion.client import NotionClient
from notion.block import PageBlock
from md2notion.upload import upload

# Follow the instructions at https://github.com/jamalex/notion-py#quickstart to setup Notion.py
client = NotionClient(
    token_v2="4c563c79b318f8b8d1f4db36e668e79dc3bf3dbb9be10e6a8ac6885191fde62e4c044611cb10b6340b45e79b3c1e17e91494d23b47233b3c855ecf4334b9016995dc4c64f67d8e13dfe59e16df9c")
page = client.get_block(
    "https://www.notion.so/Hacking-Book-Test-519047c8dfcd435d92e86616d74778c2")

with open("SUMMARY.md", "r", encoding="utf-8") as mdFile:
    newPage = page.children.add_new(PageBlock, title="Hacking Book Upload")
    # Appends the converted contents of TestMarkdown.md to newPage
    upload(mdFile, newPage)
