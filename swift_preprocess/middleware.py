"""OpenStack Swift middleware to preprocess objects."""

from swift.common import swob


class PreprocessMiddleware(object):
    
    def __init__(self, app):
        self.app = app

    @swob.wsgify
    def __call__(self, req):

        return self.app


def filter_factory(global_conf, **local_conf):
    """WSGI filter for paste.deploy."""

    conf = global_conf.copy()
    conf.update(local_conf)

    def filtered(app):
        return PreprocessMiddleware(app)

    return filtered
