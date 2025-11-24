
def load_story(path):
    """Read and return the story text from a file."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
    


def extract_placeholders(story, start="<", end=">"):
    """
    Manually extract placeholders wrapped in < >.
    No regex used — same logic as your original code.
    """
    placeholders = set()
    word_start_idx = -1

    for i, char in enumerate(story):
        if char == start:
            word_start_idx = i

        elif char == end and word_start_idx != -1:
            placeholder = story[word_start_idx:i+1]
            placeholders.add(placeholder)
            word_start_idx = -1

    return placeholders



def fill_story(story, placeholders):
    """Ask the user for each placeholder and replace it in the story."""
    for placeholder in placeholders:
        answer = input(f"Enter a word for {placeholder}: ")
        story = story.replace(placeholder, answer)
    return story



def main():
    story = load_story("story.txt")
    placeholders = extract_placeholders(story)

    if not placeholders:
        print("No placeholders found in the story.")
        return

    final_story = fill_story(story, placeholders)
    print("\n--- Your Story ---")
    print(final_story)


if __name__ == "__main__":
    main()
