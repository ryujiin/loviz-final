define([
    'jquery',
    'backbone',
    '../views/cms/pagina',    
    '../views/catalogo/page_catalogo',
    '../views/productoSingle/page_producto',
    '../views/carro/page_carro',
    '../views/procesar/page_procesar',
    '../views/usuario/page_user',
], function ($, Backbone,PaginaView,CatalogoView,PageProductoSingle,PageCarro,PageProcesar,PageUser) {
    'use strict';

    var AppRouter = Backbone.Router.extend({
        routes: {
            "":"root",
            'catalogo/:categoria/':'catalogo',
            "producto/:slug/":'productoSingle',            
            'usuario/perfil/':'perfil',
            'carro/':'carro_page',            
            'procesar-compra/':'procesar_compra',          
            'felicidades/':'',          
            '*notFound': 'notFound',
        },

        initialize:function(){
        },
        root:function(){
            PaginaView.buscar_page('home');
            console.log('primero');
        },
        catalogo:function (categoria) {
            if (categoria==='ofertas') {
                CatalogoView.catalogo_oferta('ofertas');
            }else{
                CatalogoView.get_categoria(categoria);
            }
        },
        perfil:function(){
            if ($.localStorage.get('pagina_procesar')===true) {
                $.localStorage.remove('pagina_procesar');
                this.navigate('procesar-compra/',{trigger: true});
            };
            PageUser.verificar_login();
        },
        productoSingle:function (slug) {
            PageProductoSingle.get_modelo(slug);
        },
        carro_page:function () {
            PageCarro.render();
        },
        procesar_compra:function () {
            PageProcesar.verificar_render();
        },
        felicidades:function () {
            debugger;
        },
        notFound:function () {
            $('body').removeClass();
            PaginaView.render_404();
        },
    });

    var rutas = new AppRouter();

    return rutas;
});
