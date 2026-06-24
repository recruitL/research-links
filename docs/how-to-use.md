# 使用方式

## 快速入口

- 总入口：[README.md](../README.md)
- EOB 方向：[topics/eob/README.md](../topics/eob/README.md)
- GSF 方向：[topics/gsf/README.md](../topics/gsf/README.md)
- 路线图：[roadmaps/](../roadmaps/)
- 模板：[templates/](../templates/)

## 推荐工作流

1. 先从 topic 首页理解问题、主线和已有资料。
2. 再看 roadmap，确认技术链条和先后顺序。
3. 查 CSV 数据层，筛选候选文献或代码库。
4. 对具体论文使用 `paper-note-template.md` 写阅读笔记。
5. 对代码库使用 `codebase-note-template.md` 记录安装、接口和可修改性。
6. 对任何 AI 总结或评分都补上人工校验状态。
7. 如果做过复现，记录到 `reproducibility/`，不要只写在临时笔记中。

## 更新规则

- 全量候选 CSV 只能 append、version 或显式说明覆盖原因。
- Markdown 只做解释和展示，不替代 CSV。
- 不确定的条目写 `TODO: verify`、`needs verification` 或 `not yet human-checked`。
- 新增方向时优先复制 `templates/topic-template.md` 的结构。
