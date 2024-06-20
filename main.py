import datetime
import re
import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication
from interface.progress_dialog import Dialog

if __name__ == '__main__':
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        app_path = Path(sys._MEIPASS)
    else:
        app_path = Path(sys.argv[0]).parent

    today = datetime.datetime.today().strftime("%Y.%m.%d")
    mapped_drive_root = '//primevic.sharepoint.com@SSL/DavWWWRoot'
    src_path = Path(sys.argv[1].replace('https://primevic.sharepoint.com', mapped_drive_root))
    clean_file_stem = re.sub('(?<=Master_).*', '', src_path.stem)
    copy_path = src_path.parent / 'X_OLD' / Path(clean_file_stem + today + src_path.suffix)
    app = QApplication(sys.argv)
    window = Dialog(app_path, src_path, copy_path)
    window.run_progress()
    sys.exit(app.exec())


