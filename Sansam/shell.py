from Sansam import Run
import codecs
import os

# Get the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))
trail_file = os.path.join(script_dir, "trail.txt")

with codecs.open(trail_file, encoding='utf-8') as p:
    inp = p.read()
    result, error = Run.run(trail_file, inp)

    if error:
        print(error.as_string())
    else:
        print(result)

