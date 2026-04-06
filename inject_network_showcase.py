"""Inject OBP Network Showcase block into all HTML files before <footer> tag."""
import os
import glob

SITE_DIR = os.path.dirname(os.path.abspath(__file__))

NETWORK_BLOCK = """
<!-- Open Bankruptcy Project Network Showcase -->
<div id="obp-network-showcase" style="background:#0d1117;border-top:1px solid #30363d;padding:40px 0 32px;">
<div style="max-width:1100px;margin:0 auto;padding:0 20px;">
<details style="background:#161b22;border:1px solid #30363d;border-radius:10px;overflow:hidden;">
<summary style="padding:20px 24px;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;color:#f0f6fc;font-weight:700;font-size:1.15rem;">
<span>The Open Bankruptcy Project Network -- 170+ Free Resources</span>
<span style="color:#58a6ff;font-size:1.4rem;font-weight:700;transition:transform 0.2s;" class="obp-toggle">+</span>
</summary>
<div style="padding:4px 24px 24px;">
<p style="color:#8b949e;font-size:0.88rem;margin-bottom:16px;">Every site below is free, ad-free, and built on real federal court data. No lead generation. No sponsored content. Just information.</p>
<div style="display:flex;flex-wrap:wrap;gap:6px 8px;">
<a href="https://openbankruptcyproject.org" target="_blank" rel="noopener" style="background:#238636;color:#fff;padding:5px 12px;border-radius:14px;font-size:0.78rem;font-weight:600;border:1px solid #238636;text-decoration:none;">openbankruptcyproject.org</a>
<a href="https://1328f.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">1328f.com</a>
<a href="https://1328f.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">1328f.org</a>
<a href="https://109g.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">109g.org</a>
<a href="https://341meeting.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">341meeting.org</a>
<a href="https://523a.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">523a.org</a>
<a href="https://524injunction.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">524injunction.com</a>
<a href="https://727a8.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">727a8.org</a>
<a href="https://automaticstay.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">automaticstay.org</a>
<a href="https://chapter7vs13.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">chapter7vs13.org</a>
<a href="https://meanstest.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">meanstest.org</a>
<a href="https://section1191.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">section1191.org</a>
<a href="https://section1192.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">section1192.org</a>
<a href="https://section329.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">section329.org</a>
<a href="https://lienstripping.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">lienstripping.org</a>
<a href="https://relieffromstay.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">relieffromstay.org</a>
<a href="https://dischargebar.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">dischargebar.org</a>
<a href="https://bankruptcytrustee.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">bankruptcytrustee.org</a>
<a href="https://prosebankruptcy.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">prosebankruptcy.org</a>
<a href="https://bankruptcymill.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">bankruptcymill.com</a>
<a href="https://bankruptcymill.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">bankruptcymill.org</a>
<a href="https://kansascitybankruptcymill.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">kansascitybankruptcymill.com</a>
<a href="https://chicagobankruptcymill.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">chicagobankruptcymill.com</a>
<a href="https://houstonbankruptcymill.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">houstonbankruptcymill.com</a>
<a href="https://atlantabankruptcymill.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">atlantabankruptcymill.com</a>
<a href="https://detroitbankruptcymill.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">detroitbankruptcymill.com</a>
<a href="https://miamibankruptcymill.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">miamibankruptcymill.com</a>
<a href="https://denverbankruptcymill.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">denverbankruptcymill.com</a>
<a href="https://losangelesbankruptcymill.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">losangelesbankruptcymill.com</a>
<a href="https://stlouisbankruptcymill.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">stlouisbankruptcymill.com</a>
<a href="https://birminghambankruptcymill.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">birminghambankruptcymill.com</a>
<a href="https://filebankruptcywithoutlawyer.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">filebankruptcywithoutlawyer.com</a>
<a href="https://keepmycarinbankruptcy.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">keepmycarinbankruptcy.com</a>
<a href="https://keepmyhouseinbankruptcy.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">keepmyhouseinbankruptcy.com</a>
<a href="https://howmuchdoesbankruptcycost.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">howmuchdoesbankruptcycost.com</a>
<a href="https://rebuildcreditafterbankruptcy.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">rebuildcreditafterbankruptcy.com</a>
<a href="https://buyahouseafterbankruptcy.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">buyahouseafterbankruptcy.com</a>
<a href="https://buyacarafterbankruptcy.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">buyacarafterbankruptcy.com</a>
<a href="https://bankruptcydenied.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">bankruptcydenied.com</a>
<a href="https://bankruptcyexemptionsbystate.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">bankruptcyexemptionsbystate.com</a>
<a href="https://firedbymybankruptcylawyer.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">firedbymybankruptcylawyer.com</a>
<a href="https://mybankruptcylawyerwontcallback.com" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">mybankruptcylawyerwontcallback.com</a>
<a href="https://kansascitybankruptcy.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">kansascitybankruptcy.org</a>
<a href="https://bankruptcykansascity.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">bankruptcykansascity.org</a>
<a href="https://missouribankruptcy.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">missouribankruptcy.org</a>
<a href="https://illinoisbankruptcy.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">illinoisbankruptcy.org</a>
<a href="https://ohiobankruptcy.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">ohiobankruptcy.org</a>
<a href="https://georgiabankruptcy.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">georgiabankruptcy.org</a>
<a href="https://coloradobankruptcy.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">coloradobankruptcy.org</a>
<a href="https://minnesotabankruptcy.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">minnesotabankruptcy.org</a>
<a href="https://newyorkbankruptcy.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">newyorkbankruptcy.org</a>
<a href="https://delawarebankruptcy.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">delawarebankruptcy.org</a>
<a href="https://marylandbankruptcy.org" target="_blank" rel="noopener" style="background:#21262d;color:#58a6ff;padding:5px 12px;border-radius:14px;font-size:0.78rem;border:1px solid #30363d;text-decoration:none;">marylandbankruptcy.org</a>
</div>
<p style="color:#8b949e;font-size:0.82rem;margin-top:16px;margin-bottom:0;text-align:center;font-style:italic;">170+ domains. 2,500+ pages. $0 advertising. No lead generation. Just information.</p>
</div>
</details>
</div>
</div>
<script>document.querySelector('#obp-network-showcase details').addEventListener('toggle',function(){this.querySelector('.obp-toggle').textContent=this.open?'\u2212':'+';})</script>
<!-- End Network Showcase -->
"""

html_files = glob.glob(os.path.join(SITE_DIR, "*.html"))
updated = 0
skipped = []

for filepath in sorted(html_files):
    filename = os.path.basename(filepath)
    # Skip GSC verification files and this script
    if filename.startswith("google"):
        skipped.append(filename + " (GSC verification)")
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if "obp-network-showcase" in content:
        skipped.append(filename + " (already injected)")
        continue
    footer_idx = content.find("<footer>")
    if footer_idx == -1:
        footer_idx = content.find("<footer ")
    if footer_idx == -1:
        skipped.append(filename + " (no footer tag)")
        continue
    new_content = content[:footer_idx] + NETWORK_BLOCK + "\n" + content[footer_idx:]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"DONE: {updated} files updated")
if skipped:
    print(f"Skipped {len(skipped)} files:")
    for s in skipped:
        print(f"  - {s}")
