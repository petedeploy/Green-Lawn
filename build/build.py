#!/usr/bin/env python3
"""Builds the Green Lawn Fertilizing redesign concept into ../site/"""
import os, shutil, html, json
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..")
PHONE = "888-581-5296"
TEL = "tel:8885815296"

def img(path, w=1600):
    """HubSpot resized image URL from a hubfs path (unencoded)."""
    enc = quote(path)
    name = quote(path.split("/")[-1])
    return f"https://www.greenlawnfertilizing.com/hs-fs/hubfs/{enc}?width={w}&name={name}"

P = {
 "grill": "Lifestyle Photos 2025/customer-man-woman-lifestyle-grill-yard122.jpg",
 "tech92": "Customer and Tech Photos - 2025/tech-customer-talking-service-help92.jpg",
 "tech96": "Customer and Tech Photos - 2025/tech-customer-talking-service-help96.jpg",
 "custtech": "Customer and Tech Photos - 2025/customer and technician talking about lawn care.jpeg",
 "fert": "Lawn Service Photos - 2025/green lawn being fertilized by a certified technician.jpeg",
 "natural": "walking in a natural lawn.jpeg",
 "kids": "kids-lawn-running-2.png",
 "dogs": "Photos/Customers/green lawn customers with dogs-1.jpeg",
 "dogskids": "Green Lawn Customers with dogs and kids.jpg",
 "tree13": "Tree and Shrub Service - 2025/tech-tree-shrub-service-application13.jpg",
 "tree25": "Tree and Shrub Service - 2025/tech-tree-shrub-service-application25.jpg",
 "mosq": "Mosquito Service Photos - 2025/Technician treating mulch bed for mosquitos-1.jpg",
 "grillout": "Lifestyle Photos 2025/man and woman grilling outside.jpeg",
 "aer": "aeration & seeding at a home-1.png",
 "aerba": "aeration seeding results before after photos.png",
 "dogcouple": "a man and a woman sitting with dog in lawn.jpg",
 "fungal": "fungal-damage-comparison.jpg",
 "grubs": "lawn-grubs.jpg",
 "lime": "lawn technician pouring lime out of a glass jar.jpeg",
 "limestone": "granular limestone-1.png",
 "comm": "commercial-lawn-tech-service-sky2-1.png",
 "commlawn": "commercial lawn care services.png",
 "pest": "Imported_Blog_Media/pest-control-technician-with-customer-e1673970993757-768x768-1.jpg",
 "custlawn": "customer lawn.png",
 "team": "Company Events/green lawn fertilizing team photo.png",
 "y2010": "green lawn fertilizing 2010.jpg",
 "hq": "green-lawn-fertilizing-headquarters-west-chester-pa.jpg",
 "ba": "Before-and-after lawn result-1.png",
}
LOGO = "https://www.greenlawnfertilizing.com/hubfs/Logos/GLF%20-%20Logo%20-%20SVG.svg"
BADGES = [
 ("AngiesList2023-540x540-3.png", "Angi Super Service Award"),
 ("Untitled design (18).png", "Forbes Home Best of 2024"),
 ("bbb1.png-1.webp", "BBB Accredited Business"),
 ("PBJ-best-places-to-work-250x250.png", "Philadelphia Business Journal Best Places to Work"),
 ("Top-100-Shield_toro-high-res copy.webp", "Lawn and Landscape Top 100"),
 ("Philly100-new-250x250.png", "Philadelphia 100 winner"),
 ("Fast 50 - 540x540.png", "Fast 50"),
 ("LM150.png-1.webp", "Landscape Management LM150"),
 ("Chamber-badge-250x250.png-1.webp", "Chamber of Commerce Customer Service Excellence Award"),
]

def e(s):  # escape text
    return html.escape(s, quote=True)

ICON = {
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
 "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
 "chev": '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m2.5 4.5 3.5 3.5 3.5-3.5"/></svg>',
 "menu": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
 "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10Z"/><path d="M2 21c0-3 1.9-5.4 5.1-6"/></svg>',
 "bug": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="8" y="6" width="8" height="14" rx="4"/><path d="m19 7-3 2M5 7l3 2M19 19l-3-2M5 19l3-2M20 13h-4M4 13h4M10 4l1 2M14 4l-1 2"/></svg>',
 "sprout": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 20h10M12 20v-8M12 12C12 8 9 6 5 6c0 4 3 6 7 6ZM12 12c0-3 2-5 6-5 0 3-2 5-6 5Z"/></svg>',
 "drop": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.7 6.3 9.4a7 7 0 1 0 11.4 0Z"/></svg>',
 "money": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 12h.01M18 12h.01"/></svg>',
}

# ---------------- Services data ----------------
S = [
 dict(slug="lawn-care-program", name="The Green Lawn Program", nav="Fertilization and weed control",
  chip="Lawn care", card="Eight seasonally timed visits of fertilizer, weed control and grub prevention.",
  price="$54", price_note="per application, based on a 3,000 sq ft lawn", hero="custtech", card_img="fert",
  h1="Thicker grass. Fewer weeds. Eight visits a year.",
  lede="Our signature program feeds your lawn and controls weeds on a schedule built for the PA, NJ and DE growing season. You don’t need to be home.",
  checks=["7 fertilizer applications plus grub prevention","Unlimited weed control and free service calls","100% satisfaction guarantee"],
  inc_h="Everything your lawn needs, in one program", inc_img="fert",
  included=[("7 fertilizing applications","Timed to what your lawn needs each season."),
            ("1 grub control application","Applied in early summer, before grubs damage roots."),
            ("Unlimited weed control","Pre-emergent crabgrass control and broadleaf treatments."),
            ("Free service calls","Weeds show up between visits? We come back at no charge."),
            ("Thatch density analysis","A check on the thatch layer that can choke grass roots.")],
  rounds=[("Rounds 1 to 3","Spring, March to June",["Fertilizer to wake up winter-weary grass","Pre-emergent control to stop crabgrass","Broadleaf control for dandelions and clover"]),
          ("Rounds 4 to 7","Summer, June to September",["Slow-release fertilizer for deep green color","Weed spot treatments as needed","Early-summer grub control"]),
          ("Round 8","Winter prep, September to October",["Heavy feeding to build root strength","Earlier green-up next spring","Protection through winter"])],
  guarantee=("100% Satisfaction Guarantee","If you’re not happy, we’ll come back. It’s that simple."),
  faqs=[("What does the program include?","Seven fertilizer treatments, one grub control application, unlimited weed control, free service calls and a thatch density analysis."),
        ("How often will you service my lawn?","Eight visits a year, about every 4 to 6 weeks, timed to the growing season."),
        ("Do I need to be home?","No. Your technician leaves a lawn flag and a service summary after every visit."),
        ("What if weeds show up between visits?","Call us. Service calls are free."),
        ("Is it safe for kids and pets?","Yes, once the application dries. On a dry day that’s usually within a couple of hours."),
        ("What if it rains after a treatment?","Light rain helps the lawn absorb fertilizer. Heavy rain right after a weed spray can reduce how well it works. If you’re unsure, contact us and we’ll come back if needed."),
        ("When will I see results?","Weeds usually curl and die within 10 to 14 days. Grass gets thicker and greener over the first few treatments.")],
  related=["natural-program","aeration-seeding","tree-shrub-care"]),

 dict(slug="natural-program", name="Natural Program", nav="100% organic fertilizer",
  chip="Natural program", card="Seven applications of 100% organic fertilizer for a greener lawn without synthetic products.",
  hero="natural", card_img="natural",
  h1="A green lawn, grown the natural way.",
  lede="Seven applications of 100% organic, slow-release fertilizer that build healthier soil and thicker grass over time.",
  checks=["7 applications of 100% organic fertilizer","Non-burning, slow-release organic nitrogen","Ready for kids and pets once it dries"],
  inc_h="What’s in the Natural Program", inc_img="kids",
  included=[("7 organic applications","100% organic fertilizer that meets EPA standards."),
            ("Slow-release organic nitrogen","Feeds steadily and won’t burn your lawn."),
            ("Soil-first approach","Builds soil and grass health for the long run."),
            ("Pairs with aeration and seeding","Thicker turf crowds out weeds faster.")],
  honest=("What to expect","The Natural Program doesn’t use chemical weed control, so it isn’t eligible for weed-control service calls. Results build more slowly than our traditional program, and thick, healthy grass does the weed control over time."),
  faqs=[("How is it different from the traditional program?","The traditional program uses conventional fertilizer and weed control for faster results. The Natural Program uses organic products and focuses on long-term soil and grass health, so results take longer."),
        ("Is it family and pet friendly?","Yes. Your lawn is ready to enjoy once the application dries."),
        ("Can I combine it with aeration and seeding?","Yes. The two work well together."),
        ("Does it control weeds and crabgrass?","Not directly. Instead of chemical weed removal, it grows thick grass that crowds weeds out."),
        ("Is it as effective as the traditional program?","Yes, in a different way. Results take longer and weed control is limited, but your lawn stays green and healthy without traditional chemicals.")],
  related=["lawn-care-program","aeration-seeding","flea-tick-control"]),

 dict(slug="tree-shrub-care", name="Tree & Shrub Care", nav="Seven visits of plant health care",
  chip="Tree & shrub", card="Seven visits of feeding plus pest and disease protection for your landscape.",
  hero="tree13", card_img="tree13",
  h1="Protect the trees and shrubs you’ve spent years growing.",
  lede="Seven visits from early spring through late fall. State-certified technicians feed, inspect and protect your landscape before pests and disease do damage.",
  checks=["Deep-root, soil-injected fertilization","Pest and disease treatments every season","A full inspection at every visit"],
  inc_h="Seven visits, start to finish", inc_img="tree25",
  included=[("Deep-root feeding","Soil-injected liquid fertilizer for trees and larger shrubs."),
            ("Granular feeding","For ground covers and shallow-rooted plants."),
            ("Pest control","Horticultural oils for mites, aphids, scale and beetles."),
            ("Disease control","Treatments for leaf spot, powdery mildew and other fungal disease."),
            ("Inspection every visit","We catch stress early and adjust treatments to real conditions."),
            ("Optional winter protection","Anti-desiccant for azaleas, rhododendrons, pieris, hollies and boxwoods.")],
  chips_h="Pests and diseases we treat", chips=["Mites","Aphids","Scale","Beetles","Leaf spot","Powdery mildew"],
  honest=("Pruning isn’t included","The program covers feeding and plant protection. If your trees or shrubs need pruning, your technician will recommend it separately."),
  faqs=[("What does the program include?","Seven seasonal visits with pest and disease treatments, deep-root fertilization and seasonal sprays."),
        ("Why use a professional?","Certified technicians spot pest, disease and weather stress early, before it turns into a costly replacement."),
        ("How often are treatments applied?","Seven visits spaced across the growing season, timed to each plant’s needs."),
        ("Which pests and diseases are covered?","Mites, aphids, scale, beetles and fungal diseases such as leaf spot and powdery mildew."),
        ("When is the best time to fertilize?","Spring and fall, with a late-fall feeding to strengthen roots before winter."),
        ("Does it include pruning?","No. We’ll recommend pruning separately if your plants need it.")],
  related=["lawn-care-program","mosquito-control","lime-applications"]),

 dict(slug="mosquito-control", name="Mosquito Control", nav="Up to 7 visits, spring to fall",
  chip="Mosquito control", card="Treatments every 3 to 4 weeks where mosquitoes rest and breed.",
  price="$77", price_note="per visit", hero="grillout", card_img="mosq",
  h1="Take your backyard back from mosquitoes.",
  lede="Up to seven visits, about every 3 to 4 weeks from spring into fall. We treat where mosquitoes rest and breed, so you get fewer bites.",
  checks=["State-certified mosquito technicians","Treats mulch beds, hedges, decks and eaves","Special event sprays for parties"],
  inc_h="How we cut down the bites", inc_img="mosq",
  included=[("Up to 7 timed visits","Service usually starts around April, before summer peaks."),
            ("Resting-spot treatment","Mulch beds, hedges, tall grass, ground cover, trees and shrubs."),
            ("Under decks and eaves","The shady spots mosquitoes hide during the day."),
            ("Special event spraying","A fast-acting, odor-free treatment before your party or gathering.")],
  plans=[("Mosquito Control","$77","per visit","Mosquito treatments every 3 to 4 weeks.",False),
         ("Yard Guard PRO","$99","per visit","Mosquito, flea and tick control together. Up to 22% in savings.",True),
         ("Flea & Tick Control","$50","per visit","Flea and tick treatments around your lawn.",False)],
  faqs=[("How long does a treatment last?","About 3 to 4 weeks. After that, activity can return without another treatment."),
        ("How often should I treat?","Every 3 to 4 weeks from spring through early fall."),
        ("Is it safe for kids and pets?","Yes, once dry. Keep children and pets off treated areas for about an hour."),
        ("Does it work?","Regular professional treatments noticeably reduce bites."),
        ("When should I start?","Around April, before summer populations peak.")],
  related=["flea-tick-control","tree-shrub-care","lawn-care-program"]),

 dict(slug="aeration-seeding", name="Aeration & Seeding", nav="Thicken thin, patchy lawns",
  chip="Aeration & seeding", card="Core aeration and seeding in one pass to fill thin and bare spots.",
  hero="tech96", card_img="aer",
  h1="Fill in thin spots and grow a thicker lawn.",
  lede="Core aeration and seeding in one pass. Our machine pulls soil plugs and drops premium seed right into the holes.",
  checks=["Seed blends chosen for PA, NJ and DE lawns","Best done late summer to early fall","100% service guarantee"],
  inc_h="Aeration and seeding, done in one pass", inc_img="aerba", inc_img_wide=True,
  included=[("Core aeration","Pulls soil plugs to relieve compaction so air, water and nutrients reach roots."),
            ("Precision seeding","Seed goes straight into the holes, where it has the best chance to grow."),
            ("Regional seed blends","Premium seed selected for our local climate."),
            ("Aftercare instructions","Simple watering and mowing guidance, plus ongoing support.")],
  guarantee=("100% Service Guarantee","Aeration and seeding is backed by our service guarantee."),
  faqs=[("What is aeration, and why does my lawn need it?","Aeration pulls small plugs of soil to relieve compaction, so air, water and nutrients reach the roots."),
        ("When is the best time?","Late summer to early fall is ideal. Spring is a backup option."),
        ("How often should I aerate?","Most lawns need it once a year. Heavy soil or high-traffic areas can benefit from more."),
        ("How soon can I mow?","Wait two to three weeks."),
        ("When will I see new grass?","Usually within 1 to 3 weeks, depending on grass type and watering."),
        ("Will it damage sprinklers or an invisible dog fence?","Mark your sprinkler heads and tell the crew where the dog fence runs."),
        ("Should I rake up the soil plugs?","No. They break down on their own and feed the soil.")],
  related=["lawn-care-program","natural-program","lime-applications"]),

 dict(slug="flea-tick-control", name="Flea & Tick Control", nav="Six treatments a year",
  chip="Flea & tick", card="Six treatments a year that target the shady edges where ticks wait.",
  price="$50", price_note="per visit", hero="dogcouple", card_img="dogcouple",
  h1="A yard your kids and dogs can play in, with fewer ticks.",
  lede="Six treatments a year, about every 4 to 6 weeks in the warm season, focused on the shady edges where fleas and ticks wait.",
  checks=["Kills fleas and ticks on contact","Targets shade, mulch beds and lawn edges","Starts around April, before peak season"],
  callout=("82%","of deer ticks found on lawns were within 9 feet of the lawn edge, especially near woods, stone walls or plantings.","That’s why we focus on edges."),
  inc_h="A barrier around your lawn", inc_img="dogs",
  included=[("6 treatments a year","About every 4 to 6 weeks through the warm season."),
            ("Edge and shade focus","Mulch beds, shady spots and lawn edges, where ticks wait."),
            ("Prevents new infestations","Kills on contact and helps stop the next wave."),
            ("Add mosquitoes with Yard Guard PRO","One plan for mosquitoes, fleas and ticks.")],
  faqs=[("How does the treatment work?","It kills fleas and ticks on contact and helps prevent new infestations, focusing on shady areas, mulch beds and lawn edges."),
        ("How often are treatments applied?","Six times a year, about every 4 to 6 weeks in the warm season."),
        ("Is it safe for kids and pets?","Yes, once dry. Keep children and pets off the lawn for a couple of hours."),
        ("When should I start?","Around April, before summer peak activity."),
        ("Why treat for fleas and ticks?","They carry disease and multiply quickly. Ticks can survive up to 200 days without food or water."),
        ("Does it help with mosquitoes?","Not directly. Add mosquito control, or choose Yard Guard PRO to cover all three.")],
  related=["mosquito-control","pest-control","lawn-care-program"]),

 dict(slug="fungicide-program", name="Fungicide Program", nav="Lawn disease control",
  chip="Lawn disease", card="Prevent and treat brown patch, dollar spot, red thread and more.",
  hero="fert", card_img="custlawn",
  h1="Stop lawn disease before it spreads.",
  lede="Brown patches and tan spots are often fungus. We prevent and treat the turf diseases common in our region.",
  checks=["Preventive and curative programs","Targets dollar spot, brown patch, red thread and more","Lawn program customers get fungus checks every visit"],
  inc_h="Two ways we fight lawn fungus", inc_img="fungal", inc_img_wide=True,
  included=[("Preventive program","Protects lawns at risk before disease shows up."),
            ("Curative program","Treats lawns that already show fungus."),
            ("Checks at every visit","Lawn program technicians note fungus activity and tell you what’s needed.")],
  diseases=[("Dollar spot","Light tan or white dead patches. Often shows up in humid summer weather or when the lawn is low on nitrogen."),
            ("Leaf spot","Brown spots or a burned-out look. Tall fescue and ryegrass are prone, from late spring through summer."),
            ("Red thread","Red or pink blotches, most common in perennial ryegrass and fine fescue. Low nitrogen and poor drainage contribute."),
            ("Brown patch","Circular brown areas in the lawn."),
            ("Summer patch","Patches of dying grass during summer heat.")],
  faqs=[("What causes lawn fungus?","Humidity, low nitrogen, mowing too short, poor drainage and the wrong watering schedule all raise the risk."),
        ("Which grasses are most at risk?","Tall fescue, ryegrass and fine fescue, especially in summer."),
        ("Is fungicide part of the Green Lawn Program?","Fungicide is a separate program. If you’re on our lawn program, your technician watches for fungus at every visit and tells you if treatment is needed.")],
  related=["lawn-care-program","aeration-seeding","lime-applications"]),

 dict(slug="grub-control", name="Grub Control", nav="Guaranteed for the year",
  chip="Grub control", card="One preventive application that stops grubs before they eat roots.",
  hero="custlawn", card_img="grubs",
  h1="Stop grubs before they eat your lawn’s roots.",
  lede="One preventive application in late spring or early summer, before grubs start feeding. Guaranteed for the year.",
  checks=["Pre-emergent grub preventative","Applied late spring to early summer","Guaranteed for the year"],
  inc_h="Why grubs are worth preventing", inc_img="grubs",
  included=[("They feed on roots","Grubs are beetle larvae that chew grass roots below the surface."),
            ("Damage shows up late","By the time turf dies off, the roots are already gone."),
            ("Prevention is the fix","One well-timed application stops the damage before it starts."),
            ("Included in the Green Lawn Program","Program customers already get a grub control application.")],
  guarantee=("Guaranteed for the year","Grub control applications are guaranteed for the full year."),
  faqs=[("What are grubs?","Beetle larvae that feed on grass roots. They’re among the most widespread and destructive lawn pests in the Northeast."),
        ("When is grub control applied?","Late spring or early summer, before grubs can damage turf."),
        ("Is it included in the Green Lawn Program?","Yes. The program includes one grub control application each year."),
        ("Is it guaranteed?","Yes. Grub control applications are guaranteed for the year.")],
  related=["lawn-care-program","fungicide-program","aeration-seeding"]),

 dict(slug="lime-applications", name="Lime Applications", nav="Balance acidic soil",
  chip="Lime", card="A free pH test, then lime to bring acidic soil back into balance.",
  hero="lime", card_img="lime",
  h1="Fix acidic soil so your lawn can use its food.",
  lede="Soil in PA, NJ and DE tends to run acidic. Lime brings pH back to the 6.0 to 7.0 range, where grass roots absorb nutrients best.",
  checks=["Free soil pH test","Add to your lawn program or book it on its own","Targets a pH of 6.0 to 7.0"],
  callout=("6.0–7.0","is the soil pH range where our grass types take up nutrients best.","Our local soils usually test below it."),
  inc_h="Why our soil runs acidic", inc_img="limestone",
  included=[("Heavy rainfall","Rain leaches calcium and magnesium, the minerals that buffer acidity."),
            ("Acid rain","Air pollutants make rainfall more acidic."),
            ("Decaying organic matter","Breaking-down leaves and roots release acidity into the soil."),
            ("The result","Fertilizer you’ve paid for stays locked up in the soil.")],
  faqs=[("What is liming?","Applying a material such as limestone to reduce soil acidity and raise pH."),
        ("How does lime help my lawn?","In the right pH range, more nutrients are available to grass roots, so the lawn grows better."),
        ("Why is soil acidic in PA, NJ and DE?","Rainfall washes out buffering minerals, and acid rain and decaying organic matter add acidity."),
        ("What else does balanced pH do?","It improves nutrient availability, root growth, soil structure and soil microorganism activity."),
        ("How do I know if I need it?","We test your soil pH for free and recommend lime only if it will help.")],
  related=["lawn-care-program","aeration-seeding","natural-program"]),

 dict(slug="commercial-services", name="Commercial Services", nav="HOAs, offices, retail and more",
  chip="Commercial", card="Lawn programs for HOAs, corporate centers, retail, hotels and athletic fields.",
  hero="comm", card_img="comm",
  h1="Commercial lawn care your residents and tenants notice.",
  lede="Programs of 4 to 8 applications, built around your property. Licensed, insured and certified in Pennsylvania, New Jersey and Delaware.",
  checks=["Licensed, insured and certified in PA, NJ and DE","Reliable scheduling and reporting","Free service calls if the lawn isn’t right"],
  chips_h="Properties we serve", chips=["Corporate centers","HOAs","Townhome communities","Strip malls","Hotels","Athletic fields"],
  inc_h="Commercial services", inc_img="commlawn",
  included=[("The Green Lawn Program","4 to 8 applications combining fertilizer, pre-emergent, surface insect, broadleaf, grub and crabgrass control."),
            ("Aeration and seeding","Relieves compaction and thickens high-traffic turf."),
            ("Yard Guard PRO","Mosquito, flea and tick control."),
            ("Soil amendment","Corrects soil conditions holding your turf back."),
            ("Tree and shrub care","Feeding, pest and disease protection for landscape plants."),
            ("Turf disease control","Prevents and treats lawn fungus.")],
  testimonials=[("VP and General Manager","PA and NJ"),("Operations Manager","PA")],
  faqs=[("What kinds of properties do you serve?","Corporate centers, townhome communities, HOAs, strip malls, hotels, athletic fields and more."),
        ("How many applications does a commercial program include?","Usually 4 to 8, depending on your property’s needs."),
        ("Are you licensed and insured?","Yes. We’re fully licensed, insured and certified in Pennsylvania, New Jersey and Delaware."),
        ("What if we’re unhappy with how the lawn looks?","Contact us for a free service call.")],
  related=["lawn-care-program","tree-shrub-care","mosquito-control"]),

 dict(slug="pest-control", name="Pest Control", nav="Through Green Pest Solutions",
  chip="Pest control", card="All-inclusive pest and termite control from our sister company, Green Pest Solutions.",
  hero="pest", card_img="pest",
  h1="Keep pests out of your home, too.",
  lede="Green Pest Solutions, our sister company, handles pest and termite control with all-inclusive programs and a free pest evaluation.",
  checks=["Free pest evaluation","All-inclusive programs for common household pests","Same local ownership as Green Lawn"],
  chips_h="Pests we handle", chips=["Ants","Carpenter ants","Spiders","Wasps and hornets","Mice and rats","Cockroaches","Crickets","Stink bugs","Silverfish","Fleas","Beetles","Centipedes","Clothing moths","Pantry pests","Termites"],
  inc_h="Recognized for pest control", inc_img="pest",
  included=[("Best of Philly","Earth-Friendly Exterminator, Philadelphia Magazine."),
            ("Angie’s List Super Service Award","Eight years in a row."),
            ("Best Pest Control Service","Phillyfavorites.com."),
            ("Best of HomeAdvisor","Recognized by HomeAdvisor customers.")],
  external=("Visit Green Pest Solutions","https://www.greenpestsolutions.com/free-pest-evaluation/"),
  faqs=[("Who provides pest control?","Green Pest Solutions, the pest control company that shares ownership with Green Lawn Fertilizing."),
        ("Which pests are covered?","Ants, spiders, wasps, rodents, cockroaches, stink bugs and many more household pests, plus termite control."),
        ("How do I get started?","Request a free pest evaluation and a technician will assess your home.")],
  related=["mosquito-control","flea-tick-control","tree-shrub-care"]),
]
SBY = {s["slug"]: s for s in S}

AREAS = [
 dict(slug="pennsylvania", name="Pennsylvania", abbr="PA",
  counties=["Berks","Bucks","Chester","Delaware","Lancaster","Lehigh","Montgomery","Northampton","Philadelphia"],
  lede="Locally owned and headquartered in West Chester. We serve homeowners and businesses across nine Pennsylvania counties.",
  local="Our headquarters is at 1025 Andrew Dr., West Chester, PA 19380."),
 dict(slug="new-jersey", name="New Jersey", abbr="NJ",
  counties=["Atlantic","Burlington","Camden","Cumberland","Gloucester","Hunterdon","Mercer","Middlesex","Monmouth","Ocean","Somerset"],
  lede="Local lawn care for homeowners and businesses across eleven New Jersey counties.",
  offer="Pre-pay for your season and save up to 10% on treatments, plus get 2 free insect control applications."),
 dict(slug="delaware", name="Delaware", abbr="DE",
  counties=["New Castle","Kent"],
  lede="Local lawn care for homeowners and businesses in New Castle and Kent counties."),
]

# ---------------- Shared fragments ----------------
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bitter:wght@500;700;800&family=Figtree:wght@400;500;600;700;800&display=swap" rel="stylesheet">'

def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{e(title)} | Green Lawn Fertilizing (design concept)</title>
<meta name="description" content="{e(desc)}">
{FONTS}
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="concept" role="note"><strong>Design concept</strong> for Green Lawn Fertilizing. Not the live site, and forms don’t send anything.</div>
'''

def header(current=None):
    svc_links = "".join(f'<a href="{s["slug"]}.html"{" aria-current=page" if current==s["slug"] else ""}>{e(s["name"])}<small>{e(s["nav"])}</small></a>' for s in S)
    area_links = "".join(f'<a href="{a["slug"]}.html"{" aria-current=page" if current==a["slug"] else ""}>{e(a["name"])}<small>{len(a["counties"])} counties</small></a>' for a in AREAS)
    svc_cur = " current" if current in SBY else ""
    area_cur = " current" if current in [a["slug"] for a in AREAS] else ""
    def cur(p): return ' aria-current="page"' if current==p else ""
    m_svc = "".join(f'<a href="{s["slug"]}.html">{e(s["name"])}</a>' for s in S)
    m_area = "".join(f'<a href="{a["slug"]}.html">{e(a["name"])}</a>' for a in AREAS)
    return f'''<header class="site">
  <div class="wrap">
    <div class="bar">
      <a class="logo" href="index.html" aria-label="Green Lawn Fertilizing home"><img src="{LOGO}" alt="Green Lawn Fertilizing"></a>
      <nav class="main" aria-label="Main">
        <div class="dd{svc_cur}"><button type="button" aria-expanded="false">Services{ICON["chev"]}</button><div class="dd-panel cols">{svc_links}</div></div>
        <div class="dd{area_cur}"><button type="button" aria-expanded="false">Service area{ICON["chev"]}</button><div class="dd-panel">{area_links}</div></div>
        <a href="about.html"{cur("about")}>About us</a>
        <a href="index.html#faq">FAQ</a>
      </nav>
      <div class="hdr-actions">
        <a class="login" href="#">Customer login</a>
        <a class="hdr-phone" href="{TEL}" aria-label="Call {PHONE}">{ICON["phone"]}<span class="num">{PHONE}<small>Talk to a lawn expert</small></span></a>
        <a class="btn btn-primary" href="free-estimate.html">Get a free estimate</a>
        <button class="menu-btn" type="button" aria-label="Menu" aria-expanded="false">{ICON["menu"]}</button>
      </div>
    </div>
    <div class="mnav"><h4>Services</h4>{m_svc}<h4>Service area</h4>{m_area}<h4>Company</h4><a href="about.html">About us</a><a href="index.html#faq">FAQ</a><a href="#">Customer login</a><a class="btn btn-primary" href="free-estimate.html">Get a free estimate</a></div>
  </div>
</header>
'''

def footer():
    svc = "".join(f'<li><a href="{s["slug"]}.html">{e(s["name"])}</a></li>' for s in S[:6])
    svc2 = "".join(f'<li><a href="{s["slug"]}.html">{e(s["name"])}</a></li>' for s in S[6:])
    areas = "".join(f'<li><a href="{a["slug"]}.html">{e(a["name"])}</a></li>' for a in AREAS)
    return f'''<footer>
  <div class="wrap">
    <div class="foot">
      <div class="brand">
        <img src="{LOGO}" alt="Green Lawn Fertilizing">
        <p>Locally owned lawn, tree and shrub care since 2004.</p>
        <p style="margin-top:12px">1025 Andrew Dr.<br>West Chester, PA 19380</p>
        <p style="margin-top:12px"><a href="{TEL}" style="font-weight:800;font-size:18px">{PHONE}</a></p>
      </div>
      <div><h4>Services</h4><ul>{svc}</ul></div>
      <div><h4>More services</h4><ul>{svc2}</ul></div>
      <div><h4>Company</h4><ul><li><a href="about.html">About us</a></li><li><a href="free-estimate.html">Free estimate</a></li>{areas}<li><a href="#">Careers</a></li><li><a href="#">Customer login</a></li></ul></div>
    </div>
    <div class="fine"><span>© Green Lawn Fertilizing. <span class="stars">★★★★★</span> 4.71 average from 19,345 ratings.</span><span>Design concept. Not the live site.</span></div>
  </div>
</footer>
'''

def tail(float_cta=True):
    fl = f'''<div class="float-cta" aria-hidden="true"><span><span class="stars">★★★★★</span> 4.71 from 19,345 ratings</span><a class="btn btn-primary" href="free-estimate.html" tabindex="-1">Get a free estimate</a></div>''' if float_cta else ""
    return f'''{fl}
<div class="mbar" aria-label="Quick actions"><a class="btn call" href="{TEL}">{ICON["phone"]}Call</a><a class="btn btn-primary" href="free-estimate.html">Free estimate</a></div>
<script src="assets/site.js"></script>
</body>
</html>
'''

CHIPS = ["Lawn care","Tree & shrub","Mosquito control","Aeration & seeding"]

def lead_form(selected="Lawn care", heading="What would it take to fix your lawn?", sub="Start with your address. A local expert will tell you, free.", or_call=True, services=True):
    chips = list(CHIPS)
    if selected not in chips:
        chips[-1] = selected
    chip_html = "".join(f'<label><input type="checkbox" name="svc" value="{e(c)}"{" checked" if c==selected else ""}> {e(c)}</label>' for c in chips)
    svc_block = f'<fieldset><legend>What would you like help with?</legend><div class="svc">{chip_html}</div></fieldset>' if services else ""
    oc = f'<div class="or-call" data-orcall>Prefer to talk? <a href="{TEL}">{PHONE}</a></div>' if or_call else ""
    return f'''<form class="lead" data-lead novalidate aria-label="Free estimate request">
  <h2>{e(heading)}</h2>
  <p class="sub" data-sub>{e(sub)}</p>
  <div class="progress" aria-hidden="true"><span class="on"></span><span></span></div>
  <div class="step active" data-step="1">
    <label>Property address<input type="text" name="address" placeholder="123 Main St" autocomplete="street-address" required></label>
    <label>ZIP code<input type="text" name="zip" inputmode="numeric" maxlength="5" placeholder="19380" autocomplete="postal-code" required></label>
    <button class="btn btn-primary" type="button" data-next>Start my free estimate</button>
  </div>
  <div class="step" data-step="2">
    {svc_block}
    <div class="row">
      <label>First name<input type="text" name="name" autocomplete="given-name" required></label>
      <label>Phone<input type="tel" name="phone" autocomplete="tel" placeholder="(610) 555-0123" required></label>
    </div>
    <label>Email<input type="email" name="email" autocomplete="email" placeholder="you@example.com" required></label>
    <button class="btn btn-primary" type="submit">Send me my free estimate</button>
    <button class="back" type="button" data-back>Back</button>
  </div>
  <div class="step" data-step="3">
    <div class="done">
      <div class="ok">{ICON["check"].replace('viewBox', 'width="30" height="30" viewBox')}</div>
      <h3>You’re all set<span data-fname></span>.</h3>
      <p>A Green Lawn Fertilizing expert will contact you shortly with your free estimate and lawn analysis.</p>
      <p class="demo">Design concept: nothing was sent.</p>
    </div>
  </div>
  <div class="reassure" data-reassure><span>{ICON["check"]}No obligation. No is a fine answer.</span><span>{ICON["lock"]}We never sell your info</span></div>
  {oc}
</form>'''

def checks(items):
    return '<ul class="checks">' + "".join(f'<li>{ICON["check"]}<span>{e(i)}</span></li>' for i in items) + '</ul>'

def hero(photo, alt, crumbs, h1, lede, items, form, price=None, proof=True, cls=""):
    crumb = " / ".join([f'<a href="{u}">{e(t)}</a>' if u else e(t) for t,u in crumbs])
    pc = f'<div class="price-chip">Starting at <b>{e(price[0])}</b> {e(price[1])}</div>' if price else ""
    pf = '<div class="hero-proof"><span class="stars" aria-hidden="true">★★★★★</span><b>4.71</b><span>from 19,345 ratings</span><span class="divider"></span><span>Locally owned since 2004</span></div>' if proof else ""
    return f'''<section class="hero {cls}" style="padding:0">
  <div class="hero-bg"><img src="{img(P[photo],2000)}" alt="{e(alt)}" fetchpriority="high"></div>
  <div class="wrap hero-in">
    <div class="hero-copy">
      <div class="crumb">{crumb}</div>
      <h1>{e(h1)}</h1>
      <p class="lede">{e(lede)}</p>
      {checks(items)}
      {pc}
      {pf}
    </div>
    <div>{form}</div>
  </div>
</section>
'''

def trust():
    b = "".join(f'<img src="{img(f,250)}" alt="{e(a)}" loading="lazy">' for f,a in BADGES[:5])
    return f'''<div class="trust"><div class="wrap">
  <div class="trust-rating"><b>4.71</b><div><span class="stars" aria-hidden="true">★★★★★</span><small>19,345 customer ratings</small></div></div>
  <div class="badges">{b}</div>
</div></div>
'''

def how(cta_href="free-estimate.html"):
    return f'''<section>
  <div class="wrap">
    <div class="center"><h2>Getting started is easy</h2><p class="lede">Here’s exactly what happens after you ask for an estimate.</p></div>
    <ol class="steps">
      <li><h3>Tell us about your lawn</h3><p>Share your address online or call {PHONE}. It takes under a minute.</p></li>
      <li><h3>Get your free lawn analysis</h3><p>A local expert reviews your property and recommends a program for your goals and budget.</p></li>
      <li><h3>We handle every visit</h3><p>You don’t need to be home. Your technician leaves a lawn flag and a service summary each time.</p></li>
    </ol>
    <div class="how-cta"><a class="btn btn-primary" href="{cta_href}">Start my free estimate</a></div>
  </div>
</section>
'''

def faq_block(faqs, title="Questions before you start?", intro="Hiring a lawn company for the first time can feel like a gamble. Here are straight answers to what homeowners ask us first.", alt=False, anchor="faq"):
    items = "".join(f'<details{" open" if i==0 else ""}><summary>{e(q)}</summary><div><p>{e(a)}</p></div></details>' for i,(q,a) in enumerate(faqs))
    schema = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
    return f'''<section id="{anchor}"{' class="alt"' if alt else ""}>
  <div class="wrap">
    <div class="faq-grid">
      <div class="faq-side">
        <h2>{e(title)}</h2>
        <p class="lede">{e(intro)}</p>
        <a class="btn btn-primary" href="free-estimate.html">Get a free estimate</a>
        <p style="margin-top:14px;font-size:16px;color:var(--muted)">or call <a href="{TEL}" style="font-weight:800;color:var(--head)">{PHONE}</a></p>
      </div>
      <div>{items}</div>
    </div>
  </div>
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</section>
'''

def awards():
    b = "".join(f'<img src="{img(f,250)}" alt="{e(a)}" loading="lazy">' for f,a in BADGES)
    return f'''<section class="awards"><div class="wrap">
  <h2>Recognized for service, growth and workplace</h2>
  <div class="awards-row">{b}</div>
</div></section>
'''

def final(selected="Lawn care", h="Get a head start on a greener spring.", lede="Get your free analysis now, and your program will be ready to start when the season does."):
    return f'''<section class="final" id="estimate">
  <div class="wrap">
    <div class="final-grid">
      <div>
        <h2>{e(h)}</h2>
        <p class="lede">{e(lede)}</p>
        {checks(["Free, no-obligation analysis","100% satisfaction guarantee on our lawn program","4.71★ from 19,345 customer ratings"])}
        <div class="final-phone">{ICON["phone"]}<div><a href="{TEL}">{PHONE}</a><small>Talk to a lawn expert <span class="tag">add hours</span></small></div></div>
      </div>
      {lead_form(selected, or_call=False)}
    </div>
  </div>
</section>
'''

def results(alt=True):
    return f'''<section{' class="alt"' if alt else ""}>
  <div class="wrap">
    <div class="sec-head">
      <h2>Thin, weedy lawn to thick and green.</h2>
      <p class="lede">Every program is tailored to your property and to local soil, weed and pest pressures. Here’s what that looks like.</p>
    </div>
    <div class="results-grid">
      <div>
        <div class="ba"><img src="{img(P["ba"],1400)}" alt="The same front lawn before treatment, thin and patchy, and after, thick and green" loading="lazy"></div>
        <p class="ba-cap">Customer lawn, before and after. <span class="tag">add town and program</span></p>
      </div>
      <div class="reviews">
        <div class="review"><span class="stars" aria-hidden="true">★★★★★</span><p>Real Google review about a visible result, such as weeds gone or a thicker lawn.</p><small>First name, town</small> <span class="tag">pull from Google reviews</span></div>
        <div class="review"><span class="stars" aria-hidden="true">★★★★★</span><p>Real review about the technician or how easy the service was.</p><small>First name, town</small> <span class="tag">pull from Google reviews</span></div>
        <a class="more" href="#">Read all 19,345 ratings</a>
      </div>
    </div>
    <div class="inline-cta">
      <p>Does your lawn look more like the left photo?<span>Find out what it would take to get it to the right. The analysis is free.</span></p>
      <div class="acts"><a class="btn btn-primary" href="free-estimate.html">Get a free estimate</a><a class="btn btn-line" href="{TEL}">{ICON["phone"]}{PHONE}</a></div>
    </div>
  </div>
</section>
'''

def svc_cards(slugs, alt=False):
    cards = ""
    for sl in slugs:
        s = SBY[sl]
        meta = f'Starting at {s["price"]} <span>{e(s["price_note"].split(",")[0])}</span>' if s.get("price") else "<span>Free estimate</span>"
        cards += f'''<a class="svc-card" href="{sl}.html"><div class="ph"><img src="{img(P[s["card_img"]],900)}" alt="" loading="lazy"></div><div class="bd"><h3>{e(s["name"])}</h3><p>{e(s["card"])}</p><div class="meta"><span>{meta}</span><span class="go">Learn more</span></div></div></a>'''
    return f'<div class="svc-cards">{cards}</div>'

def page(fname, title, desc, current, body, float_cta=True):
    out = head(title, desc) + header(current) + '<main id="main">\n' + body + '</main>\n' + footer() + tail(float_cta)
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(out)

# ---------------- Pages ----------------
def build_service(s):
    price = (s["price"], s["price_note"]) if s.get("price") else None
    body = hero(s["hero"], f'{s["name"]} from Green Lawn Fertilizing', [("Home","index.html"),("Services","index.html#services"),(s["name"],None)],
                s["h1"], s["lede"], s["checks"], lead_form(s["chip"]), price=price)
    body += trust()

    # Included
    inc = "".join(f'<li>{ICON["check"]}<div>{e(t)}<span>{e(d)}</span></div></li>' for t,d in s["included"])
    wide = s.get("inc_img_wide")
    photo = f'<figure class="photo-frame{" wide" if wide else ""}"><img src="{img(P[s["inc_img"]],1400)}" alt="" loading="lazy"></figure>'
    extra = ""
    if s.get("honest"):
        extra += f'<div class="honest"><b>{e(s["honest"][0])}</b><p>{e(s["honest"][1])}</p></div>'
    if s.get("external"):
        extra += f'<p style="margin-top:24px"><a class="btn btn-line" href="{s["external"][1]}" rel="noopener" target="_blank">{e(s["external"][0])}</a></p>'
    body += f'''<section>
  <div class="wrap">
    <div class="split">
      <div><h2 style="margin-bottom:28px">{e(s["inc_h"])}</h2><ul class="incl">{inc}</ul>{extra}</div>
      {photo}
    </div>
  </div>
</section>
'''
    # Optional modules
    alt_blocks = ""
    if s.get("rounds"):
        r = "".join(f'<div class="round"><div class="when">{e(w)}</div><h3>{e(t)}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in xs)}</ul></div>' for t,w,xs in s["rounds"])
        alt_blocks += f'<div class="sec-head"><h2>Eight visits, timed to the season</h2><p class="lede">About every 4 to 6 weeks, from early spring green-up to winter prep.</p></div><div class="rounds" style="--n:{len(s["rounds"])}">{r}</div>'
    if s.get("plans"):
        cards = ""
        for n,p_,u,d,best in s["plans"]:
            style = ' style="border:2px solid var(--green)"' if best else ""
            badge = '<span class="tag" style="margin-bottom:10px">Best value</span><br>' if best else ""
            cards += f'<div class="card"{style}>{badge}<h3>{e(n)}</h3><p style="margin:6px 0 10px"><b style="font-family:var(--serif);font-size:34px;color:var(--head)">{e(p_)}</b> {e(u)}</p><p>{e(d)}</p></div>'
        alt_blocks += f'<div class="sec-head"><h2>Simple per-visit pricing</h2><p class="lede">Starting prices per visit. Your estimate confirms the price for your property. <span class="tag">confirm package contents</span></p></div><div class="grid-3">{cards}</div>'
    if s.get("diseases"):
        cards = "".join(f'<div class="card"><div class="ic">{ICON["leaf"]}</div><h3>{e(n)}</h3><p>{e(d)}</p></div>' for n,d in s["diseases"])
        alt_blocks += f'<div class="sec-head"><h2>Diseases we treat</h2><p class="lede">Most common in fescue and ryegrass lawns during hot, humid stretches.</p></div><div class="grid-3">{cards}</div>'
    if s.get("callout"):
        b,t,sm = s["callout"]
        alt_blocks += f'<div class="callout"><b>{e(b)}</b><div><p>{e(t)}</p><small>{e(sm)}</small></div></div>'
    if s.get("chips"):
        ch = "".join(f'<span>{e(c)}</span>' for c in s["chips"])
        mt = ' style="margin-top:48px"' if alt_blocks else ""
        alt_blocks += f'<h2{mt} style="font-size:28px;margin-bottom:20px{";margin-top:48px" if alt_blocks else ""}">{e(s["chips_h"])}</h2><div class="chips">{ch}</div>'
    if s.get("testimonials"):
        t = "".join(f'<div class="review"><span class="stars">★★★★★</span><p>Use the existing testimonial from this client.</p><small>{e(r)}, {e(l)}</small> <span class="tag">paste from current page</span></div>' for r,l in s["testimonials"])
        alt_blocks += f'<h2 style="font-size:28px;margin:48px 0 20px">What property managers say</h2><div class="grid-3" style="grid-template-columns:1fr 1fr">{t}</div>'
    if s.get("guarantee"):
        g,t = s["guarantee"]
        alt_blocks += f'<div class="guarantee" style="margin-top:{"40px" if alt_blocks else "0"}"><div class="seal">100%</div><div><h3>{e(g)}</h3><p>{e(t)}</p></div><a class="btn btn-primary" href="free-estimate.html" style="margin-left:auto">Get a free estimate</a></div>'
    if alt_blocks:
        body += f'<section class="alt"><div class="wrap">{alt_blocks}</div></section>\n'

    body += how()
    body += faq_block(s["faqs"], title=f'{s["name"]} questions', alt=True)
    body += f'''<section>
  <div class="wrap">
    <div class="sec-head"><h2>Often paired with {e(s["name"])}</h2><p class="lede">Most customers combine two or three services. Ask about bundling when you get your estimate.</p></div>
    {svc_cards(s["related"])}
  </div>
</section>
'''
    body += final(s["chip"], h=f'Get your free {s["name"].replace("The ","")} estimate.', lede="Tell us where your lawn is. A local expert will contact you with a free estimate and analysis.")
    page(f'{s["slug"]}.html', s["name"], s["lede"], s["slug"], body)

def build_home():
    body = hero("grill","A couple relaxing by the grill on their green lawn",[("Green Lawn Fertilizing",None)],
        "A thicker, greener lawn without giving up your weekends.",
        "Locally owned since 2004 and trusted by 39,000+ homeowners in PA, NJ and DE. Programs start at $54 per application.",
        ["Free lawn health assessment, no obligation","Eight visits a year, timed to our local seasons","100% satisfaction guarantee: not happy, we come back"],
        lead_form("Lawn care"), price=None)
    body += trust()
    cards = "".join(f'<div class="card"><div class="ic">{ICON[i]}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i,t,d in [
        ("sprout","Patchy, thin grass","Bare spots drag down curb appeal and give weeds room to move in."),
        ("leaf","Weeds that spread fast","Dandelions, clover and crabgrass take over when they aren’t stopped early."),
        ("drop","Poor soil health","Acidic or compacted soil locks up the fertilizer you’ve paid for."),
        ("money","Costly DIY mistakes","Wrong product, wrong timing or a burned lawn, and you pay twice.")])
    body += f'''<section>
  <div class="wrap">
    <div class="sec-head"><h2>DIY lawn care costs more than you think.</h2><p class="lede">Most homeowners spend hundreds a year on garden-center products that only treat the surface. A professional program often costs less than a few trips to the store.</p></div>
    <div class="grid-4">{cards}</div>
  </div>
</section>
'''
    lp = SBY["lawn-care-program"]
    r = "".join(f'<div class="round"><div class="when">{e(w)}</div><h3>{e(t)}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in xs)}</ul></div>' for t,w,xs in lp["rounds"])
    body += f'''<section class="alt">
  <div class="wrap">
    <div class="sec-head"><h2>The Green Lawn Program</h2><p class="lede">Eight visits a year: seven fertilizer applications, grub prevention, unlimited weed control and free service calls. Starting at $54 per application for a typical 3,000 sq ft lawn.</p></div>
    <div class="rounds" style="--n:3">{r}</div>
    <div class="guarantee" style="margin-top:28px"><div class="seal">100%</div><div><h3>100% Satisfaction Guarantee</h3><p>If you’re not happy, we’ll come back. It’s that simple.</p></div><a class="btn btn-line" href="lawn-care-program.html" style="margin-left:auto">See the full program</a></div>
  </div>
</section>
'''
    body += f'''<section id="services">
  <div class="wrap">
    <div class="sec-head"><h2>Everything your yard needs, from one local team</h2><p class="lede">Start with the lawn, then add the services that fit your yard. Bundling is easy when it’s all one company.</p></div>
    {svc_cards([s["slug"] for s in S])}
  </div>
</section>
'''
    body += results()
    body += how()
    acards = "".join(f'<a class="card" href="{a["slug"]}.html" style="text-decoration:none"><h3>{e(a["name"])}</h3><p>{len(a["counties"])} counties: {e(", ".join(a["counties"][:4]))}{" and more" if len(a["counties"])>4 else ""}</p><p style="margin-top:12px;font-weight:700;color:var(--head)">See {e(a["abbr"])} service area</p></a>' for a in AREAS)
    body += f'''<section class="alt">
  <div class="wrap">
    <div class="split">
      <div>
        <h2>Local to your neighborhood</h2>
        <p class="lede" style="margin-top:16px">Headquartered at 1025 Andrew Dr. in West Chester, PA, with 7 branch locations across Pennsylvania, New Jersey and Delaware.</p>
        <div class="grid-3" style="grid-template-columns:1fr;gap:14px;margin-top:28px">{acards}</div>
      </div>
      <figure class="photo-frame"><img src="{img(P["dogskids"],1400)}" alt="A family with kids and dogs on their lawn" loading="lazy"></figure>
    </div>
  </div>
</section>
'''
    body += faq_block([
        ("How much does lawn care cost?","Programs start at $54 per application, with 8 applications a year, based on a 3,000 sq ft lawn. We measure your lawn and confirm your exact price in your free estimate."),
        ("Is it safe for my kids and pets?","Yes, once the application dries. On a dry day that’s usually within a couple of hours."),
        ("Do I need to be home?","No. Your technician leaves a lawn flag and a service summary after every visit."),
        ("What if I’m not happy with the results?","Our lawn program comes with a 100% satisfaction guarantee. If you’re not happy, we’ll come back."),
        ("When will I see results?","Weeds usually curl and die within 10 to 14 days. Grass gets thicker and greener over the first few treatments."),
        ("Do I have to sign a contract?","Answer needed: contract and cancellation terms."),
        ("Where do you provide service?","Southeastern Pennsylvania, New Jersey and Delaware. We’re headquartered in West Chester, PA, with 7 branch locations."),
    ])
    body += awards()
    body += final()
    page("index.html","Lawn care in PA, NJ and DE","A thicker, greener lawn without giving up your weekends. Locally owned since 2004.","home",body)

def build_estimate():
    steps = '''<ol class="steps" style="margin-top:8px;grid-template-columns:1fr;gap:22px">
      <li style="padding:0 0 0 64px;min-height:48px"><h3 style="color:#fff;font-size:19px">Tell us about your lawn</h3><p style="color:#C9D0CB">Address first, then where to reach you.</p></li>
      <li style="padding:0 0 0 64px;min-height:48px"><h3 style="color:#fff;font-size:19px">A local expert contacts you</h3><p style="color:#C9D0CB">You’ll get a free estimate and lawn analysis, shortly.</p></li>
      <li style="padding:0 0 0 64px;min-height:48px"><h3 style="color:#fff;font-size:19px">Decide with no pressure</h3><p style="color:#C9D0CB">No obligation. No is a fine answer.</p></li>
    </ol>'''
    body = f'''<section class="hero est-hero" style="padding:0">
  <div class="hero-bg"><img src="{img(P["tech96"],2000)}" alt="A Green Lawn Fertilizing technician talking with a homeowner"></div>
  <div class="wrap hero-in">
    <div class="hero-copy">
      <div class="crumb"><a href="index.html">Home</a> / Free estimate</div>
      <h1>Get your free lawn estimate.</h1>
      <p class="lede">Tell us where your lawn is. A Green Lawn Fertilizing expert will contact you with a free estimate and lawn analysis.</p>
      <style>.est-hero .steps li::before{{background:var(--green)}}.est-hero .steps li:not(:last-child)::after{{left:23px;top:56px;right:auto;bottom:-18px;width:2px;height:auto;background:rgba(255,255,255,.25)}}</style>
      {steps}
      <div class="hero-proof"><span class="stars" aria-hidden="true">★★★★★</span><b>4.71</b><span>from 19,345 ratings</span></div>
    </div>
    <div>{lead_form("Lawn care", heading="Start your free estimate", sub="Takes under a minute. Start with your address.")}</div>
  </div>
</section>
'''
    body += trust()
    body += f'''<section>
  <div class="wrap">
    <div class="grid-3">
      <div class="card"><h3>Starting at $54</h3><p>Per application, with 8 applications a year, based on a 3,000 sq ft lawn. Your estimate confirms the price for your property.</p></div>
      <div class="card"><h3>100% satisfaction guarantee</h3><p>On our lawn program: if you’re not happy, we’ll come back. It’s that simple.</p></div>
      <div class="card"><h3>You don’t need to be home</h3><p>Your technician leaves a lawn flag and a service summary after every visit.</p></div>
    </div>
  </div>
</section>
'''
    body += faq_block([
        ("What happens after I submit?","A Green Lawn Fertilizing employee will contact you shortly with your free estimate and lawn analysis."),
        ("Is the estimate really free?","Yes. There’s no cost and no obligation."),
        ("Can I get an estimate by phone?",f"Yes. Call {PHONE} to talk with a lawn expert."),
        ("Do you serve my area?","We serve homeowners and businesses in southeastern Pennsylvania, New Jersey and Delaware. Your address tells us right away."),
    ], title="Before you request", intro="Quick answers about the estimate.", alt=True)
    page("free-estimate.html","Free lawn care estimate","Request a free lawn care estimate and lawn analysis from Green Lawn Fertilizing.","estimate",body,float_cta=False)

def build_area(a):
    offer = f'<div class="honest"><b>New Jersey pre-pay offer</b><p>{e(a["offer"])} <span class="tag">confirm current terms</span></p></div>' if a.get("offer") else ""
    body = hero("grill",f'A couple enjoying their lawn in {a["name"]}',[("Home","index.html"),("Service area",None),(a["name"],None)],
        f'Local lawn care in {a["name"]}.', a["lede"],
        ["7 fertilizer applications every 4 to 6 weeks","Crabgrass and weed control, plus pH testing","Free service calls between visits"],
        lead_form("Lawn care"), price=("$54","per application"))
    body += trust()
    ch = "".join(f'<span>{e(c)} County</span>' for c in a["counties"])
    local = f'<p class="lede" style="margin-top:14px">{e(a["local"])}</p>' if a.get("local") else ""
    body += f'''<section>
  <div class="wrap">
    <div class="split">
      <div>
        <h2>Counties we serve in {e(a["name"])}</h2>
        <p class="lede" style="margin-top:16px">Not sure if we cover your street? Enter your address in the form and we’ll confirm.</p>
        {local}
        <div class="chips" style="margin-top:26px">{ch}</div>
        {offer}
      </div>
      <figure class="photo-frame"><img src="{img(P["tech92"],1400)}" alt="A Green Lawn Fertilizing technician with a homeowner" loading="lazy"></figure>
    </div>
  </div>
</section>
'''
    body += f'''<section class="alt">
  <div class="wrap">
    <div class="sec-head"><h2>Services available in {e(a["name"])}</h2><p class="lede">Residential and commercial properties.</p></div>
    {svc_cards([s["slug"] for s in S if not (a["abbr"]=="DE" and s["slug"] in ("pest-control","natural-program","commercial-services","tree-shrub-care"))])}
  </div>
</section>
'''
    body += results(alt=False)
    body += faq_block([
        (f"Which parts of {a['name']} do you serve?", f"{', '.join(a['counties'][:-1]) + (' and ' if len(a['counties'])>1 else '') + a['counties'][-1]} {'counties' if len(a['counties'])>1 else 'County'}."),
        ("How often will you visit?","Our lawn program includes 8 visits a year, about every 4 to 6 weeks."),
        ("How much does it cost?","Programs start at $54 per application, based on a 3,000 sq ft lawn. Your estimate confirms the price for your property."),
        ("Do you have a local office?","We’re headquartered in West Chester, PA, with 7 branch locations across PA, NJ and DE."),
    ], title=f"{a['name']} lawn care questions", alt=True)
    body += final()
    page(f'{a["slug"]}.html',f'Lawn care in {a["name"]}',a["lede"],a["slug"],body)

def build_about():
    body = hero("tech92","A Green Lawn Fertilizing technician talking with a homeowner at her front door",[("Home","index.html"),("About us",None)],
        "Your neighbors’ lawn care company since 2004.",
        "Locally owned in West Chester. Together with our sister company, Green Pest Solutions, we serve more than 70,000 customers in PA, NJ and DE.",
        ["Free lawn analysis from a local expert","A program built for your lawn and your goals","100% satisfaction guarantee on our lawn program"],
        lead_form("Lawn care"))
    body += trust()
    tl = "".join(f'<li style="display:grid;grid-template-columns:110px 1fr;gap:18px;padding:12px 0;border-top:1px solid var(--line)"><b style="font-family:var(--serif);color:var(--head);font-size:19px">{e(y)}</b><span style="color:var(--muted);font-size:16.5px">{t}</span></li>' for y,t in [
        ("Early days","Matt Jesson mows lawns in Havertown, PA, through his early twenties"),
        ("2004","Matt founds Green Lawn Fertilizing"),
        ("2010",'The crew grows and programs expand <span class="tag">confirm year</span>'),
        ("Growth","Green Pest Solutions launches for pest and termite control"),
        ("Today","400+ team members, 7 branches, headquartered in West Chester")])
    body += f'''<section>
  <div class="wrap">
    <div class="split">
      <figure class="photo-frame"><img src="{img(P["y2010"],1200)}" alt="The Green Lawn Fertilizing team in 2010 standing behind the company sign" loading="lazy"><figcaption>The crew in 2010</figcaption></figure>
      <div>
        <h2>It started with one kid mowing lawns in Havertown.</h2>
        <p class="lede" style="margin-top:16px;font-size:18px">Founder Matt Jesson cut his neighbors’ grass through his early twenties, then founded Green Lawn Fertilizing in 2004. Today we’re one of the largest independent lawn care companies in the Tri-State region, and still locally owned.</p>
        <ul style="list-style:none;padding:0;margin:26px 0 0">{tl}</ul>
      </div>
    </div>
  </div>
</section>
'''
    body += f'''<section class="alt">
  <div class="wrap">
    <div class="sec-head"><h2>Happy teams take better care of your lawn.</h2><p class="lede">Our mission is to be the leader in the lawn and pest industry by providing a superior customer experience. That starts with treating our team exceptionally well, and it’s why the Philadelphia Business Journal has named us a Best Place to Work eight times.</p></div>
    <figure class="photo-frame" style="aspect-ratio:16/7"><img src="{img(P["team"],1800)}" alt="Hundreds of Green Lawn Fertilizing team members together in a stadium" loading="lazy"></figure>
    <div class="grid-3" style="margin-top:28px">
      <div class="card"><h3 style="font-size:34px">8×</h3><p>Philadelphia Business Journal Best Places to Work</p></div>
      <div class="card"><h3 style="font-size:34px">400+</h3><p>Team members across Green Lawn and Green Pest Solutions</p></div>
      <div class="card"><h3 style="font-size:34px">2004</h3><p>Founded in Pennsylvania, still locally owned</p></div>
    </div>
  </div>
</section>
'''
    body += f'''<section>
  <div class="wrap">
    <div class="split">
      <figure class="photo-frame"><img src="{img(P["hq"],1400)}" alt="The lobby of the Green Lawn Fertilizing headquarters in West Chester, PA" loading="lazy"></figure>
      <div>
        <h2>Headquartered in West Chester, PA</h2>
        <p class="lede" style="margin-top:16px">1025 Andrew Dr., West Chester, PA 19380, with 7 branch locations serving Pennsylvania, New Jersey and Delaware.</p>
        <p style="margin-top:24px;color:var(--muted)"><strong style="color:var(--ink)">Proud member of</strong> NALP, NPMA, the Pennsylvania Pest Management Association, the Lawn Care Association of Pennsylvania and Project EverGreen’s GreenCare for Troops.</p>
      </div>
    </div>
  </div>
</section>
'''
    body += awards()
    body += faq_block([
        ("When was Green Lawn Fertilizing founded?","In 2004, by Matt Jesson."),
        ("Where are you headquartered?","1025 Andrew Dr., West Chester, PA 19380. We also have 7 branch locations."),
        ("What areas do you serve?","Homeowners and businesses throughout southeastern Pennsylvania, New Jersey and Delaware."),
        ("Do you offer pest control?","Yes. Pest and termite control is provided by our sister company, Green Pest Solutions."),
        ("Where can I read reviews?","On our website, Google, Facebook, Nextdoor and Angi."),
    ], title="About Green Lawn Fertilizing", intro="Quick facts about who we are.", alt=True)
    body += final()
    page("about.html","About us","Locally owned lawn care since 2004, headquartered in West Chester, PA.","about",body)

if __name__ == "__main__":
    os.makedirs(os.path.join(OUT,"assets"), exist_ok=True)
    shutil.copy(os.path.join(HERE,"style.css"), os.path.join(OUT,"assets","style.css"))
    shutil.copy(os.path.join(HERE,"site.js"), os.path.join(OUT,"assets","site.js"))
    build_home(); build_about(); build_estimate()
    for a in AREAS: build_area(a)
    for s in S: build_service(s)
    print("\n".join(sorted(os.listdir(OUT))))
