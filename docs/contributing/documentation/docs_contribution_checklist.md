# Documentation contribution checklist {#docs_contribution_checklist}

This page is a summary of the guidelines to follow when contributing to
the documentation. Before you press that **Create pull request** button
on GitHub, read over this list to double check if you missed anything.

You don\'t need to read all the guidelines here in order to start
contributing. If you do miss something, it will be pointed out during
review. However, following the guidelines you are aware of as best you
can will help speed up the review process.

## Writing style

`See here. <doc_docs_writing_guidelines_clear_english_rules>`{.interpreted-text
role="ref"}

- Use the active voice.
- Use precise action verbs.
- Avoid verbs that end in -ing.
- Remove unnecessary adverbs and adjectives.
- Ban these 8 words: obvious, simple, basic, easy, actual, just, clear,
  and however.
- Use explicit references.
- Use \'s to show possession.
- Use the Oxford comma.

## Code examples

- Use dynamic typing.
  `See here. <doc_docs_writing_guidelines_dynamic_typing>`{.interpreted-text
  role="ref"}
- Use real, practical examples. Avoid `foo` / `bar` examples.
  `See here. <doc_docs_writing_guidelines_real_world_code_example>`{.interpreted-text
  role="ref"}

## Manual style and formatting

- Use common vocabulary for the editor interface.
  `See here. <doc_docs_writing_guidelines_common_vocabulary>`{.interpreted-text
  role="ref"}
- Use `:kbd:` for keyboard shortcuts.
  `See here. <doc_docs_writing_guidelines_keyboard_shortcuts>`{.interpreted-text
  role="ref"}
- Literals use `code style`.
  `See here. <doc_docs_writing_guidelines_literals>`{.interpreted-text
  role="ref"}
- Classes link to the class reference once, then use `ClassName` for the
  rest of the page. Methods and properties link to the class ref once,
  then use `PropertyName` for the rest of the page.
  `See here. <doc_docs_writing_guidelines_class_properties_methods>`{.interpreted-text
  role="ref"}
- Editor UI, like menus, windows, and editor navigation paths, use
  `Bold Style`.
  `See here. <doc_docs_writing_guidelines_editor_ui>`{.interpreted-text
  role="ref"}
- Link to project settings when referencing them.
  `See here. <doc_docs_writing_guidelines_project_settings>`{.interpreted-text
  role="ref"}
- Text is manually wrapped to 80-100 characters.
  `See here. <doc_docs_writing_guidelines_manually_wrapping_lines>`{.interpreted-text
  role="ref"}
- No trailing whitespace at the end of lines.
- Most of the time, avoid mentioning a specific Godot version.
  `See here. <doc_docs_writing_guidelines_specific_version>`{.interpreted-text
  role="ref"}

## Images and videos

- New (and updated) images are in WebP format.
  `See here. <doc_docs_image_guidelines_format_conversion>`{.interpreted-text
  role="ref"}
- Editor screenshots are cropped.
  `See here. <doc_docs_image_guidelines_cropping>`{.interpreted-text
  role="ref"}
- Images larger than 1080p or 300kb are scaled down.
  `See here. <doc_docs_image_guidelines_scaling_down>`{.interpreted-text
  role="ref"}
- Outlines in images use `fffb44` yellow.
  `See here. <doc_docs_image_guidelines_outlines>`{.interpreted-text
  role="ref"}
- Videos use the `:autoplay:`, `:loop:`, and `:muted:` tags.
  `See here. <doc_docs_image_guidelines_videos>`{.interpreted-text
  role="ref"}

## GitHub

- The PR title starts with a word like `Fix`, `Add`, `Update`,
  `Clarify`, or `Improve`.
- If the PR closes an issue, link to the issue with one of GitHub\'s
  [keywords](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests):
  `closes`, `fixes`, or `resolves`, in the text of the PR.
- Ideally, PR contains a single commit. However, multiple commits can be
  `squashed <doc_pr_workflow_rebase>`{.interpreted-text role="ref"}
  later.
