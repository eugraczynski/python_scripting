import util.zipHelper as zipHelper


zipper = zipHelper.ZipHelper("extracted_tasks")
zipper.__call__()
zipper.unpack()
# zipper.cleanup()
