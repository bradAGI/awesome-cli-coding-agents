# Awesome CLI Coding Agents

<p align="center">
  <img src="banner.png" alt="Awesome CLI Coding Agents" width="100%" />
</p>

A terminal-first directory of **AI coding agents** (tools that can read/edit repos and run commands) plus the **harnesses** that orchestrate, sandbox, or extend them.

---

## Contents

- [Terminal-native coding agents](#terminal-native-coding-agents)
  - [Open Source agents](#open-source-agents)
  - [Platform agents](#platform-agents)

- [Harnesses & orchestration](#harnesses--orchestration)
  - [Session managers & parallel runners](#session-managers--parallel-runners)
  - [Orchestrators & autonomous loops](#orchestrators--autonomous-loops)
  - [Agent infrastructure](#agent-infrastructure)

- [Contributing](#contributing)

---

## Terminal-native coding agents

### Open Source agents

Standalone open-source projects with active communities.

- **[Pi](https://github.com/badlogic/pi-mono)** — Minimal, adaptable terminal coding harness from the pi-mono toolkit; unified LLM API, TUI, skills, and MCP support.

- **[OpenCode](https://github.com/anomalyco/opencode)** — Terminal-native coding agent with 75+ provider support, LSP integration, and privacy-first design (formerly opencode-ai; now at opencode.ai).

- **[Aider](https://github.com/Aider-AI/aider)** — Pair-programming agent for editing files via diffs/patches, with strong git and multi-file workflows.

- **[Goose](https://github.com/block/goose)** — Local, extensible agent that can execute, edit, and test; designed to run on-device and integrate with MCP.

- **[Plandex](https://github.com/plandex-ai/plandex)** — "Plan-first" CLI agent for building features across multiple files with structured steps and 2M token context.

- **[Cline CLI](https://github.com/cline/cline)** — Model-agnostic autonomous agent for planning, file edits, command execution, and browser use.

- **[Roo Code CLI](https://github.com/RooCodeInc/Roo-Code)** — Multi-mode CLI agent (architect/code/debug/orchestrator modes); 22k+ stars, Claude-like terminal interface with skills and checkpoints.

- **[Kilo Code CLI](https://github.com/Kilo-Org/kilocode)** — Agentic engineering platform with CLI; orchestrator mode, 100s of LLMs, skills, and checkpointing (15k+ stars).

- **[ForgeCode](https://github.com/antinomyhq/forge)** — AI pair programmer supporting 300+ models, with task management, custom agents, and large-scale refactor tooling.

- **[OpenHands CLI](https://github.com/OpenHands/OpenHands-CLI)** — CLI entrypoint for the OpenHands agent (ex-OpenDevin lineage), focused on autonomous repo tasks.

- **[Continue CLI](https://github.com/continuedev/continue)** — Open-source terminal extension for multi-model coding with local/privacy focus.

- **[SWE-agent](https://github.com/SWE-agent/SWE-agent)** — Agent for resolving real repo issues/PR tasks; frequently used in SWE-bench-style workflows.

- **[AutoCodeRover](https://github.com/AutoCodeRoverSG/auto-code-rover)** — Autonomous program improvement agent; patches real GitHub issues using code search and analysis.

- **[Agentless](https://github.com/OpenAutoCoder/Agentless)** — Lightweight approach to autonomous software engineering without persistent agent loops.

- **[RA.Aid](https://github.com/ai-christianson/RA.Aid)** — Autonomous coding agent built on LangGraph with research/plan/implement pipeline; optional aider integration for near-full autonomy.

- **[Devon](https://github.com/entropy-research/Devon)** — Open-source pair programmer with a TUI; autonomous planning, execution, and debugging in Git workflows.

- **[Open Interpreter](https://github.com/OpenInterpreter/open-interpreter)** — Terminal tool that can execute code and actions; often used as a "do things on my machine" agent.

- **[Claude Engineer](https://github.com/Doriandarko/claude-engineer)** — Community-driven CLI for agentic Claude workflows with file management and iterative development.

- **[Crush](https://github.com/charmbracelet/crush)** — Charmbracelet's glamorous agentic coding TUI in Go; multi-provider, LSP-aware, with rich terminal UI.

- **[gptme](https://github.com/gptme/gptme)** — Personal AI assistant in the terminal; runs code, manages files, and browses the web with tool-use.

- **[g3](https://github.com/dhanji/g3)** — "Coding AI agent" in Rust: tool-running, repo interaction, skills system, and provider abstraction.

- **[Kode CLI](https://github.com/shareAI-lab/Kode-cli)** — ShareAI's open-source CLI agent for terminal-native coding with multi-provider support.

- **[OpenClaw](https://github.com/openclaw/openclaw)** — Personal AI assistant you run locally (170k+ stars); CLI with onboarding wizard, skills, tools, and multi-channel support (WhatsApp/Slack/Discord).

- **[NanoClaw](https://github.com/gavrielc/nanoclaw)** — Security-first lightweight alternative to OpenClaw; runs agents in Apple containers/Docker with sandboxed execution, built on Anthropic's Agents SDK.

- **[PicoClaw](https://github.com/sipeed/picoclaw)** — Ultra-lightweight personal AI assistant in Go inspired by OpenClaw; runs on $10 hardware with less than 10MB RAM.

- **[IronClaw](https://github.com/nearai/ironclaw)** — OpenClaw rewritten in Rust by NEAR AI; WASM sandbox isolation, capability-based permissions, and prompt injection defense.

- **[LettaBot](https://github.com/letta-ai/lettabot)** — Personal AI assistant with persistent unified memory across Telegram, Slack, Discord, WhatsApp, and Signal; built on the Letta platform.

- **[Dexto](https://github.com/truffle-ai/dexto)** — Coding agent and general agent harness with CLI/web/API modes; ships a production-ready coding agent with sub-agent spawning.

- **[2501 CLI](https://github.com/2501-ai/cli)** — AI-powered autonomous CLI agent for coding, debugging production issues, and DevOps automation.

- **[OH-MY-PI](https://github.com/can1357/oh-my-pi)** — Terminal coding agent ("Pi") with a TypeScript/Rust monorepo and local-first ergonomics.

- **[Groq Code CLI](https://github.com/build-with-groq/groq-code-cli)** — Customizable, lightweight CLI powered by Groq's ultra-fast inference; extensible tools/commands with multi-model support.

- **[QQCode](https://github.com/qnguyen3/qqcode)** — Lightweight CLI coding agent in Rust focused on speed, determinism, and developer control; supports skills.

- **[Coro Code](https://github.com/jokas3322/coro-code)** — High-performance Rust CLI coding agent with rich terminal UI.

- **[Codebuff](https://github.com/CodebuffAI/codebuff)** — Multi-agent AI coding assistant with CLI support for collaborative coding workflows.

- **[Codel](https://github.com/semanser/codel)** — Autonomous agent for performing complex tasks via terminal; runs in Docker with a web UI.

- **[cursor-agent](https://github.com/civai-technologies/cursor-agent)** — Python-based agent replicating Cursor's coding assistant capabilities; supports Claude, OpenAI, and local Ollama models.

- **[Grok CLI](https://github.com/superagent-ai/grok-cli)** — Community CLI agent built on xAI's Grok models for terminal-based coding tasks.

- **[Every Code](https://github.com/yingpengzhang/ever-code)** — A community "Codex-inspired" CLI agent focusing on local, scriptable coding workflows.

- **[Mini-Kode](https://github.com/minmaxflow/mini-kode)** — An educational AI coding agent CLI, intended as a readable reference implementation.

- **[CodeMachine-CLI](https://github.com/moazbuilds/CodeMachine-CLI)** — Community multi-agent CLI aimed at running coding workflows locally (vibe-coding oriented).

- **[CLAII](https://github.com/agencyswarm/CLAII)** — CLI-first AI coding agent with multi-agent orchestration, MCP toolchains, and memory-persistent refactors.

- **[picocode](https://github.com/jondot/picocode)** — Minimal Rust-based coding agent focused on CI workflows and small codemods; multi-LLM with personas.

- **[Binharic](https://github.com/CogitatorTech/binharic-cli)** — A multi-provider "tech-priest persona" coding agent CLI (stylized, tool-using).

- **[Smol Developer](https://github.com/smol-ai/developer)** — Embeddable developer agent (12k+ stars) that generates entire codebases from a prompt; designed to be embedded in apps.

- **[nori-cli](https://github.com/tilework-tech/nori-cli)** — Multi-provider CLI built on Codex CLI; switch between Claude, Gemini, and Codex from the same native terminal.

- **[open-codex](https://github.com/ymichael/open-codex)** — Lightweight fork of Codex CLI with multi-provider support (OpenAI, Gemini, OpenRouter, Ollama).

- **[OpenDevin](https://github.com/OpenDevin/OpenDevin)** — Open-source agentic developer environment (not purely CLI, but often run locally with terminal entrypoints).

- **[Letta Code](https://github.com/letta-ai/letta-code)** — Memory-first CLI coding agent built on the Letta platform (formerly MemGPT); persistent memory across sessions, model-agnostic (Claude/GPT/Gemini), skill learning, and context repositories.

### Platform agents

First-party CLI agents from major AI model providers and dev-tool companies.

- **[Claude Code](https://github.com/anthropics/claude-code)** — Anthropic's repo-aware terminal agent for code edits, refactors, and git workflows.

- **[Codex CLI](https://github.com/openai/codex)** — OpenAI's local coding agent for reading/editing/running code, with an interactive TUI and tool execution.

- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** — Google's open-source terminal agent powered by Gemini, with tools for repo work and research.

- **[Amazon Q Developer CLI](https://github.com/aws/amazon-q-developer-cli)** — AWS's agentic terminal chat for building apps, debugging, and DevOps with natural language.

- **[Qwen Code](https://github.com/QwenLM/qwen-code)** — Alibaba Qwen's official CLI agent for Qwen coder models (workflow tool + repo operations).

- **[Kimi CLI](https://github.com/MoonshotAI/kimi-cli)** — Moonshot AI's open-source CLI coding agent with skills, MCP support, and ACP IDE integration.

- **[Mistral Vibe](https://github.com/mistralai/mistral-vibe)** — Mistral's open-source CLI coding assistant for conversational repo interaction and edits.

- **[Trae Agent](https://github.com/bytedance/trae-agent)** — ByteDance's research-friendly CLI agent for software engineering tasks, with modular architecture and multi-LLM support.

- **[Neovate Code](https://github.com/neovateai/neovate-code)** — Ant Group's open-source CLI agent with plugin system, multi-model/multi-provider support, MCP integrations, and headless automation mode.

- **[FetchCoder](https://github.com/fetchai/fetchcoder)** — Terminal coding agent powered by ASI1, with interactive TUI, CLI, and API server modes plus MCP integration.

- **[Amp](https://sourcegraph.com/amp)** — Sourcegraph's AI coding agent with a CLI for implementing tasks across real codebases.

- **[Junie CLI](https://junie.jetbrains.com)** — JetBrains' LLM-agnostic CLI coding agent (EAP); supports GPT-5, Claude, Gemini, Grok with plan mode and CI/CD headless usage.

- **[Cortex Code CLI](https://www.snowflake.com/en/product/cortex-code/)** — Snowflake's data-native AI coding agent CLI for building pipelines, analytics, and AI apps with enterprise governance.

- **[Devin](https://devin.ai)** — Cognition's autonomous AI software engineer with full shell/browser access, self-healing code, and PR collaboration.

- **[GitHub Copilot in the CLI](https://github.com/github/copilot-cli)** — GitHub's agentic CLI for repo/PR/issue workflows, command suggestions, and headless automation.

- **[Cursor CLI](https://cursor.com/cli)** — Cursor's official command-line agent (`agent`) with shell mode, headless/CI support, parallel agents, and multi-model access.

- **[Mentat CLI](https://mentat.ai/docs/cli)** — Cloud-native coding agent CLI for managing remote Mentat agents from your terminal; auto-detects repo/branch context.

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
