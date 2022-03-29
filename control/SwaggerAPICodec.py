import yaml
from coreapi.codecs.base import BaseCodec
from coreapi.document import Document
from coreapi.exceptions import ParseError
from openapi_codec.decode import _parse_document


class SwaggerAPICodec(BaseCodec):
    format = 'openapi'
    media_type = 'application/openapi+yaml'

    def decode(self, bytes, **options):
        try:
            data = yaml.safe_load(bytes)
        except ValueError as exc:
            raise ParseError('Malformed YAML. {}'.format(exc))

        base_url = options.get('base_url')
        doc = _parse_document(data, base_url)

        if not isinstance(doc, Document):
            raise ParseError('Top level node must be a document.')

        return doc

    def encode(self, document, **options):
        raise AttributeError('.encode() method not yet developed.')