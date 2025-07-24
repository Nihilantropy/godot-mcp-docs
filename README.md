# Godot MCP Server

A Model Context Protocol (MCP) server that provides AI assistants with access to the latest Godot documentation, helping developers with Godot development by serving class documentation directly to LLMs.

## Purpose

This server bridges the gap between AI assistants and Godot documentation, allowing developers to get instant, accurate answers about Godot classes and their usage without leaving their AI chat interface.

## Deployment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nihilantropy/godot-mcp-docs.git
   cd godot-mcp-docs
   ```

2. **Build the Docker image:**
   ```bash
   docker build -f deploy/Dockerfile -t godot-mcp-docs:local .
   ```

3. **Configure your MCP client** (Claude Desktop example):
   ```json
   {
     "mcpServers": {
       "godot-mcp-docs": {
         "command": "docker",
         "args": [
           "run",
           "--rm",
           "-i",
           "godot-mcp-docs:local"
         ]
       }
     }
   }
   ```

## Documentation Structure

The server uses the official Godot documentation with this structure:

```
docs/
├── _styleguides
├── _tools
│   └── redirects
├── about
├── classes                    # ← Currently exposed
├── community
│   └── asset_library
├── contributing
│   ├── development
│   │   ├── compiling
│   │   ├── configuring_an_ide
│   │   ├── core_and_modules
│   │   ├── debugging
│   │   │   └── vulkan
│   │   ├── editor
│   │   └── file_formats
│   ├── documentation
│   └── workflow
├── getting_started
│   ├── first_2d_game
│   ├── first_3d_game
│   ├── introduction
│   └── step_by_step
├── img
└── tutorials
    ├── 2d
    ├── 3d
    │   ├── global_illumination
    │   ├── particles
    │   └── procedural_geometry
    ├── animation
    ├── assets_pipeline
    │   ├── escn_exporter
    │   └── importing_3d_scenes
    ├── audio
    ├── best_practices
    ├── editor
    ├── export
    ├── i18n
    ├── inputs
    ├── io
    ├── math
    ├── migrating
    ├── navigation
    ├── networking
    ├── performance
    │   └── vertex_animation
    ├── physics
    │   └── interpolation
    ├── platform
    │   ├── android
    │   ├── ios
    │   └── web
    ├── plugins
    │   └── editor
    ├── rendering
    ├── scripting
    │   ├── c_sharp
    │   │   └── diagnostics
    │   ├── cpp
    │   ├── debug
    │   ├── gdextension
    │   └── gdscript
    ├── shaders
    │   ├── shader_reference
    │   └── your_first_shader
    ├── ui
    └── xr
```

## Available Resources & Tools

### Resources
- `godot://classes/{class_name}` - Get specific class documentation

### Tools
- `list_all_classes()` - List all available Godot classes
- `retrieve_specific_class(class_name: str)` - Get full documentation for a specific class

## Sample Usage

**List available classes:**
```
What Godot classes are available for 2D physics?
```

**Get specific class documentation:**
```
Show me the documentation for CharacterBody2D
```

**Learn about a specific feature:**
```
How do I use RigidBody2D for physics simulation?
```

**Compare classes:**
```
What's the difference between Node2D and CharacterBody2D?
```