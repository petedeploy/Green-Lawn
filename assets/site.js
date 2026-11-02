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
