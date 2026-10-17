# Cheaper Banana Slides images · ToAPIs low-cost API


<!-- TOAPIS-MODEL-COST-UPDATE-20261016 -->
## Tested model types, presets and costs

Updated October 16, 2026. These are tested historical presets/prices; this addition does not relabel the original batch below.

| Model (API ID) | Type | Tested preset | Unit quote | Confirmed unit charge | Count |
|---|---|---|---:|---:|---:|
| gpt-image-2(VIP) (`gpt-image-2-vip`) | Image | low / 1K / n=1 | $0.0019/image | $0.0019 | 4 |
| gpt-image-2 | Image | 1K / n=1 | $0.015/image | $0.015 | 3 |
| Grok Video 1.5 (`grok-video-1.5`) | Video / I2V | I2V / 4s requested / 480p / 16:9 | $0.0408/clip | $0.0408 | 1 |

Confirmed original image/video example subtotal: **$0.0934**.

Patched image path and image-PPTX export validated; the historical Grok clip uses a separate helper, not native video support.

gpt-image-2(VIP), **from $0.0019/image**; the tested low/1K preset here is **$0.0019/image**. Different models, qualities and resolutions do not imply equivalent results.
<!-- /TOAPIS-MODEL-COST-UPDATE-20261016 -->

<!-- TOAPIS-IMAGE-SAMPLES-20261017 -->
## Same prompt: 8 image models and example costs

Tested **2026-10-17**: the same text-to-image prompt, one output per example, sorted by example amount from low to high. **gpt-image-2(VIP) starts at $0.0019/image; low/1K here is $0.0019/image.**

Each row identifies a task settlement receipt or an account billing log. Unknown-phase logs are not final net settlements; model/time-window candidates are not confirmed task matches. Catalog rates are historical quotes, not locked prices. gpt-image-2.5-flare-vip is token-metered: **$0.005272 is this image's settled charge**, not a fixed image rate. It is a different API ID from gpt-image-2.5-flare. Qwen has no returned key quote; only its example log amount is shown.

The prompt is shared, but quality defaults and output dimensions differ. Request presets and actual pixels are listed separately. Seedream Pro requested 1K with quality omitted (medium quoted), and returned 2048×2048. These are independent ToAPIs API asset tests; they do not extend any project's native-provider, UI, import or video validation, and are not added to the historical project subtotal below.

| Model / API ID | Request preset → actual pixels | Catalog rate (2026-10-17) | Example amount USD ↑ | Cost evidence | Real output |
|---|---|---:|---:|---|---|
| gpt-image-2(VIP)<br><code>gpt-image-2-vip</code> | 1K / low → 1024×1024 | $0.0019/image | **$0.0019** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2-vip.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2-vip.png" width="112" alt="gpt-image-2(VIP) product image"></a> |
| gpt-image-2.5-flare-vip | 1024x1024 / low → 1024×1024 | Token-based; key quote unavailable | **$0.005272** | Task receipt: settled | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare-vip.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare-vip.png" width="112" alt="gpt-image-2.5-flare-vip product image"></a> |
| nano_banana | 1K / default → 1024×1024 | $0.012/image | **$0.012** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/nano_banana.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/nano_banana.png" width="112" alt="nano_banana product image"></a> |
| gemini-nano-banana-2.1 | 1K / default → 1024×1024 | $0.015/image | **$0.015** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gemini-nano-banana-2.1.jpg"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gemini-nano-banana-2.1.jpg" width="112" alt="gemini-nano-banana-2.1 product image"></a> |
| gpt-image-2 | 1K / default → 1280×1280 | $0.015/image | **$0.015** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.png" width="112" alt="gpt-image-2 product image"></a> |
| qwen-image-3.0 | 1K / default → 1024×1024 | Key quote unavailable | **$0.021** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/qwen-image-3.0.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/qwen-image-3.0.png" width="112" alt="qwen-image-3.0 product image"></a> |
| gpt-image-2.5-flare | 1K / high → 1024×1024 | $0.0225/image | **$0.0225** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare.png" width="112" alt="gpt-image-2.5-flare product image"></a> |
| doubao-seedream-5-0-pro | 1K / default → 2048×2048 | $0.042857/image | **$0.042856** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/doubao-seedream-5-0-pro.jpg"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/doubao-seedream-5-0-pro.jpg" width="112" alt="doubao-seedream-5-0-pro product image"></a> |

![8 models ordered by example amount](https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/overview-en.jpg)

[Shared prompt, originals and cost sources](https://github.com/ToAPIs-2025/toapis-quickstart/tree/main/tutorials/image-model-samples-2026-10-17/README.md) · [Pricing API](https://docs.toapis.com/docs/en/api-reference/account/pricing)

<!-- /TOAPIS-IMAGE-SAMPLES-20261017 -->

[English](README.md) · [简体中文](README_zh-CN.md) · [Pricing](PRICING.md) · [Actual charges](COSTS.md) · [Real outputs](GALLERY.md)



Build a three-slide coffee story with a lower-cost image route: **7 real images, two three-slide image PPTX files, a copy with editable captions, and one independent 4-second image-to-video clip**. Tested 2026-10-13. Actual image charges **$0.0526**, video **$0.0408**; this project total **$0.0934 (18.68 credits)**.



## Demo



![Cover](screenshots/en/01-cover.png)



## Video demo



This animated preview is extracted from our real generated coffee clip. Click to view the original MP4:



[![Real 4-second image-to-video demo](assets/coffee-motion-preview.gif)](assets/coffee-motion.mp4)



**[Watch the video](https://github.com/ToAPIs-2025/cheaper-banana-slides-toapis/blob/main/assets/coffee-motion.mp4)** · [Download original MP4](https://raw.githubusercontent.com/ToAPIs-2025/cheaper-banana-slides-toapis/main/assets/coffee-motion.mp4) · [Full demo and reuse guide](DEMO.md)



A generated coffee image becomes the first frame for the separate Grok Video 1.5 helper. Actual charge: **8.16 credits=$0.0408**. This is an output demo; an application walkthrough recording has not been made. Native Banana Slides video support is not validated.



### Generation parameters and actual charge



```json

{

  "model": "grok-video-1.5",

  "prompt": "A calm premium coffee product film. Very slow camera push-in, delicate natural steam drifting above the ivory espresso cup, subtle warm light movement. Keep the cup and studio composition recognizable. No new objects, no text, no logos.",

  "video_generation_mode": "first_frame_image_to_video",

  "duration": 4,

  "resolution": "480p",

  "aspect_ratio": "16:9",

  "image": "<uploaded-reference-url-omitted>"

}

```



`image` is the URL returned after uploading [vip-low-01.png](assets/vip-low-01.png); the temporary upload URL is omitted here. Requested tier: 480p, 16:9, 4 seconds. Actual file: 736×400, 4.04 seconds.



**Actual charge: 8.16 credits × $0.005/credit = $0.0408.** Confirmed from the account-owner-provided Task Logs screenshot; API billing remains absent. [Charge provenance](evidence/actual-costs.json).







“Cheaper” comparison: VIP low / 1K **$0.0019/image** versus standard / 1K **$0.015/image**, approximately 87.3% lower quoted rate in this test. Different quality settings and routes; compare the outputs yourself. [Price table](PRICING.md) · [Itemized actual charges](COSTS.md).



## Reproduce the test



Python 3.12 and Git; tested with openai 3.29.0 and Pillow 12.3.0. This is a community integration tutorial and minimal patch, not an official upstream low-cost edition or evidence of a partnership. Install the full application using upstream instructions; the commands here reproduce the backend provider and image export only.



```bash

git clone https://github.com/ToAPIs-2025/cheaper-banana-slides-toapis.git

git clone https://github.com/Anionex/banana-slides.git banana-upstream

git -C banana-upstream checkout 8bcde44c95646a863b23b1e4fc43c9a42ea4e3f7

cd cheaper-banana-slides-toapis

git -C ../banana-upstream apply ../cheaper-banana-slides-toapis/adapter.patch

python -m venv .venv

# Windows: .venv\Scripts\activate

# macOS/Linux: source .venv/bin/activate

python -m pip install -r requirements-demo.txt

cp .env.example .env

# Fill TOAPIS_API_KEY privately. Windows PowerShell: Copy-Item .env.example .env

python run_cases.py --upstream ../banana-upstream

python tests/test_adapter.py --upstream ../banana-upstream

python run_cases.py --upstream ../banana-upstream --key-file .env --live --case vip-low-01

python run_cases.py --upstream ../banana-upstream --key-file .env --live

```



The default command makes no API call. `--live` generates paid images; the first live command generates just one. All 7 image cases cost an estimated $0.0526 at the listed rates. Reference editing depends on vip-low-01. Completed evidence is reused in the same output folder. Keep private-state receipts; reconcile a missing task ID with Task Logs instead of automatically resubmitting.



## Adapter and reuse improvements



Pinned upstream SHA: `8bcde44c95646a863b23b1e4fc43c9a42ea4e3f7`. The patch adds ToAPIs routing to `backend/services/ai_providers/image/openai_provider.py` and a new `toapis_image_provider.py`. The existing synchronous OpenAI path cannot consume the async task ID directly; the adapter performs:



1. `Authorization: Bearer TOAPIS_API_KEY`; `https://toapis.cn` or `https://toapis.com`, origin or `/v1` normalized once.

2. `POST /v1/uploads/images` for PNG references, then `reference_images: [URL]`.

3. `POST /v1/images/generations`: exact model, prompt, n=1, size=`16:9`, resolution=`1K`; VIP low adds quality=`low`, standard omits quality.

4. Persist task ID; `GET /v1/images/generations/{id}` every 8 seconds, up to 600 seconds.

5. Download `result.data[0].url` without API Key, return a PIL image to the real upstream provider.



Improvements: durable pre-submission state, no duplicate generation POST, retained failed task IDs, completed-result reuse and downloads without credentials. Five offline tests cover these cases. The adapter validates 1K/2K/4K parameters, but only 1K was tested live; actual pixel sizes differ, as listed in [evidence](EVIDENCE.md). Full frontend settings are unverified. The existing IMAGE_MODEL_SOURCE=openai route and ToAPIs image base can be used for a later product-level check.



## Reuse outputs without another generation



```bash

python run_cases.py --upstream ../banana-upstream --output results --export-only

python extras/native_titles.py results/vip-low-three-slides.pptx --output results/vip-low-native-captions.pptx

```



The real upstream ExportService.create_pptx_from_images exported both three-image sequences; each was reopened and confirmed to have three slides. These are image-mode PPTX files. Only the three caption boxes added by the separate helper are editable. The full upstream OCR/native editable-export path was not tested. Download [standard PPTX](assets/standard-three-slides.pptx), [low-cost PPTX](assets/vip-low-three-slides.pptx) or [editable-caption copy](assets/vip-low-native-captions.pptx).



## Optional: turn the image into a 4-second clip



```bash

python extras/video_extension.py --input assets/vip-low-01.png

python extras/video_extension.py --input assets/vip-low-01.png --key-file .env --live

```



This is a separate script, not native Banana Slides video support. Exact model grok-video-1.5, first_frame_image_to_video, 4 seconds, 480p, 16:9. Actual charge: 8.16 credits=$0.0408. The helper checks the matching rate and its independent $1 safety cap before submitting. It uploads the image, submits a video task, polls and downloads an MP4. [Real clip](assets/coffee-motion.mp4) · [Request and hash](evidence/video-extension.json). Requested 480p; actual output is 736×400 and 4.04 seconds. Audio was not validated.



## Upstream and license



[Anionex/banana-slides](https://github.com/Anionex/banana-slides) · [Pinned source](https://github.com/Anionex/banana-slides/tree/8bcde44c95646a863b23b1e4fc43c9a42ea4e3f7) · [AGPL-3.0](LICENSE). Preserve upstream notices when reusing the patch. All product scenes are fictional original prompts; no customer logos or sales figures.



[Explore ToAPIs image API](https://go2v.toapis.com/1013_banana_cheaper_gh_en) · [X screenshot guide](SCREENSHOT_GUIDE.md)

