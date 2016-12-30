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
        navegar:function(e){
            e.preventDefault();
            var link = e.currentTarget.pathname;
            Backbone.history.navigate(link, {trigger:true});
            $('#navigation').removeClass('is_activo');
            $('body').animate({scrollTop:0}, 'slow');
        },
        no_navegar:function (e) {
            e.preventDefault();            
        }
    });

    return AppView;
});