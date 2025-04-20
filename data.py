from pycocotools.coco import COCO
import shutil
import os

def select_coco_images(data_dir, output_dir, categories, num_images=10):
    coco = COCO(f'{data_dir}/annotations/instances_val2017.json')
    os.makedirs(output_dir, exist_ok=True)
    selected = 0
    for cat in categories:
        cat_ids = coco.getCatIds(catNms=[cat])
        img_ids = coco.getImgIds(catIds=cat_ids)
        for img_id in img_ids:
            if selected >= num_images:
                break
            img_info = coco.loadImgs(img_id)[0]
            shutil.copy(
                f'{data_dir}/val2017/{img_info["file_name"]}',
                f'{output_dir}/{cat}_{img_info["file_name"]}'
            )
            selected += 1

select_coco_images(
    'coco_val2017',
    'selected_coco',
    ['hamburger', 'car', 'dog'],
    num_images=10
)