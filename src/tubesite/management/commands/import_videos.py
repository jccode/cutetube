from django.core.management import BaseCommand
from django.core.files.storage import get_storage_class
from django.core.files import File as DjangoFile
import jsonlines
from filer_import import FileImporter, DUPLICATE_ACTIONS
from tubesite.models import Video


class VideoImporter(object):
    """
    Video importer
    """
    def __init__(self):
        self.default_folder_name = "poster"
        self.file_importer = FileImporter(None, self.default_folder_name, get_storage_class(),
                                          DUPLICATE_ACTIONS.overwrite)

    def import_image_file(self, path):
        """
        Import image file to django-filer

        :param path: image file path
        :return: Image object
        """
        name = self.file_name(path)
        dj_file = DjangoFile(open(path, mode='rb'), name=name)
        return self.file_importer.import_file(dj_file, self.file_importer.target_folder, None)

    def import_video_model(self, obj):
        """
        Import video model to database

        :param obj:
          {
            "category":
            "name":
            "desc":
            "quality":
            "videos": [
                {"src":"", "poster":"", "duration":""},
            ]
          }
        :return:
        """
        # TODO Parse "category"
        videos = obj.get("videos")
        if videos is None or len(videos) <= 0:
            print("You have to specify at least one video.")
            return

        v0 = videos[0]
        poster = v0.get("poster")
        if not poster:
            print("The first video poster should not be null")
            return
        if not poster.lower().startswith("http"):
            img = self.import_image_file(poster)
            poster = img.url
            # save local image
        video_model = Video(name=obj.get("name", ""), desc=obj.get("desc", ""), poster=poster)
        if len(videos) > 1:
            video_model.multiple = True
            video_model.extra = {
                "videos": videos
            }
            video_model.duration = sum(int(v.get("duration", "0")) for v in videos)
        else:
            video_model.multiple = False
            video_model.src = v0.get("src")
            video_model.duration = round(v0.get("duration"))
        video_model.save()

    @staticmethod
    def file_name(path):
        return path.split("/")[-1:][0]


class Command(BaseCommand):
    """
    Import videos command.

        manage.py import_videos <videos.jsonl>

    Where,

    `videos.jsonl` should be a  jsonLine format.

    `videos.jsonl` each item definition:

    ```
        {
            "category":
            "name":
            "desc":
            "quality":
            "videos": [
                {"src":"", "poster":"", "duration":""},
            ]
        }
    ```

    """
    help = __doc__

    def add_arguments(self, parser):
        parser.add_argument("file")

    def handle(self, *args, **options):
        self.stdout.write("Import videos, %s :)" % options['file'])
        video_importer = VideoImporter()
        with jsonlines.open(options["file"]) as reader:
            for obj in reader:
                video_importer.import_video_model(obj)
                # self._import_file_test(obj["_poster"])

