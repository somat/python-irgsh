from unittest import TestCase

class DefaultTestCase(TestCase):
    def testDefault(self):
        from irgsh.data import Specification
        spec = Specification('http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx_0.7.65-1ubuntu2.debian.tar.gz')

        self.assertEqual(spec.source, 'http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx_0.7.65-1ubuntu2.debian.tar.gz')
        self.assertEqual(spec.orig, None)
        self.assertEqual(spec.source_type, 'tarball')
        self.assertEqual(spec.source_opts, {})

class SourceTestCase(TestCase):
    def setUp(self):
        from irgsh.data import Specification
        self.spec = Specification('http://dev.blankonlinux.or.id/bzr/pattimura/python-apt',
                                  'bzr',
                                  {'tag': '0.7.100ubuntu2+blankon1.2'},
                                  'http://irgsh.blankonlinux.or.id/copies/task/29/python-apt.tar.bz2')

    def testAttributes(self):
        self.assertEqual(self.spec.source, 'http://dev.blankonlinux.or.id/bzr/pattimura/python-apt')
        self.assertEqual(self.spec.orig, 'http://irgsh.blankonlinux.or.id/copies/task/29/python-apt.tar.bz2')
        self.assertEqual(self.spec.source_type, 'bzr')
        self.assertEqual(self.spec.source_opts, {'tag': '0.7.100ubuntu2+blankon1.2'})

