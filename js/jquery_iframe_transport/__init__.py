from fanstatic import Library, Resource
import js.jquery

library = Library('jquery_iframe_transport', 'resources')

jquery_iframe_transport = Resource(library,
                                   'jquery.iframe-transport.js',
                                   depends=[js.jquery.jquery, ])
