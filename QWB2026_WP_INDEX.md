# 第十届强网杯（QWB 2026）初赛 WP 索引

- 赛事：2026-11-01 完赛，41 题（Misc 6 / Crypto 6 / Reverse 3 / PWN 17 / Web 9），3206 队、14196 人。
- 官方/公开 WP 仓：`https://github.com/ThanatosXingYu/qwb2026s10_writeups`（全方向；本目录已镜像主要文件）
- 赛事题解（中文）：[Web&Reverse WP（二）](https://cn-sec.com/archives/5548848.html)、[Misc&Crypto WP（三）](https://cn-sec.com/archives/5548779.html)
- 本目录结构：
  - `qwb_wp/*.md`：Babyv8 等我们做过题目的 WP/exp
  - `qwb_wp/other/`：CanonicoPWN、Dreambound、Blackout、babyark、babystar、vaultlink、crp-12025 的 WP
  - `qwb_wp/pwn/`：其余 PWN 题 WP（12 份）
  - `qwb_wp/all/`：Web/Reverse/Misc/Crypto（除已单独存放的）
  - `qwb_wp/timu/`：8 道题的官方题面（含提示）
  - 复盘：[REFLECTION.md](REFLECTION.md)；会话摘要：[sessions_summary.tsv](sessions_summary.tsv)

> 解出队数来自 CN-SEC 赛后统计；“我们的状态”指本次会话/归档分支的真实结果（✅=有自证 flag，◐=部分/本地，✗=未解）。

## PWN（17）

| # | 题目 | 解出队数 | 我们的状态 | 本地 WP | 一句话考点 |
|---|---|---|---|---|---|
| 1 | babel | 414 | ◐ 本地 10/10 | `qwb_wp/pwn/PWN1_babel.md` | 见 WP；我们本地已打通，未转远程 |
| 2 | babyark | 399 | ◐ 原语通、差 RW | `qwb_wp/other/babyark_WP.md` | ArkTS abc `ldlexvar/stlexvar` 无边界校验（512KB OOB）→ 伪造 JSNativePointer → ROP |
| 3 | babysilent | 538 | — | `qwb_wp/pwn/PWN3_babysilent.md` | 见 WP |
| 4 | babystar | 329 | ◐ 协议/表注入方向 | `qwb_wp/other/babystar_WP.md` | cFS 三张可上传表（HK/HS/AMT）数据驱动命令注入 → CF class 1 读 `/cf/host/flag` |
| 5 | Babyv8 | 282 | ◐ 假数组/原语通 | `qwb_wp/Babyv8_WriteUp.md` + `Babyv8_exp.py` | Maglev loop-phi 类型混淆 + FeedbackCell `cached_entrypoint` → cage RW → ROP `execvp("/readflag")` |
| 6 | bad_puppet | 180 | ◐ 逻辑/race 分析 | `qwb_wp/pwn/PWN6_bad_puppet.md` | 见 WP；我们定位了 race + `inv equip 0`/`mw whisper` |
| 7 | Blackout | 167 | ✗（停在第一段） | `qwb_wp/other/Blackout_WP.md` | 两段式：装置 `ied` shell → 主站 `server_sg5000` → `oper` → `/flag` → MMS `FileRead` |
| 8 | drywell | 215 | — | `qwb_wp/pwn/PWN8_drywell.md` | 见 WP |
| 9 | easytl | 1059 | — | `qwb_wp/pwn/PWN9_easytl.md` | 见 WP |
| 10 | HESEUS | 196 | — | `qwb_wp/pwn/PWN10_HESEUS.md` | 见 WP |
| 11 | oldsvr | 605 | — | `qwb_wp/pwn/PWN11_oldsvr.md` | 见 WP |
| 12 | ez_qemu | 191 | ◐ 本地 TCG 通 | `qwb_wp/pwn/PWN12_ez_qemu.md` | QEMU/TCG 侧；本地读到 `flag{local_test_ez_qemu}`，远程未打 |
| 13 | CanonicoPWN | 264 | ✗（漏了精确版本 CVE） | `qwb_wp/other/CanonicoPWN_WP.md` | Ubuntu 26.04 `7.0.0-39.39` → **CVE-2026-98260**（公开 PoC）；POSIX CPU timer UAF → 覆盖 `task->cred` |
| 14 | hexachord | 10 | — | `qwb_wp/pwn/PWN14_hexachord.md` | 见 WP（仅 10 队） |
| 15 | What The Fox! | 161 | — | `qwb_wp/pwn/PWN15_What The Fox!.md` | 见 WP |
| 16 | shadowledger | 273 | ◐ 堆/校验链分析 | `qwb_wp/pwn/PWN16_shadowledger.md` | 见 WP |
| 17 | Ironclad | 60 | — | `qwb_wp/pwn/PWN17_Ironclad.md` | 见 WP |

## Web（9）

| # | 题目 | 解出队数 | 我们的状态 | 本地 WP | 一句话考点 |
|---|---|---|---|---|---|
| 1 | BlindReview | 12 | ◐ 分析 | `qwb_wp/all/Web1_BlindReview.md`（stub） | 见赛题/题解 |
| 2 | cwp | 1340 | ✅ `flag{622e4b70-1203-4c03-a3f9-a07c713c177c}` | `qwb_wp/all/Web2_cwp.md` | bulk 数组错位 → SQLi → 快照 hook 伪造 staff → 模板写入 → 内网 ops → root |
| 3 | ezphp | 760 | — | `qwb_wp/all/Web3_ezphp.md` | 源码泄露 → SSRF gopher → Redis session 反序列化 → 文件写 → webshell |
| 4 | ezstar | 279 | — | `qwb_wp/all/Web4_ezstar.md` | OpenMCT `/proxyUrl` → sgdecode 定长 hex dump 泄露 → Golay 长度 0 堆溢出 → ROP |
| 5 | ezcms | 467 | ✅ `flag{9aaad8d7-0f1d-49b8-a122-62d3e2f02334}` | `qwb_wp/all/Web5_ezcms.md` | SQLi → admin → PNG+JSP 上传 → SUID `easycms-restore` 命令注入 → root |
| 6 | Crack a Little Smile | 231 | ✗（502/链分析） | `qwb_wp/all/Web6_Crack a Little Smile.md` | Drupal 11.4.11 `unserialize` 无类白名单 → Drupal 原生 POP 链 → 文件写 webshell |
| 7 | fault_web_and_fault_hash | 133 | ✗ | `qwb_wp/all/Web7_fault_web_and_fault_hash.md` | 静态资源后缀绕 `/auth` → wellknown 配置源 → env 展开泄露凭据 → PTY → ARP 欺骗 runner → artifact cache |
| 8 | vaultlink | 1065 | ◐（平台补偿 `flag{see_you_revenge}`） | `qwb_wp/other/vaultlink_WP.md` | `/api/proxy` URL 解析差异绕 allow-list → ECI 元数据 user-data → Pod spec `ICQ_FLAG` |
| 9 | vaultlink_revenge | 150 | ✗ | `qwb_wp/all/Web9_vaultlink_revenge.md` | 见 WP（20KB，revenge 版新链） |

## Reverse（3）

| # | 题目 | 解出队数 | 我们的状态 | 本地 WP | 一句话考点 |
|---|---|---|---|---|---|
| 1 | ELFStudy | 1434 | — | `qwb_wp/all/Reverse1_ELFStudy.md` | 见 WP |
| 2 | firmware | 438 | ◐ 验证链通、差尾部解密 | `qwb_wp/all/Reverse2_firmware.md` | OTA/固件验证链 + `QWBPFLAG` 尾部 30 字节解密 |
| 3 | license | 473 | ✅ `flag{9530b81c-61d0-2b62-3e96-f9a5e937f893}` | `qwb_wp/all/Reverse3_license.md` | 白盒 AES/VM，线性反解 key，license 当 key 解 flag |

## Misc（6）

| # | 题目 | 解出队数 | 我们的状态 | 本地 WP | 一句话考点 |
|---|---|---|---|---|---|
| 1 | 宇宙微波背景辐射 | 801 | — | `qwb_wp/all/Misc1_宇宙微波背景辐射.md` | 见 WP |
| 2 | 0perator | 285 | ◐ dbus 分析 | `qwb_wp/all/Misc2_0perator.md` | dbus 非法 bus name 处理/`ReloadComponents` 可达性 |
| 3 | NeuronShuffle | 630 | — | `qwb_wp/all/Misc3_NeuronShuffle.md` | 见 WP |
| 4 | 谍影重重7 | 406 | ◐ 6 问中 4 问 | `qwb_wp/all/Misc4_谍影重重7.md` | DFIR/图像点击 PIN 判题 |
| 5 | Dreambound | 429 | ✗（843.683，阈值~1000） | `qwb_wp/other/Dreambound_WP.md` | 白盒世界模型；批量坐标下降 + 随机 kick 把隐状态推到 OOD，总分 1290 |
| 6 | 问卷调查 | 895 | — | `qwb_wp/all/Misc6_问卷调查.md`（stub） | 非技术题 |

## Crypto（6）

| # | 题目 | 解出队数 | 我们的状态 | 本地 WP | 一句话考点 |
|---|---|---|---|---|---|
| 1 | frozen | 874 | — | `qwb_wp/all/Crypto1_frozen.md` | 见 WP |
| 2 | vmshare | 899 | — | `qwb_wp/all/Crypto2_vmshare.md` | 见 WP |
| 3 | hoRRibleRing | 606 | — | `qwb_wp/all/Crypto3_hoRRibleRing.md` | 见 WP |
| 4 | zkRSA | 210 | — | `qwb_wp/all/Crypto4_zkRSA.md` | 见 WP |
| 5 | crp-12025 | 272 | ✗ | `qwb_wp/other/crp12025_WP.md` | `N` 的 1248=272+704+272 结构 + hint 高位；`m<q` 模 q 解密；AES 故障支线 |
| 6 | crp-11741 | 0 | — | `qwb_wp/all/Crypto6_crp-11741.md`（stub） | 无人解出 |

## 我们的战绩（有自证）

- Web-cwp：`flag{622e4b70-1203-4c03-a3f9-a07c713c177c}`（平台确认，100 分）
- Web-ezcms：`flag{9aaad8d7-0f1d-49b8-a122-62d3e2f02334}`（root 读 `/flag`）
- Rev-license：`flag{9530b81c-61d0-2b62-3e96-f9a5e937f893}`（license 自证）
- Web-vaultlink：平台补偿 `flag{see_you_revenge}`

其余题目的差距与教训见 [REFLECTION.md](REFLECTION.md)；可复用的赛时流程见 skill `ctf-recon-first`。
