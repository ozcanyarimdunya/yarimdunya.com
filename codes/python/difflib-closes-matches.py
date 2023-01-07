import difflib

matches = difflib.get_close_matches(
    word="ozc",
    possibilities=[
        "ozcan",
        "ozca",
        "zcan",
        "stat",
    ],
    n=5,
    cutoff=0.5
)
print(matches)

# ['ozca', 'ozcan', 'zcan']

