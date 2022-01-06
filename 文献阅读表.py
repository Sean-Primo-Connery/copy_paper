import os
import shutil


def copy_paper_reading_record(record_dir, term, template):
    os.chdir(record_dir)

    paper_name_list = ['2021-2022-1', '2021-2022-2', '2022-2023-1', '2022-2023-2',
                       '2023-2024-1', '2023-2024-2', '2024-2025-1', '2024-2025-2',
                       '2025-2026-1', '2025-2026-2'
                       ]

    for dir_name in paper_name_list[:term]:
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

    for i in range(20):
        for dir_name in paper_name_list[:term]:
            shutil.copy(template, f"{dir_name}/天津大学研究生文献阅读记录表_{dir_name}_{i + 1}.docx")


if __name__ == "__main__":
    record_dir_ = input("你希望记录表在哪里？\n>>")
    term_ = int(input("你需要文献阅读的学期数？\n>>"))
    template_ = input("你的文献阅读表模版在哪里？\n>>")
    copy_paper_reading_record(record_dir_, term_, template_)
    print("Done!")
