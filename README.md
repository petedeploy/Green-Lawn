# Green Lawn Fertilizing: website redesign concept

A conversion-focused redesign concept for greenlawnfertilizing.com, prepared for review with the Green Lawn Fertilizing team.

**This is a design concept, not the live site.** Every page carries a concept banner, pages are marked `noindex`, and the estimate forms don't send data anywhere.

## Viewing it

Open `index.html` in a browser. Pages link to each other, and photos load from Green Lawn's existing HubSpot file library.

## Pages (17)

- `index.html`: homepage
- `about.html`, `free-estimate.html`
- Service areas: `pennsylvania.html`, `new-jersey.html`, `delaware.html`
- Services: `lawn-care-program.html`, `natural-program.html`, `tree-shrub-care.html`, `mosquito-control.html`, `aeration-seeding.html`, `flea-tick-control.html`, `fungicide-program.html`, `grub-control.html`, `lime-applications.html`, `commercial-services.html`, `pest-control.html`

Shared styles and behavior live in `assets/style.css` and `assets/site.js`.

## Design system

- Neutral surfaces. Deep green appears once per page, on the final call to action.
- Orange is reserved for things you can click.
- Type: Bitter (headings) and Figtree (body), standing in for Clarendon and Europa.
- Every page uses the same conversion pattern: two-step estimate form in the hero, proof beside each ask, "how it works", objection-handling FAQ (with FAQPage schema), related services, final CTA.

## Content to fill in before launch

Items marked with orange tags on the pages:

- Contract and cancellation terms (homepage FAQ)
- Phone hours (final CTA)
- Real Google reviews for the results section
- Town and program for the before/after photo
- Testimonial text for the Commercial page (the current site has two)
- Mosquito / Flea & Tick / Yard Guard PRO package contents (the current page lists the same coverage under all three)
- New Jersey pre-pay offer terms
- Confirm the "2010" milestone on the About page

## Rebuilding

The pages are generated from `build/build.py` (content and templates in one file):

```
python3 build/build.py
```
