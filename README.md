# Green Lawn Fertilizing: website redesign concept

A conversion- and SEO-focused redesign concept for greenlawnfertilizing.com, prepared for review with the Green Lawn Fertilizing team.

**This is a design concept, not the live site.** Every page carries a concept banner, pages are marked `noindex`, `robots.txt` blocks crawlers, and the estimate forms don't send data anywhere.

## Viewing it

Open `index.html` in a browser. Pages link to each other.

Photos load from Green Lawn's HubSpot file library unless you've downloaded local copies. **Before a demo, run `python3 build/fetch_images.py` and rebuild**, so the site doesn't depend on wifi or on files being renamed on their end. The build uses a local copy whenever one exists and falls back to HubSpot otherwise.

## Pages (17 redesigned + 2 concept), at the live site's URL paths

Every page sits at the same path as its live counterpart, so a launch needs no redirects and keeps existing rankings and backlinks.

| Page | Path |
|---|---|
| Homepage | `/` |
| About | `/about-green-lawn-fertilizing` |
| Free estimate | `/free-lawn-care-estimate` |
| Service areas | `/lawn-care/pennsylvania`, `/lawn-care/new-jersey`, `/lawn-care/delaware` |
| Services | `/services/lawn-care-programs`, `/services/green-lawn-natural-program`, `/services/tree-shrub-program`, `/services/mosquito-control`, `/services/aeration-seeding`, `/services/flea-tick-program`, `/services/fungicide-program`, `/services/grub-control`, `/services/lime-application`, `/services/green-pest-solutions`, `/commercial-services` |

Two concept-only pages show what sits behind the site. They're linked from the concept banner, the footer and **Customer login**, and they're kept out of the sitemap:

| Page | Path | What it shows |
|---|---|---|
| My Lawn portal | `/concept/my-lawn` | Skip or move a visit, notes for the technician, approve or decline add-ons, a credit tracker, self-serve pause and cancel with a confirmation number, alert settings, and CHOP referral impact. Sample account with made-up data; every action updates the page only. |
| How it works | `/concept/how-it-works` | The path from estimate request to renewing customer, a systems map, the public complaints each fix addresses with a measure for each, a six-number dashboard, and a first-90-days plan. |

Pages the concept doesn't redesign (blog, Lawn Libraries, guides, FAQ, testimonials, special offers, referral, careers and others) are linked at their live URLs from the Learning Center menu and the footer, so internal links to them are kept.

Shared styles and behavior live in `assets/style.css` and `assets/site.js`.

## SEO in the build

- **H1s:** keyword and region ("Mosquito Control in PA, NJ & DE"), with the benefit headline shown as large display text below it.
- **Titles:** `[Service] in PA, NJ & DE | From $[price] | Green Lawn Fertilizing`. Meta descriptions come from each page's intro.
- **Structured data (JSON-LD):** `LocalBusiness` (headquarters, phone, founding, service area, social profiles) on every page, `Service` on service and area pages (with starting price where published), `BreadcrumbList` on every page, `WebSite` on the homepage, and `FAQPage` on every FAQ. No self-hosted star-rating markup, since Google doesn't show stars for a business's own reviews.
- **Technical:** canonical URL and Open Graph tags on every page, `width`/`height` on every image to prevent layout shift, descriptive alt text, lazy-loaded images below the fold, `sitemap.xml` listing the canonical URLs.
- **Local trust:** license numbers for PA, NJ and DE in every footer.

## Design system

- Neutral surfaces. Deep green appears once per page, on the final call to action.
- Orange is reserved for things you can click.
- Type: Bitter (headings) and Figtree (body), standing in for Clarendon and Europa.
- Every page uses the same conversion pattern: two-step estimate form in the hero, proof beside each ask, "how it works", objection-handling FAQ, related services, final CTA.
- Each service page's estimate form asks a question specific to that service ("Want your evenings outside back?" on Mosquito Control).

## Content to fill in before launch

The default build is **demo-clean**: placeholder reviews, the commercial testimonials, the contract FAQ and all orange content tags are hidden, so the concept can be shown as-is. Build with `--show-todos` to bring them back as a checklist:

- Contract and cancellation terms (homepage FAQ)
- Phone hours (final CTA)
- Real Google reviews for the results section (the demo build shows the rating summary instead)
- Town and program for the before/after photo
- Testimonial text for the Commercial page (the current site has two)
- Mosquito / Flea & Tick / Yard Guard PRO package contents (the current page lists the same coverage under all three)
- New Jersey pre-pay offer terms
- Confirm the "2010" milestone on the About page

Company figures (customer count, team size, branches) live in one place at the top of `build/build.py`, so pages can't drift apart.

Also needed for local SEO: addresses, phone numbers and Google Business Profile links for the 7 branches, so each can get its own page and `LocalBusiness` entry.

## Rebuilding

The pages are generated from `build/build.py` (content and templates) and `build/concept_pages.py` (the two concept pages). Edit `build/style.css` and `build/site.js`; the build copies them into `assets/`.

```
python3 build/build.py               # relative links; opens straight from disk
python3 build/build.py --clean-urls  # root-relative links (/services/...) for a web server
python3 build/build.py --show-todos  # show placeholders and orange content tags
python3 build/fetch_images.py        # one-time: download photos, badges and logo into assets/img/
```
