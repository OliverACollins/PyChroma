from PIL import Image, ImageDraw
import numpy as np
import random
from scipy.ndimage import distance_transform_edt


def generate(
    input_path,
    output_path,
    red_dots,
    green_dots,
    scale=3,
):

    random.seed()

    # -------------------------
    # Load image
    # -------------------------
    img = Image.open(input_path).convert("RGB")
    arr = np.array(img)
    h, w, _ = arr.shape

    # -------------------------
    # Colour masks
    # -------------------------
    red_mask = (
        (arr[:, :, 0] > 150) &
        (arr[:, :, 0] > arr[:, :, 1] + 40) &
        (arr[:, :, 0] > arr[:, :, 2] + 40)
    )

    green_mask = (
        (arr[:, :, 1] > 100) &
        (arr[:, :, 1] > arr[:, :, 0] + 40) &
        (arr[:, :, 1] > arr[:, :, 2] + 40)
    )

    # -------------------------
    # High-resolution canvas
    # -------------------------
    out_hi = Image.new(
        "RGBA",
        (w * scale, h * scale),
        (0, 0, 0, 255)
    )
    draw = ImageDraw.Draw(out_hi)

    # -------------------------
    # Render logging in terminal
    # -------------------------
    def cells(density):
        return ((h + density - 1) // density) * ((w + density - 1) // density)

    total_work = (
        cells(green_dots["density"]) +
        cells(red_dots["density"])
    )

    progress = {
        "done": 0,
        "last_print": -1
    }

    # -------------------------
    # Render dot layers
    # -------------------------
    _render_dots(
        draw=draw,
        mask=green_mask,
        colour=(0, 200, 0),
        scale=scale,
        h=h,
        w=w,
        progress=progress,
        total_work=total_work,
        **green_dots,
    )

    _render_dots(
        draw=draw,
        mask=red_mask,
        colour=(255, 0, 0),
        scale=scale,
        h=h,
        w=w,
        progress=progress,
        total_work=total_work,
        **red_dots,
    )

    if progress["last_print"] != 100:
        print("Rendering: 100%")

    # -------------------------
    # Downsample & save
    # -------------------------
    out = out_hi.resize((w, h), Image.LANCZOS).convert("RGB")
    out.save(output_path)

    print(f"Saved image to: {output_path}")
    out.show()


def _render_dots(
    draw,
    mask,
    colour,
    radius,
    density,
    jitter,
    ratio,
    shape,
    scale,
    h,
    w,
    progress,
    total_work,
):
    dist = distance_transform_edt(mask)

    for y0 in range(0, h, density):
        for x0 in range(0, w, density):
            progress["done"] += 1
            percent = int((progress["done"] / total_work) * 100)

            if percent % 5 == 0 and percent != progress["last_print"]:
                print(f"Rendering: {percent}%")
                progress["last_print"] = percent

            y1 = min(y0 + density, h)
            x1 = min(x0 + density, w)

            cell = mask[y0:y1, x0:x1]
            if not cell.any():
                continue

            ys, xs = np.where(cell)
            i = random.randrange(len(xs))

            x = (x0 + xs[i] + random.uniform(-jitter, jitter)) * scale
            y = (y0 + ys[i] + random.uniform(-jitter, jitter)) * scale

            xi = int(round(x / scale))
            yi = int(round(y / scale))

            if xi < 0 or xi >= w or yi < 0 or yi >= h:
                continue

            d = dist[yi, xi]
            if d <= 0.6:
                continue

            edge_norm = min(1.0, d / 5.0)
            is_small = random.random() < ratio

            if is_small:
                r = radius * random.uniform(0.5, 0.8)
            else:
                r = radius * random.uniform(1.1, 1.6)

            r *= (0.6 + 0.4 * edge_norm)

            r *= scale
            r = min(r, (d - 0.6) * scale)

            if r <= 0.6 * scale:
                continue

            if shape == "square":
                draw.rounded_rectangle(
                    (x - r, y - r, x + r, y + r),
                    radius=0.25 * r,
                    fill=colour
                )
            else:
                draw.ellipse(
                    (x - r, y - r, x + r, y + r),
                    fill=colour
                )