import pathlib
import shutil
import zipfile
import os


class ZipHelper():
    def __init__(
        self,
        path: str,
        mode: str = "unpack",
        source: str = "Data_to_extract/Tasks.zip",
        destination: str = "packed_config.zip",
    ):
        self.path = path
        self.mode = mode
        self.source = source
        self.destination = destination

        zipfile_path = pathlib.Path(source)
        with zipfile.ZipFile(zipfile_path, "r") as zip_ref:
            zip_ref.extractall(pathlib.Path(self.path))
            zip_ref.close()

        match self.mode:
            case "unpack":
                self.unpack()
            case "pack":
                self.pack()
            case "cleanup":
                self.cleanup()

    def unpack(self):
        extentions = [".zip", ".7z", "tar"]
        for dirpath, dirname, filenames in os.walk(self.path):
            for name in filenames:
                if name.endswith(tuple(extentions)):
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
                    except FileNotFoundError as e:
                        print(f"no file - message {e}")
                    finally:
                        try:
                            os.remove(os.path.join(self.path, name))
                        except FileNotFoundError as e:
                            print(f"no file - message {e}")
                            self.unpack()

    def pack(self):
        zipfile_path = pathlib.Path(self.destination)
        with zipfile.ZipFile(zipfile_path, "w") as zip_ref:
            for dirpath, dirname, filenames in os.walk(self.path):
                zip_ref.write(dirpath)
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    zip_ref.write(filepath)

    def cleanup(self):
        shutil.rmtree(self.path)
