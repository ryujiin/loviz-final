/*global define*/

define([
    'jquery',
    'underscore',
    'backbone',
    '../views/carro/minicarro',
    'carro_main',
    '../views/usuario/user_links',  
    '../models/user'
], function ($, _, Backbone,CarroView,CarroModel,UserLinkView,UserModel) {
    'use strict';

    var AppView = Backbone.View.extend({
        el:$('body'),
        className: '',
        events: {
            'click .link' : 'navegar',
            'click .no-link' : 'no_navegar',
            'click .menu-mobil-icono': 'mostrar_navegador_mobil',
            'click .link-modal':'navegar_modal',
            'click .footer-block-menu h4':'menu_activo',
            'click .footer-block-menu h4.activo':'menu_desactivo',
        },

        initialize: function () {
            var user_link = new UserLinkView({
                model:UserModel
            });
            var mini_carro = new CarroView({
                model:CarroModel
            });
        },
        mostrar_navegador_mobil:function (e) {
            $('#navigation').toggleClass('is_activo');
        },
        addBloqueSuscrito:function () {
            var bloque_suscrito = new BloqueSuscrito({
                el:$('#suscribirse'),
                model:new ModelSuscrito(),
            })
        },
        navegar_modal:function (e) {
            e.preventDefault();
            this.$('.modal.fade.in').modal('hide');
            var link  = e.target.pathname;
            //Backbone.history.navigate(link, {trigger:true});
        },
        navegar:function(e){
            e.preventDefault();
            var link = e.currentTarget.pathname;
            Backbone.history.navigate(link, {trigger:true});
            $('#navigation').removeClass('is_activo');
            $('body').animate({scrollTop:0}, 'slow');
        },
        menu_activo:function (e) {
            $(e.target).addClass('activo');
            $(e.target.nextElementSibling).addClass('activo');
        },
        menu_desactivo:function (e) {
            $(e.target).removeClass('activo');            
            $(e.target.nextElementSibling).removeClass('activo');
        },
        no_navegar:function (e) {
            e.preventDefault();            
        }
    });

    return AppView;
});