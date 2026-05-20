import torch

# PyTorch 2.6+ compatibility patch for loading older DeOldify / fastai model weights
_orig_torch_load = torch.load
def _patched_torch_load(*args, **kwargs):
    if "weights_only" not in kwargs:
        kwargs["weights_only"] = False
    return _orig_torch_load(*args, **kwargs)
torch.load = _patched_torch_load

from pathlib import Path
from PIL import Image

from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import get_image_colorizer


device.set(device=DeviceId.CPU)

ROOT_DIR = Path(".")

colorizer = get_image_colorizer(
    root_folder=ROOT_DIR,
    artistic=True
)


def restore_image(input_path, output_path):

    img = Image.open(input_path).convert("RGB")

    width, height = img.size

    if width < 600:
        scale = 600 / width
        img = img.resize(
            (int(width * scale), int(height * scale)),
            Image.LANCZOS
        )
        img.save(input_path)

    result = colorizer.get_transformed_image(
        path=input_path,
        render_factor=40
    )

    result.save(output_path)