# GRUB Symphony
A python script to convert MIDI to a GRUB init tune

## Requirements
- Python 3.9 or later

## Instructions
Clone the repo, then install the package with pip: `pip install .`

or install with poetry: `poetry install`

Run `grub_symphony <MIDI File>`

The script will output a string that can be copied and pasted into your GRUB config file.

## Tips
If your MIDI has super short notes or rests, you may want to set the `granularity` parameter. It defaults to 1440.

The `granularity` is not only the "tempo" of the init tune, but also how fine-tuned the note durations will be

Higher = more granularity, more fine-tuned note durations

Lower = less granularity, less fine-tuned note durations

Feel free to raise it or lower it as much as you want, but you'll probably have the best results if you use a multiple of 60.

## Current Caveats
- Only supports the first instrument of a MIDI file
- Overlayed notes in the MIDI creates very interesting music
- Support for rests is very minimal
- Notes or rests that are too short will round down to a duration of nothing
- Some note durations can get a bit wonky at times
- Since GRUB requires integers for note frequencies, some notes
may be very slightly off-key, but it isn't noticeable for the
most part

This script is not perfect and probably won't be able to perfectly recreate every MIDI file thrown at it, so keep that in mind.

## License
GRUB Symphony is licensed under the [GNU Affero General Public License v3.0](/LICENSE)
