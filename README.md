# operation-forward.github.io

The Operation Forward website, served by GitHub Pages at https://operation-forward.github.io/.

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

The domain currently points at Squarespace (DNS is on Cloudflare; mail is Zoho and is not affected).
To serve this site there instead:

1. Organization settings → Pages → **Add a verified domain** `operationforward.org`, and add the
   TXT record GitHub shows in Cloudflare. This stops anyone else from claiming the domain on GitHub.
2. In Cloudflare, replace the Squarespace records: `www` → `CNAME operation-forward.github.io`, and
   the apex `operationforward.org` → `A` 185.199.108.153, 185.199.109.153, 185.199.110.153,
   185.199.111.153 (and `AAAA` 2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153,
   2606:50c0:8003::153). Set them to **DNS only** (grey cloud) so GitHub can issue the certificate.
3. This repository → Settings → Pages → Custom domain `www.operationforward.org`, then tick
   **Enforce HTTPS** once the certificate is issued.
4. Update the `og:image` URL in `index.html` to the new domain.
