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

A curated list of **CLI coding agents** — AI-powered tools that live in your terminal, read/edit repos, and run commands — plus the **harnesses** that orchestrate, sandbox, or extend them.

### What is a CLI coding agent?

A CLI coding agent is an AI-powered tool that runs in your terminal and can autonomously read, write, and execute code in your repository. Unlike chat-based assistants, these agents have direct access to your filesystem, shell, and dev tools — they can edit files, run tests, commit changes, and iterate on errors. Think of them as AI pair programmers that live where you already work: the command line.

---

## Contents

- [Terminal-native coding agents](#terminal-native-coding-agents)
  - [Open Source](#open-source)
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

- **[OpenClaw](https://github.com/openclaw/openclaw)** `⭐ 310k` — Personal AI assistant you run locally; CLI with onboarding wizard, skills, tools, and multi-channel support (WhatsApp/Slack/Discord).

- **[OpenCode](https://github.com/anomalyco/opencode)** `⭐ 122k` — Terminal-native coding agent with 75+ provider support, LSP integration, and privacy-first design (formerly opencode-ai; now at opencode.ai).

- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** `⭐ 98k` `[Google]` — Google's terminal agent powered by Gemini, with tools for repo work and research. Apache-2.0.

- **[OpenDevin](https://github.com/OpenDevin/OpenDevin)** `⭐ 69k` — Open-source agentic developer environment (not purely CLI, but often run locally with terminal entrypoints).

- **[Codex CLI](https://github.com/openai/codex)** `⭐ 65k` `[OpenAI]` — OpenAI's local coding agent for reading/editing/running code, with an interactive TUI and tool execution. Apache-2.0.

- **[Open Interpreter](https://github.com/OpenInterpreter/open-interpreter)** `⭐ 63k` — Terminal tool that can execute code and actions; often used as a "do things on my machine" agent.

- **[Cline CLI](https://github.com/cline/cline)** `⭐ 59k` — Model-agnostic autonomous agent for planning, file edits, command execution, and browser use.

- **[Aider](https://github.com/Aider-AI/aider)** `⭐ 42k` — Pair-programming agent for editing files via diffs/patches, with strong git and multi-file workflows.

- **[Goose](https://github.com/block/goose)** `⭐ 33k` — Local, extensible agent that can execute, edit, and test; designed to run on-device and integrate with MCP.

- **[Continue CLI](https://github.com/continuedev/continue)** `⭐ 32k` — Open-source terminal extension for multi-model coding with local/privacy focus.

- **[ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)** `⭐ 27k` — Fully autonomous AI agent runtime in Rust; trait-driven pluggable architecture (providers, tools, memory, channels), runs on minimal hardware (<5MB RAM), multi-channel CLI/Telegram/Discord/Slack, with sandboxed execution and hybrid vector+keyword search.

- **[PicoClaw](https://github.com/sipeed/picoclaw)** `⭐ 25k` — Ultra-lightweight personal AI assistant in Go inspired by OpenClaw; runs on $10 hardware with less than 10MB RAM.

- **[Pi](https://github.com/badlogic/pi-mono)** `⭐ 23k` — Minimal, adaptable terminal coding harness from the pi-mono toolkit; unified LLM API, TUI, skills, and MCP support.

- **[Roo Code CLI](https://github.com/RooCodeInc/Roo-Code)** `⭐ 23k` — Multi-mode CLI agent (architect/code/debug/orchestrator modes); Claude-like terminal interface with skills and checkpoints.

- **[NanoClaw](https://github.com/gavrielc/nanoclaw)** `⭐ 22k` — Security-first lightweight alternative to OpenClaw; runs agents in Apple containers/Docker with sandboxed execution, built on Anthropic's Agents SDK.

- **[Crush](https://github.com/charmbracelet/crush)** `⭐ 21k` — Charmbracelet's glamorous agentic coding TUI in Go; multi-provider, LSP-aware, with rich terminal UI.

- **[Qwen Code](https://github.com/QwenLM/qwen-code)** `⭐ 20k` `[Alibaba]` — Alibaba Qwen's official CLI agent for Qwen coder models (workflow tool + repo operations). Apache-2.0.

- **[SWE-agent](https://github.com/SWE-agent/SWE-agent)** `⭐ 19k` — Agent for resolving real repo issues/PR tasks; frequently used in SWE-bench-style workflows.

- **[Kilo Code CLI](https://github.com/Kilo-Org/kilocode)** `⭐ 17k` — Agentic engineering platform with CLI; orchestrator mode, 100s of LLMs, skills, and checkpointing.

- **[Plandex](https://github.com/plandex-ai/plandex)** `⭐ 15k` — "Plan-first" CLI agent for building features across multiple files with structured steps and 2M token context.

- **[Smol Developer](https://github.com/smol-ai/developer)** `⭐ 12k` — Embeddable developer agent that generates entire codebases from a prompt; designed to be embedded in apps.

- **[Claude Engineer](https://github.com/Doriandarko/claude-engineer)** `⭐ 11k` — Community-driven CLI for agentic Claude workflows with file management and iterative development.

- **[Trae Agent](https://github.com/bytedance/trae-agent)** `⭐ 11k` `[ByteDance]` — ByteDance's research-friendly CLI agent for software engineering tasks, with modular architecture and multi-LLM support. MIT.

- **[IronClaw](https://github.com/nearai/ironclaw)** `⭐ 9.9k` — OpenClaw rewritten in Rust by NEAR AI; WASM sandbox isolation, capability-based permissions, and prompt injection defense.

- **[Kimi CLI](https://github.com/MoonshotAI/kimi-cli)** `⭐ 7.1k` `[Moonshot AI]` — Moonshot AI's CLI coding agent with skills, MCP support, and ACP IDE integration. Apache-2.0.

- **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** `⭐ 6.6k` — Nous Research's self-improving CLI agent with persistent memory, automated skill creation, sandboxed code execution via Unix socket RPC, and multi-platform reach (Telegram/Slack/Discord/WhatsApp); supports 300+ models across multiple providers.

- **[ForgeCode](https://github.com/antinomyhq/forge)** `⭐ 4.8k` — AI pair programmer supporting 300+ models, with task management, custom agents, and large-scale refactor tooling.

- **[Kode CLI](https://github.com/shareAI-lab/Kode-cli)** `⭐ 4.5k` — ShareAI's open-source CLI agent for terminal-native coding with multi-provider support.

- **[gptme](https://github.com/gptme/gptme)** `⭐ 4.2k` — Personal AI assistant in the terminal; runs code, manages files, and browses the web with tool-use.

- **[Codebuff](https://github.com/CodebuffAI/codebuff)** `⭐ 4.2k` — Multi-agent AI coding assistant with CLI support for collaborative coding workflows.

- **[Devon](https://github.com/entropy-research/Devon)** `⭐ 3.5k` — Open-source pair programmer with a TUI; autonomous planning, execution, and debugging in Git workflows.

- **[Mistral Vibe](https://github.com/mistralai/mistral-vibe)** `⭐ 3.4k` `[Mistral]` — Mistral's CLI coding assistant for conversational repo interaction and edits. Apache-2.0.

- **[AutoCodeRover](https://github.com/AutoCodeRoverSG/auto-code-rover)** `⭐ 3.1k` — Autonomous program improvement agent; patches real GitHub issues using code search and analysis.

- **[Codel](https://github.com/semanser/codel)** `⭐ 2.4k` — Autonomous agent for performing complex tasks via terminal; runs in Docker with a web UI.

- **[Grok CLI](https://github.com/superagent-ai/grok-cli)** `⭐ 2.4k` — Community CLI agent built on xAI's Grok models for terminal-based coding tasks.

- **[CodeMachine-CLI](https://github.com/moazbuilds/CodeMachine-CLI)** `⭐ 2.4k` — Community multi-agent CLI aimed at running coding workflows locally (vibe-coding oriented).

- **[RA.Aid](https://github.com/ai-christianson/RA.Aid)** `⭐ 2.2k` — Autonomous coding agent built on LangGraph with research/plan/implement pipeline; optional aider integration for near-full autonomy.

- **[open-codex](https://github.com/ymichael/open-codex)** `⭐ 2.2k` — Lightweight fork of Codex CLI with multi-provider support (OpenAI, Gemini, OpenRouter, Ollama).

- **[Agentless](https://github.com/OpenAutoCoder/Agentless)** `⭐ 2.0k` — Lightweight approach to autonomous software engineering without persistent agent loops.

- **[Amazon Q Developer CLI](https://github.com/aws/amazon-q-developer-cli)** `⭐ 1.9k` `[AWS]` — AWS's agentic terminal chat for building apps, debugging, and DevOps with natural language. Apache-2.0.

- **[OH-MY-PI](https://github.com/can1357/oh-my-pi)** `⭐ 1.9k` — Terminal coding agent ("Pi") with a TypeScript/Rust monorepo and local-first ergonomics.

- **[Letta Code](https://github.com/letta-ai/letta-code)** `⭐ 1.8k` — Memory-first CLI coding agent built on the Letta platform (formerly MemGPT); persistent memory across sessions, model-agnostic (Claude/GPT/Gemini), skill learning, and context repositories.

- **[Neovate Code](https://github.com/neovateai/neovate-code)** `⭐ 1.5k` `[Ant Group]` — Ant Group's CLI agent with plugin system, multi-model/multi-provider support, MCP integrations, and headless automation mode. MIT.

- **[Groq Code CLI](https://github.com/build-with-groq/groq-code-cli)** `⭐ 710` — Customizable, lightweight CLI powered by Groq's ultra-fast inference; extensible tools/commands with multi-model support.

- **[Dexto](https://github.com/truffle-ai/dexto)** `⭐ 596` — Coding agent and general agent harness with CLI/web/API modes; ships a production-ready coding agent with sub-agent spawning.

- **[g3](https://github.com/dhanji/g3)** `⭐ 470` — "Coding AI agent" in Rust: tool-running, repo interaction, skills system, and provider abstraction.

- **[Mini-Kode](https://github.com/minmaxflow/mini-kode)** `⭐ 292` — An educational AI coding agent CLI, intended as a readable reference implementation.

- **[LettaBot](https://github.com/letta-ai/lettabot)** `⭐ 267` — Personal AI assistant with persistent unified memory across Telegram, Slack, Discord, WhatsApp, and Signal; built on the Letta platform.

- **[OpenHands CLI](https://github.com/OpenHands/OpenHands-CLI)** `⭐ 123` — CLI entrypoint for the OpenHands agent (ex-OpenDevin lineage), focused on autonomous repo tasks.

- **[cursor-agent](https://github.com/civai-technologies/cursor-agent)** `⭐ 112` — Python-based agent replicating Cursor's coding assistant capabilities; supports Claude, OpenAI, and local Ollama models.

- **[nori-cli](https://github.com/tilework-tech/nori-cli)** `⭐ 111` — Multi-provider CLI built on Codex CLI; switch between Claude, Gemini, and Codex from the same native terminal.

- **[QQCode](https://github.com/qnguyen3/qqcode)** `⭐ 49` — Lightweight CLI coding agent in Rust focused on speed, determinism, and developer control; supports skills.

- **[picocode](https://github.com/jondot/picocode)** `⭐ 37` — Minimal Rust-based coding agent focused on CI workflows and small codemods; multi-LLM with personas.

- **[Binharic](https://github.com/CogitatorTech/binharic-cli)** `⭐ 15` — A multi-provider "tech-priest persona" coding agent CLI (stylized, tool-using).

- **[CLAII](https://github.com/agencyswarm/CLAII)** — CLI-first AI coding agent with multi-agent orchestration, MCP toolchains, and memory-persistent refactors.

- **[2501 CLI](https://github.com/2501-ai/cli)** — AI-powered autonomous CLI agent for coding, debugging production issues, and DevOps automation.

- **[Coro Code](https://github.com/jokas3322/coro-code)** — High-performance Rust CLI coding agent with rich terminal UI.

- **[Every Code](https://github.com/yingpengzhang/ever-code)** — A community "Codex-inspired" CLI agent focusing on local, scriptable coding workflows.

### Closed Source

Proprietary agents — usable but not forkable or extensible at the source level.

- **[Claude Code](https://github.com/anthropics/claude-code)** `⭐ 78k` `[Anthropic]` — Anthropic's repo-aware terminal agent for code edits, refactors, and git workflows. Source-available, no OSS license.

- **[GitHub Copilot in the CLI](https://github.com/github/copilot-cli)** `⭐ 9.3k` `[GitHub]` — GitHub's agentic CLI for repo/PR/issue workflows, command suggestions, and headless automation.

- **[Amp](https://sourcegraph.com/amp)** `[Sourcegraph]` — Sourcegraph's AI coding agent with a CLI for implementing tasks across real codebases.

- **[Junie CLI](https://junie.jetbrains.com)** `[JetBrains]` — JetBrains' LLM-agnostic CLI coding agent (EAP); supports GPT-5, Claude, Gemini, Grok with plan mode and CI/CD headless usage.

- **[Cortex Code CLI](https://www.snowflake.com/en/product/cortex-code/)** `[Snowflake]` — Snowflake's data-native AI coding agent CLI for building pipelines, analytics, and AI apps with enterprise governance.

- **[Devin](https://devin.ai)** `[Cognition]` — Cognition's autonomous AI software engineer with full shell/browser access, self-healing code, and PR collaboration.

- **[Cursor CLI](https://cursor.com/cli)** `[Cursor]` — Cursor's official command-line agent (`agent`) with shell mode, headless/CI support, parallel agents, and multi-model access.

- **[Mentat CLI](https://mentat.ai/docs/cli)** `[Mentat]` — Cloud-native coding agent CLI for managing remote Mentat agents from your terminal; auto-detects repo/branch context.

- **[FetchCoder](https://github.com/fetchai/fetchcoder)** `[Fetch.ai]` — Terminal coding agent powered by ASI1, with interactive TUI, CLI, and API server modes plus MCP integration.

- **[Command Code](https://github.com/CommandCodeAI/command-code)** `[CommandCode]` — CLI coding agent that continuously learns your coding style via taste-1 neuro-symbolic AI; adapts to preferences over time with project-specific taste profiles.

---

## Harnesses & orchestration

### Session managers & parallel runners

Tools for running and managing multiple agent sessions side-by-side.

- **[Catnip](https://github.com/wandb/catnip)** — Containerized environment + worktree automation for running multiple coding agents in parallel (optimized for Claude Code).

- **[Claude Squad](https://github.com/smtg-ai/claude-squad)** — tmux-based harness to run and manage multiple Claude Code sessions side-by-side.

- **[Emdash](https://github.com/generalaction/emdash)** — Run multiple coding agents concurrently with coordinated workflows.

- **[Superset](https://github.com/superset-sh/superset)** — A terminal built for coding agents; orchestrates parallel agent sessions.

- **[Toad](https://github.com/batrachianai/toad)** — Agent orchestrator for running and managing parallel CLI coding sessions.

- **[amux](https://github.com/andyrewlee/amux)** — Terminal UI designed for running multiple coding agents in parallel.

- **[cmux](https://github.com/manaflow-ai/cmux)** — Open-source platform for running multiple coding agents in parallel.

- **[Crystal](https://github.com/stravu/crystal)** — Execute multiple Codex and Claude Code sessions in parallel git worktrees.

- **[mux](https://github.com/coder/mux)** — Desktop application for isolated, parallel agentic development.

- **[vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** — Execute Claude Code tasks in parallel git worktrees.

- **[Agent of Empires](https://github.com/GiladShapira/agent-of-empires)** — tmux-based multi-agent harness for parallel terminal agents and task routing.

- **[CLI Agent Orchestrator (CAO)](https://github.com/awslabs/cli-agent-orchestrator)** — AWS's hierarchical multi-agent orchestration via tmux with intelligent task delegation patterns.

- **[AgentPipe](https://agentpipe.ai)** — Open-source, self-hosted platform for running and monitoring real-time multi-agent conversations across CLI tools.

- **[multi-agent-workflow-kit](https://github.com/laris-co/multi-agent-workflow-kit)** — Orchestrate parallel AI agents in isolated git worktrees with shared tmux visibility.

- **[vibe-kanban](https://github.com/BloopAI/vibe-kanban)** — Kanban interface for administering AI coding agents.

- **[jean](https://github.com/coollabsio/jean)** — Administer multiple projects, worktrees, and sessions with Claude CLI.

- **[supacode](https://github.com/supabitapp/supacode)** — Native macOS coding agent orchestrator.

- **[CodexMonitor](https://github.com/Dimillian/CodexMonitor)** — Coordinate multiple Codex agents across local workspaces.

### Orchestrators & autonomous loops

Multi-agent coordination, swarm patterns, and autonomous execution loops.

- **[claude-flow](https://github.com/ruvnet/claude-flow)** — Deploy multi-agent swarms with coordinated workflows.

- **[gastown](https://github.com/steveyegge/gastown)** — Multi-agent orchestration with persistent work tracking.

- **[loom](https://github.com/ghuntley/loom)** — Infrastructure enabling autonomous loops to evolve products via multi-agent coordination.

- **[ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator)** — Hat-based system maintaining agents in a loop until task completion.

- **[ralph-tui](https://github.com/subsy/ralph-tui)** — Direct AI agents through task lists with autonomous execution.

- **[wreckit](https://github.com/mikehostetler/wreckit)** — Apply the Ralph Wiggum Loop pattern across your roadmap for autonomous agent execution.

### Agent infrastructure

Sandboxes, routers, browser/terminal automation, and extension tools.

- **[Agentic Engineering Framework](https://github.com/DimitriGeelen/agentic-engineering-framework)** — Provider-neutral governance framework for CLI coding agents. Structural enforcement of task-driven workflows, context budget management, antifragile healing loops, and audit compliance. Works with Claude Code, Aider, Cursor, and any file-based agent.

- **[AgentManager](https://github.com/kevinelliott/agentmanager)** — Lightweight CLI for managing multiple agent runs/sessions and workflows.

- **[AgentDeck](https://github.com/agentdeck/agentdeck)** — CLI-driven "deck" of agents with configs/presets for different tasks and repos.

- **[Claude Code Tools](https://github.com/pchalasani/claude-code-tools)** — Utilities around Claude Code workflows (automation helpers, helpers for common tasks).

- **[claude-cmd](https://github.com/kiliczsh/claude-cmd)** — Terminal wrapper for interacting with Claude models; often used as a building block in harness scripts.

- **[claude-code-router](https://github.com/search?q=claude-code-router)** — Route Claude Code calls to alternative providers/endpoints (useful for self-hosting proxies).

- **[claudebox](https://github.com/numtide/claudebox)** — Sandboxed environment for Claude Code (focused on isolation/safety).

- **[agent-browser](https://github.com/vercel-labs/agent-browser)** — Headless browser automation CLI for agents (useful as a tool plugin for coding agents).

- **[agent-terminal](https://github.com/jasonkneen/agent-terminal)** — Headless terminal automation for AI agents using node-pty; capture output and send input programmatically.

- **[subtask](https://github.com/zippoxer/subtask)** — Claude Skill for delegating tasks with subagents in Git worktrees.

- **[claude-northstar](https://github.com/Nisarg38/claude-northstar)** — Transforms CLI agents from task executors into autonomous project partners.

- **[open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork)** — Open-source version of Claude Cowork with 500+ SaaS app integrations.

- **[pi-builder](https://github.com/arosstale/pi-builder)** — TypeScript monorepo that wraps any installed CLI coding agent (Claude Code, Aider, OpenCode, Codex, Gemini CLI, Goose, Plandex, SWE-agent, Crush, gptme) behind a single interface; capability-based routing, health caching, fallback chains, SQLite persistence, and a streaming OrchestratorService. MIT.

---

## Contributing

PRs welcome! Please keep each entry:

1) **Name + link**
2) **1–2 line description** (what it does, who it's for)

Optional: add a "Why it's interesting" note (diffs, LSP, sandboxing, multi-agent, MCP/skills, etc).
