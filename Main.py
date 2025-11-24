
def load_story(path):
    """Read and return the story text from a file."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()