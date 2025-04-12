from graphviz import Digraph

# Create a Digraph object
music_tree = Digraph('MusicGenres', format='png')
music_tree.attr(rankdir='TB')  # Top to Bottom layout
music_tree.attr('node', shape='rectangle', style='bold', fontname='Helvetica', fontsize='12')

# Define genres and relationships
genres = [
    "Blues",
    "Country",
    "Folk",
    "Rock and Roll",
    "R&B",
    "Soul",
    "Punk",
    "Heavy Metal",
    "Hip Hop",
    "Pop",
    "Alternative Rock",
    "Grunge",
    "Electronic",
]

# Define the connections (influence relationships)
connections = [
    ("Blues", "Rock and Roll"),
    ("Country", "Rock and Roll"),
    ("Folk", "Rock and Roll"),
    ("Rock and Roll", "Punk"),
    ("Rock and Roll", "Heavy Metal"),
    ("R&B", "Soul"),
    ("Soul", "Hip Hop"),
    ("Punk", "Alternative Rock"),
    ("Alternative Rock", "Grunge"),
    ("Electronic", "Pop"),
    ("Rock and Roll", "Pop"),
    ("Soul", "Pop"),
]

# Add nodes
for genre in genres:
    music_tree.node(genre)

# Add edges
for parent, child in connections:
    music_tree.edge(parent, child)

# Save and render the graph
music_tree.render('music_genre_family_tree', view=True)
