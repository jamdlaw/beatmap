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
            'major':       [2, 2, 1, 2, 2, 2, 1],  # Ionian
            'dorian':      [2, 1, 2, 2, 2, 1, 2],
            'phrygian':    [1, 2, 2, 2, 1, 2, 2],
            'lydian':      [2, 2, 2, 1, 2, 2, 1],
            'mixolydian':  [2, 2, 1, 2, 2, 1, 2],
            'minor':       [2, 1, 2, 2, 1, 2, 2],  # Aeolian
            'locrian':     [1, 2, 2, 1, 2, 2, 2]
    }

    if scale_type not in scale_patterns:
        print(f"Error: Invalid scale type '{scale_type}'")
        return None

    # The intervals list now has 7 steps; we only need the first 6 to get the 7 unique notes.
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

    # 4. BUILDING THE SCALE (THE FIX IS HERE)
    scale = [tonic_note]
    # This set will track the letter names we've already used (A, B, C, etc.)
    used_letters = {tonic_note[0]} 
    current_index = start_index

    # Loop through the first 6 intervals to get the next 6 notes.
    for step in intervals[:-1]:
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
    
    # Finally, add the tonic again at the end for the octave.
    scale.append(tonic_note)

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

e_major_scale = generate_scale('e', 'major')
print(f"E major: {e_major_scale}")


g_mixolydian_scale = generate_scale('g', 'mixolydian')
print(f"G mixolydian: {g_mixolydian_scale}")