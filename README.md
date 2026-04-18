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

> **Last updated:** 2026-04-06

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

- **[OpenCode](https://github.com/anomalyco/opencode)** `⭐ 122k` — Terminal-native coding agent with 75+ provider support, LSP integration, and privacy-first design (formerly opencode-ai; now at opencode.ai).

- **[Claw Code](https://github.com/instructkr/claw-code)** `⭐ 110k` — Clean-room Python/Rust rewrite of Claude Code architecture using oh-my-codex; fastest repo in GitHub history to 100K stars. Born from the March 2026 Claude Code source leak. MIT.

- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** `⭐ 98k` `[Google]` — Google's terminal agent powered by Gemini, with tools for repo work and research. Apache-2.0.

- **[OpenHands](https://github.com/All-Hands-AI/OpenHands)** `⭐ 69.3k` — Open-source agentic developer environment (formerly OpenDevin) with CLI and web entrypoints; also has a lightweight [CLI-only package](https://github.com/OpenHands/OpenHands-CLI).

- **[Codex CLI](https://github.com/openai/codex)** `⭐ 66.1k` `[OpenAI]` — OpenAI's local coding agent for reading/editing/running code, with an interactive TUI and tool execution. Apache-2.0.

- **[Open Interpreter](https://github.com/OpenInterpreter/open-interpreter)** `⭐ 63k` — Terminal tool that can execute code and actions; often used as a "do things on my machine" agent.

- **[Cline CLI](https://github.com/cline/cline)** `⭐ 59k` — Model-agnostic autonomous agent for planning, file edits, command execution, and browser use.

- **[Aider](https://github.com/Aider-AI/aider)** `⭐ 42k` — Pair-programming agent for editing files via diffs/patches, with strong git and multi-file workflows.

- **[Goose](https://github.com/block/goose)** `⭐ 33k` — Local, extensible agent that can execute, edit, and test; designed to run on-device and integrate with MCP.

- **[Continue CLI](https://github.com/continuedev/continue)** `⭐ 32k` — Open-source terminal extension for multi-model coding with local/privacy focus.

- **[Pi](https://github.com/badlogic/pi-mono)** `⭐ 25.4k` — Minimal, adaptable terminal coding harness from the pi-mono toolkit; unified LLM API, TUI, skills, and MCP support.

- **[Roo Code CLI](https://github.com/RooCodeInc/Roo-Code)** `⭐ 22.7k` — Multi-mode CLI agent (architect/code/debug/orchestrator modes); Claude-like terminal interface with skills and checkpoints.

- **[Crush](https://github.com/charmbracelet/crush)** `⭐ 21.6k` — Charmbracelet's glamorous agentic coding TUI in Go; multi-provider, LSP-aware, with rich terminal UI.

- **[Qwen Code](https://github.com/QwenLM/qwen-code)** `⭐ 20k` `[Alibaba]` — Alibaba Qwen's official CLI agent for Qwen coder models (workflow tool + repo operations). Apache-2.0.

- **[SWE-agent](https://github.com/SWE-agent/SWE-agent)** `⭐ 18.8k` — Agent for resolving real repo issues/PR tasks; frequently used in SWE-bench-style workflows.

- **[Kilo Code CLI](https://github.com/Kilo-Org/kilocode)** `⭐ 16.9k` — Agentic engineering platform with CLI; orchestrator mode, 100s of LLMs, skills, and checkpointing.

- **[Plandex](https://github.com/plandex-ai/plandex)** `⭐ 15k` — "Plan-first" CLI agent for building features across multiple files with structured steps and 2M token context.

- **[Smol Developer](https://github.com/smol-ai/developer)** `⭐ 12k` — Embeddable developer agent that generates entire codebases from a prompt; designed to be embedded in apps.

- **[Claude Engineer](https://github.com/Doriandarko/claude-engineer)** `⭐ 11k` — Community-driven CLI for agentic Claude workflows with file management and iterative development.

- **[Trae Agent](https://github.com/bytedance/trae-agent)** `⭐ 11k` `[ByteDance]` — ByteDance's research-friendly CLI agent for software engineering tasks, with modular architecture and multi-LLM support. MIT.

- **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** `⭐ 8.7k` — Nous Research's self-improving CLI agent with persistent memory, automated skill creation, sandboxed code execution via Unix socket RPC, and multi-platform reach (Telegram/Slack/Discord/WhatsApp); supports 300+ models across multiple providers.

- **[Kimi CLI](https://github.com/MoonshotAI/kimi-cli)** `⭐ 7.1k` `[Moonshot AI]` — Moonshot AI's CLI coding agent with skills, MCP support, and ACP IDE integration. Apache-2.0.

- **[Claurst](https://github.com/Kuberwastaken/claurst)** `⭐ 6.1k` — Claude Code rewritten in idiomatic Rust with architectural breakdown; includes discoveries from the source leak (KAIROS persistent assistant, buddy system). MIT.

- **[ForgeCode](https://github.com/antinomyhq/forge)** `⭐ 5.0k` — AI pair programmer supporting 300+ models, with task management, custom agents, and large-scale refactor tooling.

- **[Kode CLI](https://github.com/shareAI-lab/Kode-cli)** `⭐ 4.6k` — ShareAI's open-source CLI agent for terminal-native coding with multi-provider support.

- **[gptme](https://github.com/gptme/gptme)** `⭐ 4.2k` — AI agent in your terminal with support for persistent autonomous agents. Runs code, edits files, browses the web. Build long-lived self-modifying agents with git-backed memory via [gptme-agent-template](https://github.com/gptme/gptme-agent-template).

- **[Codebuff](https://github.com/CodebuffAI/codebuff)** `⭐ 4.2k` — Multi-agent AI coding assistant with CLI support for collaborative coding workflows.

- **[Every Code](https://github.com/just-every/code)** `⭐ 3.6k` — Fork of Codex CLI with validation, automation, browser integration, multi-agents, theming, and multi-provider orchestration (OpenAI, Claude, Gemini). Apache-2.0.

- **[Devon](https://github.com/entropy-research/Devon)** `⭐ 3.5k` — Open-source pair programmer with a TUI; autonomous planning, execution, and debugging in Git workflows.

- **[Mistral Vibe](https://github.com/mistralai/mistral-vibe)** `⭐ 3.4k` `[Mistral]` — Mistral's CLI coding assistant for conversational repo interaction and edits. Apache-2.0.

- **[Free Code](https://github.com/paoloanzn/free-code)** `⭐ 3.3k` — Fork of Claude Code with all telemetry removed, guardrails stripped, and all experimental features enabled (KAIROS, dream mode, companion system).

- **[AutoCodeRover](https://github.com/AutoCodeRoverSG/auto-code-rover)** `⭐ 3.1k` — Autonomous program improvement agent; patches real GitHub issues using code search and analysis.

- **[Codel](https://github.com/semanser/codel)** `⭐ 2.4k` — Autonomous agent for performing complex tasks via terminal; runs in Docker with a web UI.

- **[Grok CLI](https://github.com/superagent-ai/grok-cli)** `⭐ 2.4k` — Community CLI agent built on xAI's Grok models for terminal-based coding tasks.

- **[CodeMachine-CLI](https://github.com/moazbuilds/CodeMachine-CLI)** `⭐ 2.4k` — Community multi-agent CLI aimed at running coding workflows locally (vibe-coding oriented).

- **[RA.Aid](https://github.com/ai-christianson/RA.Aid)** `⭐ 2.2k` — Autonomous coding agent built on LangGraph with research/plan/implement pipeline; optional aider integration for near-full autonomy.

- **[open-codex](https://github.com/ymichael/open-codex)** `⭐ 2.2k` — Lightweight fork of Codex CLI with multi-provider support (OpenAI, Gemini, OpenRouter, Ollama).

- **[Agentless](https://github.com/OpenAutoCoder/Agentless)** `⭐ 2.0k` — Lightweight approach to autonomous software engineering without persistent agent loops.

- **[Amazon Q Developer CLI](https://github.com/aws/amazon-q-developer-cli)** `⭐ 1.9k` `[AWS]` — AWS's agentic terminal chat for building apps, debugging, and DevOps with natural language. Apache-2.0.

- **[OH-MY-PI](https://github.com/can1357/oh-my-pi)** `⭐ 2.1k` — Terminal coding agent ("Pi") with a TypeScript/Rust monorepo and local-first ergonomics.

- **[Letta Code](https://github.com/letta-ai/letta-code)** `⭐ 1.9k` — Memory-first CLI coding agent built on the Letta platform (formerly MemGPT); persistent memory across sessions, model-agnostic (Claude/GPT/Gemini), skill learning, and context repositories.

- **[Neovate Code](https://github.com/neovateai/neovate-code)** `⭐ 1.5k` `[Ant Group]` — Ant Group's CLI agent with plugin system, multi-model/multi-provider support, MCP integrations, and headless automation mode. MIT.

- **[Groq Code CLI](https://github.com/build-with-groq/groq-code-cli)** `⭐ 710` — Customizable, lightweight CLI powered by Groq's ultra-fast inference; extensible tools/commands with multi-model support.

- **[Dexto](https://github.com/truffle-ai/dexto)** `⭐ 596` — Coding agent and general agent harness with CLI/web/API modes; ships a production-ready coding agent with sub-agent spawning.

- **[g3](https://github.com/dhanji/g3)** `⭐ 477` — "Coding AI agent" in Rust: tool-running, repo interaction, skills system, and provider abstraction.

- **[Coro Code](https://github.com/Blushyes/coro-code)** `⭐ 350` — Open-source CLI coding agent, a free alternative to Claude Code; generate, debug, and manage code seamlessly.

- **[Mini-Kode](https://github.com/minmaxflow/mini-kode)** `⭐ 292` — An educational AI coding agent CLI, intended as a readable reference implementation.

- **[LettaBot](https://github.com/letta-ai/lettabot)** `⭐ 267` — Personal AI assistant with persistent unified memory across Telegram, Slack, Discord, WhatsApp, and Signal; built on the Letta platform.

- **[cursor-agent](https://github.com/civai-technologies/cursor-agent)** `⭐ 112` — Python-based agent replicating Cursor's coding assistant capabilities; supports Claude, OpenAI, and local Ollama models.

- **[nori-cli](https://github.com/tilework-tech/nori-cli)** `⭐ 113` — Multi-provider CLI built on Codex CLI; switch between Claude, Gemini, and Codex from the same native terminal.

- **[QQCode](https://github.com/qnguyen3/qqcode)** `⭐ 49` — Lightweight CLI coding agent in Rust focused on speed, determinism, and developer control; supports skills.

- **[picocode](https://github.com/jondot/picocode)** `⭐ 38` — Minimal Rust-based coding agent focused on CI workflows and small codemods; multi-LLM with personas.

- **[VibePod](https://github.com/VibePod/vibepod-cli)** `⭐ 28` — Unified CLI for running AI coding agents in isolated Docker containers; zero-config setup, local metrics, HTTP traffic tracking, and an analytics dashboard for side-by-side comparison.

- **[Binharic](https://github.com/CogitatorTech/binharic-cli)** `⭐ 15` — A multi-provider "tech-priest persona" coding agent CLI (stylized, tool-using).

- **[CLAII](https://github.com/agencyswarm/CLAII)** — CLI-first AI coding agent with multi-agent orchestration, MCP toolchains, and memory-persistent refactors.

### OpenClaw ecosystem

Projects built on, forked from, or inspired by [OpenClaw](https://github.com/openclaw/openclaw) — the open-source personal AI assistant. Sorted by GitHub stars.

- **[OpenClaw](https://github.com/openclaw/openclaw)** `⭐ 322k` — The original personal AI assistant you run locally; CLI with onboarding wizard, skills, tools, and multi-channel support (WhatsApp/Slack/Discord). MIT.

- **[nanobot](https://github.com/HKUDS/nanobot)** `⭐ 34.6k` — Ultra-lightweight ~4,000-line Python rewrite of OpenClaw; tool use, persistent memory, scheduled tasks, and multi-channel support (Telegram/Discord/WhatsApp). MIT.

- **[ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)** `⭐ 27.8k` — Fully autonomous AI agent runtime in Rust; trait-driven pluggable architecture (providers, tools, memory, channels), runs on minimal hardware (<5MB RAM), multi-channel CLI/Telegram/Discord/Slack, with sandboxed execution and hybrid vector+keyword search.

- **[PicoClaw](https://github.com/sipeed/picoclaw)** `⭐ 25.3k` — Ultra-lightweight personal AI assistant in Go inspired by OpenClaw; runs on $10 hardware with less than 10MB RAM.

- **[NanoClaw](https://github.com/gavrielc/nanoclaw)** `⭐ 24.0k` — Security-first lightweight alternative to OpenClaw; runs agents in Apple containers/Docker with sandboxed execution, built on Anthropic's Agents SDK.

- **[IronClaw](https://github.com/nearai/ironclaw)** `⭐ 10.4k` — OpenClaw rewritten in Rust by NEAR AI; WASM sandbox isolation, capability-based permissions, and prompt injection defense.

- **[NullClaw](https://github.com/nullclaw/nullclaw)** `⭐ 6.5k` — Fastest, smallest OpenClaw-compatible agent in Zig; 678KB static binary, ~1MB RAM, <2ms startup, 23+ providers, 18 channels. MIT.

- **[Moltis](https://github.com/moltis-org/moltis)** `⭐ 2.3k` — Secure, auditable Rust-native alternative to OpenClaw; zero unsafe code, 2,300+ tests, built-in voice I/O, MCP servers, and multi-channel access. MIT.

- **[Clawith](https://github.com/dataelement/Clawith)** `⭐ 1.6k` — "OpenClaw for Teams" — multi-agent collaboration platform that scales OpenClaw to organizations. Apache-2.0.

- **[GitClaw](https://github.com/open-gitagent/gitclaw)** `⭐ 149` — Git-native AI agent framework where agent identity, rules, memory, tools, and skills are all version-controlled files. MIT.

### Closed Source

Proprietary agents — usable but not forkable or extensible at the source level.

- **[Claude Code](https://github.com/anthropics/claude-code)** `⭐ 79.5k` `[Anthropic]` — Anthropic's repo-aware terminal agent for code edits, refactors, and git workflows. Source-available, no OSS license.

- **[Warp](https://github.com/warpdotdev/Warp)** `⭐ 26.2k` `[Warp]` — Modern terminal with built-in AI agent mode; understands tasks, runs commands, edits files, and orchestrates multi-step workflows.

- **[GitHub Copilot in the CLI](https://github.com/github/copilot-cli)** `⭐ 9.4k` `[GitHub]` — GitHub's agentic CLI for repo/PR/issue workflows, command suggestions, and headless automation.

- **[Droid](https://github.com/Factory-AI/factory)** `⭐ 624` `[Factory]` — Factory's multi-model CLI coding agent; #1 on Terminal-Bench, specialized droids for different tasks, headless CI mode, and multi-interface support (CLI/IDE/Slack/Linear).

- **[Amp](https://sourcegraph.com/amp)** `[Sourcegraph]` — Sourcegraph's AI coding agent with a CLI for implementing tasks across real codebases.

- **[Junie CLI](https://junie.jetbrains.com)** `[JetBrains]` — JetBrains' LLM-agnostic CLI coding agent (EAP); supports GPT-5, Claude, Gemini, Grok with plan mode and CI/CD headless usage.

- **[Cortex Code CLI](https://www.snowflake.com/en/product/cortex-code/)** `[Snowflake]` — Snowflake's data-native AI coding agent CLI for building pipelines, analytics, and AI apps with enterprise governance.

- **[Devin](https://devin.ai)** `[Cognition]` — Cognition's autonomous AI software engineer with full shell/browser access, self-healing code, and PR collaboration.

- **[Cursor CLI](https://cursor.com/cli)** `[Cursor]` — Cursor's official command-line agent (`agent`) with shell mode, headless/CI support, parallel agents, and multi-model access.

- **[Tabnine CLI](https://docs.tabnine.com/main/getting-started/tabnine-cli)** `[Tabnine]` — AI-powered terminal coding assistant with agentic workflows; distributed as a Docker container, requires enterprise license.

- **[Mentat CLI](https://mentat.ai/docs/cli)** `[Mentat]` — Cloud-native coding agent CLI for managing remote Mentat agents from your terminal; auto-detects repo/branch context.

- **[FetchCoder](https://github.com/fetchai/fetchcoder-releases)** `[Fetch.ai]` — Terminal coding agent powered by ASI1, with interactive TUI, CLI, and API server modes plus MCP integration.

- **[Command Code](https://github.com/CommandCodeAI/command-code)** `[CommandCode]` — CLI coding agent that continuously learns your coding style via taste-1 neuro-symbolic AI; adapts to preferences over time with project-specific taste profiles.

---

## Harnesses & orchestration

### Session managers & parallel runners

Tools for running and managing multiple agent sessions side-by-side. Sorted by GitHub stars.

- **[vibe-kanban](https://github.com/BloopAI/vibe-kanban)** `⭐ 23.4k` — Kanban interface for administering AI coding agents.

- **[cmux](https://github.com/manaflow-ai/cmux)** `⭐ 8.1k` — Open-source platform for running multiple coding agents in parallel.

- **[Superset](https://github.com/superset-sh/superset)** `⭐ 7.4k` — A terminal built for coding agents; orchestrates parallel agent sessions.

- **[Claude Squad](https://github.com/smtg-ai/claude-squad)** `⭐ 6.4k` — tmux-based harness to run and manage multiple Claude Code sessions side-by-side.

- **[CodexMonitor](https://github.com/Dimillian/CodexMonitor)** `⭐ 3.2k` — Coordinate multiple Codex agents across local workspaces.

- **[Crystal](https://github.com/stravu/crystal)** `⭐ 3.0k` — Execute multiple Codex and Claude Code sessions in parallel git worktrees.

- **[Toad](https://github.com/batrachianai/toad)** `⭐ 2.7k` — Agent orchestrator for running and managing parallel CLI coding sessions.

- **[Emdash](https://github.com/generalaction/emdash)** `⭐ 2.7k` — Run multiple coding agents concurrently with coordinated workflows.

- **[mux](https://github.com/coder/mux)** `⭐ 1.4k` — Desktop application for isolated, parallel agentic development.

- **[jean](https://github.com/coollabsio/jean)** `⭐ 658` — Administer multiple projects, worktrees, and sessions with Claude CLI.

- **[supacode](https://github.com/supabitapp/supacode)** `⭐ 511` — Native macOS coding agent orchestrator.

- **[Catnip](https://github.com/wandb/catnip)** `⭐ 467` — Containerized environment + worktree automation for running multiple coding agents in parallel (optimized for Claude Code).

- **[Parallel Code](https://github.com/johannesjo/parallel-code)** `⭐ 385` — Desktop app for running multiple AI coding agents (Claude Code, Codex CLI, Gemini CLI) simultaneously in isolated git worktrees.

- **[CLI Agent Orchestrator (CAO)](https://github.com/awslabs/cli-agent-orchestrator)** `⭐ 330` — AWS's hierarchical multi-agent orchestration via tmux with intelligent task delegation patterns.

- **[vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** `⭐ 244` — Execute Claude Code tasks in parallel git worktrees.

- **[AgentPipe](https://github.com/kevinelliott/agentpipe)** `⭐ 98` — CLI/TUI app that orchestrates multi-agent conversations by enabling different AI CLI tools (Claude Code, Gemini, Qwen, etc.) to communicate in shared rooms. MIT.

- **[amux](https://github.com/mixpeek/amux)** `⭐ 118` — Agent multiplexer for running dozens of parallel Claude Code sessions with web dashboard, self-healing watchdog, kanban board, agent-to-agent REST API, and mobile PWA. Single Python file, Python 3 + tmux. MIT.

- **[amux](https://github.com/andyrewlee/amux)** `⭐ 56` — Terminal UI designed for running multiple coding agents in parallel.

- **[CliDeck](https://github.com/rustykuntz/clideck)** `⭐ 35` — WhatsApp-like browser dashboard for managing multiple CLI coding agents (Claude Code, Codex, Gemini CLI, OpenCode) with live status detection, session resume, autopilot routing, and full control from a phone while away. MIT.

- **[multi-agent-workflow-kit](https://github.com/laris-co/multi-agent-workflow-kit)** `⭐ 9` — Orchestrate parallel AI agents in isolated git worktrees with shared tmux visibility.

- **[PATAPIM](https://patapim.ai)** — Terminal IDE with a 9-terminal grid for running multiple CLI coding agents simultaneously; features AI state detection, built-in Whisper voice dictation, LAN remote access, and an embedded MCP browser. Built with Electron and node-pty. Freemium.

### Orchestrators & autonomous loops

Multi-agent coordination, swarm patterns, and autonomous execution loops. Sorted by GitHub stars.

- **[claude-flow](https://github.com/ruvnet/claude-flow)** `⭐ 21.6k` — Deploy multi-agent swarms with coordinated workflows.

- **[gastown](https://github.com/steveyegge/gastown)** `⭐ 12.5k` — Multi-agent orchestration with persistent work tracking.

- **[ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator)** `⭐ 2.2k` — Hat-based system maintaining agents in a loop until task completion.

- **[ralph-tui](https://github.com/subsy/ralph-tui)** `⭐ 2.1k` — Direct AI agents through task lists with autonomous execution.

- **[AgentsMesh](https://github.com/AgentsMesh/AgentsMesh)** `⭐ 1.5k` — AI Agent Workforce Platform: remote AI workstations (AgentPods) with PTY sandbox + git worktree isolation, multi-agent collaboration via channels and pod bindings, built-in Kanban with MR/PR integration. Self-hosted with BYOK. Supports Claude Code, Codex CLI, Gemini CLI, Aider, OpenCode. BSL-1.1.

- **[loom](https://github.com/ghuntley/loom)** `⭐ 1.2k` — Infrastructure enabling autonomous loops to evolve products via multi-agent coordination.

- **[wreckit](https://github.com/mikehostetler/wreckit)** `⭐ 121` — Apply the Ralph Wiggum Loop pattern across your roadmap for autonomous agent execution.

- **[kodo](https://github.com/ikamensh/kodo)** `⭐ 37` — Autonomous multi-agent coding orchestrator that directs Claude Code, Codex, and Gemini CLI through work cycles with independent architect and tester verification. SWE-bench verified.

- **[OpenCastle](https://github.com/monkilabs/opencastle)** `⭐ 18` — Multi-agent orchestration framework that turns AI coding assistants (Copilot, Cursor, Claude Code, OpenCode, Windsurf, Codex CLI) into 19 coordinated specialist agents. CLI-driven (`npx opencastle init`), with task decomposition, parallel work, and quality gates. MIT.

- **[agx](https://github.com/ramarlina/agx)** `⭐ 15` — Checkpoint-based execution engine for AI coding agents; durable Wake→Work→Sleep loops that resume instantly across sessions. Supports Claude Code, Codex CLI, Gemini CLI, and Ollama. CLI + web dashboard + macOS app.

- **[Bernstein](https://github.com/chernistry/bernstein)** — Deterministic Python orchestrator — spawns parallel AI coding agents (Claude Code, Codex CLI, Gemini CLI), verifies with tests, auto-commits.

- **[ORCH](https://github.com/oxgeneral/ORCH)** `⭐ 9` — CLI orchestrator that manages Claude Code, Codex, and Cursor as a typed task queue with state machine (todo→in_progress→review→done), auto-retry, inter-agent messaging, and TUI dashboard.

- **[Forge](https://github.com/LucasDuys/forge)** `⭐ 4` — Autonomous spec-driven development loop for Claude Code; three-command pipeline (brainstorm specs, plan task DAGs, execute autonomously) with context survival, backpropagation that traces bugs to spec gaps, and Claude-on-Claude code review. MIT.

### Agent infrastructure

Sandboxes, routers, browser/terminal automation, and extension tools. Sorted by GitHub stars.

- **[claude-code-router](https://github.com/musistudio/claude-code-router)** `⭐ 29.9k` — Use Claude Code as a foundation while routing to alternative providers/endpoints.

- **[agent-browser](https://github.com/vercel-labs/agent-browser)** `⭐ 23.3k` — Headless browser automation CLI for agents (useful as a tool plugin for coding agents).

- **[OpenWork](https://github.com/different-ai/openwork)** `⭐ 13.0k` — Open-source alternative to Claude Cowork for teams; local-first desktop app powered by OpenCode with one-click setup. MIT.

- **[NemoClaw](https://github.com/NVIDIA/NemoClaw)** `⭐ 8.0k` `[NVIDIA]` — CLI tool for securely provisioning and managing sandboxed OpenClaw agent environments; enforces network, filesystem, and process-level security policies via OpenShell runtime. Apache-2.0.

- **[open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork)** `⭐ 3.2k` — Open-source version of Claude Cowork with 500+ SaaS app integrations.

- **[Claude Code Tools](https://github.com/pchalasani/claude-code-tools)** `⭐ 1.6k` — Utilities around Claude Code workflows (automation helpers, helpers for common tasks).

- **[OneCLI](https://github.com/onecli/onecli)** `⭐ 809` — Open-source credential vault for AI agents; Rust HTTP gateway injects API keys transparently so agents never handle raw secrets. Per-agent scoped tokens, AES-256-GCM encryption at rest. Apache-2.0.

- **[subtask](https://github.com/zippoxer/subtask)** `⭐ 320` — Claude Skill for delegating tasks with subagents in Git worktrees.

- **[claude-cmd](https://github.com/kiliczsh/claude-cmd)** `⭐ 294` — Terminal wrapper for interacting with Claude models; often used as a building block in harness scripts.

- **[Coasts](https://github.com/coast-guard/coasts)** `⭐ 59` — Containerized host orchestration for git worktrees; isolates ports, networks, and services per environment using DinD/Sysbox/Podman. MIT.

- **[claudebox](https://github.com/numtide/claudebox)** `⭐ 36` — Sandboxed environment for Claude Code (focused on isolation/safety).

- **[skill-optimizer](https://github.com/fastxyz/skill-optimizer)** `⭐ 25` — CLI tool that benchmarks SDK, CLI, and MCP guidance docs (SKILL.md) across multiple LLMs using static action + argument matching. Iteratively rewrites docs until every configured model meets a PASS/FAIL score floor. MIT.

- **[AgentManager](https://github.com/kevinelliott/agentmanager)** `⭐ 17` — Lightweight CLI for managing multiple agent runs/sessions and workflows.

- **[brood-box](https://github.com/stacklok/brood-box)** `⭐ 11` — Hardware-isolated microVM sandbox for AI coding agents (Claude Code, Codex, OpenCode) with COW snapshot isolation, egress control, and MCP authorization.

- **[agent-terminal](https://github.com/jasonkneen/agent-terminal)** `⭐ 10` — Headless terminal automation for AI agents using node-pty; capture output and send input programmatically.

- **[gate4agent](https://github.com/ZENG3LD/gate4agent)** `[ZENG3LD]` — Universal Rust transport library for CLI AI agents (Claude Code, Codex, Gemini, OpenCode). Pipe/NDJSON, PTY, and ACP (JSON-RPC 2.0) modes with tokio broadcast fan-out. MIT.

- **[Untether](https://github.com/littlebearapps/untether)** `⭐ 8` — Telegram bridge for 6 CLI coding agents (Claude Code, Codex, OpenCode, Pi, Gemini CLI, Amp); remote task control via voice or text, progress streaming, interactive permissions, and cost tracking. MIT.

- **[pi-builder](https://github.com/arosstale/pi-builder)** `⭐ 5` — TypeScript monorepo that wraps any installed CLI coding agent (Claude Code, Aider, OpenCode, Codex, Gemini CLI, Goose, Plandex, SWE-agent, Crush, gptme) behind a single interface; capability-based routing, health caching, fallback chains, SQLite persistence, and a streaming OrchestratorService. MIT.

- **[zosma-qa](https://github.com/zosmaai/zosma-qa)** `⭐ 5` — Generates QA agent prompts (planner, generator, healer, analyzer) for CLI coding tools (OpenCode, Claude Code, VS Code Copilot); scaffolds autonomous test workflows across Playwright, Appium, and k6.

- **[Wit](https://github.com/amaar-mc/wit)** `⭐ 4` — Coordination protocol that prevents merge conflicts between parallel AI agents. Locks specific functions (not files) via Tree-sitter AST parsing; agents declare intents, acquire symbol-level locks, and get conflict warnings before writing code. JSON-RPC daemon. MIT.

- **[OSOP](https://github.com/Archie0125/osop-agent-rules)** `⭐ 0` — Universal workflow logging protocol for CLI coding agents; produces `.osop` workflow definitions and `.osoplog.yaml` execution records. Supports Claude Code, Codex, Cursor, Windsurf, Aider, Cline, Roo Code, Devin, and OpenClaw. Includes a [visual editor](https://osop-editor.vercel.app) and [spec](https://github.com/Archie0125/osop-spec).

- **[Agentic Engineering Framework](https://github.com/DimitriGeelen/agentic-engineering-framework)** — Provider-neutral governance framework for CLI coding agents. Structural enforcement of task-driven workflows, context budget management, antifragile healing loops, and audit compliance. Works with Claude Code, Aider, Cursor, and any file-based agent.

- **[claude-northstar](https://github.com/Nisarg38/claude-northstar)** — Transforms CLI agents from task executors into autonomous project partners.

- **[kasetto](https://github.com/pivoshenko/kasetto)** — A declarative AI agent environment manager, written in Rust.

- **[toprank](https://github.com/nowork-studio/toprank)** — Claude Code plugin with 9 SEO and Google Ads skills. Connects Google Search Console, PageSpeed Insights, and the Google Ads API, then ships fixes (meta tags, JSON-LD schema, keyword bids) directly to source code or CMS. Open-source, MIT.

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
