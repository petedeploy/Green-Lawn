// Green Lawn Fertilizing redesign concept: shared behavior. Forms never send data.
(function(){
  // Dropdown menus
  const dds=[...document.querySelectorAll('.dd')];
  dds.forEach(dd=>{
    const btn=dd.querySelector('button');
    btn.addEventListener('click',e=>{
      e.stopPropagation();
      const open=dd.hasAttribute('data-open');
      dds.forEach(d=>{d.removeAttribute('data-open');d.querySelector('button').setAttribute('aria-expanded','false');});
      if(!open){dd.setAttribute('data-open','');btn.setAttribute('aria-expanded','true');}
    });
  });
  document.addEventListener('click',()=>dds.forEach(d=>{d.removeAttribute('data-open');d.querySelector('button').setAttribute('aria-expanded','false');}));
  document.addEventListener('keydown',e=>{if(e.key==='Escape')dds.forEach(d=>d.removeAttribute('data-open'));});

  // Mobile menu
  const mb=document.querySelector('.menu-btn'), mn=document.querySelector('.mnav');
  if(mb&&mn) mb.addEventListener('click',()=>{const o=mn.toggleAttribute('data-open');mb.setAttribute('aria-expanded',o);});

  // Multi-step lead forms (concept: nothing is sent)
  document.querySelectorAll('[data-lead]').forEach(form=>{
    const steps=[...form.querySelectorAll('[data-step]')];
    const bars=[...form.querySelectorAll('.progress span')];
    const sub=form.querySelector('[data-sub]');
    const subs=[sub?sub.textContent:'','Last step: where should we send your estimate?','Thanks, we’ve got your request.'];
    const show=n=>{
      steps.forEach(s=>s.classList.toggle('active',s.dataset.step==n));
      bars.forEach((b,i)=>b.classList.toggle('on',i<n));
      if(sub) sub.textContent=subs[n-1];
      const prog=form.querySelector('.progress'); if(prog) prog.style.display=n==3?'none':'';
      ['[data-reassure]','[data-orcall]'].forEach(q=>{const el=form.querySelector(q); if(el) el.style.display=n==3?'none':'';});
      const first=steps[n-1].querySelector('input[type=text],input[type=tel],input[type=email]'); if(first) first.focus({preventScroll:true});
    };
    const valid=step=>{
      let ok=true;
      step.querySelectorAll('input[required]').forEach(i=>{
        const v=i.value.trim(); let good=v.length>0;
        if(i.name==='zip') good=/^\d{5}$/.test(v);
        if(i.type==='email') good=/^\S+@\S+\.\S+$/.test(v);
        if(i.type==='tel') good=v.replace(/\D/g,'').length>=10;
        i.classList.toggle('err',!good); i.setAttribute('aria-invalid',String(!good));
        if(!good&&ok){ok=false;i.focus();}
      });
      return ok;
    };
    form.querySelector('[data-next]').addEventListener('click',()=>{if(valid(steps[0]))show(2);});
    form.querySelector('[data-back]').addEventListener('click',()=>show(1));
    form.addEventListener('submit',e=>{
      e.preventDefault();
      if(!valid(steps[1]))return;
      const n=form.querySelector('input[name=name]').value.trim();
      form.querySelectorAll('[data-fname]').forEach(s=>s.textContent=n?', '+n:'');
      show(3);
    });
    form.querySelectorAll('input').forEach(i=>i.addEventListener('input',()=>i.classList.remove('err')));
  });

  // Header shadow and floating CTA (hidden while any lead form is on screen)
  const hdr=document.querySelector('header.site');
  addEventListener('scroll',()=>hdr&&hdr.classList.toggle('scrolled',scrollY>10),{passive:true});
  const fl=document.querySelector('.float-cta');
  const forms=[...document.querySelectorAll('[data-lead]')];
  if(fl&&forms.length&&'IntersectionObserver' in window){
    const vis=new Map(forms.map(f=>[f,true]));
    const upd=()=>{const on=![...vis.values()].some(Boolean)&&scrollY>400;fl.classList.toggle('show',on);fl.setAttribute('aria-hidden',String(!on));fl.querySelector('a').tabIndex=on?0:-1;};
    const io=new IntersectionObserver(es=>{es.forEach(e=>vis.set(e.target,e.isIntersecting));upd();});
    forms.forEach(f=>io.observe(f));
    addEventListener('scroll',upd,{passive:true});
  }
})();

// My Lawn portal concept: every action updates the page only. Nothing is saved or sent.
(function(){
  const root=document.querySelector('[data-portal]'); if(!root) return;
  const CHECK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>';
  const ref=()=> 'GLF-'+String(Math.floor(10000+Math.random()*89999));
  const say=(box,msg,undo)=>{
    const st=box.querySelector('[data-status]');
    st.innerHTML=msg?CHECK+'<span>'+msg+'</span>'+(undo?'<button type="button" data-undo>Undo</button>':''):'';
    const u=st.querySelector('[data-undo]'); if(u) u.addEventListener('click',()=>{undo();u.closest('[data-status]').innerHTML='';});
  };
  const show=(el,on)=>{ if(el) el.hidden=!on; };
  const acts=box=>box.querySelector('[data-acts]');

  // Next visit
  const visit=root.querySelector('[data-box="visit"]');
  if(visit){
    const h=visit.querySelector('h2'), orig=h.textContent, days=visit.querySelector('[data-days]'), note=visit.querySelector('[data-notebox]');
    visit.addEventListener('click',e=>{
      const b=e.target.closest('[data-act],[data-day]'); if(!b) return;
      const a=b.dataset.act;
      if(a==='skip'){ show(days,false); show(note,false); show(acts(visit),false); h.textContent='Skipped: '+h.textContent;
        say(visit,'Round 6 is skipped and you won’t be charged for it. Your next visit moves to Round 7.',()=>{h.textContent=orig;show(acts(visit),true);}); }
      if(a==='move'){ show(note,false); show(days,days.hidden); say(visit,''); }
      if(b.dataset.day){ const prev=h.textContent; h.textContent=b.dataset.day.replace(/^(\w+), /,(m,d)=>({Mon:'Monday',Tue:'Tuesday',Wed:'Wednesday',Thu:'Thursday',Fri:'Friday'}[d]||d)+', ').replace('Jun','June');
        show(days,false); say(visit,'Moved. You’ll get a text the day before.',()=>{h.textContent=prev;}); }
      if(a==='note'){ show(days,false); show(note,note.hidden); say(visit,''); if(!note.hidden) note.querySelector('textarea').focus(); }
      if(a==='save-note'){ const t=note.querySelector('textarea').value.trim(); show(note,false);
        say(visit,t?'Saved. Your technician sees this note on their route for this visit.':'Nothing to save yet.'); }
    });
  }

  // Add-on approval
  const ap=root.querySelector('[data-box="approve"]');
  if(ap) ap.addEventListener('click',e=>{
    const a=(e.target.closest('[data-act]')||{}).dataset?.act; if(!a) return;
    const label=ap.querySelector('.p-label'), was=label.textContent;
    show(acts(ap),false);
    const undo=()=>{show(acts(ap),true);label.textContent=was;ap.classList.remove('done-state');};
    if(a==='yes'){ label.textContent='Approved'; say(ap,'Approved. Lime goes down at your next visit, and $65 is added to that visit’s charge.',undo); }
    if(a==='no'){ label.textContent='Declined'; ap.classList.add('done-state'); say(ap,'Got it. No lime this year. We’ll ask again after your fall soil test.',undo); }
  });

  // Pause or cancel
  const plan=root.querySelector('[data-box="plan"]');
  if(plan){
    const conf=plan.querySelector('[data-confirm]');
    plan.addEventListener('click',e=>{
      const a=(e.target.closest('[data-act]')||{}).dataset?.act; if(!a) return;
      const back=()=>{show(acts(plan),true);show(conf,false);};
      if(a==='pause'){ show(acts(plan),false); say(plan,'Paused. No visits until you resume. Confirmation '+ref()+' is on its way by text and email.',back); }
      if(a==='cancel'){ show(acts(plan),false); show(conf,true); say(plan,''); conf.querySelector('.btn-primary').focus(); }
      if(a==='keep'){ back(); say(plan,'Your program stays as it is.'); }
      if(a==='confirm-cancel'){ show(conf,false); say(plan,'Cancelled. Confirmation '+ref()+'. Your remaining visits are off the schedule, and a copy is on its way by text and email.',back); }
    });
  }

  // Referral link
  const chop=root.querySelector('[data-box="chop"]');
  if(chop) chop.addEventListener('click',e=>{
    if(!e.target.closest('[data-act="share"]')) return;
    try{ navigator.clipboard && navigator.clipboard.writeText('Referral link (concept demo)'); }catch(_){}
    say(chop,'Copied. Share it with a neighbor.');
  });
})();
