
define([
    'jquery',
    'underscore',
    'backbone',
    'swig',
    'carro_main',
    'headModel',
    '../../views/carro/lineas_carro',
], function ($, _, Backbone, swig,CarroModel,Head,LineasView) {
    'use strict';

    var CarroPageView = Backbone.View.extend({
        el:$('#contenido'),

        template: swig.compile($('#page_carro_template').html()),        

        tagName: 'div',

        id: '',

        className: '',

        model:CarroModel,

        events: {},

        initialize: function () {
            this.listenTo(this.model, 'change:id',this.render);
        },

        render: function () {
            var locacion = Backbone.history.location.pathname;
            if (locacion === '/carro/') {
                this.$el.html(this.template(this.model.toJSON()));
                this.change_head();
                if (this.model.id) {
                    this.lineasview= new LineasView({
                        el:this.$('.lineas_carro'),
                        model:this.model,
                    });
                };            
            };            
        },

        change_head:function () {
            var titulo = 'Mi carro de compras';
            var descripcion = 'Mi carro de compras en Loviz DelCarpio®, lovizdc.com';
            Head.set({titulo:titulo,descripcion:descripcion});
        },
    });

    var vista = new CarroPageView();

    return vista;
});
