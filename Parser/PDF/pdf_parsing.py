import pymupdf
from multi_column import column_boxes

doc = pymupdf.open("./Parser/PDF/sample2.pdf")
for page in doc:
    bboxes = column_boxes(page, footer_margin=50, no_image_text=True)
    print(len(bboxes))
    # for idx, rect in enumerate(bboxes):
    #     print("RECT - ", idx, "\n")
    #     print(page.get_text(clip=rect, sort=True))
    #     print("*"*50)
    # print("-" * 80)
doc.close()
