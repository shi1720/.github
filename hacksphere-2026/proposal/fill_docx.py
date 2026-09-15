#!/usr/bin/env python3
"""
AKAR proposal builder — fills the official HACKSPHERE 2026 template DOCX.

Approach: surgical XML edits on the unpacked official template so all
branding (header/footer art, tables, fonts, numbered headings) is preserved.
Content is defined in content.py as a small block model; this engine renders
blocks to OOXML and splices them in.
"""
import copy, os, re, shutil, subprocess, sys, zipfile
from html import escape

SCRATCH = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(SCRATCH, "tpl")
BUILD = os.path.join(SCRATCH, "build")

TNR = '<w:rFonts w:ascii="Times New Roman" w:cs="Times New Roman" w:eastAsia="Times New Roman" w:hAnsi="Times New Roman"/>'
ACCENT_TEAL = "a7eae8"
ACCENT_GRAY = "efefef"
NAVY = "1F3864"
DXA_FULL = 9029          # template table width
DXA_BODY = 8309          # width available at indent 720
EMU_PER_DXA = 635        # 914400/1440

# ------------------------------------------------------------- references
class _Refs:
    """{r:key} tokens in text become superscript numbers in order of first use.
    Register with REFS.define(key, label, url)."""
    def __init__(self):
        self.defs = {}
        self.order = []
    def define(self, key, label, url):
        self.defs[key] = (label, url)
    def number(self, key):
        if key not in self.defs:
            raise KeyError(f"undefined reference: {key}")
        if key not in self.order:
            self.order.append(key)
        return self.order.index(key) + 1
    def bibliography(self):
        return [(i + 1, *self.defs[k]) for i, k in enumerate(self.order)]
REFS = _Refs()

def _expand_refs(text):
    def sub(m):
        keys = [k.strip() for k in m.group(1).split(",")]
        nums = sorted(REFS.number(k) for k in keys)
        return "~" + ",".join(str(n) for n in nums) + "~"
    return re.sub(r"\{r:([^}]+)\}", sub, text)

# ---------------------------------------------------------------- inline runs
def _runs(text, base=""):
    """Mini-markup: **bold**, *italic*, ~sup~ (superscript), §[url|label] link.
    Returns OOXML runs. base = extra rPr props for every run."""
    out = []
    text = _expand_refs(text)
    token = re.compile(r"(\*\*.+?\*\*|\*.+?\*|~.+?~|§\[.+?\|.+?\])")
    for part in token.split(text):
        if not part:
            continue
        props = base
        if part.startswith("**") and part.endswith("**"):
            part = part[2:-2]; props += "<w:b w:val=\"1\"/>"
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            part = part[1:-1]; props += "<w:i w:val=\"1\"/>"
        elif part.startswith("~") and part.endswith("~"):
            part = part[1:-1]
            props += '<w:vertAlign w:val="superscript"/>'
        elif part.startswith("§["):
            url, label = part[2:-1].split("|", 1)
            rid = LINKS.add(url)
            run = (f'<w:r><w:rPr>{TNR}<w:color w:val="1155CC"/><w:u w:val="single"/>'
                   f'{base}<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">{escape(label)}</w:t></w:r>')
            out.append(f'<w:hyperlink r:id="{rid}">{run}</w:hyperlink>')
            continue
        out.append(f'<w:r><w:rPr>{TNR}{props}<w:rtl w:val="0"/></w:rPr>'
                   f'<w:t xml:space="preserve">{escape(part)}</w:t></w:r>')
    return "".join(out)


class _Links:
    def __init__(self):
        self.urls = []
    def add(self, url):
        self.urls.append(url)
        return f"rIdX{len(self.urls)}"
LINKS = _Links()

# ------------------------------------------------------------------- blocks
def P(text, *, size=22, after=120, before=0, align="left", indent=720,
      color=None, line=276, bold=False):
    props = f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    if color: props += f'<w:color w:val="{color}"/>'
    if bold: props += '<w:b w:val="1"/>'
    jc = {"left": "left", "both": "both", "center": "center", "right": "right"}[align]
    return (f'<w:p><w:pPr><w:spacing w:after="{after}" w:before="{before}" '
            f'w:line="{line}" w:lineRule="auto"/>'
            f'<w:ind w:left="{indent}" w:firstLine="0"/><w:jc w:val="{jc}"/>'
            f'<w:rPr>{TNR}{props}</w:rPr></w:pPr>{_runs(text, props)}</w:p>')

def SUBHEAD(text, *, size=23, before=160, after=80, indent=720, color=NAVY):
    props = (f'<w:b w:val="1"/><w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
             f'<w:color w:val="{color}"/>')
    return (f'<w:p><w:pPr><w:keepNext w:val="1"/><w:spacing w:after="{after}" w:before="{before}" '
            f'w:line="240" w:lineRule="auto"/><w:ind w:left="{indent}" w:firstLine="0"/>'
            f'<w:rPr>{TNR}{props}</w:rPr></w:pPr>{_runs(text, props)}</w:p>')

def BULLETS(items, *, size=22, indent=1080, after=60, last_after=120, level=0):
    """items: list of strings (mini-markup ok)."""
    out = []
    for i, it in enumerate(items):
        a = last_after if i == len(items) - 1 else after
        props = f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
        out.append(
            f'<w:p><w:pPr><w:numPr><w:ilvl w:val="{level}"/><w:numId w:val="50"/></w:numPr>'
            f'<w:spacing w:after="{a}" w:before="0" w:line="276" w:lineRule="auto"/>'
            f'<w:ind w:left="{indent}" w:hanging="216"/>'
            f'<w:rPr>{TNR}{props}</w:rPr></w:pPr>{_runs(it, props)}</w:p>')
    return "".join(out)

def SPACER(h=60):
    return (f'<w:p><w:pPr><w:spacing w:after="0" w:before="0" w:line="240" '
            f'w:lineRule="auto"/><w:rPr><w:sz w:val="{h}"/></w:rPr></w:pPr></w:p>')

def _cell(text, w, *, fill=None, bold=False, size=20, align="left", color=None,
          vmerge=None, span=None):
    props = f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    if bold: props += '<w:b w:val="1"/>'
    if color: props += f'<w:color w:val="{color}"/>'
    tcpr = f'<w:tcW w:w="{w}" w:type="dxa"/>'
    if span: tcpr += f'<w:gridSpan w:val="{span}"/>'
    if fill: tcpr += f'<w:shd w:fill="{fill}" w:val="clear"/>'
    tcpr += ('<w:tcMar><w:top w:w="60" w:type="dxa"/><w:left w:w="100" w:type="dxa"/>'
             '<w:bottom w:w="60" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tcMar>'
             '<w:vAlign w:val="center"/>')
    return (f'<w:tc><w:tcPr>{tcpr}</w:tcPr>'
            f'<w:p><w:pPr><w:spacing w:after="0" w:before="0" w:line="240" w:lineRule="auto"/>'
            f'<w:jc w:val="{align}"/><w:rPr>{TNR}{props}</w:rPr></w:pPr>'
            f'{_runs(str(text), props)}</w:p></w:tc>')

def TABLE(rows, widths, *, indent=720, header_fill=ACCENT_TEAL, size=20,
          header=True, zebra=None):
    """rows: list of list of cell values; first row = header if header=True.
    cell value may be (text, dict) for per-cell overrides."""
    total = sum(widths)
    bd = ('<w:tblBorders>' + ''.join(
        f'<w:{s} w:color="000000" w:space="0" w:sz="6" w:val="single"/>'
        for s in ("top", "left", "bottom", "right", "insideH", "insideV")) + '</w:tblBorders>')
    grid = '<w:tblGrid>' + ''.join(f'<w:gridCol w:w="{w}"/>' for w in widths) + '</w:tblGrid>'
    xml = [f'<w:tbl><w:tblPr><w:tblW w:w="{total}" w:type="dxa"/>'
           f'<w:tblInd w:w="{indent}" w:type="dxa"/>{bd}'
           f'<w:tblLayout w:type="fixed"/><w:tblLook w:val="0600"/></w:tblPr>{grid}']
    for r, row in enumerate(rows):
        cells = []
        for c, val in enumerate(row):
            o = {}
            if isinstance(val, tuple):
                val, o = val
            fill = o.get("fill")
            bold = o.get("bold", False)
            alg = o.get("align", "left")
            colr = o.get("color")
            sz = o.get("size", size)
            span = o.get("span")
            if header and r == 0:
                fill = fill or header_fill; bold = True; alg = o.get("align", "center")
            elif zebra and r % 2 == 0:
                fill = fill or zebra
            w = widths[c] if not span else sum(widths[c:c+span])
            cells.append(_cell(val, w, fill=fill, bold=bold, size=sz, align=alg,
                               color=colr, span=span))
        xml.append(f'<w:tr><w:trPr><w:cantSplit w:val="1"/></w:trPr>{"".join(cells)}</w:tr>')
    xml.append('</w:tbl>')
    # A table directly followed by a table/end needs a spacer paragraph after.
    return "".join(xml) + SPACER(40)

_IMG_COUNT = [0]
def IMG(path, width_dxa=DXA_BODY, *, indent=720, after=120, before=60):
    """Embed PNG at given display width (aspect preserved)."""
    from PIL import Image
    im = Image.open(path)
    w_emu = width_dxa * EMU_PER_DXA
    h_emu = int(w_emu * im.height / im.width)
    _IMG_COUNT[0] += 1
    n = _IMG_COUNT[0]
    rid = f"rIdIMG{n}"
    IMAGES.append((rid, path, f"media/akar_img{n}.png"))
    did = 9000 + n
    return (f'<w:p><w:pPr><w:spacing w:after="{after}" w:before="{before}" w:line="240" w:lineRule="auto"/>'
            f'<w:ind w:left="{indent}" w:firstLine="0"/><w:jc w:val="center"/></w:pPr>'
            f'<w:r><w:rPr/><w:drawing>'
            f'<wp:inline distT="0" distB="0" distL="0" distR="0">'
            f'<wp:extent cx="{w_emu}" cy="{h_emu}"/><wp:effectExtent b="0" l="0" r="0" t="0"/>'
            f'<wp:docPr id="{did}" name="image_akar_{n}.png"/>'
            f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
            f'<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<pic:nvPicPr><pic:cNvPr id="{did}" name="image_akar_{n}.png"/><pic:cNvPicPr/></pic:nvPicPr>'
            f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{w_emu}" cy="{h_emu}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
            f'</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>')

IMAGES = []  # (rid, src_path, zip_name)

def CAPTION(text, indent=720):
    return P(text, size=18, color="666666", align="center", indent=indent, after=160)

def STATBAND(items, *, indent=720, width=DXA_BODY):
    """items: list of (big_number, label). Renders a borderless infographic row."""
    n = len(items)
    w = width // n
    tops, bots = [], []
    for big, label in items:
        big_props = '<w:b w:val="1"/><w:sz w:val="40"/><w:szCs w:val="40"/><w:color w:val="044064"/>'
        lab_props = f'<w:sz w:val="17"/><w:szCs w:val="17"/><w:color w:val="4a4a4a"/>'
        tops.append(
            f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>'
            f'<w:tcBorders><w:top w:color="33c1cc" w:sz="18" w:space="0" w:val="single"/>'
            f'<w:left w:color="ffffff" w:sz="24" w:space="0" w:val="single"/>'
            f'<w:bottom w:val="nil"/>'
            f'<w:right w:color="ffffff" w:sz="24" w:space="0" w:val="single"/></w:tcBorders>'
            f'<w:shd w:fill="f2fafb" w:val="clear"/>'
            f'<w:tcMar><w:top w:w="120" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
            f'<w:bottom w:w="20" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>'
            f'<w:vAlign w:val="center"/></w:tcPr>'
            f'<w:p><w:pPr><w:spacing w:after="0" w:before="0" w:line="240" w:lineRule="auto"/>'
            f'<w:jc w:val="center"/><w:rPr>{TNR}{big_props}</w:rPr></w:pPr>'
            f'{_runs(str(big), big_props)}</w:p></w:tc>')
        bots.append(
            f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>'
            f'<w:tcBorders><w:top w:val="nil"/>'
            f'<w:left w:color="ffffff" w:sz="24" w:space="0" w:val="single"/>'
            f'<w:bottom w:color="ffffff" w:sz="4" w:space="0" w:val="single"/>'
            f'<w:right w:color="ffffff" w:sz="24" w:space="0" w:val="single"/></w:tcBorders>'
            f'<w:shd w:fill="f2fafb" w:val="clear"/>'
            f'<w:tcMar><w:top w:w="20" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
            f'<w:bottom w:w="120" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>'
            f'<w:vAlign w:val="center"/></w:tcPr>'
            f'<w:p><w:pPr><w:spacing w:after="0" w:before="0" w:line="240" w:lineRule="auto"/>'
            f'<w:jc w:val="center"/><w:rPr>{TNR}{lab_props}</w:rPr></w:pPr>'
            f'{_runs(label, lab_props)}</w:p></w:tc>')
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for _ in items)
    return (f'<w:tbl><w:tblPr><w:tblW w:w="{width}" w:type="dxa"/>'
            f'<w:tblInd w:w="{indent}" w:type="dxa"/>'
            f'<w:tblBorders><w:top w:val="nil"/><w:left w:val="nil"/><w:bottom w:val="nil"/>'
            f'<w:right w:val="nil"/><w:insideH w:val="nil"/><w:insideV w:val="nil"/></w:tblBorders>'
            f'<w:tblLayout w:type="fixed"/><w:tblLook w:val="0600"/></w:tblPr>'
            f'<w:tblGrid>{grid}</w:tblGrid>'
            f'<w:tr>{"".join(tops)}</w:tr><w:tr>{"".join(bots)}</w:tr></w:tbl>' + SPACER(60))

def CALLOUT(text, *, indent=720, width=DXA_BODY, fill="f2fafb", accent="0e7c86",
            size=21, title=None):
    """Accent-bordered callout box (e.g., field vignette)."""
    props = f'<w:i w:val="1"/><w:sz w:val="{size}"/><w:szCs w:val="{size}"/><w:color w:val="1f2937"/>'
    inner = ""
    if title:
        tprops = f'<w:b w:val="1"/><w:sz w:val="{size}"/><w:szCs w:val="{size}"/><w:color w:val="{accent}"/>'
        inner += (f'<w:p><w:pPr><w:spacing w:after="40" w:before="0" w:line="252" w:lineRule="auto"/>'
                  f'<w:rPr>{TNR}{tprops}</w:rPr></w:pPr>{_runs(title, tprops)}</w:p>')
    inner += (f'<w:p><w:pPr><w:spacing w:after="0" w:before="0" w:line="252" w:lineRule="auto"/>'
              f'<w:rPr>{TNR}{props}</w:rPr></w:pPr>{_runs(text, props)}</w:p>')
    return (f'<w:tbl><w:tblPr><w:tblW w:w="{width}" w:type="dxa"/>'
            f'<w:tblInd w:w="{indent}" w:type="dxa"/>'
            f'<w:tblBorders><w:top w:color="{accent}" w:sz="4" w:space="0" w:val="single"/>'
            f'<w:left w:color="{accent}" w:sz="24" w:space="0" w:val="single"/>'
            f'<w:bottom w:color="{accent}" w:sz="4" w:space="0" w:val="single"/>'
            f'<w:right w:color="{accent}" w:sz="4" w:space="0" w:val="single"/>'
            f'<w:insideH w:val="nil"/><w:insideV w:val="nil"/></w:tblBorders>'
            f'<w:tblLayout w:type="fixed"/><w:tblLook w:val="0600"/></w:tblPr>'
            f'<w:tblGrid><w:gridCol w:w="{width}"/></w:tblGrid>'
            f'<w:tr><w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>'
            f'<w:shd w:fill="{fill}" w:val="clear"/>'
            f'<w:tcMar><w:top w:w="140" w:type="dxa"/><w:left w:w="200" w:type="dxa"/>'
            f'<w:bottom w:w="140" w:type="dxa"/><w:right w:w="200" w:type="dxa"/></w:tcMar>'
            f'</w:tcPr>{inner}</w:tc></w:tr></w:tbl>' + SPACER(60))

def REFERENCES_BLOCK():
    """Numbered bibliography from all {r:} uses, small type, hyperlinked."""
    out = [SUBHEAD("References", size=24, before=240, indent=720, color="044064")]
    for n, label, url in REFS.bibliography():
        props = '<w:sz w:val="17"/><w:szCs w:val="17"/><w:color w:val="374151"/>'
        out.append(
            f'<w:p><w:pPr><w:spacing w:after="36" w:before="0" w:line="240" w:lineRule="auto"/>'
            f'<w:ind w:left="1080" w:hanging="360"/>'
            f'<w:rPr>{TNR}{props}</w:rPr></w:pPr>'
            f'{_runs(f"[{n}]  {label}  ", props)}'
            f'{_runs(f"§[{url}|{url}]", props)}</w:p>')
    return "".join(out)

def PAGEBREAK():
    return '<w:p><w:pPr><w:spacing w:after="0"/></w:pPr><w:r><w:br w:type="page"/></w:r></w:p>'

# ------------------------------------------------------------------- engine
def build(content, out_docx):
    if os.path.exists(BUILD):
        shutil.rmtree(BUILD)
    shutil.copytree(TPL, BUILD)
    # Pre-apply the Word "washout" the template intends for its watermark:
    # LibreOffice misrenders VML gain/blacklevel, drawing a gray box + harsh
    # lines. Bake a 15% ghost into the image and strip the VML attributes.
    from PIL import Image as _Img
    _p = f"{BUILD}/word/media/image3.png"
    _im = _Img.open(_p).convert("RGB")
    _im = _Img.blend(_Img.new("RGB", _im.size, (255, 255, 255)), _im, 0.15)
    _im.save(_p)
    _hp = f"{BUILD}/word/header1.xml"
    _hx = open(_hp).read()
    _hx = _hx.replace(' blacklevel="22938f"', '').replace(' gain="19661f"', '')
    _hx = _hx.replace('<v:shape id="WordPictureWatermark1" ',
                      '<v:shape id="WordPictureWatermark1" stroked="f" filled="f" ')
    open(_hp, "w").write(_hx)
    doc = open(f"{BUILD}/word/document.xml").read()

    # 1. identity cells --------------------------------------------------
    def fill_cell(placeholder, value, *, align=None, bold=False, size=None):
        nonlocal doc
        i = doc.find(escape(placeholder, quote=False))
        if i < 0:
            i = doc.find(placeholder)
        assert i >= 0, f"placeholder not found: {placeholder}"
        # find enclosing <w:p ...>...</w:p>
        ps = doc.rfind("<w:p ", 0, i)
        pe = doc.find("</w:p>", i) + len("</w:p>")
        old = doc[ps:pe]
        m = re.search(r'<w:jc w:val="([^"]+)"', old)
        jc = align or (m.group(1) if m else "left")
        props = ""
        if bold: props += '<w:b w:val="1"/>'
        if size: props += f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
        new = (f'<w:p><w:pPr><w:widowControl w:val="0"/><w:spacing w:line="240" w:lineRule="auto"/>'
               f'<w:jc w:val="{jc}"/><w:rPr>{TNR}{props}</w:rPr></w:pPr>'
               f'{_runs(value, props)}</w:p>')
        doc = doc[:ps] + new + doc[pe:]

    for ph, val, opts in content["cells"]:
        fill_cell(ph, val, **opts)

    # 2. section content -------------------------------------------------
    for marker, blocks in content["sections"]:
        i = doc.find("[Instructions:")
        # find the instruction para that FOLLOWS the heading containing marker
        h = doc.find(f">{escape(marker, quote=False)}<")
        if h < 0:
            h = doc.find(marker)
        assert h >= 0, f"heading not found: {marker}"
        i = doc.find("[Instructions:", h)
        assert i >= 0, f"instruction para not found after: {marker}"
        ps = doc.rfind("<w:p ", 0, i)
        pe = doc.find("</w:p>", i) + len("</w:p>")
        doc = doc[:ps] + "".join(blocks) + doc[pe:]

    # 3. optional appendix before sectPr ---------------------------------
    if content.get("appendix"):
        i = doc.find("<w:sectPr")
        doc = doc[:i] + "".join(content["appendix"]) + doc[i:]
    doc = doc.replace('<w:pgMar ', '<w:pgMar w:gutter="0" ') if 'w:gutter' not in doc else doc

    # 4. relationships (links + images) ----------------------------------
    rels_path = f"{BUILD}/word/_rels/document.xml.rels"
    rels = open(rels_path).read()
    add = ""
    for n, url in enumerate(LINKS.urls, 1):
        add += (f'<Relationship Id="rIdX{n}" '
                f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" '
                f'Target="{escape(url)}" TargetMode="External"/>')
    for rid, src, zname in IMAGES:
        shutil.copy(src, f"{BUILD}/word/{zname}")
        add += (f'<Relationship Id="{rid}" '
                f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" '
                f'Target="{zname}"/>')
    rels = rels.replace("</Relationships>", add + "</Relationships>")
    open(rels_path, "w").write(rels)

    # 5. bullet numbering -------------------------------------------------
    numb_path = f"{BUILD}/word/numbering.xml"
    numb = open(numb_path).read()
    if 'w:numId="50"' not in numb:
        bullet_lvls = ""
        chars = ["▪", "◦", "–"]  # ▪ ◦ –
        for lvl in range(3):
            ind = 1080 + lvl * 360
            bullet_lvls += (
                f'<w:lvl w:ilvl="{lvl}"><w:start w:val="1"/><w:numFmt w:val="bullet"/>'
                f'<w:lvlText w:val="{chars[lvl]}"/><w:lvlJc w:val="left"/>'
                f'<w:pPr><w:ind w:left="{ind}" w:hanging="216"/></w:pPr>'
                f'<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="18"/>'
                f'<w:color w:val="{NAVY}"/></w:rPr></w:lvl>')
        abstract = f'<w:abstractNum w:abstractNumId="50">{bullet_lvls}</w:abstractNum>'
        numdef = '<w:num w:numId="50"><w:abstractNumId w:val="50"/></w:num>'
        numb = numb.replace('<w:num w:numId="1">', abstract + '<w:num w:numId="1">')
        numb = numb.replace('</w:numbering>', numdef + '</w:numbering>')
        open(numb_path, "w").write(numb)

    open(f"{BUILD}/word/document.xml", "w").write(doc)

    # 6. zip --------------------------------------------------------------
    if os.path.exists(out_docx):
        os.remove(out_docx)
    with zipfile.ZipFile(out_docx, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(BUILD):
            for f in files:
                fp = os.path.join(root, f)
                z.write(fp, os.path.relpath(fp, BUILD))
    print(f"built {out_docx} ({os.path.getsize(out_docx)//1024} KB)")


if __name__ == "__main__":
    sys.path.insert(0, SCRATCH)
    import content as C
    build(C.CONTENT, os.path.join(SCRATCH, C.OUT_NAME + ".docx"))
