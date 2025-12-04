import pathlib
import zipfile
import os


class ZipHelper:
    def __init__(self, path: str, mode: str = "unpack"):
        self.path = path
        self.mode = mode

    def __call__(self):
        zipfile_path = pathlib.Path("Data_to_extract/Tasks.zip")
        with zipfile.ZipFile(zipfile_path, "r") as zip_ref:
            zip_ref.extractall(pathlib.Path(self.path))
            zip_ref.close()

    def unpack(self):
        if self.mode == "unpack":
            for dirpath, dirname, filenames in os.walk(self.path):
                for name in filenames:
                    if name.endswith(".zip"):
                        zipfile_path = pathlib.Path(os.path.join(self.path, name))
                        try:
                            with zipfile.ZipFile(zipfile_path, "r") as zip_ref:
                                zip_ref.extractall(
                                    pathlib.Path(os.path.join(self.path, name[:-4]))
                                )
                        except FileNotFoundError:
                            break
                        else:
                            pass
                        finally:
                            zip_ref.close()
                            try:
                                os.remove(os.path.join(self.path, name))
                            except FileNotFoundError:
                                print("no file")
                            finally:
                                self.unpack()

        elif self.mode == "pack":
            zipfile_path = pathlib.Path("packed_config.zip")
            with zipfile.ZipFile(zipfile_path, "w") as zip_ref:
                for dirpath, dirname, filenames in os.walk("./extracted_tasks"):
                    zip_ref.write(dirpath)
                    for filename in filenames:
                        filepath = os.path.join(dirpath, filename)
                        zip_ref.write(filepath)
        else:
            print("Unknown mode")

    def cleanup(self):
        try:
            for dirpath, dirname, filenames in os.walk(self.path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    os.remove(filepath)
        finally:
            for dirpath, dirname, filenames in os.walk(self.path):
                for dir in dirname:
                    folderpath = os.path.join(self.path, dir)
                    os.rmdir(folderpath)
