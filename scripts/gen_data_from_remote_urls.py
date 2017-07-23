# Generate "poster", "duration" from remote video urls

import jsonlines
import os
import sys
from subprocess import PIPE, Popen, call
import logging


# VIDEO_URLS = "/Users/IT/temp/tubesite/url_split_00"
IMAGE_PREFIX = "kkkk9"

IMAGE_SAVE_PATH = "gen_poster"
IMAGE_SCALE = "784:516"

curr_dir = os.getcwd()
logging.basicConfig(filename="gen.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s:\%(message)s")
logger = logging.getLogger(__file__)


def _filename(url):
    return url.split("/")[-1:][0].split(".")[:-1][0]


def gen_poster(url, path):
    cmd = 'ffmpeg -i {url} -vf thumbnail,scale={scale} -vframes 1 {path}'.format(
        url=url, prefix=IMAGE_PREFIX, scale=IMAGE_SCALE, path=path)
    call(cmd.split(" "))


def gen_duration(url):
    p1 = Popen("ffprobe -i {0} -show_format -v quiet".format(url).split(" "), stdout=PIPE)
    p2 = Popen(["sed", "-n", "s/duration=//p"], stdin=p1.stdout, stdout=PIPE)
    stdout, err = p2.communicate()
    if err:
        raise Exception("Get duration error")
    return int(round(float(stdout.rstrip("\n"))))


def gen_item(url):
    img_path = os.path.join(curr_dir, IMAGE_SAVE_PATH, "{0}_{1}.png".format(IMAGE_PREFIX, _filename(url)))
    try:
        gen_poster(url, img_path)
        duration = gen_duration(url)
        return {"videos": [{"src": url, "poster": img_path, "duration": duration}]}
    except Exception:
        logger.error("[ERR] %s" % url)


def main(file):
    print("Generating data file for %s " % file)
    with open(file) as f:
        urls = f.readlines()

    with jsonlines.open('output.jsonl', mode='w', flush=True) as writer:
        for url in urls:
            print("processing: %s" % url)
            i = gen_item(url.rstrip("\n"))
            writer.write(i)

    print("END")


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) <= 0:
        print("Usage: {0} <filename>".format(__file__.split("/")[-1:][0]))
    else:
        main(args[0])
