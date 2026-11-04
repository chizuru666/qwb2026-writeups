# QWB 2026 赛后复盘：为什么没做出来

时间：2026-11-04
数据源：`~\.dsh\sessions\--D-COMPETITIOM-QWB--\*`（96 个会话）+ 项目内 SOLUTION/FINDINGS + 官方 WP 仓 `ThanatosXingYu/qwb2026s10_writeups`。
一句话结论：**大多数题不是“不会”，而是赛时没做“精确版本 + 公开 N-day/上游源码”的情报侦察，也没把已有的现成工具/exp 跑起来。**

## 逐题

### Babyv8（V8 sandbox pwn，282 队解出）— 未解
- 我们：逆向 8 个 patch，定位 0006 loop-phi 与 0007 cached_entrypoint；复现 addrof、UAF、服务端假 JSArray（len=2）；卡在 elements 指针/堆布局，容器短命。
- WP：`put()` 触发器 + `String(SMI array)` 还原压缩指针 + `moveOnce` 观测 GC + double 数组按 4/8 相位重占位伪 JSArray + `fake[1]` 改 `victim.elements` 任意读写 + FeedbackCell `cached_entrypoint` 泄露 PIE + ROP `execvp("/readflag")`。
- 差异：我们用自造的 `+k` 混淆做 addrof，WP 用 `String()` 直接读 SMI 槽位；我们执着自己标定 backing elements，WP 用“悬空地址 + 固定 double spray 重占位”；我们不知道 GitHub 上有现成 exp。
- 教训：**V8 题先搜 `题目名 + 赛事 + writeup`；`String(SMI array)` 是标准 addrof 技巧；先找现成链再调偏移。**

### CanonicoPWN（Ubuntu 内核 LPE，264 队解出）— 未解
- 我们：枚举加固、排除 Copy Fail / Dirty Frag / Fraggap、试图找自定义驱动；结论“无公开 CVE”。
- WP：环境 = Ubuntu 26.04 `7.0.0-39.39`，考点就是 **CVE-2026-98260**（公开 PoC 完整）；从官方 deb + `vmlinux-to-elf` 还原符号/BTF；POSIX CPU timer UAF → timerqueue 悬空节点 → `rb_erase` 覆盖 `task->cred`。
- 差异：**没有按“精确内核版本 + CVE/PoC”搜索**，只按“通用子系统”找。
- 教训：内核题第一步是锁定 `uname -r`/构建串，搜该版本近 3 个月的公开 LPE。

### Dreambound（白盒世界模型，429 队解出）— 未解
- 我们：拿到 843.683，未过阈值。
- WP：48×5 离散空间做**批量坐标下降**（每轮枚举 192 条），局部最优后“随机踢两个位置”再下降；全 4=170.5，最优 1290.26（单步 564），阈值大概率 1000。
- 差异：我们的优化没有“全扫描 + kick”，停在局部最优；也没意识到阈值在 1000 量级。
- 教训：可微模型不等于适合梯度；离散、窄峰、评估便宜 → 坐标下降 + 重启/kick。

### Blackout（工控两段式，167 队解出）— 未解
- 我们：卡在“第一段 shell 前提”，放弃。
- WP：第一段拿装置侧 `ied` shell；第二段用 `mlclient.conf` 打主站 `server_sg5000`，以 `oper` 读 `/flag` 并写回文件区，再用 MMS `FileRead` 取回。
- 教训：题面“只拿到第一个 shell 好像还不够”就是明示；**不要在第一段停**。

### babyark（ArkTS 字节码，399 队解出）— 未解
- 我们：按引擎/JIT 方向找 bug，卡在 heap 泄露。
- WP：运行时 `--asm-interpreter`，漏洞是 abc 的 `ldlexvar/stlexvar` **无边界校验**（wide slot 65535，约 512KB OOB）；用 `es2abc` 编模板替换探针闭包；伪造 `JSNativePointer`（`externalPointer@+8`）→ 任意地址；ROP `system()`。
- 教训：**先读解释器 opcode 的校验实现**，再考虑 JIT bug；手写/改字节码是这类题的主线。

### babystar / bad_puppet / shadowledger / babel / ez_qemu — 未解或仅本地
- babystar：cFS 三张可上传表（`HK.CopyTable`/`HS.MsgActs_Tbl`/`HS.AppMon_Tbl`）被当可信配置执行：HK 把地面字节搬进遥测包模板，HS 把“发送该 MID”登记成自动动作，AMT 触发 → CF class 1 读 `/cf/host/flag`（CFDP `F` 帧、目的 EID 25）。我们只在 CFDP/文件读方向摸索，没串起“表数据=可执行指令”。
- babystar 实例 12–15 分钟即回收；我们没在单次实例内完成整链。
- babel：本地 10/10，远程没打（没现成 exp / 没花时间）。
- 共同教训：**本地打通后必须立刻转到远程**；实例寿命短，先准备好一键 exp。

### Web-vaultlink（1065 队解出）— 未解
- 正解：`/api/proxy?url=http://<allowlist>%5C@127.0.0.1:31337/...`，用 URL 解析差异（`userinfo@host` + 反斜杠）绕过 allow-list；随后打**阿里云 ECI 元数据** `100.100.100.200/latest/user-data` → base64 → gunzip → Pod spec 的 `ICQ_FLAG`。
- 我们：抓到 Upgrade 头绕过与 relay/WebSocket（AUTH 被 guest 限制），但没有先试云元数据；最终平台补偿 `flag{see_you_revenge}`。
- 教训：代理/allowlist 题**先测云元数据 + 解析差异**；relay 协议只是干扰项。

### crp / crp-12025 / firmware / license / cls / fault / BlindReview / 0perator / 谍影7
- license：已解（`flag{9530b81c-...}`）。
- crp：bitstream 解到 14% 未文档化 bit，差最后一格标定；crp-12025 的 `gylike{...}` 是 hint 不是 flag。
- crp-12025 正解：1248-bit `N` 有特殊结构 + `hint.txt` 给因子高位；`m < q`，按 `q` 模解密 `TARGET_CT` 即得 42 字节明文，再用 `m^e mod N` 回验；AES 故障支线（故障 S 盒 + 2500 次查询）不是必经路径。
- firmware：验证链全通，差 OTA 尾部 30 字节解密。
- cls/fault/BlindReview/0perator/谍影7：分析到一半，缺“最后一击”的耐心/工具。
- 教训：赛后用 WP 对照时才发现，赛时应当先按“精确组件/版本”查公开资料与上游实现，确认“最后一击”是什么，再决定投入。

## 流程级问题

1. **赛时没有固定侦察流程**：没有先锁定精确版本/组件去搜公开 N-day/CVE/PoC（CanonicoPWN 因此误判“无公开 CVE”），也没有先读上游源码/协议；赛后才发现 WP 里的关键信息本来就是赛时公开可查的。赛时搜“本题 WP”本身不成立，错的是缺了“版本/CVE/上游”这层侦察。
2. **没有按精确版本搜 CVE**（CanonicoPWN）。
3. **工具不齐**：pwntools 未装（现成 exp 跑不了）、zstandard 未装（会话归档读不了）、CDP 选错 page target、容器 TTL 管理混乱。
4. **本地→远程断层**：多题本地打通却没在实例存活期内完成远程验证。
5. **优化题方法单一**：Dreambound 没上“坐标下降 + kick”。

## 已补的工具/资料

- 新 skill：`~/.dsh/skills/ctf-recon-first/`（SKILL.md + `references/v8-pwn.md` + `references/tooling.md` + 3 个脚本）。
- 资料：`D:\COMPETITIOM\QWB\_archive\`（96 会话 digest、flags、SOLUTION 摘录、`qwb_wp/` 官方 WP 与 exp）。
- 环境：zstandard 已装；pwntools 正在装（PyPI 慢，装完 `python -c "import pwn"` 自检）。

## 低级错误清单（下次直接对照，不犯）

1. **停在第一段**：Blackout 拿到装置侧 `ied` shell 就停；题面“只拿到第一个 shell 好像还不够”已明示还有第二段（`mlclient.conf` → 主站 `server_sg5000` → `oper` → `/flag`）。**任何第一个 shell/RCE 之后，先写“最终目标/下一跳/判定完成”，再动手。**
2. **把本地占位当 flag**：`flag{local_test_ez_qemu}`、`gylike{...}` hint、vaultlink 首页注释的 staging flag 都不是提交值；平台 toast/目标文件读出才算。
3. **第一个原语就满足**：babyark 只到地址泄露/局部读写，没升级到伪造 `JSNativePointer` → ROP；V8 只到 addrof/假数组，没到 RW → 控制流。
4. **不按精确版本搜 CVE**：CanonicoPWN 的“没有附件”就是提示——环境即附件，先 `uname` 锁 `7.0.0-39.39` 再搜公开 N-day。
5. **忘记题面数字/结构提示**：crp-12025 的 `1248=272+704+272` 直接给模数结构，不用硬分解。
6. **本地通不转远程**：容器寿命短（12–20 分钟），本地 10/10 后必须立刻一键打远程。
7. **CDP 选错页面 / 把显示 TTL 当真实寿命**：按 URL 选 target；拿到地址立刻打。

## 下次的“前 30 分钟”

1. 读题 → 记下**精确版本/构建串/服务形态/附件**。
2. **赛时情报**（不是搜本题 WP）：按精确版本搜公开 CVE/N-day/PoC；读上游源码/文档/协议规范；确认是否回收题（同名/同附件 hash）。10 分钟。
3. 检查工具（pwntools/zstandard/CDP/服务 runner）。
4. 本地复现 → **立刻**远程打（容器寿命短）。
5. 卡住 30 分钟 → 换维度（版本/组件/协议/同类题型），不是去搜本题 WP。
6. **赛后**：读公开 WP、写差异、把可复用模式沉淀进 `ctf-recon-first` skill。
