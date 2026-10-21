# operation-forward.github.io

The Operation Forward website, served by GitHub Pages at https://operationforward.org/ (`operation-forward.github.io` and `www` redirect there).

Plain HTML and CSS: no build step, no JavaScript, no third-party requests. The look comes from the
charity's design system in [opfor-design](https://github.com/Operation-Forward/opfor-design):

| File | Source |
|---|---|
| `assets/tokens.css` | `design-system/dist/tokens.css` (font paths point at `assets/fonts/`) |
| `assets/components.css` | `design-system/system/components/bundle.css` |
| `assets/fonts/` | `design-system/system/fonts/` (SIL Open Font License texts included) |
| logos, icons, social card | `brand/` |
| `assets/site.css` | this site's layout only |

When the design system changes, copy those files again.

## Editing

Change `index.html`, open a pull request, merge it: Pages publishes `main` within a minute. Preview
locally with `python3 -m http.server` in this folder (fonts don't load from `file://`).

CI runs the shared security gates and `scripts/check-links.py` (every local link and `#anchor`
resolves).

Before publishing a change, check the page in a browser at phone width and on a wide screen, in
light and dark mode.

## Moving operationforward.org here

The domain currently points at Squarespace (DNS on Cloudflare; mail is Zoho and is not affected).
Records for the DNS owner:

| Type | Name | Value | Notes |
|---|---|---|---|
| A | `operationforward.org` (`@`) | `185.199.108.153` | replace the four Squarespace A records |
| A | `@` | `185.199.109.153` | |
| A | `@` | `185.199.110.153` | |
| A | `@` | `185.199.111.153` | |
| AAAA | `@` | `2606:50c0:8000::153` | |
| AAAA | `@` | `2606:50c0:8001::153` | |
| AAAA | `@` | `2606:50c0:8002::153` | |
| AAAA | `@` | `2606:50c0:8003::153` | |
| CNAME | `www` | `operation-forward.github.io` | replaces `ext-cust.squarespace.com` |
| TXT | `_gh-Operation-Forward-o` | from organization settings → Verified & approved domains | verifies the domain for the organization |
| TXT | `_github-pages-challenge-Operation-Forward` | from organization settings → Pages → Add a domain | stops anyone else using the domain on GitHub Pages |

In Cloudflare, set the A, AAAA and CNAME records to **DNS only** (grey cloud) so GitHub can issue
the HTTPS certificate. Leave the MX, SPF and `zoho-verification` records alone.

Once the records resolve: add a `CNAME` file containing `operationforward.org` (GitHub then
redirects `www` and `operation-forward.github.io` to it), turn on **Enforce HTTPS** in this
repository's Pages settings, and change the `og:image` URL in `index.html` to the new domain. Don't
add the `CNAME` file earlier: it would redirect the GitHub address to the Squarespace site.
