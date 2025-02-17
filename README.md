# RAG-based QA System (Ollama)

## 簡介
本專案是一個基於 Retrieval-Augmented Generation (RAG) 的問答系統，使用 **LangChain** 和 **FAISS** 進行文本檢索，並透過 **Ollama** LLM 生成答案。使用者可以上傳 `.txt` 文件，系統會根據這些文件內容回答問題。

## 功能特點
- 🔍 **文本檔案檢索**：從 `data/` 資料夾讀取所有 `.txt` 文件。
- 📖 **向量化處理**：使用 FAISS 建立向量索引。
- 🤖 **語言模型回應**：使用 `Ollama` LLM 生成答案。
- 🎯 **流暢的 Streamlit 介面**：簡單直觀的 UI 讓使用者輸入問題並獲取回答。

---

## 安裝與使用
### 1️⃣ 安裝相依套件
請先確保 Python 3.8 以上已安裝，然後執行：
```bash
pip install streamlit langchain faiss-cpu ollama
```

### 2️⃣ 準備資料
請在專案目錄下建立 `data/` 資料夾，並放入 `.txt` 檔案。

### 3️⃣ 執行應用程式
```bash
streamlit run app.py
```

---

## 程式架構
```
📂 project-root/
│── 📂 data/               # 存放文本文件 (.txt)
│── rag
    │──📄 app.py             # Streamlit 應用主程式
│── 📄 README.md         # 使用說明文件
│── 📄 requirements.txt  # 依賴套件清單
```

### `app.py` 主要邏輯：
1. **讀取 `data/` 目錄下的所有 `.txt` 文件**
2. **將內容轉換為向量嵌入 (embeddings)**
3. **使用 FAISS 建立索引，作為檢索器 (retriever)**
4. **透過 Ollama LLM 進行問答生成**
5. **使用 Streamlit 建立簡單的 UI 介面**

---

## 主要技術
- **[LangChain](https://python.langchain.com/)**：提供檔案載入、語言模型調用、檢索等功能。
- **[FAISS](https://faiss.ai/)**：高效向量檢索庫，用於查找最相關的文檔。
- **[Ollama](https://ollama.com/)**：用於執行 LLM（如 Mistral、DeepSeek）生成回答。
- **[Streamlit](https://streamlit.io/)**：建立互動式網頁應用。

---

## 參數設定
| 參數名稱          |  預設值               |  描述 |
|------------------|-------------------|-------------------------------|
| `folder_path`   | `data/`           | 存放 `.txt` 文件的資料夾 |
| `model_name`    | `mistral`         | 用於生成詞嵌入的模型 |
| `llm_model`     | `deepseek-r1:7b`  | 問答系統使用的 LLM |

---

## 未來改進方向
- ✅ 支援更多文件格式（如 `.pdf`, `.csv`）
- ✅ 增強 UI 體驗，例如即時回應建議
- ✅ 允許動態選擇 LLM 模型


