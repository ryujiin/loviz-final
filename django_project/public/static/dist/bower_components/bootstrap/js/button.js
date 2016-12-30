/* ========================================================================
 * Bootstrap: button.js v3.3.7
 * http://getbootstrap.com/javascript/#buttons
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */

+function(e){function n(n){return this.each(function(){var r=e(this),i=r.data("bs.button"),s=typeof n=="object"&&n;i||r.data("bs.button",i=new t(this,s)),n=="toggle"?i.toggle():n&&i.setState(n)})}var t=function(n,r){this.$element=e(n),this.options=e.extend({},t.DEFAULTS,r),this.isLoading=!1};t.VERSION="3.3.7",t.DEFAULTS={loadingText:"loading..."},t.prototype.setState=function(t){var n="disabled",r=this.$element,i=r.is("input")?"val":"html",s=r.data();t+="Text",s.resetText==null&&r.data("resetText",r[i]()),setTimeout(e.proxy(function(){r[i](s[t]==null?this.options[t]:s[t]),t=="loadingText"?(this.isLoading=!0,r.addClass(n).attr(n,n).prop(n,!0)):this.isLoading&&(this.isLoading=!1,r.removeClass(n).removeAttr(n).prop(n,!1))},this),0)},t.prototype.toggle=function(){var e=!0,t=this.$element.closest('[data-toggle="buttons"]');if(t.length){var n=this.$element.find("input");n.prop("type")=="radio"?(n.prop("checked")&&(e=!1),t.find(".active").removeClass("active"),this.$element.addClass("active")):n.prop("type")=="checkbox"&&(n.prop("checked")!==this.$element.hasClass("active")&&(e=!1),this.$element.toggleClass("active")),n.prop("checked",this.$element.hasClass("active")),e&&n.trigger("change")}else this.$element.attr("aria-pressed",!this.$element.hasClass("active")),this.$element.toggleClass("active")};var r=e.fn.button;e.fn.button=n,e.fn.button.Constructor=t,e.fn.button.noConflict=function(){return e.fn.button=r,this},e(document).on("click.bs.button.data-api",'[data-toggle^="button"]',function(t){var r=e(t.target).closest(".btn");n.call(r,"toggle"),e(t.target).is('input[type="radio"], input[type="checkbox"]')||(t.preventDefault(),r.is("input,button")?r.trigger("focus"):r.find("input:visible,button:visible").first().trigger("focus"))}).on("focus.bs.button.data-api blur.bs.button.data-api",'[data-toggle^="button"]',function(t){e(t.target).closest(".btn").toggleClass("focus",/^focus(in)?$/.test(t.type))})}(jQuery);