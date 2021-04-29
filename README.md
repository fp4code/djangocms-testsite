# djangocms-testsite

## Install

    cd <somewhere>
    python3 -m venv env
    . env/bin/activate
    pip install --upgrade pip
    git clone https://github.com/fp4code/djangocms-testsite.git
    cd djangocms-testsite
    git submodule init
    git submodule update --depth 1
    pip install -r requirements.txt
    deactivate

## Usage

    cd <somewhere>/djangocms-testsite
    . ../env/bin/activate
    rm db.sqlite3 # if necessary
    ./manage.py migrate
    python starting_site.py
    (SITE_ID=1; ./manage.py runserver 8001&)
    (SITE_ID=2; ./manage.py runserver 8002&)

Open http://localhost:8001/admin/ or http://localhost:8002/admin/ with admin/admin credentials.
    
    
    