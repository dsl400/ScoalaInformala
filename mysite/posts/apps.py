from django.apps import AppConfig
from django.db.models import F, Field, Lookup


@Field.register_lookup
class NotEqual(Lookup):
    lookup_name = 'ne'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        print(compiler,lhs,rhs,params)
        print(params)
        return '%s <> %s' % (lhs, rhs), params


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

    def ready(self):
        Field.register_lookup(NotEqual)

