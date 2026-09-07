def test_file_path(file_path):
    res1331 = file_path.split("\\")
    file_name = res1331[-1].rsplit(".", 1)[0]
    disk_name = res1331[0][:1]
    root_folder = res1331[1]

    return file_name, disk_name, root_folder
