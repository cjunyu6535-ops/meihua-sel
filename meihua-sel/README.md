# 🔮 梅花易數SEL版 v1.05 · 掐指一算成大師 (`meihua-sel`)

本專案為 **「梅花易數SEL版 v1.05 (Mei Hua Yi Shu x CASEL SEL Navigator)」** 跨平台 AI Agent 技能套件，源自 Google GEMs 提示詞架構並依據開放 Agent Skills (`SKILL.md`) 標準全面升級。結合中國傳統《梅花易數》預測數理（先天八卦、體用五行生剋、本卦／互卦／變卦推演）與西方 **CASEL 社會情緒學習（SEL）五大核心素養**，提供非宿命論、高賦能的深度決策諮詢。

本技能原生支援 **ChatGPT Codex (OpenAI Codex CLI)**、**Claude Code**、**OpenCode**、**Google Gemini CLI** 以及 **Google Gemini 網頁版／行動版（跨帳號匯入）**。

## 📂 專案與技能目錄結構

```text
meihua-sel/
├── SKILL.md                                  # 核心技能定義、跨平台執行規範與四階段互動狀態機
├── README.md                                 # 跨平台安裝指南（Codex / Claude Code / OpenCode / Gemini）與架構說明
├── references/
│   ├── prompt_spec_yaml.md                   # 【梅花易數SEL版 v1.05】完整 YAML 格式架構規範
│   ├── meihua_lookup_tables.md               # 跨裝置免代碼「三步查表計算矩陣」（8經卦爻變、64卦與互卦總表、5x5體用生剋）
│   └── sel_psychology_matrix.md              # 八經卦 × CASEL SEL 五大素養轉譯、認知偏差重構與動爻調節知識庫
└── scripts/
    └── meihua_calc.py                        # 選配輔助 Python 確定性排卦驗算引擎（純標準庫、零外部依賴）
```

## ✨ 核心功能與架構優化亮點

1. **跨平台開放標準 (`SKILL.md`) 相容**：移除特定平台鎖定的 Frontmatter 屬性，無論在終端機 Coding Agent（Claude Code、Codex、OpenCode、Gemini CLI）或雲端對話介面（Gemini Web/App）皆可無縫載入。
2. **跨裝置免代碼「三步查表計算矩陣」**：針對瀏覽器或雲端前端無法執行外部 Python 代碼之限制，於 `references/meihua_lookup_tables.md` 建立 **8 經卦動爻翻轉速查表**與 **8×8 六十四卦暨標準互卦全息總表**，徹底解決大語言模型心算二進制爻變與互卦時的幻覺問題。
3. **四階段互動式資料補齊狀態機**：開場主動宣導起卦三原則（「一事不二問」、「問題須明確」、「卦象僅供參考，決策由你合理判斷」），並自動檢查是否具備「具體問題背景」與「起卦數字／時間」，缺漏時主動引導補齊。
4. **雙軌深度推演與線上典故檢索**：結合傳統梅花易數體用生剋與 CASEL 五大素養（自我覺察、社會覺察、自我管理、關係技能、負責任的決策），並支援聯網檢索《周易》卦爻辭典故與現代心理學策略。

## 🚀 跨平台安裝與使用指南 (Multi-Platform Setup)

### 1. ChatGPT Codex (OpenAI Codex CLI / Codex Agent)

OpenAI Codex 支援從專案或全域的 `.agents/skills/` 與 `.codex/skills/` 目錄自動探索 `SKILL.md`：

* **方式 A：使用通用 `skills` CLI 一鍵安裝**
  ```bash
  npx skills add cjunyu6535-ops/meihua-sel --agent codex
  ```
* **方式 B：手動複製目錄安裝**
  ```bash
  # 全域安裝（所有專案皆可使用）
  mkdir -p ~/.agents/skills ~/.codex/skills
  cp -r meihua-sel ~/.agents/skills/meihua-sel

  # 或專案級安裝（僅在當前工作目錄生效）
  mkdir -p .agents/skills
  cp -r meihua-sel .agents/skills/meihua-sel
  ```
* **執行方式**：啟動 `codex` 後，可直接輸入 `$meihua-sel` 點名呼叫，或直接輸入：「請用梅花易數SEL版幫我起卦分析近期轉職決策，報數 3、5、9」。

### 2. Claude Code (Anthropic CLI / IDE Agent)

Claude Code 原生支援讀取 `~/.claude/skills/`（個人全域）與 `.claude/skills/`（專案級）下的技能套件：

* **方式 A：使用通用 `skills` CLI 一鍵安裝**
  ```bash
  npx skills add cjunyu6535-ops/meihua-sel --agent claude-code
  ```
* **方式 B：手動複製目錄安裝**
  ```bash
  # 全域安裝（推薦，所有地方皆可呼叫）
  mkdir -p ~/.claude/skills
  cp -r meihua-sel ~/.claude/skills/meihua-sel

  # 或專案級安裝
  mkdir -p .claude/skills
  cp -r meihua-sel .claude/skills/meihua-sel
  ```
* **執行方式**：在 Claude Code 中輸入斜線指令 `/meihua-sel`，或直接對 Claude 說：「呼叫掐指一算成大師，幫我算梅花易數」。

### 3. OpenCode (開源終端機 AI Agent)

OpenCode 原生支援 Agent Skills 標準，會自動掃描 `~/.config/opencode/skills/`、`.opencode/skills/`，同時相容讀取 `~/.claude/skills/` 與 `.agents/skills/`：

* **方式 A：使用通用 `skills` CLI 安裝**
  ```bash
  npx skills add cjunyu6535-ops/meihua-sel --agent opencode
  ```
* **方式 B：手動安裝至 OpenCode 全域技能目錄**
  ```bash
  mkdir -p ~/.config/opencode/skills
  cp -r meihua-sel ~/.config/opencode/skills/meihua-sel
  ```
* **執行方式**：啟動 `opencode` 後，可透過 `/meihua-sel` 載入技能，或直接在對話中提出起卦需求。

### 4. Google Gemini CLI (終端機 Agent)

Gemini CLI 支援原生 `gemini skills` 管理指令，並讀取 `~/.gemini/skills/`（全域）、`.gemini/skills/`（專案）及 `.agents/skills/`：

* **方式 A：使用通用 `skills` CLI 安裝**
  ```bash
  npx skills add cjunyu6535-ops/meihua-sel --agent gemini-cli
  ```
* **方式 B：手動複製至 Gemini CLI 技能目錄**
  ```bash
  # 全域安裝
  mkdir -p ~/.gemini/skills
  cp -r meihua-sel ~/.gemini/skills/meihua-sel

  # 驗證是否成功載入
  gemini skills list --all
  ```
* **執行方式**：在 `gemini` 互動視窗中輸入 `/skills list` 確認 `meihua-sel` 為啟用狀態，直接輸入起卦問題並在跳出授權提示時確認即可。

### 5. 其他 Google Gemini 帳號（Gemini 網頁版 / 行動版 App）

若要將此技能分享給其他 Google Gemini 帳號安裝使用，共有兩種方式：

* **方式 A：透過「Skills Manager（技能管理員）」UI 匯入（推薦）**
  1. 將本儲存庫下載或將 `meihua-sel/` 資料夾壓縮為 `meihua-sel.zip`（確保壓縮包內含 `SKILL.md`、`references/` 與 `scripts/`）。
  2. 登入目標 Gemini 帳號，打開左側選單的 **「技能管理員 (Skills Manager)」**。
  3. 點選 **「新增技能 / 上傳技能」**，上傳 `meihua-sel.zip`（或單獨上傳 `SKILL.md`）即可完成安裝。
* **方式 B：在對話視窗中請 Gemini 自動安裝**
  1. 在目標 Gemini 帳號開啟新對話，將 `meihua-sel/` 內的檔案（或打包好的 `meihua-sel.zip`）作為附件上傳。
  2. 輸入指令：`請幫我將附件中的梅花易數SEL版技能安裝並儲存為我的個人技能 meihua-sel`。
  3. Gemini 會自動呼叫內建技能建立工具完成驗證與儲存。
