import time
from pythonosc import udp_client
from music-key-generation import generate_scale

class ScalePlayer:
    def __init__(self, sc_ip="127.0.0.1", sc_port=57110, synth_name="default", group_id=1000):
        self.sc_ip = sc_ip
        self.sc_port = sc_port
        self.synth_name = synth_name
        self.group_id = group_id
        self.client = udp_client.SimpleUDPClient(self.sc_ip, self.sc_port)

    @staticmethod
    def note_name_to_midi(note_name):
        """
        Converts a note name (e.g., 'c', 'c#', 'db', 'a4', 'g#3') to a MIDI note number.
        Defaults to octave 4 if not specified.
        """
        note_base = {'c': 0, 'c#': 1, 'db': 1, 'd': 2, 'd#': 3, 'eb': 3, 'e': 4, 'fb': 4, 'e#': 5, 'f': 5, 'f#': 6, 'gb': 6, 'g': 7, 'g#': 8, 'ab': 8, 'a': 9, 'a#': 10, 'bb': 10, 'b': 11, 'cb': 11, 'b#': 0}
        import re
        m = re.match(r"([a-gA-G][b#]?)(\d*)", note_name.lower())
        if not m:
            raise ValueError(f"Invalid note name: {note_name}")
        note = m.group(1)
        octave = int(m.group(2)) if m.group(2) else 4
        midi = 12 * (octave + 1) + note_base[note]
        return midi

    @staticmethod
    def midi_note_to_freq(midi_note):
        return 440.0 * (2.0 ** ((midi_note - 69.0) / 12.0))

    def generate_scale(self, tonic, mode):
        return generate_scale(tonic, mode)

    def play_scale(self, scale, tempo=140, octave=4):
        beat_duration = 60 / tempo
        # Convert note names to MIDI numbers (with octave)
        midi_notes = [self.note_name_to_midi(note + str(octave) if not any(char.isdigit() for char in note) else note) for note in scale]
        # 1. Create a new Group on the server to hold our synths.
        print("Creating a synth group...")
        self.client.send_message("/g_new", [self.group_id, 1, 0])
        print(f"Playing the scale: {scale}")
        for midi_note in midi_notes:
            freq = self.midi_note_to_freq(midi_note)
            self.client.send_message("/s_new", [self.synth_name, -1, 1, self.group_id, "freq", freq])
            time.sleep(beat_duration)
        time.sleep(0.5)
        print("Force-stopping all sounds in the group...")
        self.client.send_message("/g_freeAll", [self.group_id])
        print("Scale finished.") 