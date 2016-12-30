define(["../core","../css"],function(e){function t(e,n,r,i,s){return new t.prototype.init(e,n,r,i,s)}e.Tween=t,t.prototype={constructor:t,init:function(t,n,r,i,s,o){this.elem=t,this.prop=r,this.easing=s||e.easing._default,this.options=n,this.start=this.now=this.cur(),this.end=i,this.unit=o||(e.cssNumber[r]?"":"px")},cur:function(){var e=t.propHooks[this.prop];return e&&e.get?e.get(this):t.propHooks._default.get(this)},run:function(n){var r,i=t.propHooks[this.prop];return this.options.duration?this.pos=r=e.easing[this.easing](n,this.options.duration*n,0,1,this.options.duration):this.pos=r=n,this.now=(this.end-this.start)*r+this.start,this.options.step&&this.options.step.call(this.elem,this.now,this),i&&i.set?i.set(this):t.propHooks._default.set(this),this}},t.prototype.init.prototype=t.prototype,t.propHooks={_default:{get:function(t){var n;return t.elem.nodeType!==1||t.elem[t.prop]!=null&&t.elem.style[t.prop]==null?t.elem[t.prop]:(n=e.css(t.elem,t.prop,""),!n||n==="auto"?0:n)},set:function(t){e.fx.step[t.prop]?e.fx.step[t.prop](t):t.elem.nodeType!==1||t.elem.style[e.cssProps[t.prop]]==null&&!e.cssHooks[t.prop]?t.elem[t.prop]=t.now:e.style(t.elem,t.prop,t.now+t.unit)}}},t.propHooks.scrollTop=t.propHooks.scrollLeft={set:function(e){e.elem.nodeType&&e.elem.parentNode&&(e.elem[e.prop]=e.now)}},e.easing={linear:function(e){return e},swing:function(e){return.5-Math.cos(e*Math.PI)/2},_default:"swing"},e.fx=t.prototype.init,e.fx.step={}});