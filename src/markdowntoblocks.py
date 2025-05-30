def markdown_to_blocks(markdown):
    return list(filter(lambda b: len(b) != 0, list(map(lambda b: b.strip(), markdown.split('\n\n')))))