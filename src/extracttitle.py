import re
def extract_title(markdown):
    markdown_title = re.findall(r"#\s{1}.+", markdown)
    #print(f"the found markdown titles {markdown_title}")
    if len(markdown_title) == 0:
        raise Exception("No title found in markdown")
    title = markdown_title[0].replace('# ', '').strip()
    return title

