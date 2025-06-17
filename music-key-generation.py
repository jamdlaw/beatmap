def generate_scale(tonic_note, scale_type):
    """
    Generates a musical scale with correct enharmonic spellings.

    Args:
        tonic_note (str): The starting note of the scale (e.g., 'c', 'f', 'g#').
        scale_type (str): The type of scale to generate ('major' or 'minor').

    Returns:
        list: A list of strings representing the notes in the scale, 
              or None if the tonic or scale type is invalid.
    """
    
    # 1. THE NEW DATA STRUCTURE
    # A list of lists, where each inner list contains the enharmonic names for a pitch.
    notes = [
        ['b#', 'c'],
        ['c#', 'db'],
        ['d'],
        ['d#', 'eb'],
        ['e', 'fb'],
        ['e#', 'f'],
        ['f#', 'gb'],
        ['g'],
        ['g#', 'ab'],
        ['a'],
        ['a#', 'bb'],
        ['b', 'cb']
    ]

    # 2. THE SCALE PATTERNS
    # We can store our scale patterns in a dictionary for easy access.
    scale_patterns = {
        'major': [2, 2, 1, 2, 2, 2, 1],
        'minor': [2, 1, 2, 2, 1, 2, 2]
    }

    if scale_type not in scale_patterns:
        print(f"Error: Invalid scale type '{scale_type}'")
        return None

    intervals = scale_patterns[scale_type]
    
    # 3. FINDING THE STARTING NOTE
    # We need to search the nested lists to find the starting index.
    start_index = -1
    for i, names in enumerate(notes):
        if tonic_note in names:
            start_index = i
            break
            
    if start_index == -1:
        print(f"Error: Invalid tonic note '{tonic_note}'")
        return None

    # 4. BUILDING THE SCALE
    scale = [tonic_note]
    # This set will track the letter names we've already used (A, B, C, etc.)
    used_letters = {tonic_note[0]} 
    current_index = start_index

    for step in intervals:
        current_index = (current_index + step) % len(notes)
        possible_notes = notes[current_index]

        # 5. THE CORE LOGIC: CHOOSING THE RIGHT NOTE NAME
        if len(possible_notes) == 1:
            # If there's no ambiguity, just add the note.
            chosen_note = possible_notes[0]
        else:
            # If there's an enharmonic choice (e.g., ['c#', 'db'])...
            for note_option in possible_notes:
                letter = note_option[0]
                if letter not in used_letters:
                    # ...pick the one whose letter name we haven't used yet.
                    chosen_note = note_option
                    break
            else:
                # Fallback in case of a logical error or unusual scale.
                chosen_note = possible_notes[0]

        scale.append(chosen_note)
        used_letters.add(chosen_note[0])
        
    return scale

# --- Let's test it out! ---

# C Major (no sharps or flats)
c_major_scale = generate_scale('c', 'major')
print(f"C Major: {c_major_scale}")

# G Major (a "sharp" key)
g_major_scale = generate_scale('g', 'major')
print(f"G Major: {g_major_scale}")

# F Major (our "flat" key test case)
f_major_scale = generate_scale('f', 'major')
print(f"F Major: {f_major_scale}")

# E-flat Major (a key with multiple flats)
eb_major_scale = generate_scale('eb', 'major')
print(f"Eb Major: {eb_major_scale}")

# A Minor (a natural minor scale)
a_minor_scale = generate_scale('a', 'minor')
print(f"A minor: {a_minor_scale}")