import os
import re
import sys
import json
import time

import hackpad_backup


def parse_pad_html(content):
    pad = {}
    for lineno, line in enumerate(content.splitlines()):
        if lineno > 10:
            break  # shortcut

        m = re.match(r'<meta name="version" content="(\d+)"/>', line)
        if m:
            pad['version'] = int(m.group(1))
            continue

        #m = re.search(r'<title>(.+)</title>', line)
        #if m:
        #    pad['title'] = m.group(1)
        #    continue

        m = re.search('<h1>(.+?)</h1>', line)
        if m:
            if 'title' not in pad:
                pad['title'] = m.group(1)
            continue
    return pad


def gen_site_index(site):
    storage = hackpad_backup.Storage(site)

    pads = []
    for fn in os.listdir(storage.base):
        if fn == 'index.html':
            continue
        padid, ext = os.path.splitext(fn)
        print padid
        if ext != '.html':
            continue
        path = os.path.join(storage.base, fn)

        pad = parse_pad_html(file(path).read())
        pad['padid'] = padid
        # Note, this is not last modified time.
        pad['last_backup_time'] = os.path.getmtime(path)
        pads.append(pad)

    pads.sort(key=lambda row: row['padid'])

    fn = 'pads.json'
    datestr = '%s %s' % (int(time.time()), hackpad_backup.g_timezone)
    # indent=1 make it human readable
    content = json.dumps(pads, indent=1)
    storage._git_commit_file(fn, datestr, 'update %s' % fn, content)


def main():
    for site, item in hackpad_backup.get_backup_list():
        gen_site_index(site)


if __name__ == '__main__':
    main()
