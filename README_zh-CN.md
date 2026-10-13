# 更便宜的 Banana Slides 图片方案 · ToAPIs 低价 API

[English](README.md) · [简体中文](README_zh-CN.md) · [Pricing](PRICING.md) · [Actual charges](COSTS.md) · [Real outputs](GALLERY.md)

用低价 API 做三页咖啡主题演示：**7 张真实图片、两份三页图片 PPT、一份加可编辑标题的副本，以及 1 条独立 4 秒图生视频**。2026-10-13 实测，图片消费 **$0.0526**，视频 **$0.0408**，本项目合计 **$0.0934（18.68 积分）**。

![Cover](screenshots/cn/01-cover.png)

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
