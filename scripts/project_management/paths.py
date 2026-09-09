#!/usr/bin/env python3
"""
PPT Master - Project Management Paths

Own the repository and Skill resource roots used by project-management modules.

Usage:
    Import the required path constants from project_management.paths.

Examples:
    from project_management.paths import PROJECTS_ROOT, SCHEMA_DIR

Dependencies:
    None (only uses the standard library)
"""

import os
from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = PACKAGE_DIR.parent
SKILL_DIR = SCRIPTS_DIR.parent
REPO_ROOT = SKILL_DIR.parent.parent

# deeppath-agent:宿主通过 PPT_PROJECTS_ROOT 注入当前会话的 PPT 工作区
# （<数据目录>/ppt-projects/<chatId>）。project_manager.py init 默认必须落到
# 会话工作区，而不是技能自带的全局 projects/ 目录；宿主未注入时退回旧默认值。
_env_ppt_projects_root = os.environ.get("PPT_PROJECTS_ROOT")
PROJECTS_ROOT = Path(_env_ppt_projects_root) if _env_ppt_projects_root else REPO_ROOT / "projects"
SOURCE_TO_MD_DIR = SCRIPTS_DIR / "source_to_md"
CHARTS_DIR = SKILL_DIR / "templates" / "charts"
SCHEMA_DIR = SKILL_DIR / "templates" / "schemas"
SCAFFOLD_DIR = SKILL_DIR / "templates" / "scaffolds"
