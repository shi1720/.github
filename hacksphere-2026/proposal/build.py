#!/usr/bin/env python3
"""Runner: imports content (which populates fill_docx registries), then builds."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fill_docx
import content as C
fill_docx.build(C.CONTENT, os.path.join(fill_docx.SCRATCH, C.OUT_NAME + ".docx"))
