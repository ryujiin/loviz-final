define(["./core","./var/document","./var/rcssNum","./var/rnothtmlwhite","./css/var/cssExpand","./css/var/isHiddenWithinTree","./css/var/swap","./css/adjustCSS","./data/var/dataPriv","./css/showHide","./core/init","./queue","./deferred","./traversing","./manipulation","./css","./effects/Tween"],function(e,t,n,r,i,s,o,u,a,f){function d(){c&&(window.requestAnimationFrame(d),e.fx.tick())}function v(){return window.setTimeout(function(){l=undefined}),l=e.now()}function m(e,t){var n,r=0,s={height:e};t=t?1:0;for(;r<4;r+=2-t)n=i[r],s["margin"+n]=s["padding"+n]=e;return t&&(s.opacity=s.width=e),s}function g(e,t,n){var r,i=(w.tweeners[t]||[]).concat(w.tweeners["*"]),s=0,o=i.length;for(;s<o;s++)if(r=i[s].call(n,t,e))return r}function y(t,n,r){var i,o,u,l,c,p,d,v,m="width"in n||"height"in n,y=this,b={},w=t.style,E=t.nodeType&&s(t),S=a.get(t,"fxshow");r.queue||(l=e._queueHooks(t,"fx"),l.unqueued==null&&(l.unqueued=0,c=l.empty.fire,l.empty.fire=function(){l.unqueued||c()}),l.unqueued++,y.always(function(){y.always(function(){l.unqueued--,e.queue(t,"fx").length||l.empty.fire()})}));for(i in n){o=n[i];if(h.test(o)){delete n[i],u=u||o==="toggle";if(o===(E?"hide":"show")){if(o!=="show"||!S||S[i]===undefined)continue;E=!0}b[i]=S&&S[i]||e.style(t,i)}}p=!e.isEmptyObject(n);if(!p&&e.isEmptyObject(b))return;m&&t.nodeType===1&&(r.overflow=[w.overflow,w.overflowX,w.overflowY],d=S&&S.display,d==null&&(d=a.get(t,"display")),v=e.css(t,"display"),v==="none"&&(d?v=d:(f([t],!0),d=t.style.display||d,v=e.css(t,"display"),f([t]))),(v==="inline"||v==="inline-block"&&d!=null)&&e.css(t,"float")==="none"&&(p||(y.done(function(){w.display=d}),d==null&&(v=w.display,d=v==="none"?"":v)),w.display="inline-block")),r.overflow&&(w.overflow="hidden",y.always(function(){w.overflow=r.overflow[0],w.overflowX=r.overflow[1],w.overflowY=r.overflow[2]})),p=!1;for(i in b)p||(S?"hidden"in S&&(E=S.hidden):S=a.access(t,"fxshow",{display:d}),u&&(S.hidden=!E),E&&f([t],!0),y.done(function(){E||f([t]),a.remove(t,"fxshow");for(i in b)e.style(t,i,b[i])})),p=g(E?S[i]:0,i,y),i in S||(S[i]=p.start,E&&(p.end=p.start,p.start=0))}function b(t,n){var r,i,s,o,u;for(r in t){i=e.camelCase(r),s=n[i],o=t[r],e.isArray(o)&&(s=o[1],o=t[r]=o[0]),r!==i&&(t[i]=o,delete t[r]),u=e.cssHooks[i];if(u&&"expand"in u){o=u.expand(o),delete t[i];for(r in o)r in t||(t[r]=o[r],n[r]=s)}else n[i]=s}}function w(t,n,r){var i,s,o=0,u=w.prefilters.length,a=e.Deferred().always(function(){delete f.elem}),f=function(){if(s)return!1;var e=l||v(),n=Math.max(0,c.startTime+c.duration-e),r=n/c.duration||0,i=1-r,o=0,u=c.tweens.length;for(;o<u;o++)c.tweens[o].run(i);return a.notifyWith(t,[c,i,n]),i<1&&u?n:(a.resolveWith(t,[c]),!1)},c=a.promise({elem:t,props:e.extend({},n),opts:e.extend(!0,{specialEasing:{},easing:e.easing._default},r),originalProperties:n,originalOptions:r,startTime:l||v(),duration:r.duration,tweens:[],createTween:function(n,r){var i=e.Tween(t,c.opts,n,r,c.opts.specialEasing[n]||c.opts.easing);return c.tweens.push(i),i},stop:function(e){var n=0,r=e?c.tweens.length:0;if(s)return this;s=!0;for(;n<r;n++)c.tweens[n].run(1);return e?(a.notifyWith(t,[c,1,0]),a.resolveWith(t,[c,e])):a.rejectWith(t,[c,e]),this}}),h=c.props;b(h,c.opts.specialEasing);for(;o<u;o++){i=w.prefilters[o].call(c,t,h,c.opts);if(i)return e.isFunction(i.stop)&&(e._queueHooks(c.elem,c.opts.queue).stop=e.proxy(i.stop,i)),i}return e.map(h,g,c),e.isFunction(c.opts.start)&&c.opts.start.call(t,c),e.fx.timer(e.extend(f,{elem:t,anim:c,queue:c.opts.queue})),c.progress(c.opts.progress).done(c.opts.done,c.opts.complete).fail(c.opts.fail).always(c.opts.always)}var l,c,h=/^(?:toggle|show|hide)$/,p=/queueHooks$/;return e.Animation=e.extend(w,{tweeners:{"*":[function(e,t){var r=this.createTween(e,t);return u(r.elem,e,n.exec(t),r),r}]},tweener:function(t,n){e.isFunction(t)?(n=t,t=["*"]):t=t.match(r);var i,s=0,o=t.length;for(;s<o;s++)i=t[s],w.tweeners[i]=w.tweeners[i]||[],w.tweeners[i].unshift(n)},prefilters:[y],prefilter:function(e,t){t?w.prefilters.unshift(e):w.prefilters.push(e)}}),e.speed=function(n,r,i){var s=n&&typeof n=="object"?e.extend({},n):{complete:i||!i&&r||e.isFunction(n)&&n,duration:n,easing:i&&r||r&&!e.isFunction(r)&&r};e.fx.off||t.hidden?s.duration=0:typeof s.duration!="number"&&(s.duration in e.fx.speeds?s.duration=e.fx.speeds[s.duration]:s.duration=e.fx.speeds._default);if(s.queue==null||s.queue===!0)s.queue="fx";return s.old=s.complete,s.complete=function(){e.isFunction(s.old)&&s.old.call(this),s.queue&&e.dequeue(this,s.queue)},s},e.fn.extend({fadeTo:function(e,t,n,r){return this.filter(s).css("opacity",0).show().end().animate({opacity:t},e,n,r)},animate:function(t,n,r,i){var s=e.isEmptyObject(t),o=e.speed(n,r,i),u=function(){var n=w(this,e.extend({},t),o);(s||a.get(this,"finish"))&&n.stop(!0)};return u.finish=u,s||o.queue===!1?this.each(u):this.queue(o.queue,u)},stop:function(t,n,r){var i=function(e){var t=e.stop;delete e.stop,t(r)};return typeof t!="string"&&(r=n,n=t,t=undefined),n&&t!==!1&&this.queue(t||"fx",[]),this.each(function(){var n=!0,s=t!=null&&t+"queueHooks",o=e.timers,u=a.get(this);if(s)u[s]&&u[s].stop&&i(u[s]);else for(s in u)u[s]&&u[s].stop&&p.test(s)&&i(u[s]);for(s=o.length;s--;)o[s].elem===this&&(t==null||o[s].queue===t)&&(o[s].anim.stop(r),n=!1,o.splice(s,1));(n||!r)&&e.dequeue(this,t)})},finish:function(t){return t!==!1&&(t=t||"fx"),this.each(function(){var n,r=a.get(this),i=r[t+"queue"],s=r[t+"queueHooks"],o=e.timers,u=i?i.length:0;r.finish=!0,e.queue(this,t,[]),s&&s.stop&&s.stop.call(this,!0);for(n=o.length;n--;)o[n].elem===this&&o[n].queue===t&&(o[n].anim.stop(!0),o.splice(n,1));for(n=0;n<u;n++)i[n]&&i[n].finish&&i[n].finish.call(this);delete r.finish})}}),e.each(["toggle","show","hide"],function(t,n){var r=e.fn[n];e.fn[n]=function(e,t,i){return e==null||typeof e=="boolean"?r.apply(this,arguments):this.animate(m(n,!0),e,t,i)}}),e.each({slideDown:m("show"),slideUp:m("hide"),slideToggle:m("toggle"),fadeIn:{opacity:"show"},fadeOut:{opacity:"hide"},fadeToggle:{opacity:"toggle"}},function(t,n){e.fn[t]=function(e,t,r){return this.animate(n,e,t,r)}}),e.timers=[],e.fx.tick=function(){var t,n=0,r=e.timers;l=e.now();for(;n<r.length;n++)t=r[n],!t()&&r[n]===t&&r.splice(n--,1);r.length||e.fx.stop(),l=undefined},e.fx.timer=function(t){e.timers.push(t),t()?e.fx.start():e.timers.pop()},e.fx.interval=13,e.fx.start=function(){c||(c=window.requestAnimationFrame?window.requestAnimationFrame(d):window.setInterval(e.fx.tick,e.fx.interval))},e.fx.stop=function(){window.cancelAnimationFrame?window.cancelAnimationFrame(c):window.clearInterval(c),c=null},e.fx.speeds={slow:600,fast:200,_default:400},e});