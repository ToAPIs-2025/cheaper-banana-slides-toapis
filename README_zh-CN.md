# 更便宜的 Banana Slides 图片方案 · ToAPIs 低价 API


<!-- TOAPIS-MODEL-COST-UPDATE-20261016 -->
## 模型类型、测试档位与花费

更新：2026-10-16。下表为已验证案例的历史档位与价格；本段补充不改变下方原批次记录。

| 模型（API ID） | 类型 | 测试档位 | 单次报价 | 已确认单次消费 | 数量 |
|---|---|---|---:|---:|---:|
| gpt-image-2(VIP) (`gpt-image-2-vip`) | 图片 | low / 1K / n=1 | $0.0019/image | $0.0019 | 4 |
| gpt-image-2 | 图片 | 1K / n=1 | $0.015/image | $0.015 | 3 |
| Grok Video 1.5 (`grok-video-1.5`) | 视频 / 图生视频 | I2V / 4s requested / 480p / 16:9 | $0.0408/clip | $0.0408 | 1 |

原图片/视频案例已核对消费小计：**$0.0934**。

图片适配及图片PPTX导出已验证；历史Grok视频为独立脚本，不是原生视频入口。

gpt-image-2(VIP) **$0.0019/image 起**；本表 low/1K 实测档位为 **$0.0019/image**。不同模型、质量和分辨率不代表同质效果。
<!-- /TOAPIS-MODEL-COST-UPDATE-20261016 -->

<!-- TOAPIS-IMAGE-SAMPLES-20261017 -->
## 同一提示词：8 个图片模型与消费对比

测试日期：**2026-10-17**。8 个模型使用同一条文生图提示词，每例 1 张，按本例消费金额从低到高排列。**gpt-image-2(VIP) $0.0019/image 起；本例 low/1K 为 $0.0019/image。**

金额来自任务结算回执或账号计费日志，逐行注明来源。阶段未知的日志不代表最终净结算；按模型/时间窗口匹配的记录尚未确认到单个任务。目录价是历史报价，不是锁价。gpt-image-2.5-flare-vip 按 Token 计费，**$0.005272 仅为这一张的已结算费用**，不是固定单张价；它与 gpt-image-2.5-flare 是不同 API ID。Qwen 的目录价未返回，只展示本例日志金额。

提示词相同，模型默认质量和实际分辨率不同；表内将请求与输出分别列出。Seedream Pro 请求 1K、未传 quality（报价档位 medium），实际返回 2048×2048。这组图片是独立 ToAPIs API 素材测试，不新增任何项目原生 Provider、UI、图片导入或视频的验收结论，也不计入下方历史项目消费小计。

| 模型 / API ID | 请求档位 → 实际尺寸 | 目录价（2026-10-17） | 本例消费金额 USD ↑ | 费用依据 | 真实输出 |
|---|---|---:|---:|---|---|
| gpt-image-2(VIP)<br><code>gpt-image-2-vip</code> | 1K / low → 1024×1024 | $0.0019/image | **$0.0019** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2-vip.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2-vip.png" width="112" alt="gpt-image-2(VIP) product image"></a> |
| gpt-image-2.5-flare-vip | 1024x1024 / low → 1024×1024 | 按 Token；Key 报价未返回 | **$0.005272** | 任务回执 settled | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare-vip.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare-vip.png" width="112" alt="gpt-image-2.5-flare-vip product image"></a> |
| nano_banana | 1K / default → 1024×1024 | $0.012/image | **$0.012** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/nano_banana.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/nano_banana.png" width="112" alt="nano_banana product image"></a> |
| gemini-nano-banana-2.1 | 1K / default → 1024×1024 | $0.015/image | **$0.015** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gemini-nano-banana-2.1.jpg"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gemini-nano-banana-2.1.jpg" width="112" alt="gemini-nano-banana-2.1 product image"></a> |
| gpt-image-2 | 1K / default → 1280×1280 | $0.015/image | **$0.015** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.png" width="112" alt="gpt-image-2 product image"></a> |
| qwen-image-3.0 | 1K / default → 1024×1024 | Key 报价未返回 | **$0.021** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/qwen-image-3.0.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/qwen-image-3.0.png" width="112" alt="qwen-image-3.0 product image"></a> |
| gpt-image-2.5-flare | 1K / high → 1024×1024 | $0.0225/image | **$0.0225** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare.png" width="112" alt="gpt-image-2.5-flare product image"></a> |
| doubao-seedream-5-0-pro | 1K / default → 2048×2048 | $0.042857/image | **$0.042856** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/doubao-seedream-5-0-pro.jpg"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/doubao-seedream-5-0-pro.jpg" width="112" alt="doubao-seedream-5-0-pro product image"></a> |

![8 models ordered by example amount](https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/overview-cn.jpg)

[共同提示词、原图与费用来源](https://github.com/ToAPIs-2025/toapis-quickstart/tree/main/tutorials/image-model-samples-2026-10-17/README_zh-CN.md) · [Pricing API](https://docs.toapis.com/docs/en/api-reference/account/pricing)

<!-- /TOAPIS-IMAGE-SAMPLES-20261017 -->

[English](README.md) · [简体中文](README_zh-CN.md) · [Pricing](PRICING.md) · [Actual charges](COSTS.md) · [Real outputs](GALLERY.md)



用低价 API 做三页咖啡主题演示：**7 张真实图片、两份三页图片 PPT、一份加可编辑标题的副本，以及 1 条独立 4 秒图生视频**。2026-10-13 实测，图片消费 **$0.0526**，视频 **$0.0408**，本项目合计 **$0.0934（18.68 积分）**。



## 演示



![Cover](screenshots/cn/01-cover.png)



## 视频演示



下方动态预览来自本次真实生成的咖啡视频。点击观看原始 MP4：



[![4秒真实图生视频演示](assets/coffee-motion-preview.gif)](assets/coffee-motion.mp4)



**[打开视频](https://github.com/ToAPIs-2025/cheaper-banana-slides-toapis/blob/main/assets/coffee-motion.mp4)** · [下载原始 MP4](https://raw.githubusercontent.com/ToAPIs-2025/cheaper-banana-slides-toapis/main/assets/coffee-motion.mp4) · [完整演示与复用入口](DEMO_zh-CN.md)



用已生成的咖啡图片作为首帧，独立 Grok Video 1.5 脚本生成；消费 **8.16积分=$0.0408**。这是生成结果展示；产品操作录屏尚未制作。不是 Banana Slides 原生视频功能验收。



### 生成参数与实际消费



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



`image` 为上传 [vip-low-01.png](assets/vip-low-01.png) 后返回的 URL；公开材料省略临时上传地址。请求档位为480p、16:9、4秒；实际文件为736×400、4.04秒。



**实际消费：8.16积分 × $0.005/积分 = $0.0408。** 后台任务日志由账号持有人提供，API billing仍为空；来源见[消费记录](evidence/actual-costs.json)。







“更便宜”对比：VIP low / 1K **$0.0019/张**；标准 / 1K **$0.015/张**，本次报价低约 87.3%。画质档位与通道不同，请自己比较效果。[完整价表](PRICING_zh-CN.md) · [逐项实际消费](COSTS_zh-CN.md)。



## 开始复现



Python 3.12、Git；本次 openai 3.29.0、Pillow 12.3.0。此仓库是独立社区适配教程和最小补丁，不是上游官方低价版，也不代表已建立商务合作。完整应用按上游文档安装；以下只复现后台 Provider 与图片导出。



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



默认命令不调用 API。`--live` 才付费生成；首个用例只生成一张。全部 7 张按本次价表预估 $0.0526。参考编辑依赖先生成 vip-low-01。相同输出目录已有 evidence 会复用；不要删除 private-state 重跑来“排错”。未拿到任务 ID 时先查后台日志，不能自动重发 POST。



## 接口适配与优化



上游固定 SHA `8bcde44c95646a863b23b1e4fc43c9a42ea4e3f7`。修改 `backend/services/ai_providers/image/openai_provider.py` 的 ToAPIs 分流，新增 `toapis_image_provider.py`；现有 OpenAI 接口返回方式无法直接消费任务 ID，补丁执行以下步骤：



1. `Authorization: Bearer TOAPIS_API_KEY`; `https://toapis.cn` or `https://toapis.com`, origin or `/v1` normalized once.

2. `POST /v1/uploads/images` for PNG references, then `reference_images: [URL]`.

3. `POST /v1/images/generations`: exact model, prompt, n=1, size=`16:9`, resolution=`1K`; VIP low adds quality=`low`, standard omits quality.

4. Persist task ID; `GET /v1/images/generations/{id}` every 8 seconds, up to 600 seconds.

5. Download `result.data[0].url` without API Key, return a PIL image to the real upstream provider.



最小安全优化：持久化提交前状态、防重复付费、保留失败任务、复用已完成结果、下载不携带鉴权。五项离线测试覆盖上述异常。底层支持 1K/2K/4K 参数校验，本次仅实测 1K；真实像素尺寸不同，见 [证据表](EVIDENCE.md)。完整前端配置未验收；后续可用现有 `IMAGE_MODEL_SOURCE=openai` 和 ToAPIs image base 配置做产品内验证。



## 生成之后复用：不再调用 API



```bash

python run_cases.py --upstream ../banana-upstream --output results --export-only

python extras/native_titles.py results/vip-low-three-slides.pptx --output results/vip-low-native-captions.pptx

```



两组各三张图经上游 `ExportService.create_pptx_from_images` 真实导出、重新打开确认三页。它们是图片模式 PPT；独立 helper 添加的三个标题框才可编辑，未运行上游完整 OCR/原生可编辑导出。你也可直接下载 [标准版 PPT](assets/standard-three-slides.pptx)、[低价版 PPT](assets/vip-low-three-slides.pptx)、[可编辑标题副本](assets/vip-low-native-captions.pptx)。



## 可选：图片扩展为 4 秒视频



```bash

python extras/video_extension.py --input assets/vip-low-01.png

python extras/video_extension.py --input assets/vip-low-01.png --key-file .env --live

```



这是独立脚本，不代表 Banana Slides 原生视频能力。准确模型 `grok-video-1.5`、first_frame_image_to_video、4秒、480p、16:9；本次消费 8.16 积分=$0.0408。脚本先匹配当前报价并检查其独立 $1 上限。原图先上传，视频 POST→任务查询→MP4 下载。[真实 MP4](assets/coffee-motion.mp4) · [请求和哈希](evidence/video-extension.json)。请求 480p，实际输出 736×400、4.04秒，未验收音频。



## 原项目与协议



[Anionex/banana-slides](https://github.com/Anionex/banana-slides) · [Pinned source](https://github.com/Anionex/banana-slides/tree/8bcde44c95646a863b23b1e4fc43c9a42ea4e3f7) · [AGPL-3.0](LICENSE). Preserve upstream notices when reusing the patch. All product scenes are fictional original prompts; no customer logos or sales figures.



[开通 ToAPIs 图片 API](https://go2v.toapis.com/1013_banana_cheaper_gh_cn) · [X screenshot guide](SCREENSHOT_GUIDE_zh-CN.md)

