"""Fails if any page links to a local file that doesn't exist or to an #anchor with no matching id.

Usage: python3 scripts/check-links.py   (from the repository root)
"""
import html.parser, pathlib, sys, urllib.parse

class Page(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs = set(), []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        for key in ("href", "src"):
            if a.get(key):
                self.refs.append(a[key])

root = pathlib.Path(".").resolve()
pages = sorted(root.glob("*.html"))
errors, checked = [], 0
for path in pages:
    page = Page()
    page.feed(path.read_text())
    for ref in page.refs:
        url = urllib.parse.urlparse(ref)
        if url.scheme in ("http", "https", "mailto"):
            continue
        checked += 1
        if ref.startswith("#"):
            if ref[1:] not in page.ids:
                errors.append(f"{path.name}: no element with id {ref}")
            continue
        target = (root / url.path.lstrip("/")) if url.path.startswith("/") else (path.parent / url.path)
        if url.path in ("", "/", "./"):
            target = root / "index.html"
        if not target.exists():
            errors.append(f"{path.name}: {ref} does not exist")

print(f"{len(pages)} pages, {checked} local links checked")
if not checked:
    sys.exit("no local links found: the check examined nothing")
for e in errors:
    print(e)
sys.exit(1 if errors else 0)
