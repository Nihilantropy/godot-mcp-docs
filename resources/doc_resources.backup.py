"""
Godot MCP Server - Documentation Resources
Resource handlers for serving Godot documentation files
"""

from pathlib import Path
from server import mcp, validate_doc_path

# Root level directories
@mcp.resource("godot://about/{topic}")
def get_about_documentation(topic: str) -> str:
    """Get Godot about documentation"""
    try:
        doc_path = validate_doc_path(f"about/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"About documentation not found: {topic}. Use list_about() tool to see available docs."
    except Exception as e:
        return f"Error accessing about documentation: {str(e)}"

@mcp.resource("godot://classes/{class_name}")
def get_class_documentation(class_name: str) -> str:
    """Get Godot class documentation"""
    try:
        # Handle both clean names (CharacterBody2D) and filename formats (class_characterbody2d)
        if not class_name.startswith('class_'):
            # Try to find the file with class_ prefix and convert case
            class_file_name = f"class_{class_name.lower()}"
            doc_path = validate_doc_path(f"classes/{class_file_name}.md")
        else:
            doc_path = validate_doc_path(f"classes/{class_name}.md")
        
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # Try alternative naming patterns
        try:
            # Try without class_ prefix
            clean_name = class_name.replace('class_', '')
            doc_path = validate_doc_path(f"classes/{clean_name}.md")
            return doc_path.read_text(encoding='utf-8')
        except FileNotFoundError:
            return f"Class documentation not found: {class_name}. Use list_classes() tool to see available classes."
    except Exception as e:
        return f"Error accessing class documentation: {str(e)}"

# Community resources
@mcp.resource("godot://community/{topic}")
def get_community_documentation(topic: str) -> str:
    """Get Godot community documentation"""
    try:
        doc_path = validate_doc_path(f"community/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Community documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing community documentation: {str(e)}"

@mcp.resource("godot://community/asset_library/{topic}")
def get_community_asset_library_documentation(topic: str) -> str:
    """Get Godot community asset library documentation"""
    try:
        doc_path = validate_doc_path(f"community/asset_library/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Community asset library documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing community asset library documentation: {str(e)}"

# Contributing resources
@mcp.resource("godot://contributing/{topic}")
def get_contributing_root_documentation(topic: str) -> str:
    """Get Godot contributing documentation from root"""
    try:
        doc_path = validate_doc_path(f"contributing/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Contributing documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing contributing documentation: {str(e)}"

@mcp.resource("godot://contributing/development/{topic}")
def get_contributing_development_documentation(topic: str) -> str:
    """Get Godot contributing development documentation"""
    try:
        doc_path = validate_doc_path(f"contributing/development/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Contributing development documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing contributing development documentation: {str(e)}"

@mcp.resource("godot://contributing/development/compiling/{topic}")
def get_contributing_development_compiling_documentation(topic: str) -> str:
    """Get Godot contributing development compiling documentation"""
    try:
        doc_path = validate_doc_path(f"contributing/development/compiling/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Contributing development compiling documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing contributing development compiling documentation: {str(e)}"

@mcp.resource("godot://contributing/development/configuring_an_ide/{topic}")
def get_contributing_development_ide_documentation(topic: str) -> str:
    """Get Godot contributing development IDE configuration documentation"""
    try:
        doc_path = validate_doc_path(f"contributing/development/configuring_an_ide/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Contributing development IDE documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing contributing development IDE documentation: {str(e)}"

@mcp.resource("godot://contributing/development/core_and_modules/{topic}")
def get_contributing_development_core_documentation(topic: str) -> str:
    """Get Godot contributing development core and modules documentation"""
    try:
        doc_path = validate_doc_path(f"contributing/development/core_and_modules/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Contributing development core documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing contributing development core documentation: {str(e)}"

@mcp.resource("godot://contributing/development/debugging/{topic}")
def get_contributing_development_debugging_documentation(topic: str) -> str:
    """Get Godot contributing development debugging documentation"""
    try:
        doc_path = validate_doc_path(f"contributing/development/debugging/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Contributing development debugging documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing contributing development debugging documentation: {str(e)}"

@mcp.resource("godot://contributing/development/debugging/vulkan/{topic}")
def get_contributing_development_debugging_vulkan_documentation(topic: str) -> str:
    """Get Godot contributing development debugging vulkan documentation"""
    try:
        doc_path = validate_doc_path(f"contributing/development/debugging/vulkan/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Contributing development debugging vulkan documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing contributing development debugging vulkan documentation: {str(e)}"

@mcp.resource("godot://contributing/development/editor/{topic}")
def get_contributing_development_editor_documentation(topic: str) -> str:
    """Get Godot contributing development editor documentation"""
    try:
        doc_path = validate_doc_path(f"contributing/development/editor/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Contributing development editor documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing contributing development editor documentation: {str(e)}"

@mcp.resource("godot://contributing/development/file_formats/{topic}")
def get_contributing_development_file_formats_documentation(topic: str) -> str:
    """Get Godot contributing development file formats documentation"""
    try:
        doc_path = validate_doc_path(f"contributing/development/file_formats/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Contributing development file formats documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing contributing development file formats documentation: {str(e)}"

@mcp.resource("godot://contributing/documentation/{topic}")
def get_contributing_documentation_documentation(topic: str) -> str:
    """Get Godot contributing documentation documentation"""
    try:
        doc_path = validate_doc_path(f"contributing/documentation/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Contributing documentation documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing contributing documentation documentation: {str(e)}"

@mcp.resource("godot://contributing/workflow/{topic}")
def get_contributing_workflow_documentation(topic: str) -> str:
    """Get Godot contributing workflow documentation"""
    try:
        doc_path = validate_doc_path(f"contributing/workflow/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Contributing workflow documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing contributing workflow documentation: {str(e)}"

# Getting started resources
@mcp.resource("godot://getting_started/{topic}")
def get_getting_started_root_documentation(topic: str) -> str:
    """Get Godot getting started documentation from root"""
    try:
        doc_path = validate_doc_path(f"getting_started/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Getting started documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing getting started documentation: {str(e)}"

@mcp.resource("godot://getting_started/first_2d_game/{topic}")
def get_getting_started_first_2d_game_documentation(topic: str) -> str:
    """Get Godot getting started first 2D game documentation"""
    try:
        doc_path = validate_doc_path(f"getting_started/first_2d_game/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Getting started first 2D game documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing getting started first 2D game documentation: {str(e)}"

@mcp.resource("godot://getting_started/first_3d_game/{topic}")
def get_getting_started_first_3d_game_documentation(topic: str) -> str:
    """Get Godot getting started first 3D game documentation"""
    try:
        doc_path = validate_doc_path(f"getting_started/first_3d_game/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Getting started first 3D game documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing getting started first 3D game documentation: {str(e)}"

@mcp.resource("godot://getting_started/introduction/{topic}")
def get_getting_started_introduction_documentation(topic: str) -> str:
    """Get Godot getting started introduction documentation"""
    try:
        doc_path = validate_doc_path(f"getting_started/introduction/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Getting started introduction documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing getting started introduction documentation: {str(e)}"

@mcp.resource("godot://getting_started/step_by_step/{topic}")
def get_getting_started_step_by_step_documentation(topic: str) -> str:
    """Get Godot getting started step by step documentation"""
    try:
        doc_path = validate_doc_path(f"getting_started/step_by_step/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Getting started step by step documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing getting started step by step documentation: {str(e)}"

# Tutorial resources
@mcp.resource("godot://tutorials/{topic}")
def get_tutorials_root_documentation(topic: str) -> str:
    """Get Godot tutorials documentation from root"""
    try:
        doc_path = validate_doc_path(f"tutorials/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/2d/{topic}")
def get_tutorials_2d_documentation(topic: str) -> str:
    """Get Godot 2D tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/2d/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"2D tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing 2D tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/3d/{topic}")
def get_tutorials_3d_documentation(topic: str) -> str:
    """Get Godot 3D tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/3d/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"3D tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing 3D tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/3d/global_illumination/{topic}")
def get_tutorials_3d_global_illumination_documentation(topic: str) -> str:
    """Get Godot 3D global illumination tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/3d/global_illumination/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"3D global illumination tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing 3D global illumination tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/3d/particles/{topic}")
def get_tutorials_3d_particles_documentation(topic: str) -> str:
    """Get Godot 3D particles tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/3d/particles/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"3D particles tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing 3D particles tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/3d/procedural_geometry/{topic}")
def get_tutorials_3d_procedural_geometry_documentation(topic: str) -> str:
    """Get Godot 3D procedural geometry tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/3d/procedural_geometry/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"3D procedural geometry tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing 3D procedural geometry tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/animation/{topic}")
def get_tutorials_animation_documentation(topic: str) -> str:
    """Get Godot animation tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/animation/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Animation tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing animation tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/assets_pipeline/{topic}")
def get_tutorials_assets_pipeline_documentation(topic: str) -> str:
    """Get Godot assets pipeline tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/assets_pipeline/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Assets pipeline tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing assets pipeline tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/assets_pipeline/escn_exporter/{topic}")
def get_tutorials_assets_pipeline_escn_exporter_documentation(topic: str) -> str:
    """Get Godot assets pipeline ESCN exporter tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/assets_pipeline/escn_exporter/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Assets pipeline ESCN exporter tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing assets pipeline ESCN exporter tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/assets_pipeline/importing_3d_scenes/{topic}")
def get_tutorials_assets_pipeline_importing_3d_scenes_documentation(topic: str) -> str:
    """Get Godot assets pipeline importing 3D scenes tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/assets_pipeline/importing_3d_scenes/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Assets pipeline importing 3D scenes tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing assets pipeline importing 3D scenes tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/audio/{topic}")
def get_tutorials_audio_documentation(topic: str) -> str:
    """Get Godot audio tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/audio/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Audio tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing audio tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/best_practices/{topic}")
def get_tutorials_best_practices_documentation(topic: str) -> str:
    """Get Godot best practices tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/best_practices/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Best practices tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing best practices tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/editor/{topic}")
def get_tutorials_editor_documentation(topic: str) -> str:
    """Get Godot editor tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/editor/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Editor tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing editor tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/export/{topic}")
def get_tutorials_export_documentation(topic: str) -> str:
    """Get Godot export tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/export/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Export tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing export tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/i18n/{topic}")
def get_tutorials_i18n_documentation(topic: str) -> str:
    """Get Godot internationalization tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/i18n/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Internationalization tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing internationalization tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/inputs/{topic}")
def get_tutorials_inputs_documentation(topic: str) -> str:
    """Get Godot inputs tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/inputs/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Inputs tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing inputs tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/io/{topic}")
def get_tutorials_io_documentation(topic: str) -> str:
    """Get Godot I/O tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/io/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"I/O tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing I/O tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/math/{topic}")
def get_tutorials_math_documentation(topic: str) -> str:
    """Get Godot math tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/math/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Math tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing math tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/migrating/{topic}")
def get_tutorials_migrating_documentation(topic: str) -> str:
    """Get Godot migrating tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/migrating/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Migrating tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing migrating tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/navigation/{topic}")
def get_tutorials_navigation_documentation(topic: str) -> str:
    """Get Godot navigation tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/navigation/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Navigation tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing navigation tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/networking/{topic}")
def get_tutorials_networking_documentation(topic: str) -> str:
    """Get Godot networking tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/networking/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Networking tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing networking tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/performance/{topic}")
def get_tutorials_performance_documentation(topic: str) -> str:
    """Get Godot performance tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/performance/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Performance tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing performance tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/performance/vertex_animation/{topic}")
def get_tutorials_performance_vertex_animation_documentation(topic: str) -> str:
    """Get Godot performance vertex animation tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/performance/vertex_animation/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Performance vertex animation tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing performance vertex animation tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/physics/{topic}")
def get_tutorials_physics_documentation(topic: str) -> str:
    """Get Godot physics tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/physics/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Physics tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing physics tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/physics/interpolation/{topic}")
def get_tutorials_physics_interpolation_documentation(topic: str) -> str:
    """Get Godot physics interpolation tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/physics/interpolation/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Physics interpolation tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing physics interpolation tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/platform/{topic}")
def get_tutorials_platform_documentation(topic: str) -> str:
    """Get Godot platform tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/platform/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Platform tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing platform tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/platform/android/{topic}")
def get_tutorials_platform_android_documentation(topic: str) -> str:
    """Get Godot platform Android tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/platform/android/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Platform Android tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing platform Android tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/platform/ios/{topic}")
def get_tutorials_platform_ios_documentation(topic: str) -> str:
    """Get Godot platform iOS tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/platform/ios/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Platform iOS tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing platform iOS tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/platform/web/{topic}")
def get_tutorials_platform_web_documentation(topic: str) -> str:
    """Get Godot platform web tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/platform/web/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Platform web tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing platform web tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/plugins/{topic}")
def get_tutorials_plugins_documentation(topic: str) -> str:
    """Get Godot plugins tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/plugins/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Plugins tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing plugins tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/plugins/editor/{topic}")
def get_tutorials_plugins_editor_documentation(topic: str) -> str:
    """Get Godot plugins editor tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/plugins/editor/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Plugins editor tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing plugins editor tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/rendering/{topic}")
def get_tutorials_rendering_documentation(topic: str) -> str:
    """Get Godot rendering tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/rendering/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Rendering tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing rendering tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/scripting/{topic}")
def get_tutorials_scripting_documentation(topic: str) -> str:
    """Get Godot scripting tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/scripting/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Scripting tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing scripting tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/scripting/c_sharp/{topic}")
def get_tutorials_scripting_c_sharp_documentation(topic: str) -> str:
    """Get Godot scripting C# tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/scripting/c_sharp/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Scripting C# tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing scripting C# tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/scripting/c_sharp/diagnostics/{topic}")
def get_tutorials_scripting_c_sharp_diagnostics_documentation(topic: str) -> str:
    """Get Godot scripting C# diagnostics tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/scripting/c_sharp/diagnostics/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Scripting C# diagnostics tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing scripting C# diagnostics tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/scripting/cpp/{topic}")
def get_tutorials_scripting_cpp_documentation(topic: str) -> str:
    """Get Godot scripting C++ tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/scripting/cpp/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Scripting C++ tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing scripting C++ tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/scripting/debug/{topic}")
def get_tutorials_scripting_debug_documentation(topic: str) -> str:
    """Get Godot scripting debug tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/scripting/debug/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Scripting debug tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing scripting debug tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/scripting/gdextension/{topic}")
def get_tutorials_scripting_gdextension_documentation(topic: str) -> str:
    """Get Godot scripting GDExtension tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/scripting/gdextension/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Scripting GDExtension tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing scripting GDExtension tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/scripting/gdscript/{topic}")
def get_tutorials_scripting_gdscript_documentation(topic: str) -> str:
    """Get Godot scripting GDScript tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/scripting/gdscript/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Scripting GDScript tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing scripting GDScript tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/shaders/{topic}")
def get_tutorials_shaders_documentation(topic: str) -> str:
    """Get Godot shaders tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/shaders/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Shaders tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing shaders tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/shaders/shader_reference/{topic}")
def get_tutorials_shaders_reference_documentation(topic: str) -> str:
    """Get Godot shaders reference tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/shaders/shader_reference/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Shaders reference tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing shaders reference tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/shaders/your_first_shader/{topic}")
def get_tutorials_shaders_first_shader_documentation(topic: str) -> str:
    """Get Godot your first shader tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/shaders/your_first_shader/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Your first shader tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing your first shader tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/ui/{topic}")
def get_tutorials_ui_documentation(topic: str) -> str:
    """Get Godot UI tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/ui/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"UI tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing UI tutorial documentation: {str(e)}"

@mcp.resource("godot://tutorials/xr/{topic}")
def get_tutorials_xr_documentation(topic: str) -> str:
    """Get Godot XR tutorials documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/xr/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"XR tutorial documentation not found: {topic}."
    except Exception as e:
        return f"Error accessing XR tutorial documentation: {str(e)}"

# Generic fallback resource for any documentation file
@mcp.resource("godot://doc/{file_path}")
def get_any_documentation(file_path: str) -> str:
    """Get any documentation file by path"""
    try:
        # Add .md extension if not present
        if not file_path.endswith('.md'):
            file_path += '.md'
        doc_path = validate_doc_path(file_path)
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Documentation file not found: {file_path}. Use search_docs() tool to find available documentation."
    except Exception as e:
        return f"Error accessing documentation: {str(e)}"