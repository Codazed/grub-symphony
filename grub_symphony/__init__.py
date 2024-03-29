import argparse
import os
import pathlib
import pretty_midi

def generate_init_tune_string(input_midi: str, granularity: int = 1440, prefix: bool = True) -> str:
    grub_init_tune_str = ""

    midi_data = pretty_midi.PrettyMIDI(input_midi)

    # Add prefix if desired
    if prefix:
        grub_init_tune_str += 'GRUB_INIT_TUNE="'

    duration_multiplier = granularity / 60

    # Add tempo to string
    grub_init_tune_str += f"{granularity} "

    # Select the first instrument
    selected_instrument = midi_data.instruments[0]

    # Iterate through each note in the MIDI
    current_note = None
    last_note = None
    for note in selected_instrument.notes:
        current_note = note

        if last_note and current_note.start != last_note.start:
            # There is a rest
            rest_duration = int(
                current_note.start * duration_multiplier
                - last_note.end * duration_multiplier
            )
            # Don't add a rest if it has a duration of 0
            if rest_duration != 0:
                grub_init_tune_str += "0 "
                grub_init_tune_str += f"{str(rest_duration)} "

        note_hz = str(int(pretty_midi.note_number_to_hz(note.pitch)))
        note_duration = str(int(note.get_duration() * duration_multiplier))
        grub_init_tune_str += f"{note_hz} "
        grub_init_tune_str += f"{note_duration} "
        last_note = note

    # Close the string
    grub_init_tune_str = grub_init_tune_str[:-1] + '"'
    return grub_init_tune_str

def main():
    parser = argparse.ArgumentParser(description="Turn a MIDI file into a GRUB init tune")
    parser.add_argument("midi", metavar="FILE", type=pathlib.Path, help="input MIDI file")
    parser.add_argument("--granularity", type=int, help="higher value means more fine-tuned note duration", default=1440)
    args = parser.parse_args()
    midi_name = os.path.basename(args.midi)
    init_tune_string = f"# '{midi_name}' : Generated by grub-symphony\n"
    init_tune_string += generate_init_tune_string(str(args.midi), args.granularity)
    print(init_tune_string)



if __name__ == "__main__":
    main()
