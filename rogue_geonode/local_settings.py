# These settings override the default settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<APPLICATION_DB_NAME>',
        'USER': '<APPLICATION_USER_NAME>',
        'PASSWORD': '<APPLICATION_USER_PASSWORD>',
        'HOST': '<APPLICATION_DB_HOST>',
        'PORT': '<APPLICATION_DB_PORT>',
    },
    'datastore': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '<DB_DATASTORE_NAME>',
        'USER': '<DB_DATASTORE_USER>',
        'PASSWORD': '<DB_DATASTORE_PASSWORD>',
        'HOST': '<DB_DATASTORE_HOST>',
        'PORT': '<DB_DATASTORE_PORT>',
    },
}

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default': {
        'BACKEND': 'geonode.geoserver',
        'LOCATION': 'http://localhost/geoserver/', # This replaces GEOSERVER_BASE_URL
        'USER': 'admin',
        'PASSWORD': 'geoserver',
        'OPTIONS': {
            'MAPFISH_PRINT_ENABLED': True,
            'PRINTNG_ENABLED': True,
            'GEONODE_SECURITY_ENABLED': True,
            'GEOGIT_ENABLED': True,
            'WMST_ENABLED': False,

            # This replaces DB_DATASTORE=True
            # If DATASTORE != '' then geonode will use the datastore backend
            'DATASTORE': 'datastore',
        }
    }
}

#Import uploaded shapefiles into a database such as PostGIS?
DB_DATASTORE = True

UPLOADER_SHOW_TIME_STEP = True

#Database datastore connection settings
GEOGIT_DATASTORE_NAME = 'geogit-repo'
GEOGIT_DATASTORE = True

# Use the printNG geoserver lib
PRINTNG_ENABLED = True

# Uploader backend (rest or importer)
UPLOADER_BACKEND_URL = 'importer'

