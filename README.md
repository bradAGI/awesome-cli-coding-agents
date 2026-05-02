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

A curated list of **80+ CLI coding agents** — AI-powered tools that live in your terminal, read/edit repos, and run commands — plus the **harnesses** that orchestrate, sandbox, or extend them.

> **Last updated:** 2026-04-30

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

- **[Claw Code](https://github.com/ultraworkers/claw-code)** `⭐ 189k` — Clean-room Python/Rust rewrite of Claude Code architecture using oh-my-codex; fastest repo in GitHub history to 100K stars. Born from the March 2026 Claude Code source leak. MIT.

- **[OpenCode](https://github.com/anomalyco/opencode)** `⭐ 153k` — Terminal-native coding agent with 75+ provider support, LSP integration, and privacy-first design (formerly opencode-ai; now at opencode.ai).

- **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** `⭐ 127k` — Nous Research's self-improving CLI agent with persistent memory, automated skill creation, sandboxed code execution via Unix socket RPC, and multi-platform reach (Telegram/Slack/Discord/WhatsApp); supports 300+ models across multiple providers.

- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** `⭐ 103k` `[Google]` — Google's terminal agent powered by Gemini, with tools for repo work and research. Apache-2.0.

- **[Codex CLI](https://github.com/openai/codex)** `⭐ 79.2k` `[OpenAI]` — OpenAI's local coding agent for reading/editing/running code, with an interactive TUI and tool execution. Apache-2.0.

- **[OpenHands](https://github.com/All-Hands-AI/OpenHands)** `⭐ 72.4k` — Open-source agentic developer environment (formerly OpenDevin) with CLI and web entrypoints; also has a lightweight [CLI-only package](https://github.com/OpenHands/OpenHands-CLI).

- **[Open Interpreter](https://github.com/OpenInterpreter/open-interpreter)** `⭐ 63.4k` — Terminal tool that can execute code and actions; often used as a "do things on my machine" agent.

- **[Cline CLI](https://github.com/cline/cline)** `⭐ 61.2k` — Model-agnostic autonomous agent for planning, file edits, command execution, and browser use.

- **[Aider](https://github.com/Aider-AI/aider)** `⭐ 44.2k` — Pair-programming agent for editing files via diffs/patches, with strong git and multi-file workflows.

- **[Goose](https://github.com/block/goose)** `⭐ 43.6k` — Local, extensible agent that can execute, edit, and test; designed to run on-device and integrate with MCP.

- **[Pi](https://github.com/badlogic/pi-mono)** `⭐ 43.2k` — Minimal, adaptable terminal coding harness from the pi-mono toolkit; unified LLM API, TUI, skills, and MCP support.

- **[Continue CLI](https://github.com/continuedev/continue)** `⭐ 32.9k` — Open-source terminal extension for multi-model coding with local/privacy focus.

- **[Qwen Code](https://github.com/QwenLM/qwen-code)** `⭐ 24.1k` `[Alibaba]` — Alibaba Qwen's official CLI agent for Qwen coder models (workflow tool + repo operations). Apache-2.0.

- **[Roo Code CLI](https://github.com/RooCodeInc/Roo-Code)** `⭐ 23.8k` — Multi-mode CLI agent (architect/code/debug/orchestrator modes); Claude-like terminal interface with skills and checkpoints.

- **[Crush](https://github.com/charmbracelet/crush)** `⭐ 23.7k` — Charmbracelet's glamorous agentic coding TUI in Go; multi-provider, LSP-aware, with rich terminal UI.

- **[SWE-agent](https://github.com/SWE-agent/SWE-agent)** `⭐ 19.1k` — Agent for resolving real repo issues/PR tasks; frequently used in SWE-bench-style workflows.

- **[Kilo Code CLI](https://github.com/Kilo-Org/kilocode)** `⭐ 18.8k` — Agentic engineering platform with CLI; orchestrator mode, 100s of LLMs, skills, and checkpointing.

- **[Plandex](https://github.com/plandex-ai/plandex)** `⭐ 15.3k` — "Plan-first" CLI agent for building features across multiple files with structured steps and 2M token context.

- **[Smol Developer](https://github.com/smol-ai/developer)** `⭐ 12.2k` — Embeddable developer agent that generates entire codebases from a prompt; designed to be embedded in apps.

- **[Trae Agent](https://github.com/bytedance/trae-agent)** `⭐ 11.4k` `[ByteDance]` — ByteDance's research-friendly CLI agent for software engineering tasks, with modular architecture and multi-LLM support. MIT.

- **[Claude Engineer](https://github.com/Doriandarko/claude-engineer)** `⭐ 11.2k` — Community-driven CLI for agentic Claude workflows with file management and iterative development.

- **[Claurst](https://github.com/Kuberwastaken/claurst)** `⭐ 9.4k` — Claude Code rewritten in idiomatic Rust with architectural breakdown; includes discoveries from the source leak (KAIROS persistent assistant, buddy system). MIT.

- **[Kimi CLI](https://github.com/MoonshotAI/kimi-cli)** `⭐ 8.3k` `[Moonshot AI]` — Moonshot AI's CLI coding agent with skills, MCP support, and ACP IDE integration. Apache-2.0.

- **[Free Code](https://github.com/paoloanzn/free-code)** `⭐ 8.2k` — Fork of Claude Code with all telemetry removed, guardrails stripped, and all experimental features enabled (KAIROS, dream mode, companion system).

- **[ForgeCode](https://github.com/antinomyhq/forge)** `⭐ 7.1k` — AI pair programmer supporting 300+ models, with task management, custom agents, and large-scale refactor tooling.

- **[Kode CLI](https://github.com/shareAI-lab/Kode-cli)** `⭐ 5k` — ShareAI's open-source CLI agent for terminal-native coding with multi-provider support.

- **[Codebuff](https://github.com/CodebuffAI/codebuff)** `⭐ 4.6k` — Multi-agent AI coding assistant with CLI support for collaborative coding workflows.

- **[gptme](https://github.com/gptme/gptme)** `⭐ 4.3k` — AI agent in your terminal with support for persistent autonomous agents. Runs code, edits files, browses the web. Build long-lived self-modifying agents with git-backed memory via [gptme-agent-template](https://github.com/gptme/gptme-agent-template).

- **[Mistral Vibe](https://github.com/mistralai/mistral-vibe)** `⭐ 4.1k` `[Mistral]` — Mistral's CLI coding assistant for conversational repo interaction and edits. Apache-2.0.

- **[Every Code](https://github.com/just-every/code)** `⭐ 3.7k` — Fork of Codex CLI with validation, automation, browser integration, multi-agents, theming, and multi-provider orchestration (OpenAI, Claude, Gemini). Apache-2.0.

- **[OH-MY-PI](https://github.com/can1357/oh-my-pi)** `⭐ 3.7k` — Terminal coding agent ("Pi") with a TypeScript/Rust monorepo and local-first ergonomics.

- **[Devon](https://github.com/entropy-research/Devon)** `⭐ 3.4k` — Open-source pair programmer with a TUI; autonomous planning, execution, and debugging in Git workflows.

- **[AutoCodeRover](https://github.com/AutoCodeRoverSG/auto-code-rover)** `⭐ 3.1k` — Autonomous program improvement agent; patches real GitHub issues using code search and analysis.

- **[Grok CLI](https://github.com/superagent-ai/grok-cli)** `⭐ 3k` — Community CLI agent built on xAI's Grok models for terminal-based coding tasks.

- **[CodeMachine-CLI](https://github.com/moazbuilds/CodeMachine-CLI)** `⭐ 2.5k` — Community multi-agent CLI aimed at running coding workflows locally (vibe-coding oriented).

- **[Codel](https://github.com/semanser/codel)** `⭐ 2.4k` — Autonomous agent for performing complex tasks via terminal; runs in Docker with a web UI.

- **[Letta Code](https://github.com/letta-ai/letta-code)** `⭐ 2.4k` — Memory-first CLI coding agent built on the Letta platform (formerly MemGPT); persistent memory across sessions, model-agnostic (Claude/GPT/Gemini), skill learning, and context repositories.

- **[RA.Aid](https://github.com/ai-christianson/RA.Aid)** `⭐ 2.2k` — Autonomous coding agent built on LangGraph with research/plan/implement pipeline; optional aider integration for near-full autonomy.

- **[open-codex](https://github.com/ymichael/open-codex)** `⭐ 2.2k` — Lightweight fork of Codex CLI with multi-provider support (OpenAI, Gemini, OpenRouter, Ollama).

- **[Agentless](https://github.com/OpenAutoCoder/Agentless)** `⭐ 2k` — Lightweight approach to autonomous software engineering without persistent agent loops.

- **[Amazon Q Developer CLI](https://github.com/aws/amazon-q-developer-cli)** `⭐ 1.9k` `[AWS]` — AWS's agentic terminal chat for building apps, debugging, and DevOps with natural language. Apache-2.0.

- **[Neovate Code](https://github.com/neovateai/neovate-code)** `⭐ 1.5k` `[Ant Group]` — Ant Group's CLI agent with plugin system, multi-model/multi-provider support, MCP integrations, and headless automation mode. MIT.

- **[Groq Code CLI](https://github.com/build-with-groq/groq-code-cli)** `⭐ 725` — Customizable, lightweight CLI powered by Groq's ultra-fast inference; extensible tools/commands with multi-model support.

- **[Dexto](https://github.com/truffle-ai/dexto)** `⭐ 613` — Coding agent and general agent harness with CLI/web/API modes; ships a production-ready coding agent with sub-agent spawning.

- **[g3](https://github.com/dhanji/g3)** `⭐ 509` — "Coding AI agent" in Rust: tool-running, repo interaction, skills system, and provider abstraction.

- **[claw-code-agent](https://github.com/HarnessLab/claw-code-agent)** `⭐ 442` — Python-only Claude Code rewrite with zero external dependencies; born from the March 2026 Claude Code source leak, positioned as easier to hack on than the Rust/TypeScript reimplementations.

- **[Coro Code](https://github.com/Blushyes/coro-code)** `⭐ 358` — Open-source CLI coding agent, a free alternative to Claude Code; generate, debug, and manage code seamlessly.

- **[LettaBot](https://github.com/letta-ai/lettabot)** `⭐ 324` — Personal AI assistant with persistent unified memory across Telegram, Slack, Discord, WhatsApp, and Signal; built on the Letta platform.

- **[Mini-Kode](https://github.com/minmaxflow/mini-kode)** `⭐ 301` — An educational AI coding agent CLI, intended as a readable reference implementation.

- **[nori-cli](https://github.com/tilework-tech/nori-cli)** `⭐ 123` — Multi-provider CLI built on Codex CLI; switch between Claude, Gemini, and Codex from the same native terminal.

- **[cursor-agent](https://github.com/civai-technologies/cursor-agent)** `⭐ 116` — Python-based agent replicating Cursor's coding assistant capabilities; supports Claude, OpenAI, and local Ollama models.

- **[openHarness](https://github.com/zhijiewong/openharness)** `⭐ 89` — Open-source Claude Code alternative. 78 slash commands, 42 tools, MCP (stdio/HTTP/SSE + OAuth 2.1), hooks, subagents, plan mode. Works with Anthropic/OpenAI/Ollama/llama.cpp/LM Studio. Ships both npm and Python SDK. MIT.

- **[VibePod](https://github.com/VibePod/vibepod-cli)** `⭐ 67` — Unified CLI for running AI coding agents in isolated Docker containers; zero-config setup, local metrics, HTTP traffic tracking, and an analytics dashboard for side-by-side comparison.

- **[Crab Code](https://github.com/lingcoder/crab-code)** `⭐ 54` — Rust-native agentic coding CLI aligned with Claude Code's toolset and permission model; works with any LLM provider (Anthropic/OpenAI/DeepSeek/Bedrock/Vertex). 27 crates, 4,700+ tests, layered config system. Apache-2.0.

- **[QQCode](https://github.com/qnguyen3/qqcode)** `⭐ 52` — Lightweight CLI coding agent in Rust focused on speed, determinism, and developer control; supports skills.

- **[Octomind](https://github.com/Muvon/octomind)** `⭐ 51` — Open-source, model-agnostic AI agent runtime with community tap registry (`developer:rust`, `doctor:blood`, `legal:contracts`), MCP support with runtime self-extension, 13+ providers, and adaptive compression. Written in Rust. Apache-2.0.

- **[picocode](https://github.com/jondot/picocode)** `⭐ 47` — Minimal Rust-based coding agent focused on CI workflows and small codemods; multi-LLM with personas.

- **[Smelt](https://github.com/leonardcser/smelt)** `⭐ 18` — Rust TUI coding agent; multi-provider (Anthropic, OpenAI, Ollama, GitHub Copilot, any OpenAI-compatible endpoint), four modes (Normal/Plan/Apply/Yolo), granular permission system, parallel subagents, vim keybindings, and headless scriptable mode. MIT.

- **[Binharic](https://github.com/CogitatorTech/binharic-cli)** `⭐ 16` — A multi-provider "tech-priest persona" coding agent CLI (stylized, tool-using).

- **[Darce](https://github.com/AmerSarhan/darce-cli)** `⭐ 4` — Ultralight (14 kB) multi-model CLI agent built with Ink; 7 tools, smart model routing across providers, streaming, session resume, and slash commands. MIT.

- **[CLAII](https://github.com/agencyswarm/CLAII)** `⭐ 2` — CLI-first AI coding agent with multi-agent orchestration, MCP toolchains, and memory-persistent refactors.

### OpenClaw ecosystem

Projects built on, forked from, or inspired by [OpenClaw](https://github.com/openclaw/openclaw) — the open-source personal AI assistant. Sorted by GitHub stars.

- **[OpenClaw](https://github.com/openclaw/openclaw)** `⭐ 367k` — The original personal AI assistant you run locally; CLI with onboarding wizard, skills, tools, and multi-channel support (WhatsApp/Slack/Discord). MIT.

- **[nanobot](https://github.com/HKUDS/nanobot)** `⭐ 41.4k` — Ultra-lightweight ~4,000-line Python rewrite of OpenClaw; tool use, persistent memory, scheduled tasks, and multi-channel support (Telegram/Discord/WhatsApp). MIT.

- **[ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)** `⭐ 30.9k` — Fully autonomous AI agent runtime in Rust; trait-driven pluggable architecture (providers, tools, memory, channels), runs on minimal hardware (<5MB RAM), multi-channel CLI/Telegram/Discord/Slack, with sandboxed execution and hybrid vector+keyword search.

- **[PicoClaw](https://github.com/sipeed/picoclaw)** `⭐ 28.6k` — Ultra-lightweight personal AI assistant in Go inspired by OpenClaw; runs on $10 hardware with less than 10MB RAM.

- **[NanoClaw](https://github.com/gavrielc/nanoclaw)** `⭐ 28.4k` — Security-first lightweight alternative to OpenClaw; runs agents in Apple containers/Docker with sandboxed execution, built on Anthropic's Agents SDK.

- **[IronClaw](https://github.com/nearai/ironclaw)** `⭐ 12.1k` — OpenClaw rewritten in Rust by NEAR AI; WASM sandbox isolation, capability-based permissions, and prompt injection defense.

- **[NullClaw](https://github.com/nullclaw/nullclaw)** `⭐ 7.4k` — Fastest, smallest OpenClaw-compatible agent in Zig; 678KB static binary, ~1MB RAM, <2ms startup, 23+ providers, 18 channels. MIT.

- **[Clawith](https://github.com/dataelement/Clawith)** `⭐ 3.5k` — "OpenClaw for Teams" — multi-agent collaboration platform that scales OpenClaw to organizations. Apache-2.0.

- **[Moltis](https://github.com/moltis-org/moltis)** `⭐ 2.6k` — Secure, auditable Rust-native alternative to OpenClaw; zero unsafe code, 2,300+ tests, built-in voice I/O, MCP servers, and multi-channel access. MIT.

- **[claw0](https://github.com/shareAI-lab/claw0)** `⭐ 2.4k` — 0-to-1 tutorial companion for the OpenClaw ecosystem; walks through building an agent harness from scratch, covering planning, context compression, and task persistence.

- **[GitClaw](https://github.com/open-gitagent/gitclaw)** `⭐ 321` — Git-native AI agent framework where agent identity, rules, memory, tools, and skills are all version-controlled files. MIT.

- **[LionClaw](https://github.com/moshthepitt/lionclaw)** `⭐ 4` — Secure-first local AI CLI with a small auditable kernel, durable sessions, and installable skills. MIT.

### Closed Source

Proprietary agents — usable but not forkable or extensible at the source level.

- **[Claude Code](https://github.com/anthropics/claude-code)** `⭐ 119k` `[Anthropic]` — Anthropic's repo-aware terminal agent for code edits, refactors, and git workflows. Source-available, no OSS license.

- **[Warp](https://github.com/warpdotdev/Warp)** `⭐ 48.9k` `[Warp]` — Modern terminal with built-in AI agent mode; understands tasks, runs commands, edits files, and orchestrates multi-step workflows.

- **[GitHub Copilot in the CLI](https://github.com/github/copilot-cli)** `⭐ 10.3k` `[GitHub]` — GitHub's agentic CLI for repo/PR/issue workflows, command suggestions, and headless automation.

- **[Droid](https://github.com/Factory-AI/factory)** `⭐ 819` `[Factory]` — Factory's multi-model CLI coding agent; #1 on Terminal-Bench, specialized droids for different tasks, headless CI mode, and multi-interface support (CLI/IDE/Slack/Linear).

- **[Command Code](https://github.com/CommandCodeAI/command-code)** `⭐ 17` `[CommandCode]` — CLI coding agent that continuously learns your coding style via taste-1 neuro-symbolic AI; adapts to preferences over time with project-specific taste profiles.

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

- **[vibe-kanban](https://github.com/BloopAI/vibe-kanban)** `⭐ 25.7k` — Kanban interface for administering AI coding agents.

- **[cmux](https://github.com/manaflow-ai/cmux)** `⭐ 15.9k` — Open-source platform for running multiple coding agents in parallel.

- **[Superset](https://github.com/superset-sh/superset)** `⭐ 10.2k` — A terminal built for coding agents; orchestrates parallel agent sessions.

- **[Claude Squad](https://github.com/smtg-ai/claude-squad)** `⭐ 7.2k` — tmux-based harness to run and manage multiple Claude Code sessions side-by-side.

- **[Emdash](https://github.com/generalaction/emdash)** `⭐ 4.2k` — Run multiple coding agents concurrently with coordinated workflows.

- **[CodexMonitor](https://github.com/Dimillian/CodexMonitor)** `⭐ 3.7k` — Coordinate multiple Codex agents across local workspaces.

- **[Crystal](https://github.com/stravu/crystal)** `⭐ 3k` — Execute multiple Codex and Claude Code sessions in parallel git worktrees.

- **[Toad](https://github.com/batrachianai/toad)** `⭐ 3k` — Agent orchestrator for running and managing parallel CLI coding sessions.

- **[mux](https://github.com/coder/mux)** `⭐ 1.7k` — Desktop application for isolated, parallel agentic development.

- **[supacode](https://github.com/supabitapp/supacode)** `⭐ 950` — Native macOS coding agent orchestrator.

- **[jean](https://github.com/coollabsio/jean)** `⭐ 884` — Administer multiple projects, worktrees, and sessions with Claude CLI.

- **[Parallel Code](https://github.com/johannesjo/parallel-code)** `⭐ 598` — Desktop app for running multiple AI coding agents (Claude Code, Codex CLI, Gemini CLI) simultaneously in isolated git worktrees.

- **[CLI Agent Orchestrator (CAO)](https://github.com/awslabs/cli-agent-orchestrator)** `⭐ 521` — AWS's hierarchical multi-agent orchestration via tmux with intelligent task delegation patterns.

- **[Catnip](https://github.com/wandb/catnip)** `⭐ 480` — Containerized environment + worktree automation for running multiple coding agents in parallel (optimized for Claude Code).

- **[vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** `⭐ 253` — Execute Claude Code tasks in parallel git worktrees.

- **[amux](https://github.com/mixpeek/amux)** `⭐ 155` — Agent multiplexer for running dozens of parallel Claude Code sessions with web dashboard, self-healing watchdog, kanban board, agent-to-agent REST API, and mobile PWA. Single Python file, Python 3 + tmux. MIT.

- **[AgentPipe](https://github.com/kevinelliott/agentpipe)** `⭐ 120` — CLI/TUI app that orchestrates multi-agent conversations by enabling different AI CLI tools (Claude Code, Gemini, Qwen, etc.) to communicate in shared rooms. MIT.

- **[amux](https://github.com/andyrewlee/amux)** `⭐ 101` — Terminal UI designed for running multiple coding agents in parallel.

- **[CliDeck](https://github.com/rustykuntz/clideck)** `⭐ 63` — WhatsApp-like browser dashboard for managing multiple CLI coding agents (Claude Code, Codex, Gemini CLI, OpenCode) with live status detection, session resume, autopilot routing, and full control from a phone while away. MIT.

- **[multi-agent-workflow-kit](https://github.com/laris-co/multi-agent-workflow-kit)** `⭐ 9` — Orchestrate parallel AI agents in isolated git worktrees with shared tmux visibility.

- **[CLITrigger](https://github.com/HyperAITeam/CLITrigger)** `⭐ 4` — Self-hosted web UI for orchestrating Claude Code, Codex, and Gemini CLIs in parallel git worktrees. Features multi-agent discussion mode (architect/developer/reviewer debate before implementation), cross-project Morning Review Queue, scheduled execution with rate-limit auto-recovery, and a built-in Git client. MIT.

- **[PATAPIM](https://patapim.ai)** — Terminal IDE with a 9-terminal grid for running multiple CLI coding agents simultaneously; features AI state detection, built-in Whisper voice dictation, LAN remote access, and an embedded MCP browser. Built with Electron and node-pty. Freemium.

### Orchestrators & autonomous loops

Multi-agent coordination, swarm patterns, and autonomous execution loops. Sorted by GitHub stars.

- **[claude-flow](https://github.com/ruvnet/claude-flow)** `⭐ 34.1k` — Deploy multi-agent swarms with coordinated workflows.

- **[gastown](https://github.com/steveyegge/gastown)** `⭐ 14.8k` — Multi-agent orchestration with persistent work tracking.

- **[ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator)** `⭐ 2.8k` — Hat-based system maintaining agents in a loop until task completion.

- **[ralph-tui](https://github.com/subsy/ralph-tui)** `⭐ 2.3k` — Direct AI agents through task lists with autonomous execution.

- **[AgentsMesh](https://github.com/AgentsMesh/AgentsMesh)** `⭐ 1.8k` — AI Agent Workforce Platform: remote AI workstations (AgentPods) with PTY sandbox + git worktree isolation, multi-agent collaboration via channels and pod bindings, built-in Kanban with MR/PR integration. Self-hosted with BYOK. Supports Claude Code, Codex CLI, Gemini CLI, Aider, OpenCode. BSL-1.1.

- **[loom](https://github.com/ghuntley/loom)** `⭐ 1.3k` — Infrastructure enabling autonomous loops to evolve products via multi-agent coordination.

- **[Aeon](https://github.com/aaronjmars/aeon)** `⭐ 263` — Autonomous agent framework that runs unattended on GitHub Actions; orchestrates Claude Code across 90+ skills (research, dev, crypto, productivity) on cron or reactive triggers, with quality scoring (1–5 via Haiku), persistent memory, and a self-healing loop. MCP + A2A integrations. MIT.

- **[Bernstein](https://github.com/chernistry/bernstein)** `⭐ 249` — Deterministic Python orchestrator — spawns parallel AI coding agents (Claude Code, Codex CLI, Gemini CLI), verifies with tests, auto-commits.

- **[wreckit](https://github.com/mikehostetler/wreckit)** `⭐ 126` — Apply the Ralph Wiggum Loop pattern across your roadmap for autonomous agent execution.

- **[kodo](https://github.com/ikamensh/kodo)** `⭐ 69` — Autonomous multi-agent coding orchestrator that directs Claude Code, Codex, and Gemini CLI through work cycles with independent architect and tester verification. SWE-bench verified.

- **[ORCH](https://github.com/oxgeneral/ORCH)** `⭐ 43` — CLI orchestrator that manages Claude Code, Codex, and Cursor as a typed task queue with state machine (todo→in_progress→review→done), auto-retry, inter-agent messaging, and TUI dashboard.

- **[OpenCastle](https://github.com/monkilabs/opencastle)** `⭐ 41` — Multi-agent orchestration framework that turns AI coding assistants (Copilot, Cursor, Claude Code, OpenCode, Windsurf, Codex CLI) into 19 coordinated specialist agents. CLI-driven (`npx opencastle init`), with task decomposition, parallel work, and quality gates. MIT.

- **[Forge](https://github.com/LucasDuys/forge)** `⭐ 25` — Autonomous spec-driven development loop for Claude Code; three-command pipeline (brainstorm specs, plan task DAGs, execute autonomously) with context survival, backpropagation that traces bugs to spec gaps, and Claude-on-Claude code review. MIT.

- **[agx](https://github.com/ramarlina/agx)** `⭐ 20` — Checkpoint-based execution engine for AI coding agents; durable Wake→Work→Sleep loops that resume instantly across sessions. Supports Claude Code, Codex CLI, Gemini CLI, and Ollama. CLI + web dashboard + macOS app.

- **[sage](https://github.com/youwangd/SageCLI)** `⭐ 3` — Pure bash agent orchestrator (zero frameworks) with runtime-agnostic support (Claude Code, Cline, Codex, Gemini CLI, ACP), wave-based plan execution, git worktree isolation, MCP integration, skills system, headless CI mode, and 295 bats tests. MIT.

- **[Relay](https://github.com/jcast90/relay)** `⭐ 3` — Local-first orchestrator that runs inside your existing Claude or Codex CLI via MCP; classifies a request, decomposes it into tickets with a dependency DAG, dispatches across one or more repos, and supervises with live PR tracking + approval gates. CLI, TUI (ratatui), and GUI (Tauri) dashboards share `~/.relay/` state. MIT.

### Agent infrastructure

Sandboxes, routers, browser/terminal automation, and extension tools. Sorted by GitHub stars.

- **[claude-code-router](https://github.com/musistudio/claude-code-router)** `⭐ 33.3k` — Use Claude Code as a foundation while routing to alternative providers/endpoints.

- **[agent-browser](https://github.com/vercel-labs/agent-browser)** `⭐ 31.2k` — Headless browser automation CLI for agents (useful as a tool plugin for coding agents).

- **[NemoClaw](https://github.com/NVIDIA/NemoClaw)** `⭐ 20k` `[NVIDIA]` — CLI tool for securely provisioning and managing sandboxed OpenClaw agent environments; enforces network, filesystem, and process-level security policies via OpenShell runtime. Apache-2.0.

- **[OpenWork](https://github.com/different-ai/openwork)** `⭐ 14.6k` — Open-source alternative to Claude Cowork for teams; local-first desktop app powered by OpenCode with one-click setup. MIT.

- **[open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork)** `⭐ 4k` — Open-source version of Claude Cowork with 500+ SaaS app integrations.

- **[OneCLI](https://github.com/onecli/onecli)** `⭐ 2.1k` — Open-source credential vault for AI agents; Rust HTTP gateway injects API keys transparently so agents never handle raw secrets. Per-agent scoped tokens, AES-256-GCM encryption at rest. Apache-2.0.

- **[Claude Code Tools](https://github.com/pchalasani/claude-code-tools)** `⭐ 1.8k` — Utilities around Claude Code workflows (automation helpers, helpers for common tasks).

- **[toprank](https://github.com/nowork-studio/toprank)** `⭐ 1.5k` — Claude Code plugin with 9 SEO and Google Ads skills. Connects Google Search Console, PageSpeed Insights, and the Google Ads API, then ships fixes (meta tags, JSON-LD schema, keyword bids) directly to source code or CMS. Open-source, MIT.

- **[Coasts](https://github.com/coast-guard/coasts)** `⭐ 377` — Containerized host orchestration for git worktrees; isolates ports, networks, and services per environment using DinD/Sysbox/Podman. MIT.

- **[subtask](https://github.com/zippoxer/subtask)** `⭐ 328` — Claude Skill for delegating tasks with subagents in Git worktrees.

- **[claude-cmd](https://github.com/kiliczsh/claude-cmd)** `⭐ 301` — Terminal wrapper for interacting with Claude models; often used as a building block in harness scripts.

- **[kasetto](https://github.com/pivoshenko/kasetto)** `⭐ 67` — A declarative AI agent environment manager, written in Rust.

- **[claudebox](https://github.com/numtide/claudebox)** `⭐ 46` — Sandboxed environment for Claude Code (focused on isolation/safety).

- **[skill-optimizer](https://github.com/fastxyz/skill-optimizer)** `⭐ 45` — CLI tool that benchmarks SDK, CLI, and MCP guidance docs (SKILL.md) across multiple LLMs using static action + argument matching. Iteratively rewrites docs until every configured model meets a PASS/FAIL score floor. MIT.

- **[Untether](https://github.com/littlebearapps/untether)** `⭐ 42` — Telegram bridge for 6 CLI coding agents (Claude Code, Codex, OpenCode, Pi, Gemini CLI, Amp); remote task control via voice or text, progress streaming, interactive permissions, and cost tracking. MIT.

- **[Wit](https://github.com/amaar-mc/wit)** `⭐ 40` — Coordination protocol that prevents merge conflicts between parallel AI agents. Locks specific functions (not files) via Tree-sitter AST parsing; agents declare intents, acquire symbol-level locks, and get conflict warnings before writing code. JSON-RPC daemon. MIT.

- **[AgentPlane](https://github.com/basilisk-labs/agentplane)** `⭐ 41` — Local CLI that wraps Claude Code, Codex, Cursor, and Aider work in an auditable Git-native workflow (task → plan → approve → implement → verify → finish). All state stays in `.agentplane/` inside the repo; no hosted runtime. MIT.

- **[Nex](https://github.com/nex-crm/nex-as-a-skill)** `⭐ 40` — Organizational context and memory for AI agents; connects email, Slack, CRM, and 100+ tools into one knowledge graph with a 60-tool MCP server (`npx @nex-ai/nex`) and persistent memory across agent sessions. MIT.

- **[brood-box](https://github.com/stacklok/brood-box)** `⭐ 29` — Hardware-isolated microVM sandbox for AI coding agents (Claude Code, Codex, OpenCode) with COW snapshot isolation, egress control, and MCP authorization.

- **[AgentManager](https://github.com/kevinelliott/agentmanager)** `⭐ 23` — Lightweight CLI for managing multiple agent runs/sessions and workflows.

- **[AgentLint](https://github.com/0xmariowu/AgentLint)** `⭐ 22` — 33 evidence-backed checks for AI-friendly repos. Scans file structure, instruction quality, build setup, session continuity, and security posture. Claude Code plugin with auto-fix. Your AI agent is only as good as your repo.

- **[EchoCoding](https://github.com/launsion-boop/EchoCoding)** `⭐ 21` — Audio layer for CLI coding agents with hook-triggered SFX, ambient soundscape, and optional cloud TTS/ASR voice interaction for Codex and Claude Code workflows.

- **[agent-terminal](https://github.com/jasonkneen/agent-terminal)** `⭐ 10` — Headless terminal automation for AI agents using node-pty; capture output and send input programmatically.

- **[zosma-qa](https://github.com/zosmaai/zosma-qa)** `⭐ 6` — Generates QA agent prompts (planner, generator, healer, analyzer) for CLI coding tools (OpenCode, Claude Code, VS Code Copilot); scaffolds autonomous test workflows across Playwright, Appium, and k6.

- **[lifeos-cli](https://github.com/liujuanjuan1984/lifeos-cli)** `⭐ 6` — Terminal-native LifeOS for managing intentions, habits, and timelogs; provides structured persistent context for agentic workflows.

- **[gate4agent](https://github.com/ZENG3LD/gate4agent)** `⭐ 5` `[ZENG3LD]` — Universal Rust transport library for CLI AI agents (Claude Code, Codex, Gemini, OpenCode). Pipe/NDJSON, PTY, and ACP (JSON-RPC 2.0) modes with tokio broadcast fan-out. MIT.

- **[pi-builder](https://github.com/arosstale/pi-builder)** `⭐ 5` — TypeScript monorepo that wraps any installed CLI coding agent (Claude Code, Aider, OpenCode, Codex, Gemini CLI, Goose, Plandex, SWE-agent, Crush, gptme) behind a single interface; capability-based routing, health caching, fallback chains, SQLite persistence, and a streaming OrchestratorService. MIT.

- **[Praman](https://github.com/mrkanitkar/playwright-praman)** `⭐ 5` — Playwright plugin with CLI agents (planner, generator, healer) for SAP UI5/Fiori test automation; 199 typed control proxies, OData V2/V4, AI-driven test generation via MCP. Apache-2.0.

- **[Agentic Engineering Framework](https://github.com/DimitriGeelen/agentic-engineering-framework)** `⭐ 4` — Provider-neutral governance framework for CLI coding agents. Structural enforcement of task-driven workflows, context budget management, antifragile healing loops, and audit compliance. Works with Claude Code, Aider, Cursor, and any file-based agent.

- **[OSOP](https://github.com/Archie0125/osop-agent-rules)** `⭐ 1` — Universal workflow logging protocol for CLI coding agents; produces `.osop` workflow definitions and `.osoplog.yaml` execution records. Supports Claude Code, Codex, Cursor, Windsurf, Aider, Cline, Roo Code, Devin, and OpenClaw. Includes a [visual editor](https://osop-editor.vercel.app) and [spec](https://github.com/Archie0125/osop-spec).

- **[claude-northstar](https://github.com/Nisarg38/claude-northstar)** `⭐ 1` — Transforms CLI agents from task executors into autonomous project partners.

- **[linear-cli](https://github.com/phnx-labs/linear-cli)** `⭐ 0` — Single-file Python CLI for Linear (the issue tracker), zero dependencies. Designed for use as a subagent tool by Claude Code, Codex, Gemini, or Cursor; ships a SKILL.md for drop-in Claude Code integration. MIT.

- **[Not Human Search](https://github.com/unitedideas/nothumansearch)** `⭐ 0` — Search engine for AI agents that ranks sites by agentic readiness (llms.txt, OpenAPI, MCP, ai-plugin); 8,000+ indexed sites exposed via MCP server, REST API, and full-text search. Lets agents discover and verify external services before wiring them into a repo. MIT.

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
