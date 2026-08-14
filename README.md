# 机器人智能客服

这是一个基于 Streamlit + LangChain 的机器人智能客服项目，支持基于本地知识库的 RAG 检索问答、工具调用和报告场景提示词切换。入口页面位于 [app.py](app.py)，启动后会在浏览器中展示对话式客服界面。

## 主要功能

- 对话式智能客服界面，支持流式输出回答。
- 基于本地文档的 RAG 检索总结。
- 工具调用能力，包括天气、用户信息、外部数据读取等示例工具。
- 报告生成场景下的动态提示词切换。
- 本地 Chroma 向量库持久化，支持 txt / pdf 知识文件。

## 目录说明

- [app.py](app.py)：Streamlit 应用入口。
- [agent/](agent/)：Agent 组装、工具与中间件。
- [rag/](rag/)：向量库与 RAG 检索逻辑。
- [model/](model/)：模型工厂，封装聊天模型和向量模型。
- [config/](config/)：模型、向量库和提示词配置。
- [prompts/](prompts/)：系统提示词、RAG 提示词和报告提示词。
- [data/](data/)：知识库与外部数据源。
- [chroma_db/](chroma_db/)：本地向量库持久化目录。
- [logs/](logs/)：运行日志。

## 环境要求

- Python 3.10 或更高版本。
- 可访问 DashScope / 通义千问相关模型服务的账号与 API Key。

## 安装依赖

建议先创建虚拟环境，再安装依赖：

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 启动方式

安装完成后直接运行 Streamlit：

```bash
streamlit run app.py
```

首次启动时，项目会加载本地知识库并初始化向量存储。若知识文件较多，首次运行可能需要一些时间。

## 知识库与数据

- 知识文件默认读取 [data/](data/) 目录下的 `.txt` 和 `.pdf` 文件。
- 外部数据示例位于 [data/external/records.csv](data/external/records.csv)。
- 向量库持久化在 [chroma_db/](chroma_db/)，文件哈希记录在 [md5.text](md5.text)。

## 配置说明

- [config/agent.yml](config/agent.yml)：外部数据路径等 Agent 配置。
- [config/rag.yml](config/rag.yml)：模型名称配置。
- [config/chroma.yml](config/chroma.yml)：向量库参数与数据目录配置。
- [config/prompts.yml](config/prompts.yml)：提示词文件路径配置。

如需修改提示词，可直接编辑 [prompts/](prompts/) 下对应的文本文件。

## 常见问题

- 如果 PDF 加载失败，请确认已安装 `pypdf`。
- 如果文本文件出现编码报错，请确认文件使用 UTF-8 编码保存。
- 如果模型调用失败，请检查 DashScope 账号与 API Key 配置是否正确。
