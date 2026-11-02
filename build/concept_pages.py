"""Concept-only pages: the My Lawn customer portal and the How it works systems map.
Not redesigns of live pages. Kept out of the sitemap and linked from the concept banner and footer."""
from build import page, img, e, P, ICON, LAST, BRANCHES


def build_portal():
    LAST["og"] = img(P["tech92"], 1200)
    hist = "".join(f'<li><div class="h-date"><b>{d}</b><span>{r}</span></div><div><p class="h-what">{w}</p><p class="h-note">{n}</p></div></li>' for d, r, w, n in [
        ("May 26", "Round 5", "Slow-release fertilizer, broadleaf weed spot treatment", "Technician note: “Clover along the driveway edge treated. The back corner is thin. Ask me about seeding this fall.”"),
        ("May 12", "Soil test", "Soil pH tested at 5.6", "Below the 6.0 to 7.0 range. A lime recommendation is waiting for your OK."),
        ("Apr 21", "Round 4", "Fertilizer, early-summer grub prevention", "Lawn flag left. Summary texted and emailed."),
        ("Mar 30", "Round 3", "Fertilizer, broadleaf weed control", "Lawn flag left. Summary texted and emailed.")])
    days = "".join(f'<button type="button" class="chip-btn" data-day="{d}">{d}</button>' for d in ["Wed, Jun 17", "Thu, Jun 18", "Mon, Jun 22"])
    body = f'''<section class="portal-top">
  <div class="wrap">
    <div class="demo-note">{ICON["lock"]}<span><b>Portal concept.</b> A sample account with made-up data. Nothing here touches a real account.</span></div>
    <div class="p-hello">
      <div><p class="crumb-d">My Lawn</p><h1>Hi, Jordan.</h1><p class="lede">The Green Lawn Program · 214 Sample Ln, West Chester, PA</p></div>
      <div class="p-stats"><div><b>5 of 8</b><span>visits done</span></div><div><b>$0.00</b><span>balance</span></div><div><b>Jun 16</b><span>next visit</span></div></div>
    </div>
  </div>
</section>
<section class="portal" data-portal>
  <div class="wrap p-grid">
    <div class="p-main">
      <article class="p-card next" data-box="visit">
        <div class="p-label">Next visit</div>
        <h2>Tuesday, June 16</h2>
        <p class="p-sub">Round 6 of 8 · Slow-release fertilizer and weed spot treatment · Morning, 8 to 11 am</p>
        <div class="p-weather">{ICON["drop"]}<span>Rain is possible that morning. If we move your visit, you’ll get a text with the new day.</span></div>
        <div class="p-acts" data-acts>
          <button class="btn btn-primary" type="button" data-act="skip">Skip this visit</button>
          <button class="btn btn-line" type="button" data-act="move">Pick another day</button>
          <button class="btn btn-line" type="button" data-act="note">Note for your technician</button>
        </div>
        <div class="p-days" data-days hidden><p>Open days on your route:</p><div>{days}</div></div>
        <div class="p-notebox" data-notebox hidden><label>Note for your technician<textarea rows="3" placeholder="Gate code, dogs in the yard, a spot to look at"></textarea></label><button class="btn btn-primary" type="button" data-act="save-note">Save note</button></div>
        <p class="p-status" data-status role="status" aria-live="polite"></p>
      </article>

      <article class="p-card approve" data-box="approve">
        <div class="p-label warn">Needs your OK</div>
        <h2>Lime application</h2>
        <p>Your soil tested at pH 5.6 on May 12. Lime would bring it toward 6.0 to 7.0, so your lawn can use the fertilizer you’re paying for.</p>
        <div class="p-price"><b>$65</b><span>one time, applied at your next visit</span></div>
        <p class="p-rule">{ICON["lock"]}<span>Nothing outside your program is applied unless you approve it here.</span></p>
        <div class="p-acts" data-acts>
          <button class="btn btn-primary" type="button" data-act="yes">Approve lime</button>
          <button class="btn btn-line" type="button" data-act="no">Not this year</button>
        </div>
        <p class="p-status" data-status role="status" aria-live="polite"></p>
      </article>

      <article class="p-card">
        <div class="p-label">Service history</div>
        <ol class="p-hist">{hist}</ol>
      </article>
    </div>

    <aside class="p-side">
      <article class="p-card">
        <div class="p-label">Billing</div>
        <div class="p-row"><span>Next charge</span><b>$58 after your next visit</b></div>
        <div class="p-row"><span>Autopay</span><b>Visa ending 4242</b></div>
        <h3 class="p-h3">Service credit: $45.00</h3>
        <ol class="p-track"><li class="done"><b>Requested</b><span>May 28</span></li><li class="done"><b>Approved</b><span>May 29</span></li><li class="done"><b>Sent to your card</b><span>Jun 2</span></li><li><b>On your statement</b><span>by Jun 7</span></li></ol>
      </article>

      <article class="p-card" data-box="plan">
        <div class="p-label">Your plan</div>
        <p>Need a break, or done for good? Do it here. No phone call needed.</p>
        <div class="p-acts col" data-acts>
          <button class="btn btn-line" type="button" data-act="pause">Pause for the rest of the season</button>
          <button class="btn btn-line danger" type="button" data-act="cancel">Cancel my program</button>
        </div>
        <div class="p-confirm" data-confirm hidden>
          <p><b>Cancel the Green Lawn Program?</b> Your 3 remaining visits come off the schedule right away.</p>
          <div class="p-acts"><button class="btn btn-primary" type="button" data-act="confirm-cancel">Yes, cancel</button><button class="btn btn-line" type="button" data-act="keep">Keep my program</button></div>
        </div>
        <p class="p-status" data-status role="status" aria-live="polite"></p>
      </article>

      <article class="p-card">
        <div class="p-label">Text and email alerts</div>
        <label class="tgl"><input type="checkbox" checked><span>Text the day before a visit</span></label>
        <label class="tgl"><input type="checkbox" checked><span>Text when my technician is on the way</span></label>
        <label class="tgl"><input type="checkbox" checked><span>Visit summary by email</span></label>
      </article>

      <article class="p-card chop" data-box="chop">
        <div class="p-label">Giving back</div>
        <p class="chop-n"><b>$50</b> sent to Children’s Hospital of Philadelphia from your 2 referrals.</p>
        <p>Every friend who signs up sends $25 to CHOP and gets you a $25 gift card.</p>
        <div class="p-acts"><button class="btn btn-primary" type="button" data-act="share">Copy my referral link</button></div>
        <p class="p-status" data-status role="status" aria-live="polite"></p>
      </article>
    </aside>
  </div>
</section>
<section class="alt">
  <div class="wrap center">
    <h2>Every button here replaces a phone call.</h2>
    <p class="lede">Most of them fix a complaint customers post publicly today.</p>
    <div class="how-cta"><a class="btn btn-primary" href="@@systems@@">See how the systems fit together</a></div>
  </div>
</section>
'''
    page("portal", "My Lawn | Customer Portal Concept | Green Lawn Fertilizing",
         "Concept for a self-serve customer portal: skip or move a visit, approve add-ons, track credits, pause or cancel online.",
         body, float_cta=False)


def build_systems():
    LAST["og"] = img(P["tech92"], 1200)
    flow = "".join(f'<li><span class="f-n">{i}</span><b>{e(t)}</b><span>{e(d)}</span></li>' for i, (t, d) in enumerate([
        ("Estimate form", "Address first, then contact details"),
        ("CRM record", "Contact and deal created in HubSpot"),
        ("Branch routing", f"ZIP code assigns one of {BRANCHES} branches"),
        ("Fast follow-up", "A rep calls back within minutes in business hours"),
        ("Program booked", "Customer and program created in the field service system"),
        ("Route and visit", "Technician app, lawn flag, photo summary"),
        ("Portal and alerts", "Texts, visit history, approvals, billing")], 1))
    groups = [
        ("Customer-facing", ["Website on HubSpot CMS", "My Lawn portal", "Text and email alerts"]),
        ("Revenue", ["HubSpot CRM", "Phone system and call tracking", "Referral and prepay programs"]),
        ("Operations", ["Field service platform for scheduling, routing and billing (to confirm)", "Technician mobile app", "Fleet telematics for 200+ vehicles"]),
        ("Back office", ["Payments and accounting", "HR, recruiting and seasonal onboarding", "Licensing and product-use records"]),
        ("Data", ["One reporting layer across everything above", "Branch and route dashboards"]),
    ]
    gcards = "".join(f'<div class="card sys"><h3>{e(t)}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in xs)}</ul></div>' for t, xs in groups)
    rows = "".join(f'<tr><td data-l="What customers say">{e(a)}</td><td data-l="Why it happens">{e(b)}</td><td data-l="The fix">{e(c)}</td><td data-l="Measure">{e(d)}</td></tr>' for a, b, c, d in [
        ("Charged for a treatment they didn’t want", "The opt-out lives in the fine print of a bill", "Add-ons need an Approve tap in the portal", "Disputed charges per 1,000 visits"),
        ("Cancellation not honored", "Cancelling is a phone call and a manual update", "Self-serve cancel with a confirmation number, and the schedule updates itself", "Visits after cancellation: zero"),
        ("Refunds and credits slow to arrive", "Credits are tracked by hand", "A credit tracker the customer can see", "Days from request to posted credit"),
        ("A booked visit never happened", "The same record is typed into more than one system", "One record from form to route", "Missed appointments"),
        ("Hard to reach anyone", "Phone is the only channel", "Skip, move, approve and pay online, with a text at each step", "Calls per customer per season"),
    ])
    kpis = "".join(f'<div class="card"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in [
        ("Speed to lead", "Minutes from form submit to first call."),
        ("Estimate to sale", "Share of estimates that become programs."),
        ("Renewal rate", "Customers who come back next season."),
        ("Revenue per route day", "Route density across 200+ trucks."),
        ("Self-serve share", "Changes made online instead of by phone."),
        ("Credit cycle time", "Days to make a customer whole."),
    ])
    body = f'''<section class="sys-top">
  <div class="wrap">
    <p class="crumb-d">Concept · How it works</p>
    <h1>What sits behind the website.</h1>
    <p class="lede">A new website brings in more estimate requests. What happens after the form decides whether they become customers who renew. This page maps that path and the systems behind it.</p>
    <p class="demo-note">{ICON["lock"]}<span>Anything marked “to confirm” is an assumption for discussion.</span></p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head solo"><h2>From estimate request to renewing customer</h2><p class="lede">Seven steps, one customer record the whole way through.</p></div>
    <ol class="flow">{flow}</ol>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="sec-head solo"><h2>The systems map</h2><p class="lede">The first thing to confirm is which field service platform runs routing and billing today. Everything else connects to it.</p></div>
    <div class="sys-grid">{gcards}</div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head solo"><h2>Complaints this fixes</h2><p class="lede">Drawn from public customer complaints. Each one traces back to a system, not a person.</p></div>
    <div class="tbl-wrap"><table class="fix">
      <thead><tr><th>What customers say</th><th>Why it happens</th><th>The fix</th><th>Measure</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
    <div class="how-cta"><a class="btn btn-line" href="@@portal@@">See the My Lawn portal</a></div>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="sec-head solo"><h2>Six numbers on one dashboard</h2><p class="lede">Every branch, every week.</p></div>
    <div class="grid-3">{kpis}</div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head solo"><h2>The first 90 days</h2></div>
    <ol class="steps">
      <li><h3>Days 1 to 30: Listen and map</h3><p>Ride along with technicians, sit with customer service, and map every system and who owns it.</p></li>
      <li><h3>Days 31 to 60: Quick wins</h3><p>Route web leads by ZIP, turn on visit texts, and stop applying add-ons nobody approved.</p></li>
      <li><h3>Days 61 to 90: Roadmap</h3><p>Portal, reporting and platform decisions, paid for first by consolidating tools we don’t need.</p></li>
    </ol>
  </div>
</section>
'''
    page("systems", "How It Works | Systems Concept | Green Lawn Fertilizing",
         "Concept: the path from estimate request to renewing customer, and the systems behind it.", body, float_cta=False)
