# 视频与PPT演示

[English](DEMO.md) · [中文](DEMO_zh-CN.md)

## 真实图生视频

[![Coffee motion preview](assets/coffee-motion-preview.gif)](assets/coffee-motion.mp4)

[MP4 viewer](https://github.com/ToAPIs-2025/cheaper-banana-slides-toapis/blob/main/assets/coffee-motion.mp4) · [Original MP4](https://raw.githubusercontent.com/ToAPIs-2025/cheaper-banana-slides-toapis/main/assets/coffee-motion.mp4)

输入：[真实生成的首帧图片](assets/vip-low-01.png)。独立扩展：上传图片 → `grok-video-1.5` / `first_frame_image_to_video` / 4秒 / 480p / 16:9 → 任务查询 → 下载 MP4。实际输出736×400、4.04秒，后台消费8.16积分=$0.0408。[完整请求与任务证据](evidence/video-extension.json)。

GIF从原始成片每0.1秒取帧，仅为首页播放预览；原始MP4未修改。展示的是生成结果，不是客户端操作录屏。未验证上游原生视频功能和音频。

## 三页PPT复用展示

[Standard PPTX](assets/standard-three-slides.pptx) · [VIP-low PPTX](assets/vip-low-three-slides.pptx) · [Editable-caption copy](assets/vip-low-native-captions.pptx)

![Three-slide outputs](screenshots/cn/01-cover.png)

两个原始PPT为图片模式；独立helper添加的标题框可编辑，完整OCR可编辑导出未测。复现命令见[中文教程](README_zh-CN.md)。
