import pathlib
import shutil
import zipfile
import os


# make 'mode' a parameter type
class ZipHelper:
    def __init__(self, path: str, source: str, mode: str = "unpack"):
        self.path = path
        self.mode = mode

        zipfile_path = pathlib.Path("Data_to_extract/Tasks.zip")
        with zipfile.ZipFile(zipfile_path, "r") as zip_ref:
            zip_ref.extractall(pathlib.Path(self.path))
            zip_ref.close()

        if self.mode == "unpack":
            self.unpack()

        elif self.mode == "pack":
            self.pack()

        elif self.mode == "cleanup":
            self.cleanup()

    def unpack(self):
        for dirpath, dirname, filenames in os.walk(self.path):
            for name in filenames:
                if name.endswith(".zip") | name.endswith(".7z"):
                    zipfile_path = pathlib.Path(os.path.join(self.path, name))
                    try:
                        with zipfile.ZipFile(zipfile_path, "r") as zip_ref:
                            zip_ref.extractall(
                                pathlib.Path(
                                    os.path.join(self.path, name[0 : name.rfind(".")])
                                    # trying to fit this logic for every file extention
                                    # candidates are:
                                    # name[0 : name.rfind(".")]     name.rsplit(".", 1)[0]
                                )
                            )

                    # fix this
                    except FileNotFoundError as e:
                        print(f"no file - message {e}")
                        try:
                            os.remove(os.path.join(self.path, name))
                        except FileNotFoundError as e:
                            print(f"no file - message {e}")
                            self.unpack()

    def pack(self):
        zipfile_path = pathlib.Path("packed_config.zip")
        with zipfile.ZipFile(zipfile_path, "w") as zip_ref:
            for dirpath, dirname, filenames in os.walk(self.path):
                zip_ref.write(dirpath)
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    zip_ref.write(filepath)

    def cleanup(self):
        shutil.rmtree(self.path)
