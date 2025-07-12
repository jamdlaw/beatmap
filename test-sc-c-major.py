import time
from pythonosc import udp_client

# --- Configuration ---
SC_IP = "127.0.0.1"
SC_PORT = 57110
SYNTH_NAME = "default"
SCALE_GROUP_ID = 1000  # A dedicated ID for our Group

# --- C Major Scale (MIDI note numbers) ---
c_major_scale_midi = [60, 62, 64, 65, 67, 69, 71, 72]

# --- Note duration and tempo ---
TEMPO = 140
beat_duration = 60 / TEMPO

# --- Create an OSC client ---
client = udp_client.SimpleUDPClient(SC_IP, SC_PORT)

def midi_note_to_freq(midi_note):
  """Converts a MIDI note number to frequency in Hertz."""
  return 440.0 * (2.0 ** ((midi_note - 69.0) / 12.0))

# --- Main Execution ---
try:
    # 1. Create a new Group on the server to hold our synths.
    print("Creating a synth group...")
    client.send_message("/g_new", [SCALE_GROUP_ID, 1, 0])

    print("Playing the C major scale...")
    # 2. Loop and create a new synth for each note inside our group.
    # This creates the overlapping sound.
    for midi_note in c_major_scale_midi:
        freq = midi_note_to_freq(midi_note)
        # addAction '1' adds the new synth to the tail of our group.
        client.send_message("/s_new", [SYNTH_NAME, -1, 1, SCALE_GROUP_ID, "freq", freq])
        time.sleep(beat_duration)

    # Allow the last note to ring for a moment.
    time.sleep(0.5)

    # 3. Forcefully free all synths in the group.
    # The '/g_freeAll' command immediately removes every node from the target group.
    print("Force-stopping all sounds in the group...")
    client.send_message("/g_freeAll", [SCALE_GROUP_ID])

    print("Scale finished.")

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please ensure the SuperCollider server (scsynth) is running.")