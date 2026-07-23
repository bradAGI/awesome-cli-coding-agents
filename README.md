# Awesome CLI Coding Agents

<p align="center">
  <img src="banner.png" alt="Awesome CLI Coding Agents" width="100%" />
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="https://github.com/bradAGI/awesome-cli-coding-agents/stargazers"><img src="https://img.shields.io/github/stars/bradAGI/awesome-cli-coding-agents?style=social" alt="Stars"></a>
  <a href="#contributing"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <a href="https://github.com/bradAGI/awesome-cli-coding-agents/blob/main/LICENSE"><img src="https://img.shields.io/github/license/bradAGI/awesome-cli-coding-agents" alt="License"></a>
</p>

A curated list of **90+ CLI coding agents** — AI-powered tools that live in your terminal, read/edit repos, and run commands — plus the **harnesses** that orchestrate, sandbox, or extend them.

> **Last updated:** 2026-07-20

### What is a CLI coding agent?

A CLI coding agent is an AI-powered tool that runs in your terminal and can autonomously read, write, and execute code in your repository. Unlike chat-based assistants, these agents have direct access to your filesystem, shell, and dev tools — they can edit files, run tests, commit changes, and iterate on errors. Think of them as AI pair programmers that live where you already work: the command line.

---

## Contents

- [Terminal-native coding agents](#terminal-native-coding-agents)
  - [Open Source](#open-source)
  - [OpenClaw ecosystem](#openclaw-ecosystem)
  - [Closed Source](#closed-source)

- [Harnesses & orchestration](#harnesses--orchestration)
  - [Session managers & parallel runners](#session-managers--parallel-runners)
  - [Orchestrators & autonomous loops](#orchestrators--autonomous-loops)
  - [Agent infrastructure](#agent-infrastructure)

- [Contributing](#contributing)

---

## Terminal-native coding agents

### Open Source

Forkable, extensible, and community-driven. Sorted by GitHub stars. Provider tags `[Company]` indicate the backing organization.

- **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** `⭐ 218k` — Nous Research's self-improving CLI agent with persistent memory, automated skill creation, sandboxed code execution via Unix socket RPC, and multi-platform reach (Telegram/Slack/Discord/WhatsApp); supports 300+ models across multiple providers.

- **[Claw Code](https://github.com/ultraworkers/claw-code)** `⭐ 195k` — Clean-room Python/Rust rewrite of Claude Code architecture using oh-my-codex; fastest repo in GitHub history to 100K stars. Born from the March 2026 Claude Code source leak. MIT.

- **[OpenCode](https://github.com/anomalyco/opencode)** `⭐ 188k` — Terminal-native coding agent with 75+ provider support, LSP integration, and privacy-first design (formerly opencode-ai; now at opencode.ai).

- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** `⭐ 106k` `[Google]` — Google's terminal agent powered by Gemini, with tools for repo work and research. Apache-2.0.

- **[Codex CLI](https://github.com/openai/codex)** `⭐ 99.9k` `[OpenAI]` — OpenAI's local coding agent for reading/editing/running code, with an interactive TUI and tool execution. Apache-2.0.

- **[OpenHands](https://github.com/All-Hands-AI/OpenHands)** `⭐ 81.4k` — Open-source agentic developer environment (formerly OpenDevin) with CLI and web entrypoints; also has a lightweight [CLI-only package](https://github.com/OpenHands/OpenHands-CLI).

- **[Pi](https://github.com/badlogic/pi-mono)** `⭐ 73.1k` — Minimal, adaptable terminal coding harness from the pi-mono toolkit; unified LLM API, TUI, skills, and MCP support.

- **[Open Interpreter](https://github.com/OpenInterpreter/open-interpreter)** `⭐ 66.9k` — Terminal tool that can execute code and actions; often used as a "do things on my machine" agent.

- **[Cline CLI](https://github.com/cline/cline)** `⭐ 64.8k` — Model-agnostic autonomous agent for planning, file edits, command execution, and browser use.

- **[Goose](https://github.com/aaif-goose/goose)** `⭐ 51.3k` — Local, extensible agent that can execute, edit, and test; designed to run on-device and integrate with MCP.

- **[Aider](https://github.com/Aider-AI/aider)** `⭐ 47.5k` — Pair-programming agent for editing files via diffs/patches, with strong git and multi-file workflows.

- **[Continue CLI](https://github.com/continuedev/continue)** `⭐ 35k` — Open-source terminal extension for multi-model coding with local/privacy focus.

- **[Crush](https://github.com/charmbracelet/crush)** `⭐ 26.7k` — Charmbracelet's glamorous agentic coding TUI in Go; multi-provider, LSP-aware, with rich terminal UI.

- **[Deep Agents Code](https://github.com/langchain-ai/deepagents)** `⭐ 26.6k` `[LangChain]` — LangChain's official terminal coding agent built on the Deep Agents SDK; interactive TUI, file ops, shell access, subagents, headless mode, and human-in-the-loop approvals with any tool-calling LLM. PyPI `deepagents-code`.

- **[Kilo Code CLI](https://github.com/Kilo-Org/kilocode)** `⭐ 26.4k` — Agentic engineering platform with CLI; orchestrator mode, 100s of LLMs, skills, and checkpointing.

- **[Qwen Code](https://github.com/QwenLM/qwen-code)** `⭐ 26.1k` `[Alibaba]` — Alibaba Qwen's official CLI agent for Qwen coder models (workflow tool + repo operations). Apache-2.0.

- **[Roo Code CLI](https://github.com/RooCodeInc/Roo-Code)** `⭐ 24.4k` — Multi-mode CLI agent (architect/code/debug/orchestrator modes); Claude-like terminal interface with skills and checkpoints.

- **[SWE-agent](https://github.com/SWE-agent/SWE-agent)** `⭐ 19.9k` — Agent for resolving real repo issues/PR tasks; frequently used in SWE-bench-style workflows.

- **[OH-MY-PI](https://github.com/can1357/oh-my-pi)** `⭐ 18.6k` — Terminal coding agent ("Pi") with a TypeScript/Rust monorepo and local-first ergonomics.

- **[Plandex](https://github.com/plandex-ai/plandex)** `⭐ 15.5k` — "Plan-first" CLI agent for building features across multiple files with structured steps and 2M token context.

- **[MiMo Code](https://github.com/XiaomiMiMo/MiMo-Code)** `⭐ 12.2k` `[Xiaomi]` — Xiaomi's official terminal coding agent; TUI + non-interactive modes, MCP, skills, hooks, git worktrees, and resumable sessions. Runs MiMo-V2.5-Pro or any mainstream provider; npm `@xiaomi-mimo/cli`. MIT.

- **[Smol Developer](https://github.com/smol-ai/developer)** `⭐ 12.2k` — Embeddable developer agent that generates entire codebases from a prompt; designed to be embedded in apps.

- **[Trae Agent](https://github.com/bytedance/trae-agent)** `⭐ 11.9k` `[ByteDance]` — ByteDance's research-friendly CLI agent for software engineering tasks, with modular architecture and multi-LLM support. MIT.

- **[Claude Engineer](https://github.com/Doriandarko/claude-engineer)** `⭐ 11.2k` — Community-driven CLI for agentic Claude workflows with file management and iterative development.

- **[Claurst](https://github.com/Kuberwastaken/claurst)** `⭐ 10.1k` — Claude Code rewritten in idiomatic Rust with architectural breakdown; includes discoveries from the source leak (KAIROS persistent assistant, buddy system). MIT.

- **[Kimi CLI](https://github.com/MoonshotAI/kimi-cli)** `⭐ 10.1k` `[Moonshot AI]` — Moonshot AI's CLI coding agent with skills, MCP support, and ACP IDE integration. Apache-2.0.

- **[Free Code](https://github.com/paoloanzn/free-code)** `⭐ 8.6k` — Fork of Claude Code with all telemetry removed, guardrails stripped, and all experimental features enabled (KAIROS, dream mode, companion system).

- **[Codebuff](https://github.com/CodebuffAI/codebuff)** `⭐ 7.8k` — Multi-agent AI coding assistant with CLI support for collaborative coding workflows.

- **[ForgeCode](https://github.com/antinomyhq/forge)** `⭐ 7.5k` — AI pair programmer supporting 300+ models, with task management, custom agents, and large-scale refactor tooling.

- **[OpenSquilla](https://github.com/opensquilla/opensquilla)** `⭐ 6.2k` — Self-hostable microkernel agent runtime with a full CLI (`opensquilla chat` REPL, one-shot agent mode, gateway); autonomous file edits, shell and background processes, git tools, ML-based tier routing, sandboxing (Bubblewrap/Seatbelt), persistent memory, and 20+ providers. Apache-2.0.

- **[Kode CLI](https://github.com/shareAI-lab/Kode-cli)** `⭐ 5.2k` — ShareAI's open-source CLI agent for terminal-native coding with multi-provider support.

- **[Mistral Vibe](https://github.com/mistralai/mistral-vibe)** `⭐ 4.7k` `[Mistral]` — Mistral's CLI coding assistant for conversational repo interaction and edits. Apache-2.0.

- **[gptme](https://github.com/gptme/gptme)** `⭐ 4.4k` — AI agent in your terminal with support for persistent autonomous agents. Runs code, edits files, browses the web. Build long-lived self-modifying agents with git-backed memory via [gptme-agent-template](https://github.com/gptme/gptme-agent-template).

- **[Every Code](https://github.com/just-every/code)** `⭐ 3.8k` — Fork of Codex CLI with validation, automation, browser integration, multi-agents, theming, and multi-provider orchestration (OpenAI, Claude, Gemini). Apache-2.0.

- **[Devon](https://github.com/entropy-research/Devon)** `⭐ 3.5k` — Open-source pair programmer with a TUI; autonomous planning, execution, and debugging in Git workflows.

- **[Grok CLI](https://github.com/superagent-ai/grok-cli)** `⭐ 3.3k` — Community CLI agent built on xAI's Grok models for terminal-based coding tasks.

- **[AutoCodeRover](https://github.com/AutoCodeRoverSG/auto-code-rover)** `⭐ 3.1k` — Autonomous program improvement agent; patches real GitHub issues using code search and analysis.

- **[Letta Code](https://github.com/letta-ai/letta-code)** `⭐ 2.9k` — Memory-first CLI coding agent built on the Letta platform (formerly MemGPT); persistent memory across sessions, model-agnostic (Claude/GPT/Gemini), skill learning, and context repositories.

- **[CodeMachine-CLI](https://github.com/moazbuilds/CodeMachine-CLI)** `⭐ 2.5k` — Community multi-agent CLI aimed at running coding workflows locally (vibe-coding oriented).

- **[Codel](https://github.com/semanser/codel)** `⭐ 2.5k` — Autonomous agent for performing complex tasks via terminal; runs in Docker with a web UI.

- **[open-codex](https://github.com/ymichael/open-codex)** `⭐ 2.2k` — Lightweight fork of Codex CLI with multi-provider support (OpenAI, Gemini, OpenRouter, Ollama).

- **[RA.Aid](https://github.com/ai-christianson/RA.Aid)** `⭐ 2.2k` — Autonomous coding agent built on LangGraph with research/plan/implement pipeline; optional aider integration for near-full autonomy.

- **[Nanocoder](https://github.com/Nano-Collective/nanocoder)** `⭐ 2.2k` — Local-first CLI coding agent built by a community collective; bring your own model (Ollama, OpenRouter, or any OpenAI-compatible API), native tool calling with XML fallback, MCP support, and file-based custom commands and tools. MIT.

- **[Agentless](https://github.com/OpenAutoCoder/Agentless)** `⭐ 2.1k` — Lightweight approach to autonomous software engineering without persistent agent loops.

- **[Amazon Q Developer CLI](https://github.com/aws/amazon-q-developer-cli)** `⭐ 2k` `[AWS]` — AWS's agentic terminal chat for building apps, debugging, and DevOps with natural language. Apache-2.0.

- **[Neovate Code](https://github.com/neovateai/neovate-code)** `⭐ 1.6k` `[Ant Group]` — Ant Group's CLI agent with plugin system, multi-model/multi-provider support, MCP integrations, and headless automation mode. MIT.

- **[VT Code](https://github.com/vinhnx/vtcode)** `⭐ 757` — Open-source coding agent with LLM-native code understanding and robust shell safety. Supports multiple LLM providers with automatic failover and efficient context management. MIT.

- **[Groq Code CLI](https://github.com/build-with-groq/groq-code-cli)** `⭐ 739` — Customizable, lightweight CLI powered by Groq's ultra-fast inference; extensible tools/commands with multi-model support.

- **[Dexto](https://github.com/truffle-ai/dexto)** `⭐ 639` — Coding agent and general agent harness with CLI/web/API modes; ships a production-ready coding agent with sub-agent spawning.

- **[claw-code-agent](https://github.com/HarnessLab/claw-code-agent)** `⭐ 532` — Python-only Claude Code rewrite with zero external dependencies; born from the March 2026 Claude Code source leak, positioned as easier to hack on than the Rust/TypeScript reimplementations.

- **[g3](https://github.com/dhanji/g3)** `⭐ 515` — "Coding AI agent" in Rust: tool-running, repo interaction, skills system, and provider abstraction.

- **[Coro Code](https://github.com/Blushyes/coro-code)** `⭐ 366` — Open-source CLI coding agent, a free alternative to Claude Code; generate, debug, and manage code seamlessly.

- **[LettaBot](https://github.com/letta-ai/lettabot)** `⭐ 327` — Personal AI assistant with persistent unified memory across Telegram, Slack, Discord, WhatsApp, and Signal; built on the Letta platform.

- **[Mini-Kode](https://github.com/minmaxflow/mini-kode)** `⭐ 304` — An educational AI coding agent CLI, intended as a readable reference implementation.

- **[zot](https://github.com/patriceckhart/zot)** `⭐ 295` — Zero-overhead and lightweight coding agent harness with TUI/JSON/RPC modes, structured tools, reviewable file diffs, skills, extensions, and optional guardrails.

- **[nori-cli](https://github.com/tilework-tech/nori-cli)** `⭐ 159` — Multi-provider CLI built on Codex CLI; switch between Claude, Gemini, and Codex from the same native terminal.

- **[cursor-agent](https://github.com/civai-technologies/cursor-agent)** `⭐ 126` — Python-based agent replicating Cursor's coding assistant capabilities; supports Claude, OpenAI, and local Ollama models.

- **[VibePod](https://github.com/VibePod/vibepod-cli)** `⭐ 97` — Unified CLI for running AI coding agents in isolated Docker containers; zero-config setup, local metrics, HTTP traffic tracking, and an analytics dashboard for side-by-side comparison.

- **[openHarness](https://github.com/zhijiewong/openharness)** `⭐ 96` — Open-source Claude Code alternative. 78 slash commands, 42 tools, MCP (stdio/HTTP/SSE + OAuth 2.1), hooks, subagents, plan mode. Works with Anthropic/OpenAI/Ollama/llama.cpp/LM Studio. Ships both npm and Python SDK. MIT.

- **[DvalinCode](https://github.com/arthurpanhku/dvalincode)** `⭐ 92` — Provider-neutral, local-first coding agent (Chat/Cowork/Code modes) built for governance: an org policy engine, enforced network egress (per-request checks plus OS-sandboxed subprocesses via `sandbox-exec`/Bubblewrap), and a tamper-evident, hash-chained audit trail. Inline diff approval, durable session journal, built-in Web GUI from a single binary; works with any OpenAI-compatible endpoint (DeepSeek, OpenAI, Claude via OpenRouter, Groq, Ollama). Zero runtime deps. MIT.

- **[Codex Infinity](https://github.com/lee101/codex-infinity)** `⭐ 87` — Autonomous terminal coding agent (OpenAI Codex CLI fork) adding auto-continuation, parallel multi-agent runs, and CI repair loops.

- **[Octomind](https://github.com/Muvon/octomind)** `⭐ 87` — Open-source, model-agnostic AI agent runtime with community tap registry (`developer:rust`, `doctor:blood`, `legal:contracts`), MCP support with runtime self-extension, 13+ providers, and adaptive compression. Written in Rust. Apache-2.0.

- **[Crab Code](https://github.com/lingcoder/crab-code)** `⭐ 74` — Rust-native agentic coding CLI aligned with Claude Code's toolset and permission model; works with any LLM provider (Anthropic/OpenAI/DeepSeek/Bedrock/Vertex). 27 crates, 4,700+ tests, layered config system. Apache-2.0.

- **[San](https://github.com/genai-io/san)** `⭐ 70` — Go terminal-native runtime for specialized AI agents; provider-agnostic (Anthropic, OpenAI, Google, DeepSeek, Moonshot, Qwen, MiniMax, GLM), runs Claude Code skills/plugins/MCP unmodified, swappable search backends, custom personas, sandboxed subagents, lifecycle hooks, and a self-evolving memory loop. Single ~12 MB binary, zero runtime deps. Apache-2.0.

- **[picocode](https://github.com/jondot/picocode)** `⭐ 57` — Minimal Rust-based coding agent focused on CI workflows and small codemods; multi-LLM with personas.

- **[QQCode](https://github.com/qnguyen3/qqcode)** `⭐ 51` — Lightweight CLI coding agent in Rust focused on speed, determinism, and developer control; supports skills.

- **[Keen Code](https://github.com/mochow13/keen-code)** `⭐ 49` — Go-based CLI coding agent focused on efficient context management — uses lean TurnMemory summaries instead of raw tool traces to maximize context efficiency. 9+ providers, skill-driven MCP servers, and full transparency with every prompt, design doc, and implementation plan saved as markdown. MIT.

- **[Waveloom](https://github.com/Menfre01/waveloom)** `⭐ 43` — Go terminal-native coding agent with Bubble Tea TUI; DeepSeek V4 prompt caching for long-context efficiency; Claude Code-compatible UX with skill/MCP auto-discovery; four-tier context compaction, three subagent modes (Fork/Cold/Explore), permission engine, and plan mode. Single ~19 MB binary, zero runtime deps. Apache-2.0.

- **[Smelt](https://github.com/leonardcser/smelt)** `⭐ 34` — Rust TUI coding agent; multi-provider (Anthropic, OpenAI, Ollama, GitHub Copilot, any OpenAI-compatible endpoint), four modes (Normal/Plan/Apply/Yolo), granular permission system, parallel subagents, vim keybindings, and headless scriptable mode. MIT.

- **[Zap](https://github.com/zap-coding-agent/zap-coding-agent)** `⭐ 24` — Skill-first Rust TUI coding agent that injects only the context your task needs — no system prompt bloat. Single binary, no runtime. Supports Claude, Gemini, OpenAI, and local models via LM Studio; code-indexed via SQLite for fast symbol lookup; MCP support. MIT.

- **[Grinta](https://github.com/josephsenior/Grinta-Coding-Agent)** `⭐ 22` — Local-first, provider-agnostic terminal coding agent built for long-horizon autonomous execution; durable state and recovery, context management, structured tool orchestration, LSP/DAP integration, and validation-gated completion. Python, MIT.

- **[Binharic](https://github.com/CogitatorTech/binharic-cli)** `⭐ 17` — A multi-provider "tech-priest persona" coding agent CLI (stylized, tool-using).

- **[Darce](https://github.com/AmerSarhan/darce-cli)** `⭐ 7` — Ultralight (14 kB) multi-model CLI agent built with Ink; 7 tools, smart model routing across providers, streaming, session resume, and slash commands. MIT.

- **[CLAII](https://github.com/agencyswarm/CLAII)** `⭐ 3` — CLI-first AI coding agent with multi-agent orchestration, MCP toolchains, and memory-persistent refactors.

### OpenClaw ecosystem

Projects built on, forked from, or inspired by [OpenClaw](https://github.com/openclaw/openclaw) — the open-source personal AI assistant. Sorted by GitHub stars.

- **[OpenClaw](https://github.com/openclaw/openclaw)** `⭐ 384k` — The original personal AI assistant you run locally; CLI with onboarding wizard, skills, tools, and multi-channel support (WhatsApp/Slack/Discord). MIT.

- **[nanobot](https://github.com/HKUDS/nanobot)** `⭐ 45.9k` — Ultra-lightweight ~4,000-line Python rewrite of OpenClaw; tool use, persistent memory, scheduled tasks, and multi-channel support (Telegram/Discord/WhatsApp). MIT.

- **[ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)** `⭐ 32.3k` — Fully autonomous AI agent runtime in Rust; trait-driven pluggable architecture (providers, tools, memory, channels), runs on minimal hardware (<5MB RAM), multi-channel CLI/Telegram/Discord/Slack, with sandboxed execution and hybrid vector+keyword search.

- **[NanoClaw](https://github.com/gavrielc/nanoclaw)** `⭐ 30.3k` — Security-first lightweight alternative to OpenClaw; runs agents in Apple containers/Docker with sandboxed execution, built on Anthropic's Agents SDK.

- **[PicoClaw](https://github.com/sipeed/picoclaw)** `⭐ 29.7k` — Ultra-lightweight personal AI assistant in Go inspired by OpenClaw; runs on $10 hardware with less than 10MB RAM.

- **[IronClaw](https://github.com/nearai/ironclaw)** `⭐ 12.5k` — OpenClaw rewritten in Rust by NEAR AI; WASM sandbox isolation, capability-based permissions, and prompt injection defense.

- **[NullClaw](https://github.com/nullclaw/nullclaw)** `⭐ 7.8k` — Fastest, smallest OpenClaw-compatible agent in Zig; 678KB static binary, ~1MB RAM, <2ms startup, 23+ providers, 18 channels. MIT.

- **[Clawith](https://github.com/dataelement/Clawith)** `⭐ 4.1k` — "OpenClaw for Teams" — multi-agent collaboration platform that scales OpenClaw to organizations. Apache-2.0.

- **[claw0](https://github.com/shareAI-lab/claw0)** `⭐ 3.2k` — 0-to-1 tutorial companion for the OpenClaw ecosystem; walks through building an agent harness from scratch, covering planning, context compression, and task persistence.

- **[Moltis](https://github.com/moltis-org/moltis)** `⭐ 2.8k` — Secure, auditable Rust-native alternative to OpenClaw; zero unsafe code, 2,300+ tests, built-in voice I/O, MCP servers, and multi-channel access. MIT.

- **[GitClaw](https://github.com/open-gitagent/gitclaw)** `⭐ 612` — Git-native AI agent framework where agent identity, rules, memory, tools, and skills are all version-controlled files. MIT.

- **[LionClaw](https://github.com/moshthepitt/lionclaw)** `⭐ 13` — Secure-first local AI CLI with a small auditable kernel, durable sessions, and installable skills. MIT.

### Closed Source

Proprietary agents — usable but not forkable or extensible at the source level.

- **[Claude Code](https://github.com/anthropics/claude-code)** `⭐ 138k` `[Anthropic]` — Anthropic's repo-aware terminal agent for code edits, refactors, and git workflows. Source-available, no OSS license.

- **[Warp](https://github.com/warpdotdev/Warp)** `⭐ 63.4k` `[Warp]` — Modern terminal with built-in AI agent mode; understands tasks, runs commands, edits files, and orchestrates multi-step workflows.

- **[GitHub Copilot in the CLI](https://github.com/github/copilot-cli)** `⭐ 11k` `[GitHub]` — GitHub's agentic CLI for repo/PR/issue workflows, command suggestions, and headless automation.

- **[Command Code](https://github.com/CommandCodeAI/command-code)** `⭐ 3.5k` `[CommandCode]` — CLI coding agent that continuously learns your coding style via taste-1 neuro-symbolic AI; adapts to preferences over time with project-specific taste profiles.

- **[Droid](https://github.com/Factory-AI/factory)** `⭐ 1k` `[Factory]` — Factory's multi-model CLI coding agent; #1 on Terminal-Bench, specialized droids for different tasks, headless CI mode, and multi-interface support (CLI/IDE/Slack/Linear).

- **[Ante](https://github.com/AntigmaLabs/ante-preview)** `⭐ 575` `[Antigma Labs]` — Single ~15 MB Rust binary terminal coding agent (research preview) with client–daemon architecture, interactive TUI + headless CLI, offline GGUF inference via embedded llama.cpp, and 12+ providers; strong verified Terminal-Bench 2.1 results. Core agent ships as a prebuilt binary.

- **[pool](https://github.com/poolsideai/pool)** `⭐ 310` `[Poolside]` — Poolside's terminal coding agent backed by its Laguna models; interactive TUI, headless `pool exec`, ACP client/server for Zed/JetBrains/Xcode, AGENTS.md, skills, and MCP. Binary distribution under a proprietary EULA.

- **[FetchCoder](https://github.com/fetchai/fetchcoder-releases)** `⭐ 2` `[Fetch.ai]` — Terminal coding agent powered by ASI1, with interactive TUI, CLI, and API server modes plus MCP integration.

- **[Amp](https://sourcegraph.com/amp)** `[Sourcegraph]` — Sourcegraph's AI coding agent with a CLI for implementing tasks across real codebases.

- **[Junie CLI](https://junie.jetbrains.com)** `[JetBrains]` — JetBrains' LLM-agnostic CLI coding agent (EAP); supports GPT-5, Claude, Gemini, Grok with plan mode and CI/CD headless usage.

- **[Cortex Code CLI](https://www.snowflake.com/en/product/cortex-code/)** `[Snowflake]` — Snowflake's data-native AI coding agent CLI for building pipelines, analytics, and AI apps with enterprise governance.

- **[Devin](https://devin.ai)** `[Cognition]` — Cognition's autonomous AI software engineer with full shell/browser access, self-healing code, and PR collaboration.

- **[Cursor CLI](https://cursor.com/cli)** `[Cursor]` — Cursor's official command-line agent (`agent`) with shell mode, headless/CI support, parallel agents, and multi-model access.

- **[Tabnine CLI](https://docs.tabnine.com/main/getting-started/tabnine-cli)** `[Tabnine]` — AI-powered terminal coding assistant with agentic workflows; distributed as a Docker container, requires enterprise license.

- **[Mentat CLI](https://mentat.ai/docs/cli)** `[Mentat]` — Cloud-native coding agent CLI for managing remote Mentat agents from your terminal; auto-detects repo/branch context.

---

## Harnesses & orchestration

### Session managers & parallel runners

Tools for running and managing multiple agent sessions side-by-side. Sorted by GitHub stars.

- **[vibe-kanban](https://github.com/BloopAI/vibe-kanban)** `⭐ 27.5k` — Kanban interface for administering AI coding agents.

- **[cmux](https://github.com/manaflow-ai/cmux)** `⭐ 24.8k` — Open-source platform for running multiple coding agents in parallel.

- **[Superset](https://github.com/superset-sh/superset)** `⭐ 12.5k` — A terminal built for coding agents; orchestrates parallel agent sessions.

- **[Claude Squad](https://github.com/smtg-ai/claude-squad)** `⭐ 8.1k` — tmux-based harness to run and manage multiple Claude Code sessions side-by-side.

- **[Emdash](https://github.com/generalaction/emdash)** `⭐ 5.2k` — Run multiple coding agents concurrently with coordinated workflows.

- **[CodexMonitor](https://github.com/Dimillian/CodexMonitor)** `⭐ 4.2k` — Coordinate multiple Codex agents across local workspaces.

- **[Toad](https://github.com/batrachianai/toad)** `⭐ 3.3k` — Agent orchestrator for running and managing parallel CLI coding sessions.

- **[Crystal](https://github.com/stravu/crystal)** `⭐ 3.1k` — Execute multiple Codex and Claude Code sessions in parallel git worktrees.

- **[agent-of-empires](https://github.com/njbrake/agent-of-empires)** `⭐ 2.8k` — Manage multiple Claude Code, OpenCode, Codex CLI, Gemini CLI, Pi, Copilot CLI, Mistral Vibe, and Factory Droid agents from a TUI or web UI (mobile-friendly). Rust, uses tmux + git worktrees. MIT.

- **[supacode](https://github.com/supabitapp/supacode)** `⭐ 2.2k` — Native macOS coding agent orchestrator.

- **[mux](https://github.com/coder/mux)** `⭐ 1.9k` — Desktop application for isolated, parallel agentic development.

- **[Cate](https://github.com/0-AI-UG/cate)** `⭐ 1.9k` — Desktop app that runs terminals, Claude Code agent panels, editors, and browsers on an infinite zoomable canvas; multiple agent sessions sit side by side and panels can dock into tabs or detach into separate windows. Built with Electron and node-pty. MIT.

- **[Nimbalyst](https://github.com/nimbalyst/nimbalyst)** `⭐ 1.3k` — Open-source visual workspace for building with Codex, Claude Code, and more; manage your agents, edit the work visually, and track tasks. MIT.

- **[jean](https://github.com/coollabsio/jean)** `⭐ 1.1k` — Administer multiple projects, worktrees, and sessions with Claude CLI.

- **[CLI Agent Orchestrator (CAO)](https://github.com/awslabs/cli-agent-orchestrator)** `⭐ 925` — AWS's hierarchical multi-agent orchestration via tmux with intelligent task delegation patterns.

- **[Parallel Code](https://github.com/johannesjo/parallel-code)** `⭐ 873` — Desktop app for running multiple AI coding agents (Claude Code, Codex CLI, Gemini CLI) simultaneously in isolated git worktrees.

- **[Agent Sessions](https://github.com/jazzyalex/agent-sessions)** `⭐ 729` — Local-first macOS session-history browser for AI coding agents, with transcript search across Codex, Claude Code, OpenCode, Cursor Agent, Hermes, Copilot CLI, OpenClaw, and more; resume is available where the underlying CLI supports it. MIT.

- **[agent-deck](https://github.com/asheshgoplani/agent-deck)** `⭐ 548` — Terminal session manager for AI coding agents — one TUI for Claude, Gemini, OpenCode, Codex, and more. Worktree-aware, MCP integration, 8+ contributors. MIT.

- **[Catnip](https://github.com/wandb/catnip)** `⭐ 491` — Containerized environment + worktree automation for running multiple coding agents in parallel (optimized for Claude Code).

- **[ntm](https://github.com/Dicklesworthstone/ntm)** `⭐ 404` — Named Tmux Manager — spawn, tile, and coordinate multiple AI coding agents (Claude, Codex, Gemini) across tmux panes with a TUI command palette.

- **[hcom](https://github.com/aannoo/hcom)** `⭐ 392` — Hooks Claude Code, Antigravity, Codex, OpenCode, Kilo, and Cursor into a shared messaging and event bus; agents message, observe, and spawn each other mid-turn without changing how you use them. TUI dashboard, collision detection, cross-device relay. Rust, MIT.

- **[amux](https://github.com/mixpeek/amux)** `⭐ 304` — Agent multiplexer for running dozens of parallel Claude Code sessions with web dashboard, self-healing watchdog, kanban board, agent-to-agent REST API, and mobile PWA. Single Python file, Python 3 + tmux. MIT.

- **[AgentBox](https://github.com/madarco/agentbox)** `⭐ 281` — Run multiple coding agents in parallel, each teleported into its own sandboxed VM (local Docker, self-hosted, or cloud: Hetzner/Daytona/Vercel/E2B); sub-second checkpoints, per-box browser/VS Code/shells, git creds kept on the host. Works with Claude Code, Codex, and OpenCode. MIT.

- **[vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** `⭐ 259` — Execute Claude Code tasks in parallel git worktrees.

- **[Proliferate](https://github.com/proliferate-ai/proliferate)** `⭐ 158` — Open-source local and cloud agent IDE for Claude Code, Codex, Gemini CLI, OpenCode, and similar coding agents; parallel workspaces, subagents, plugins, MCP, and review/merge flow around real CLI sessions.

- **[AgentPipe](https://github.com/kevinelliott/agentpipe)** `⭐ 145` — CLI/TUI app that orchestrates multi-agent conversations by enabling different AI CLI tools (Claude Code, Gemini, Qwen, etc.) to communicate in shared rooms. MIT.

- **[CliDeck](https://github.com/rustykuntz/clideck)** `⭐ 143` — WhatsApp-like browser dashboard for managing multiple CLI coding agents (Claude Code, Codex, Gemini CLI, OpenCode) with live status detection, session resume, autopilot routing, and full control from a phone while away. MIT.

- **[amux](https://github.com/andyrewlee/amux)** `⭐ 139` — Terminal UI designed for running multiple coding agents in parallel.

- **[Agent AFK](https://github.com/griffinwork40/agent-afk)** `⭐ 45` — Coding-agent harness built for unattended, away-from-keyboard runs across four surfaces sharing one session manager: one-shot CLI, REPL, cron-friendly headless daemon, and a Telegram bot. Editable agent loop (prompts, permission gates, model routing, explicit terminal states), MCP (stdio/HTTP/SSE + OAuth), lifecycle hooks, background subagents, plan mode, cross-session memory, and an append-only trace receipt (`afk trace show`). Works with Anthropic and any OpenAI-compatible endpoint (GPT, Codex, local MLX/llama.cpp/Ollama). npm `agent-afk`, Node ≥22. Apache-2.0.

- **[Clave](https://github.com/codika-io/clave)** `⭐ 41` — Native macOS app for running multiple AI coding-agent CLIs (Claude Code, Gemini CLI, Codex) in parallel — split/grid terminal layouts, per-project session groups, a built-in git panel, and remote sessions over SSH. Fully local, no account. Electron. MIT.

- **[showagent](https://github.com/aytzey/showagent)** `⭐ 35` — Bubble Tea TUI that unifies the local session stores of Claude Code, Codex, Gemini CLI, and OpenCode: fuzzy search grouped by workspace, resume via each agent's own CLI, branch local copies, and cross-agent transcript conversion into the target's native format. Scriptable (`list --json`), fully local, single Go binary. MIT.

- **[Claudescope](https://github.com/vladar107/claudescope)** `⭐ 13` — Local, read-only CLI that serves a web UI to browse, search, and analyze AI coding-agent transcripts across Claude Code, Codex, Junie, pi, opencode, and Copilot CLI — sessions merged by working directory, with full-text search and token-cost analytics. npm, cross-platform. MIT.

- **[multi-agent-workflow-kit](https://github.com/laris-co/multi-agent-workflow-kit)** `⭐ 11` — Orchestrate parallel AI agents in isolated git worktrees with shared tmux visibility.

- **[CLITrigger](https://github.com/HyperAITeam/CLITrigger)** `⭐ 11` — Self-hosted web UI for orchestrating Claude Code, Codex, and Gemini CLIs in parallel git worktrees. Features multi-agent discussion mode (architect/developer/reviewer debate before implementation), cross-project Morning Review Queue, scheduled execution with rate-limit auto-recovery, and a built-in Git client. MIT.

- **[pi-boss](https://github.com/skyfallsin/pi-boss)** `⭐ 11` — Multi-agent orchestration for the Pi coding agent; spawns sub-agents in visible tmux panes with task delegation, monitoring, and coordination. MIT.

- **[repomon](https://github.com/AliHamzaAzam/repomon)** `⭐ 8` — Run a fleet of AI coding agents (Claude Code, Codex, Aider) across many repos, branches, and git worktrees from one tmux-backed terminal. Four-zoom TUI (fleet, split, babysit grid, focus), needs-you triage, durable sessions that survive restarts.

- **[tmuxlet](https://github.com/CodefiLabs/tmuxlet)** `⭐ 7` — Rust CLI that runs interactive coding CLIs (Claude, Codex, Gemini, opencode, pi, Cursor) inside tmux and exposes a normalized `claude -p` style blocking interface. Single binary, zero deps. Works against the regular Claude subscription bucket (not the separate Agent SDK credit) by driving interactive Claude Code from the outside.

- **[iris](https://github.com/itzenata/iris-tui)** `⭐ 5` — Live TUI supervisor for every active Claude Code session: status, tokens, estimated cost, and one-pane approval of pending tool calls via a PreToolUse hook. Rust, MIT.

- **[construct](https://github.com/construct-worlds/construct)** `⭐ 3` — Terminal-native agentic development environment: fleet TUI for coding agent CLIs (Codex, Claude Code, Antigravity, Grok) with fork/merge, collaborative Program Markdown orchestration, generative widgets, agent-to-agent orchestration. Single Rust binary.

- **[Agent CLI Menu](https://github.com/roypadina/AgentCliMenu)** `⭐ 1` — macOS TUI and menu-bar app to start or resume Claude Code and Codex sessions; frecency project launcher plus full-transcript fuzzy search across past sessions, with a working-directory confidence gate. MIT.

- **[postmortemthis](https://github.com/Softeria/postmortemthis)** `⭐ 1` — Runs every coding-agent CLI you have (Claude Code, Codex, Gemini, Qwen, Vibe) in parallel and read-only over your diff, then synthesizes their reviews into one ship / no-ship verdict. A cross-model second opinion before you ship. MIT.

- **[PATAPIM](https://patapim.ai)** — Terminal IDE with a 9-terminal grid for running multiple CLI coding agents simultaneously; features AI state detection, built-in Whisper voice dictation, LAN remote access, and an embedded MCP browser. Built with Electron and node-pty. Freemium.

- **[Bwee](https://bwee.app)** — Desktop app for CLI coding agents where users build their own views (BYOUI) — custom tools and dashboards that live alongside the terminal. Persistent sessions and task management. macOS.

- **[Unpeel](https://unpeel.com)** — Native macOS app built on the Ghostty terminal engine for running and remote-controlling multiple CLI agent sessions (Claude Code, Codex, Gemini CLI, Amp, OpenCode, Cline, and more): persistent terminals that survive app restarts, git worktree isolation for parallel agents, busy/attention notifications, and iPhone remote control via a self-hosted E2E-encrypted relay. Closed-source; free with paid remote access.

### Orchestrators & autonomous loops

Multi-agent coordination, swarm patterns, and autonomous execution loops. Sorted by GitHub stars.

- **[claude-flow](https://github.com/ruvnet/claude-flow)** `⭐ 65.2k` — Deploy multi-agent swarms with coordinated workflows.

- **[gastown](https://github.com/steveyegge/gastown)** `⭐ 17.1k` — Multi-agent orchestration with persistent work tracking.

- **[ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator)** `⭐ 3.1k` — Hat-based system maintaining agents in a loop until task completion.

- **[ralph-tui](https://github.com/subsy/ralph-tui)** `⭐ 2.4k` — Direct AI agents through task lists with autonomous execution.

- **[AgentsMesh](https://github.com/AgentsMesh/AgentsMesh)** `⭐ 2.3k` — AI Agent Workforce Platform: remote AI workstations (AgentPods) with PTY sandbox + git worktree isolation, multi-agent collaboration via channels and pod bindings, built-in Kanban with MR/PR integration. Self-hosted with BYOK. Supports Claude Code, Codex CLI, Gemini CLI, Aider, OpenCode. BSL-1.1.

- **[zeroshot](https://github.com/the-open-engine/zeroshot)** `⭐ 1.7k` — Runs a planner, an implementer, and independent validators in isolated local, git worktree, or Docker environments, looping until a change is verified or rejected with reproducible failures. Works with Claude, Codex, Gemini, and OpenCode CLIs; issue backends for GitHub, GitLab, Jira, Azure DevOps. MIT.

- **[loom](https://github.com/ghuntley/loom)** `⭐ 1.4k` — Infrastructure enabling autonomous loops to evolve products via multi-agent coordination.

- **[Loki Mode](https://github.com/asklokesh/loki-mode)** `⭐ 1k` — Spec-to-product autonomous loop with a built-in verification gate: a reason/act/reflect/verify closure plus a blind-review completion council that can veto "done", so it will not mark work complete until the evidence passes. Brownfield healing (`loki heal`), local-first BYO-keys, 26-tool MCP server, reads AGENTS.md. Source-available (BUSL-1.1).

- **[Hephaestus](https://github.com/agentlas-ai/Hephaestus)** `⭐ 951` — Open Agent OS for Claude Code, Codex, and Cursor with a meta-agent builder, A2A Hub routing, local ontology, and memory/security gates. Apache-2.0.

- **[Bernstein](https://github.com/chernistry/bernstein)** `⭐ 707` — Deterministic Python orchestrator — spawns parallel AI coding agents (Claude Code, Codex CLI, Gemini CLI), verifies with tests, auto-commits.

- **[Traycer](https://github.com/traycerai/traycer)** `⭐ 657` — Desktop orchestration app that runs multiple CLI coding agents (Claude Code, Codex, Cursor, OpenCode, and custom CLI agents) in parallel with shared context, agent-to-agent loops, Epic mode, and team collaboration. Apache-2.0.

- **[Aeon](https://github.com/aaronjmars/aeon)** `⭐ 577` — Autonomous agent framework that runs unattended on GitHub Actions; orchestrates Claude Code across 90+ skills (research, dev, crypto, productivity) on cron or reactive triggers, with quality scoring (1–5 via Haiku), persistent memory, and a self-healing loop. MCP + A2A integrations. MIT.

- **[h5i](https://github.com/h5i-dev/h5i)** `⭐ 475` — Runs several coding agents (Claude Code, Codex) on the same task in isolated sandboxes, has them peer-review each other, then a neutral verifier replays and tests each candidate and merges the one that passes. Run metadata is versioned in the repo under `refs/h5i/*`. Apache-2.0.

- **[wreckit](https://github.com/mikehostetler/wreckit)** `⭐ 129` — Apply the Ralph Wiggum Loop pattern across your roadmap for autonomous agent execution.

- **[OMK](https://github.com/dmae97/open-multi-agent-kit)** `⭐ 125` — Provider-neutral CLI control plane for coding agents: routes runtimes, scopes MCP, runs DAG workers, and verifies evidence before completion. MIT.

- **[kodo](https://github.com/ikamensh/kodo)** `⭐ 118` — Autonomous multi-agent coding orchestrator that directs Claude Code, Codex, and Gemini CLI through work cycles with independent architect and tester verification. SWE-bench verified.

- **[ORCH](https://github.com/oxgeneral/ORCH)** `⭐ 96` — CLI orchestrator that manages Claude Code, Codex, and Cursor as a typed task queue with state machine (todo→in_progress→review→done), auto-retry, inter-agent messaging, and TUI dashboard.

- **[LoopTroop](https://github.com/looptroop-ai/LoopTroop)** `⭐ 72` — Local, open-source GUI orchestrator for AI coding agents. An LLM Council plans, atomic "beads" execute in isolated git worktrees, and a "Ralph Loop" retries failures with fresh context to fight context rot. Built on OpenCode. MIT.

- **[OpenCastle](https://github.com/monkilabs/opencastle)** `⭐ 58` — Multi-agent orchestration framework that turns AI coding assistants (Copilot, Cursor, Claude Code, OpenCode, Windsurf, Codex CLI) into 19 coordinated specialist agents. CLI-driven (`npx opencastle init`), with task decomposition, parallel work, and quality gates. MIT.

- **[Forge](https://github.com/LucasDuys/forge)** `⭐ 55` — Autonomous spec-driven development loop for Claude Code; three-command pipeline (brainstorm specs, plan task DAGs, execute autonomously) with context survival, backpropagation that traces bugs to spec gaps, and Claude-on-Claude code review. MIT.

- **[great_cto](https://github.com/avelikiy/great_cto)** `⭐ 54` — Engineering-management layer of 34 specialist AI agents covering the full SDLC (architect, PM, senior-dev, reviewer, QA, security, devops, L3-support + 18 archetype-specific reviewers) with auto-detected archetypes and compliance gates (PCI-DSS, HIPAA, FedRAMP, GDPR, EU AI Act). Runs in Claude Code, Cursor, Codex CLI, Aider, and Continue via AGENTS.md + MCP. MIT.

- **[The Factory](https://github.com/akashgit/remote-factory)** `⭐ 51` — Self-evolving meta-harness for autonomous software dev and research; turns any codebase into an auto-research project, auto-discovers eval dimensions, generates scoring harness, and runs keep/revert experiment loops with monotonic-improvement guards. Multi-contributor. MIT.

- **[agx](https://github.com/ramarlina/agx)** `⭐ 26` — Checkpoint-based execution engine for AI coding agents; durable Wake→Work→Sleep loops that resume instantly across sessions. Supports Claude Code, Codex CLI, Gemini CLI, and Ollama. CLI + web dashboard + macOS app.

- **[5dive](https://github.com/5dive-ai/5dive)** `⭐ 25` — Run a company of AI coding agents on a server you own: one-command spin-up of named agents (Claude Code, Codex, Grok, and more), cron + heartbeat scheduling, multi-agent orchestration, Telegram control, and a babysit + needs-you triage dashboard. Self-hosted. MIT.

- **[Galley](https://github.com/shinpr/galley)** `⭐ 15` — Local-first runtime for supervised AI coding tasks: isolated git worktrees, supervisor review against acceptance criteria, retry/escalate loops, on-disk run evidence, and PR handoff. Supports Codex CLI and Claude Code. Go, MIT.

- **[ralph-harness](https://github.com/rxdt/py_ralph_frame)** `⭐ 11` — Minimal repo-local loop scaffold for Claude Code, Codex CLI, and Gemini CLI. Uses `PROMPT.md`, specs, fresh-context iterations, git hooks, CI verification, and hard iteration/time caps so agents make small gated commits instead of drifting in one long chat. MIT.

- **[Relay](https://github.com/jcast90/relay)** `⭐ 4` — Local-first orchestrator that runs inside your existing Claude or Codex CLI via MCP; classifies a request, decomposes it into tickets with a dependency DAG, dispatches across one or more repos, and supervises with live PR tracking + approval gates. CLI, TUI (ratatui), and GUI (Tauri) dashboards share `~/.relay/` state. MIT.

- **[sage](https://github.com/youwangd/SageCLI)** `⭐ 4` — Pure bash agent orchestrator (zero frameworks) with runtime-agnostic support (Claude Code, Cline, Codex, Gemini CLI, ACP), wave-based plan execution, git worktree isolation, MCP integration, skills system, headless CI mode, and 295 bats tests. MIT.

- **[Ralph Workflow](https://github.com/Ralph-Workflow/Ralph-Workflow)** `⭐ 3` — Local-first loop runner for Claude Code/Codex CLI: executes a spec in a real git repo with `progress.json` + `resume.md` + a 3-step timeout-cap; restartable, test-feedback-driven, no hosted runtime. MIT.

- **[the-perfect-orchestrator](https://github.com/daman8271/the-perfect-orchestrator)** `⭐ 1` — One lead Claude Code session commands N autonomous workers in tmux panes — spawn, brief, monitor, then adversarially verify results. Pure bash + tmux, zero daemons, coordination via plain files. Also a Claude Code plugin shipping the `/orch` skill. MIT.

### Agent infrastructure

Sandboxes, routers, browser/terminal automation, and extension tools. Sorted by GitHub stars.

- **[agent-browser](https://github.com/vercel-labs/agent-browser)** `⭐ 38.8k` — Headless browser automation CLI for agents (useful as a tool plugin for coding agents).

- **[claude-code-router](https://github.com/musistudio/claude-code-router)** `⭐ 35.9k` — Use Claude Code as a foundation while routing to alternative providers/endpoints.

- **[NemoClaw](https://github.com/NVIDIA/NemoClaw)** `⭐ 21.9k` `[NVIDIA]` — CLI tool for securely provisioning and managing sandboxed OpenClaw agent environments; enforces network, filesystem, and process-level security policies via OpenShell runtime. Apache-2.0.

- **[OpenWork](https://github.com/different-ai/openwork)** `⭐ 17k` — Open-source alternative to Claude Cowork for teams; local-first desktop app powered by OpenCode with one-click setup. MIT.

- **[Camofox Browser](https://github.com/jo-inc/camofox-browser)** `⭐ 7.8k` — Stealth headless browser for coding agents; Playwright-compatible with anti-detection, human-like fingerprinting, and a REST API for agent tool integration. MIT.

- **[open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork)** `⭐ 4.3k` — Open-source version of Claude Cowork with 500+ SaaS app integrations.

- **[toprank](https://github.com/nowork-studio/toprank)** `⭐ 3.2k` — Claude Code plugin with 9 SEO and Google Ads skills. Connects Google Search Console, PageSpeed Insights, and the Google Ads API, then ships fixes (meta tags, JSON-LD schema, keyword bids) directly to source code or CMS. Open-source, MIT.

- **[OneCLI](https://github.com/onecli/onecli)** `⭐ 2.5k` — Open-source credential vault for AI agents; Rust HTTP gateway injects API keys transparently so agents never handle raw secrets. Per-agent scoped tokens, AES-256-GCM encryption at rest. Apache-2.0.

- **[Claude Code Tools](https://github.com/pchalasani/claude-code-tools)** `⭐ 1.9k` — Utilities around Claude Code workflows (automation helpers, helpers for common tasks).

- **[Vestige](https://github.com/samvallad33/vestige)** `⭐ 587` — Local-first cognitive memory MCP server for coding agents; SQLite store, FSRS-6 retention, prediction-error gating, active forgetting, spreading activation, hybrid retrieval, and provenance/correction tools. Single Rust binary with a 3D dashboard. Works with Claude Code, Cursor, VS Code, Codex, Windsurf, and JetBrains. AGPL-3.0.

- **[AgentSight](https://github.com/eunomia-bpf/AgentSight)** `⭐ 532` — Zero-instrumentation eBPF observability for LLM/coding agents; captures syscall-level traces (file, process, network) without modifying the agent. MIT.

- **[Coasts](https://github.com/coast-guard/coasts)** `⭐ 414` — Containerized host orchestration for git worktrees; isolates ports, networks, and services per environment using DinD/Sysbox/Podman. MIT.

- **[subtask](https://github.com/zippoxer/subtask)** `⭐ 337` — Claude Skill for delegating tasks with subagents in Git worktrees.

- **[claude-cmd](https://github.com/kiliczsh/claude-cmd)** `⭐ 310` — Terminal wrapper for interacting with Claude models; often used as a building block in harness scripts.

- **[cc-router](https://github.com/finch-xu/cc-router)** `⭐ 207` — Local Anthropic-Messages-API proxy that bundles multiple provider subscriptions and API quotas (DeepSeek, Qwen, Kimi, GLM, MiniMax, Claude — 18+ providers) into virtual opus/sonnet/haiku slots with failover and load balancing for Claude Code, Claude Desktop, OpenClaw, and OpenCode. No relation to claude-code-router. Rust, MIT.

- **[agent-qa](https://github.com/vostride/agent-qa)** `⭐ 161` — Self-improving QA harness for web and mobile workflows, with a CLI, dashboard, MCP and skills for coding agents, memory-backed self-healing, and sandboxed hooks for setup/teardown. FSL-1.1-ALv2.

- **[kasetto](https://github.com/pivoshenko/kasetto)** `⭐ 117` — A declarative AI agent environment manager, written in Rust.

- **[AgentTier](https://github.com/agenttier/agenttier)** `⭐ 113` — Kubernetes-native sandbox runtime for AI coding agents. A `Sandbox` CRD provisions a Pod + PVC + NetworkPolicy with optional gVisor isolation; the `agenttier` Go CLI runs agent invocations that stream stdout/stderr/exit as SSE. Ships reference templates for Claude Code + Bedrock and LangGraph. Apache-2.0.

- **[agenttrace](https://github.com/luoyuctl/agenttrace)** `⭐ 107` — Local-first Bubble Tea TUI for inspecting Claude Code, Codex CLI, Gemini CLI, Aider, Cursor, Hermes, OpenCode, Kimi, and Copilot-style session logs; surfaces cost, cache usage, failures, latency, anomalies, health gates, and diffs.

- **[Harness Starter Kit](https://github.com/harnessworks/harness-starter-kit)** `⭐ 106` — Prompt-first harness engineering starter kit for adding durable agent instructions, drift checks, failure memory, and evaluation loops to repositories. MIT.

- **[agent-lsp](https://github.com/blackwell-systems/agent-lsp)** `⭐ 85` — MCP server giving any CLI coding agent type-aware language intelligence: 50+ LSP tools, speculative execution (preview edits without touching disk), 21 skills, 30 CI-verified languages. Measured 5–34× token savings vs grep/read. Works with Claude Code, Codex, Gemini CLI, Goose, and any MCP client. Go, MIT.

- **[ax](https://github.com/Necmttn/ax)** `⭐ 83` — Local-first agent telemetry and observability for Claude Code and Codex sessions.

- **[ActPlane](https://github.com/eunomia-bpf/ActPlane)** `⭐ 77` — OS-level agent harness that compiles a policy DSL to an eBPF engine for labeled information-flow control at the syscall boundary, with corrective feedback. MIT.

- **[RoleCraft](https://github.com/sametcelikbicak/rolecraft)** `⭐ 75` — Zero-dependency CLI to install AI agent skills as roles & behaviors from any source (local folder or GitHub repo). Works with opencode, Claude Code, Cursor, and 30+ spec-compliant agents; no marketplace or signup required.

- **[handoff](https://github.com/dazuiba/handoff)** `⭐ 74` — Let your coding agents work together: delegate tasks to DeepSeek right inside your Claude Code or Codex sessions. Python, `uv tool install handoff-cli`.

- **[AgentPlane](https://github.com/basilisk-labs/agentplane)** `⭐ 72` — Local CLI that wraps Claude Code, Codex, Cursor, and Aider work in an auditable Git-native workflow (task → plan → approve → implement → verify → finish). All state stays in `.agentplane/` inside the repo; no hosted runtime. MIT.

- **[skill-optimizer](https://github.com/fastxyz/skill-optimizer)** `⭐ 71` — CLI tool that benchmarks SDK, CLI, and MCP guidance docs (SKILL.md) across multiple LLMs using static action + argument matching. Iteratively rewrites docs until every configured model meets a PASS/FAIL score floor. MIT.

- **[authsome](https://github.com/agentrhq/authsome)** `⭐ 71` — Local credential broker for AI agents; Python CLI with encrypted local vault and a local HTTPS proxy that injects OAuth2 access tokens and API keys at request time. 45 providers bundled (14 OAuth2, 31 API key) including GitHub, Google, OpenAI, Linear, Slack, Notion, Resend, Stripe. Browser PKCE / device code / API key flows, background token refresh, no SaaS dependency. MIT.

- **[pi-mem](https://github.com/jo-inc/pi-mem)** `⭐ 68` — Plain-Markdown persistent memory for coding agents; long-term, daily, scratchpad, and searchable notes with zero dependencies on vector DBs. MIT.

- **[codex-profiles](https://github.com/Ducksss/codex-profiles)** `⭐ 62` — Bash CLI helper for switching OpenAI Codex CLI/Desktop accounts via isolated `CODEX_HOME` profiles; Homebrew install with `brew install Ducksss/tap/codex-profile`. MIT, no token copying.

- **[Untether](https://github.com/littlebearapps/untether)** `⭐ 56` — Telegram bridge for 6 CLI coding agents (Claude Code, Codex, OpenCode, Pi, Gemini CLI, Amp); remote task control via voice or text, progress streaming, interactive permissions, and cost tracking. MIT.

- **[Nex](https://github.com/nex-crm/nex-as-a-skill)** `⭐ 55` — Organizational context and memory for AI agents; connects email, Slack, CRM, and 100+ tools into one knowledge graph with a 60-tool MCP server (`npx @nex-ai/nex`) and persistent memory across agent sessions. MIT.

- **[claudebox](https://github.com/numtide/claudebox)** `⭐ 52` — Sandboxed environment for Claude Code (focused on isolation/safety).

- **[brood-box](https://github.com/stacklok/brood-box)** `⭐ 52` — Hardware-isolated microVM sandbox for AI coding agents (Claude Code, Codex, OpenCode) with COW snapshot isolation, egress control, and MCP authorization.

- **[AgentLint](https://github.com/0xmariowu/AgentLint)** `⭐ 46` — 33 evidence-backed checks for AI-friendly repos. Scans file structure, instruction quality, build setup, session continuity, and security posture. Claude Code plugin with auto-fix. Your AI agent is only as good as your repo.

- **[Wit](https://github.com/amaar-mc/wit)** `⭐ 45` — Coordination protocol that prevents merge conflicts between parallel AI agents. Locks specific functions (not files) via Tree-sitter AST parsing; agents declare intents, acquire symbol-level locks, and get conflict warnings before writing code. JSON-RPC daemon. MIT.

- **[skillreaper](https://github.com/thousandflowers/skillreaper)** `⭐ 44` — CLI that reads real session transcripts to find skills, MCP servers, and agents loaded but never fired, then safely quarantines them in a reversible operation. Supports Claude Code, Codex CLI, Hermes, OpenCode, Cursor, and OpenClaw. Zero telemetry, single static binary, Homebrew and npm. MIT.

- **[Armorer Guard](https://github.com/ArmorerLabs/Armorer-Guard)** `⭐ 41` — Local Rust scanner and MCP proxy for AI-agent prompt injection, credential leakage, exfiltration, and risky tool-call arguments before execution. MIT.

- **[pi-reflect](https://github.com/jo-inc/pi-reflect)** `⭐ 38` — Self-improving behavioral files for coding agents; automated self-reviews that evolve AGENTS.md rules from actual mistakes. MIT.

- **[AgentDiff](https://github.com/codeprakhar25/agentdiff)** `⭐ 34` — Git-native provenance for AI-written code: hooks every CLI agent (Claude Code, Codex, Cursor, Gemini, OpenCode, Windsurf, Copilot) and records which agent wrote which line, reconciles it against each commit, and signs every attribution with ed25519. Records live in your own git refs (`agentdiff list/blame/report`); no server. Rust, MIT/Apache-2.0.

- **[AgentManager](https://github.com/kevinelliott/agentmanager)** `⭐ 29` — Lightweight CLI for managing multiple agent runs/sessions and workflows.

- **[EchoCoding](https://github.com/launsion-boop/EchoCoding)** `⭐ 27` — Audio layer for CLI coding agents with hook-triggered SFX, ambient soundscape, and optional cloud TTS/ASR voice interaction for Codex and Claude Code workflows.

- **[agent-runbook](https://github.com/KnoxOps/agent-runbook)** `⭐ 22` — Python CLI that compiles contract-based YAML runbooks into SKILL.md files for Claude Code and Codex agents. Define multi-step workflows with loops, branching, parallelism, checkpoints, and file-based state passing between steps. `pip install git+https://github.com/KnoxOps/agent-runbook.git`

- **[AgentPack](https://github.com/vishal2612200/agentpack)** `⭐ 22` — Local context engine for CLI coding agents: routes tasks to relevant files, tests, repo rules, skills, and commands, then writes compact context packs and MCP/CLI receipts for Claude Code, Codex, Cursor, Windsurf, and other agents.

- **[m1nd](https://github.com/maxkle1nz/m1nd)** `⭐ 22` — Local-first MCP server that gives a CLI coding agent a neuro-symbolic code graph over the repo: `impact`/`why`/change-reasoning across a call + cross-file-imports graph (10 languages), calibrated-trust retrieval that returns `abstain`/`insufficient_evidence` instead of guessing, and persistent agent memory. A SessionStart hook pre-orients the agent before its first turn. Works with Claude Code, Codex, Cursor, and any MCP client. Rust, MIT.

- **[Unship](https://github.com/mbenhard/unship)** `⭐ 16` — Local CLI and browser picker for comparing temporary UI variants created by coding agents, then keeping one and cleaning up unused code. MIT.

- **[Data Olympus](https://github.com/knaisoma/data-olympus)** `⭐ 15` — Governance-grade project knowledge MCP server and CLI for coding agents; accepted rules, proposals, validity windows, and supersession-aware retrieval keep durable context reviewable. Apache-2.0.

- **[Agent Memory System](https://github.com/RavByte-AI/agent-memory-system)** `⭐ 13` — Persistent memory infrastructure for AI coding agents and multi-agent workflows. MIT.

- **[agent-terminal](https://github.com/jasonkneen/agent-terminal)** `⭐ 11` — Headless terminal automation for AI agents using node-pty; capture output and send input programmatically.

- **[lifeos-cli](https://github.com/liujuanjuan1984/lifeos-cli)** `⭐ 11` — Terminal-native LifeOS for managing intentions, habits, and timelogs; provides structured persistent context for agentic workflows.

- **[machine](https://github.com/katspaugh/machine)** `⭐ 11` — Provisions one isolated Lima VM per GitHub project as a sandbox for Claude Code/Codex, with Docker, Node, and signed git preconfigured. MIT.

- **[Agentic Engineering Framework](https://github.com/DimitriGeelen/agentic-engineering-framework)** `⭐ 10` — Provider-neutral governance framework for CLI coding agents. Structural enforcement of task-driven workflows, context budget management, antifragile healing loops, and audit compliance. Works with Claude Code, Aider, Cursor, and any file-based agent.

- **[Praman](https://github.com/mrkanitkar/playwright-praman)** `⭐ 10` — Playwright plugin with CLI agents (planner, generator, healer) for SAP UI5/Fiori test automation; 199 typed control proxies, OData V2/V4, AI-driven test generation via MCP. Apache-2.0.

- **[gate4agent](https://github.com/ZENG3LD/gate4agent)** `⭐ 9` `[ZENG3LD]` — Universal Rust transport library for CLI AI agents (Claude Code, Codex, Gemini, OpenCode). Pipe/NDJSON, PTY, and ACP (JSON-RPC 2.0) modes with tokio broadcast fan-out. MIT.

- **[zosma-qa](https://github.com/zosmaai/zosma-qa)** `⭐ 9` — Generates QA agent prompts (planner, generator, healer, analyzer) for CLI coding tools (OpenCode, Claude Code, VS Code Copilot); scaffolds autonomous test workflows across Playwright, Appium, and k6.

- **[Not Human Search](https://github.com/unitedideas/nothumansearch)** `⭐ 9` — Search engine for AI agents that ranks sites by agentic readiness (llms.txt, OpenAPI, MCP, ai-plugin); 8,000+ indexed sites exposed via MCP server, REST API, and full-text search. Lets agents discover and verify external services before wiring them into a repo. MIT.

- **[cowork-to-code-bridge](https://github.com/abhinaykrupa/cowork-to-code-bridge)** `⭐ 9` — Async file-based bridge that lets a sandboxed/cloud agent (Claude Cowork, CrewAI, AutoGen, LlamaIndex) delegate work to Claude Code running on your real macOS/Linux machine. A local daemon picks tasks off a shared bind-mounted directory, runs them through `run_claude.sh` (per-task model routing + budget caps + permission scoping), and returns results — no inbound network, no HTTPS tunnel. Ships a Claude Code skill, MCP audit, and selfcheck. MIT.

- **[grite](https://github.com/neul-labs/grite)** `⭐ 8` — Git-backed issue tracker with CRDT merging for AI coding agents. Issues live as an append-only event log in `refs/grite/wal`, sync via `git push`/`fetch`, and converge deterministically across agents — no server, no database, no merge conflicts. Stable `--json` output and a `grite install-skill` command for Claude Code. MIT.

- **[schliff](https://github.com/Zandereins/schliff)** `⭐ 8` — Deterministic quality linter for agent instruction files (`AGENTS.md`, `SKILL.md`, `CLAUDE.md`, `.cursorrules`) with deterministic auto-fixes, anti-gaming detection, and a GitHub Action CI gate; no LLM in the scoring path. MIT.

- **[clu](https://github.com/arjia-labs/clu)** `⭐ 7` — Codified Likeness Utility: a SQLite-backed issue tracker for coordinating fleets of AI coding agents. Atomic task claim, dependency graphs, workflows & checkpoints, and an audit log. CLI-native with clean `--json` output, built to be driven by agents. Go.

- **[Terminai](https://github.com/emosenkis/terminai)** `⭐ 6` — Makes your terminal of choice AI-enabled using your favorite CLI coding agent. Completely transparent until you activate the AI with Ctrl-Space, then runs your agent in an overlay with access to your terminal.

- **[OSOP](https://github.com/Archie0125/osop-agent-rules)** `⭐ 5` — Universal workflow logging protocol for CLI coding agents; produces `.osop` workflow definitions and `.osoplog.yaml` execution records. Supports Claude Code, Codex, Cursor, Windsurf, Aider, Cline, Roo Code, Devin, and OpenClaw. Includes a [visual editor](https://osop-editor.vercel.app) and [spec](https://github.com/Archie0125/osop-spec).

- **[Project Tiny Context Harness](https://github.com/Seven128/project-tiny-context-harness)** `⭐ 3` — Minimal repo-native project memory for CLI coding agents. Installs `AGENTS.md`, `project_context/**`, role Skills, and a `validate-context` gate so Codex, Claude Code, Cursor, Gemini CLI, OpenCode, and similar agents can recover project intent, boundaries, and validation paths across fresh sessions. MIT.

- **[Weaver](https://github.com/sean35mm/weaver)** `⭐ 2` — Local coordination layer for multiple coding agents working in the same repo. Agents announce tasks, claim paths/globs, check overlaps, and leave repo-local notes through a shared SQLite store. MIT.

- **[linear-cli](https://github.com/phnx-labs/linear-cli)** `⭐ 2` — Single-file Python CLI for Linear (the issue tracker), zero dependencies. Designed for use as a subagent tool by Claude Code, Codex, Gemini, or Cursor; ships a SKILL.md for drop-in Claude Code integration. MIT.

- **[claude-northstar](https://github.com/Nisarg38/claude-northstar)** `⭐ 1` — Transforms CLI agents from task executors into autonomous project partners.

- **[Hivelore](https://github.com/Doucs91/hivelore)** `⭐ 1` — Deterministic policy gate for agent-written code: a lesson captured via MCP (`mem_tried`) becomes a validated regex/AST/test guard that Git hooks and CI use to refuse any diff reintroducing the documented mistake; briefs any agent with the team's repo-specific rules over MCP. TypeScript CLI, npm (`@hivelore/cli`). Apache-2.0.

- **[agent-trace](https://github.com/ertygiq/agent-trace)** `⭐ 1` — Text-only CLI for extracting filtered transcripts from Claude Code, Codex, and Pi session files; useful for debugging, review, and piping transcripts into other tools. MIT.

---

## Contributing

PRs welcome! To add an entry, please ensure it meets these criteria:

**Inclusion requirements:**
- Must have a **CLI or terminal interface** (IDE-only tools don't qualify)
- Must be able to **read/write code or run commands** autonomously
- Link must point to a **valid, active** project (no dead repos)

**Entry format:**
1. **Name + link** (GitHub preferred)
2. **Star count** (for GitHub repos)
3. **1–2 line description** — what it does, who it's for

**Optional:** provider tag `[Company]`, license, or a "why it's interesting" note (diffs, LSP, sandboxing, multi-agent, MCP/skills, etc).

Entries are sorted by GitHub stars within each section. Place your entry in the correct position.
